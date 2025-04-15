import asyncio
import collections
import datetime

import click
import cloup
import polars as pl
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


def filter_employees(
    all_employees: list[factorialhr.Employee],
    employees: tuple[str],
    all_teams: list[factorialhr.Team],
    teams: tuple[str],
) -> list[factorialhr.Employee]:
    if not employees and not teams:
        return all_employees

    selected_employees = set()
    if teams:
        filtered_teams = [t for t in all_teams if t.name in teams]
        employee_ids_contained_in_team = {eid for t in filtered_teams for eid in t.employee_ids or []}
        selected_employees = selected_employees.union(
            {e.id for e in all_employees if e.id in employee_ids_contained_in_team},
        )
    if employees:
        selected_employees = selected_employees.union({e.id for e in all_employees if e.full_name in employees})
    return [e for e in all_employees if e.id in selected_employees]


@cloup.group('projects', help='Project related cli methods.')
def project_entrypoint():
    pass


@cloup.command(help='Calculate the imputed minutes for projects')
@common_cli.file_output
@cloup.option_group(
    'Filter options',
    *common_cli.upper_lower_bounds,
    cloup.option('--project', multiple=True, help='Filter by project name'),
    *common_cli.team_employee_filter,
    cloup.option(
        '--include-contributors-only',
        is_flag=True,
        help='Include only employees that contributed to at least one project',
    ),
)
@common_cli.generic_options
@common_cli.to_async
async def imputed_minutes(  # noqa: PLR0913, C901, PLR0912
    output: str | None,
    project: tuple[str],
    start: datetime.date | None,
    end: datetime.date,
    http_timeout: int,
    employee: tuple[str],
    team: tuple[str],
    include_contributors_only: bool,  # noqa: FBT001
    **_,
):
    auth, url = account.get_session()
    async with factorialhr.ApiClient(auth=auth, base_url=url, timeout=http_timeout) as client:
        time_records, projects, project_worker, employees, teams = await asyncio.gather(
            get_time_records(client, start, end),
            factorialhr.ProjectEndpoint(client).all(),
            factorialhr.ProjectWorkerEndpoint(client).all(),
            factorialhr.EmployeeEndpoint(client).all(),
            factorialhr.TeamEndpoint(client).all(),
        )
    if not time_records:
        raise click.ClickException('No project time records found')
    if not projects:
        raise click.ClickException('No projects found')
    if project:
        projects = [p for p in projects if p.name in project]
    selected_employees = filter_employees(
        all_employees=employees,
        employees=employee,
        all_teams=teams,
        teams=team,
    )
    employees_by_ids = {e.id: e for e in selected_employees}
    projects_by_id = {project.id: project for project in projects}
    project_workers_by_id = {project_worker.id: project_worker for project_worker in project_worker}

    project_times_by_employee_name = collections.defaultdict(lambda: collections.defaultdict(int))
    contributed_projects = set(project)  # ensure that the selected projects are always shown
    for record in time_records:
        project_worker = project_workers_by_id[record.project_worker_id]
        if project_worker.project_id in projects_by_id and project_worker.employee_id in employees_by_ids:
            if record.imputed_minutes is None:
                msg = (
                    f'Time record contains no imputed minutes. This might happen if a time record has no end time yet '
                    f'(e.g. is someone is currently working). Record: "{record}"'
                )
                raise click.ClickException(msg)

            employee_name = employees_by_ids[project_worker.employee_id].full_name
            project_name = projects_by_id[project_worker.project_id].name
            project_times_by_employee_name[employee_name][project_name] += record.imputed_minutes
            contributed_projects.add(project_name)

    if not include_contributors_only:
        employees_not_contributed = [
            e.full_name for e in selected_employees if e.full_name not in project_times_by_employee_name
        ]
        for project_name in contributed_projects:
            for employee_name in employees_not_contributed:
                project_times_by_employee_name[employee_name][project_name] = 0

    project_times_sum_by_project_name = collections.defaultdict(int)
    for project_times in project_times_by_employee_name.values():
        for project_name, minutes in project_times.items():
            project_times_sum_by_project_name[project_name] += minutes
    minutes_by_project_name = collections.defaultdict(list[int])
    for project_name, minutes in project_times_sum_by_project_name.items():
        minutes_by_project_name[project_name].append(minutes)
    employee_names = []
    for employee_name, project_times in project_times_by_employee_name.items():
        employee_names.append(employee_name)
        for project_name in project_times_sum_by_project_name:
            if project_name not in project_times:
                minutes_by_project_name[project_name].append(0)
            else:
                minutes_by_project_name[project_name].append(project_times[project_name])

    if output:
        pl.DataFrame(
            [(name, *minutes) for name, minutes in minutes_by_project_name.items()],
            schema=['Projectname', 'Imputed minutes', *employee_names],
            orient='row',
        ).write_csv(output)
    else:
        table_to_print = tabulate.tabulate(
            [(name, *minutes) for name, minutes in minutes_by_project_name.items()],
            headers=['Projectname', 'Imputed minutes', *employee_names],
        )
        click.echo(table_to_print)


@cloup.command(help='Calculate the minutes not assigned to any project')
@cloup.option_group(
    'Filter options',
    *common_cli.upper_lower_bounds,
    *common_cli.team_employee_filter,
)
@common_cli.generic_options
@common_cli.file_output
@common_cli.to_async
async def unrelated_minutes(  # noqa: PLR0913
    start: datetime.date | None,
    end: datetime.date,
    http_timeout: int,
    employee: tuple[str],
    team: tuple[str],
    output: str,
    **_,
):
    auth, url = account.get_session()
    async with factorialhr.ApiClient(auth=auth, base_url=url, timeout=http_timeout) as client:
        shifts, time_records, employees, teams = await asyncio.gather(
            # get raw data as its not worth parsing because it can take very long time
            factorialhr.ShiftEndpoint(client).all_raw(params={'start_on': start, 'end_on': end}),
            get_time_records(client, start, end),
            factorialhr.EmployeeEndpoint(client).all(),
            factorialhr.TeamEndpoint(client).all(),
        )
    if not shifts:
        raise click.ClickException('No shifts found')
    if not time_records:
        raise click.ClickException('No project time records found')
    selected_employees = filter_employees(
        all_employees=employees,
        employees=employee,
        all_teams=teams,
        teams=team,
    )
    employees_by_id = {employee.id: employee.full_name for employee in selected_employees}
    records_by_shift_id = {record.attendance_shift_id: record for record in time_records}
    unrelated_shifts_by_employee_id = collections.defaultdict(list)
    for shift in shifts:
        if shift['id'] not in records_by_shift_id and shift['employee_id'] in employees_by_id:
            unrelated_shifts_by_employee_id[shift['employee_id']].append(shift)

    pairing = []
    for eid, shifts in unrelated_shifts_by_employee_id.items():
        pairing.append((employees_by_id[eid], sum(s['minutes'] for s in shifts)))

    if output:
        pl.DataFrame(
            pairing,
            schema=['Employee', 'Minutes'],
            orient='row',
        ).write_csv(output)
    else:
        click.echo(tabulate.tabulate(pairing, headers=['Employee', 'Minutes', 'Dates']))
        click.echo()
        click.echo(f'Total: {sum(s[1] for s in pairing)} minutes')


project_entrypoint.add_command(imputed_minutes)
project_entrypoint.add_command(unrelated_minutes)
