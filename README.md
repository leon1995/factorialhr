# FactorialHR api python wrapper

This package provides a python wrapper to the [api of FactorialHR](https://apidoc.factorialhr.com/docs).

> [!IMPORTANT]
> Currently only the get requests responses are modeled with pydantic

## Disclaimer

I am not affiliated, associated, authorized, endorsed by, or in any way officially connected with EVERYDAY SOFTWARE, S.L. or FactorialHR, or any of its subsidiaries or its affiliates. The official factorialhr.com website can be found at https://factorialhr.com/

## Usage

Get all employees
```python
import factorialhr

authorizer = factorialhr.ApiKeyAuth('<api_key>')  # checkout other authorization methods
async with factorialhr.ApiClient(auth=authorizer) as api:
    employee_endpoint = factorialhr.EmployeeEndpoint(api)
    all_employees = await employee_endpoint.all()  # fetches all employees. on big companies you might want to increase the timeout by using timeout=httpx.Timeout(...)
```
Get a dictionary with team id as key and a list of member as value
```python
import asyncio

import factorialhr

authorizer = factorialhr.AccessTokenAuth('<access_token>')  # checkout other authorization methods
async with factorialhr.ApiClient(auth=authorizer) as api:
        employees_endpoint = factorialhr.EmployeeEndpoint(api)
        teams_endpoint = factorialhr.TeamEndpoint(api)
        all_employees, all_teams = await asyncio.gather(employees_endpoint.all(), teams_endpoint.all())  # remember to increase the timeout if you have a lot of employees or teams
        employees_by_team_id = {team.id: [employee for employee in all_employees if employee.id in team.employee_ids] for team in all_teams}
```

### Different request than `GET`

Update an employee
```python
import factorialhr

async with factorialhr.ApiClient(...) as api:
    response = await api.put(factorialhr.EmployeeEndpoint.endpoint, '<employee_id>', data={ 'first_name': 'Alice', ... })
```

## CLI

A commandline interface can be installed with `factorialhr[cli]`. This is especially useful as a uv tool `uv tool install factorialhr[cli]`.

`(uvx) factorialhr --help`

### Login

The cli currently only supports oauth2 as login method. Please create an issue or contribute yourself if you need a different login method.

`(uvx) factorialhr account login`

## Implemented endpoints for api version 2025-01-01

- [x] ApiPublic
- [x] Ats
- [x] Attendance
- [ ] BookkeepersManagement
- [ ] Companies
- [ ] Contracts
- [ ] CustomFields
- [ ] CustomResources
- [ ] Documents
- [x] Employees
- [ ] EmployeeUpdates
- [ ] Expenses
- [ ] Finance
- [ ] Holidays
- [ ] JobCatalog
- [ ] Locations
- [ ] Marketplace
- [ ] Payroll
- [ ] PayrollEmployees
- [ ] PayrollIntegrationBase
- [ ] Performance
- [ ] Posts
- [x] ProjectManagement
- [ ] ShiftManagement
- [ ] Tasks
- [x] Teams
- [ ] Timeoff
- [ ] TimePlanning
- [ ] TimeSettings
- [ ] Trainings
- [ ] WorkSchedule
- [ ] Webhooks

## Contribute

Feel free to contribute! Please fork this repository, install the development dependencies with `uv sync --dev`
and create pull request.
