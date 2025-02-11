from factorialhr.endpoints import _base


class BreakConfiguration(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/attendance/break_configurations'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-break-configurations."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-break-configurations."""
        return await self.api.post(self._endpoint, **kwargs)

    async def update(self, *, break_configuration_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-attendance-break-configurations-id."""
        return await self.api.put(f'{self._endpoint}/{break_configuration_id}', **kwargs)

    async def single(self, *, break_configuration_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-break-configurations-id."""
        return await self.api.get(f'{self._endpoint}/{break_configuration_id}', **kwargs)


class EditTimesheetRequest(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/attendance/edit_timesheet_requests'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-edit-timesheet-requests."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-edit-timesheet-requests."""
        return await self.api.post(self._endpoint, **kwargs)

    async def delete(self, *, edit_time_sheet_request_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-attendance-edit-timesheet-requests-id."""
        return await self.api.delete(f'{self._endpoint}/{edit_time_sheet_request_id}', **kwargs)

    async def update(self, *, edit_time_sheet_request_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-attendance-edit-timesheet-requests-id."""
        return await self.api.put(f'{self._endpoint}/{edit_time_sheet_request_id}', **kwargs)

    async def single(self, *, edit_time_sheet_request_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-edit-timesheet-requests-id."""
        return await self.api.get(f'{self._endpoint}/{edit_time_sheet_request_id}', **kwargs)


class EstimatedTimes(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/attendance/estimated_times'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-estimated-times."""
        return await self.api.get(self._endpoint, **kwargs)


class OpenShifts(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/attendance/open_shifts'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-open-shifts."""
        return await self.api.get(self._endpoint, **kwargs)


class OverTimeRequest(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/attendance/overtime_requests'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-overtime-requests."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-overtime-requests."""
        return await self.api.post(self._endpoint, **kwargs)

    async def delete(self, *, over_time_request_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-attendance-overtime-requests-id."""
        return await self.api.delete(f'{self._endpoint}/{over_time_request_id}', **kwargs)

    async def update(self, *, over_time_request_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-attendance-overtime-requests-id."""
        return await self.api.put(f'{self._endpoint}/{over_time_request_id}', **kwargs)

    async def single(self, *, over_time_request_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-overtime-requests-id."""
        return await self.api.get(f'{self._endpoint}/{over_time_request_id}', **kwargs)

    async def approve(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-overtime-requests-approve."""
        return await self.api.post(self._endpoint, **kwargs)

    async def reject(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-overtime-requests-reject."""
        return await self.api.post(self._endpoint, **kwargs)


class Shift(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/attendance/shifts'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-shifts."""
        return await self.api.get(self._endpoint, **kwargs)

    async def create(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-shifts."""
        return await self.api.post(self._endpoint, **kwargs)

    async def delete(self, *, over_time_request_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/delete_api-2025-01-01-resources-attendance-shifts-id."""
        return await self.api.delete(f'{self._endpoint}/{over_time_request_id}', **kwargs)

    async def update(self, *, over_time_request_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/put_api-2025-01-01-resources-attendance-shifts-id."""
        return await self.api.put(f'{self._endpoint}/{over_time_request_id}', **kwargs)

    async def single(self, *, over_time_request_id: int, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-shifts-id."""
        return await self.api.get(f'{self._endpoint}/{over_time_request_id}', **kwargs)

    async def autofill(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-shifts-autofill."""
        return await self.api.post(self._endpoint, **kwargs)

    async def break_end(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-shifts-break-end."""
        return await self.api.post(self._endpoint, **kwargs)

    async def break_start(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-shifts-break-start."""
        return await self.api.post(self._endpoint, **kwargs)

    async def clock_in(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-shifts-clock-in."""
        return await self.api.post(self._endpoint, **kwargs)

    async def clock_out(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-shifts-clock-out."""
        return await self.api.post(self._endpoint, **kwargs)

    async def clock_in_out(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/post_api-2025-01-01-resources-attendance-shifts-toggle-clock."""
        return await self.api.post(self._endpoint, **kwargs)


class WorkedTime(_base.Endpoint):
    @property
    def _endpoint(self) -> str:
        return '/2025-01-01/resources/attendance/worked_times'

    async def all(self, **kwargs) -> dict:
        """Implement https://apidoc.factorialhr.com/reference/get_api-2025-01-01-resources-attendance-worked-times."""
        return await self.api.get(self._endpoint, **kwargs)
