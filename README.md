# FactorialHR api python wrapper

This package provides a python wrapper to the [api of FactorialHR](https://apidoc.factorialhr.com/docs).

## Disclaimer

I am not affiliated, associated, authorized, endorsed by, or in any way officially connected with EVERYDAY SOFTWARE, S.L. or FactorialHR, or any of its subsidiaries or its affiliates. The official factorialhr.com website can be found at https://factorialhr.com/

## Usage

Get all employees
```python
import factorialhr
from factorialhr.endpoints import employees

authorizer = factorialhr.ApiKeyAuth('<api_key>')  # checkout other authorization methods
async with factorialhr.ApiClient(auth=authorizer) as api:
    employee_endpoint = employees.Employee(api)
    all_employees = await employee_endpoint.all()  # this fetches the first 100 employees, because the maximum limit is 100
    await api.get_all(employee_endpoint.endpoint)  # fetches all employees. on big companies you might want to increase the timeout by using timeout=httpx.Timeout(...)
```
Get a dictionary with team id as key and a list of member as value
```python
import asyncio

import factorialhr
from factorialhr.endpoints import employees, teams

authorizer = factorialhr.AccessTokenAuth('<access_token>')  # checkout other authorization methods
async with factorialhr.ApiClient(auth=authorizer) as api:
        employees_endpoint = employees.Employee(api)
        teams_endpoint = teams.Team(api)
        all_employees, all_teams = await asyncio.gather(employees_endpoint.all(), teams_endpoint.all())  # remember, this fetches only the first 100 employees and teams, because of the limitation by factorialhr
        employees_by_team_id = {team['id']: [employee['id'] for employee in all_employees['data']] for team in all_teams['data']}
```

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
