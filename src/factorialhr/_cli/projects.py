import asyncio
import datetime

import click
import cloup
import tabulate

import factorialhr
from factorialhr._cli import account
from factorialhr._cli import common as common_cli


async def get_time_records(
    client: factorialhr.ApiClient,
    start: datetime.date | None,
    end: datetime.date,
) -> list[factorialhr.TimeRecord]:
    if start is not None:
        time_records = [
            x
            for xs in await asyncio.gather(
                *(
                    factorialhr.TimeRecordEndpoint(client).all(year=date.year, month=date.month)
                    for date in common_cli.get_months_in(start, end)
                ),
            )
            for x in xs
        ]
        return [
            time_record
            for time_record in time_records
            if time_record.date is not None and start <= time_record.date <= end
        ]
    return await factorialhr.TimeRecordEndpoint(client).all()


@cloup.group('projects', help='Project related cli methods.')
def project_entrypoint():
    pass


@cloup.command(help='Calculate the imputed minutes for projects')
@cloup.option_group(
    'Filter options',
    cloup.option('--name', type=str, help='Filter by project name'),
    cloup.option('--active', is_flag=True, help='Filter by active projects only'),
    *common_cli.upper_lower_bounds,
    cloup.option('--ignore-unassigned', is_flag=True, help='Ignore time records that are not assigned to any project'),
)
@common_cli.generic_options
@common_cli.to_async
async def imputed_minutes(  # noqa: PLR0913
    name: str | None,
    start: datetime.date | None,
    end: datetime.date,
    active: bool,  # noqa: FBT001
    less: bool,  # noqa: FBT001
    http_timeout: int,
    **_,
):
    auth, url = account.get_session()
    async with factorialhr.ApiClient(auth=auth, base_url=url, timeout=http_timeout) as client:
        time_records, projects, project_worker = await asyncio.gather(
            get_time_records(client, start, end),
            factorialhr.ProjectEndpoint(client).all(name=name),
            factorialhr.ProjectWorkerEndpoint(client).all(),
        )
    if not time_records:
        raise click.ClickException('No project time records found')
    if not projects:
        raise click.ClickException('No projects found')
    projects_by_id = {project.id: project for project in projects}
    project_workers_by_id = {project_worker.id: project_worker for project_worker in project_worker}

    # ensures that also projects that don't have imputed minutes are respected
    if active:
        projects_time = {project.name: 0 for project in projects if project.status == factorialhr.ProjectStatus.active}
    else:
        projects_time = {project.name: 0 for project in projects}
    for record in time_records:
        project_worker = project_workers_by_id[record.project_worker_id]
        if project_worker.project_id in projects_by_id:
            if record.imputed_minutes is None:
                msg = (
                    f'Time record contains no imputed minutes. This might happen if a time record has no end time yet '
                    f'(e.g. is someone is currently working). Record: "{record}"'
                )
                raise click.ClickException(msg)
            projects_time[projects_by_id[project_worker.project_id].name] += record.imputed_minutes

    table_to_print = tabulate.tabulate(list(projects_time.items()), headers=['Projectname', 'Imputed minutes'])
    if less:
        click.echo_via_pager(table_to_print)
    else:
        click.echo(table_to_print)


@cloup.command(help='Calculate the minutes not assigned to any project')
@cloup.option_group(
    'Filter options',
    *common_cli.upper_lower_bounds,
)
@common_cli.generic_options
@common_cli.to_async
async def unrelated_minutes(
    start: datetime.date | None,
    end: datetime.date,
    http_timeout: int,
    **_,
):
    auth, url = account.get_session()
    async with factorialhr.ApiClient(auth=auth, base_url=url, timeout=http_timeout) as client:
        shifts, time_records = await asyncio.gather(
            # get raw data as its not worth parsing the data because only integer are used
            factorialhr.ShiftEndpoint(client).all_raw(params={'start_on': start, 'end_on': end}),
            get_time_records(client, start, end),
        )
    if not shifts:
        raise click.ClickException('No shifts found')
    if not time_records:
        raise click.ClickException('No project time records found')
    records_by_shift_id = {record.attendance_shift_id: record for record in time_records}
    click.echo(f'{sum(s["minutes"] for s in shifts if s["id"] not in records_by_shift_id)} minutes')


project_entrypoint.add_command(imputed_minutes)
project_entrypoint.add_command(unrelated_minutes)
