# FactorialHR api python wrapper

This package provides a python wrapper to the [api of FactorialHR](https://apidoc.factorialhr.com/docs).

The package currently supports the api version 2025-07-01. You can find the openapi specification [here](https://apidoc.factorialhr.com/openapi/67e137b5e9907d003ce15082).
**I derived some types from the examples given. They might be incorrect. If you encounter any problems, please create an issue and/or contribute a fix.**

## Disclaimer

I am not affiliated, associated, authorized, endorsed by, or in any way officially connected with EVERYDAY SOFTWARE, S.L. or FactorialHR, or any of its subsidiaries or its affiliates. The official factorialhr.com website can be found at https://factorialhr.com/

## Usage

Get all employees
```python
import factorialhr

authorizer = factorialhr.ApiKeyAuth('<api_key>')  # checkout other authorization methods
async with factorialhr.ApiClient(auth=authorizer) as api:
    all_employees = factorialhr.EmployeesEndpoint(api).all()  # fetches all employees. on big companies you might want to increase the timeout by using timeout=...
```
Get a dictionary with team id as key and a list of member as value
```python
import asyncio

import factorialhr

authorizer = factorialhr.AccessTokenAuth('<access_token>')  # checkout other authorization methods
async with factorialhr.ApiClient(auth=authorizer) as api:
        employees_endpoint = factorialhr.EmployeesEndpoint(api)
        teams_endpoint = factorialhr.TeamsEndpoint(api)
        all_employees, all_teams = await asyncio.gather(employees_endpoint.all(), teams_endpoint.all())  # remember to increase the timeout if you have a lot of employees or teams
        employees_by_team_id = {team.id: [employee for employee in all_employees.data() if employee.id in team.employee_ids] for team in all_teams.data()}
```

## CLI

A commandline interface can be installed with `factorialhr[cli]`. This is especially useful as a uv tool `uv tool install factorialhr[cli]`.

`(uvx) factorialhr --help`

### Login

The cli currently only supports oauth2 as login method. Please create an issue or contribute yourself if you need a different login method.

`(uvx) factorialhr account login`

## Contribute

Feel free to contribute! Please fork this repository, install the development dependencies with `uv sync --dev`
and create pull request.
