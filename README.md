# FactorialHR api python wrapper

This package provides a python wrapper to the [api of FactorialHR](https://apidoc.factorialhr.com/docs).

## Disclaimer

I am not affiliated, associated, authorized, endorsed by, or in any way officially connected with EVERYDAY SOFTWARE, S.L. or FactorialHR, or any of its subsidiaries or its affiliates. The official factorialhr.com website can be found at https://factorialhr.com/

Unfortunately, the documentation is not detailed and updated, such that many parameters have been reverse engineered and
may be wrong or change at any time. If you encounter some
problems, [open an issue](https://github.com/leon1995/factorialhr/issues) or [contribute](#Contribute) the fix yourself.

## Usage

Get all employees
```python
from factorialhr import endpoints

async with endpoints.NetworkHandler as api:
    endpoint = endpoints.EmployeesEndpoint(api)
    all_employees = await endpoint.all()
```
Get a dictionary with team id as key and a list of member as value
```python
from factorialhr import endpoints
from factorialhr import models

async with endpoints.NetworkHandler('<api_key>') as api:
    e_endpoint = endpoints.EmployeesEndpoint(api)
    t_endpoint = endpoints.TeamsEndpoint(api)
    all_employees = await e_endpoint.all()
    all_teams = await t_endpoint.all()
    employees_by_team_id: dict[int, models.Employee] = {team.id: [e for e in all_employees
                                                                  if e.id in team.employee_ids] for team in all_teams}
```

## TODO

- [ ] tests
- [x] oauth2 support
- [ ] [Family situation endpoint](https://apidoc.factorialhr.com/reference/get_v1-payroll-family-situation)
- [ ] [Contract versions endpoint](https://apidoc.factorialhr.com/reference/get_v1-payroll-contract-versions)
- [ ] [Supplements endpoint](https://apidoc.factorialhr.com/reference/get_v1-payroll-supplements)
- [ ] [Shift management endpoint](https://apidoc.factorialhr.com/reference/get_v1-time-shifts-management)
- [ ] [Breaks endpoint](https://apidoc.factorialhr.com/reference/post_v1-time-breaks-start)
- [ ] [Application endpoint](https://apidoc.factorialhr.com/reference/post_v1-ats-applications)
- [ ] [ATS messages endpoint](https://apidoc.factorialhr.com/reference/get_v1-ats-messages)
- [ ] [Expenses endpoint](https://apidoc.factorialhr.com/reference/get_v1-finance-expenses)
- [ ] [Get Custom Table Fields](https://apidoc.factorialhr.com/reference/get_v1-core-custom-tables-id-values-employee-id)
- [ ] [Creates a custom table value](https://apidoc.factorialhr.com/reference/post_v1-core-custom-tables-id-values-employee-id)

## Contribute

Feel free to contribute! Please fork this repository, install the development dependencies with `pip install -e ".[dev]"`
and create pull request.