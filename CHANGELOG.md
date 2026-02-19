# Changelog

All notable changes to factorialhr module will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0)

## [Unreleased]

### Changed

- support api version `2026-01-01`. Checkout full [changelog](https://apidoc.factorialhr.com/changelog/changelog_2026-01-01)

### Added

- `EmployeesEndpoint.set_regular_access_start_date()` method
- `ProcurementType`, `ProcurementTypesEndpoint`, `PurchaseOrder`, `PurchaseOrdersEndpoint`, `PurchaseRequest`, `PurchaseRequestsEndpoint` classes for procurement management
- `PlannedRecord`, `PlannedRecordsEndpoint` classes for project management planned records
- `budget_id`, `project_id`, `cost_center_ids` fields to `Expensable`, `Expense`, `Mileage`, and `PerDiem` models
- `updated_at` field to `CustomFieldValue` model
- `resource_id` field to `CustomResourcesValue` model (removed deprecated value fields)
- `job_catalog_tree_node_uuid` and `is_reference` fields to `ContractVersion` model
- `job_catalog_tree_node_uuid` field to `ContractVersionHistory` model
- `syncable_type` field to `SyncableItem` model
- `days_taken` field to `Leave` model
- `thumbnail`, `is_mandatory`, `total_duration` fields to `Training` model
- `completed_attendances_count`, `total_attendances_count` fields to `TrainingClass` model
- `description`, `status`, `code`, `start_date`, `due_date`, `is_billable` fields to `Subproject` model
- `BudgetOption`, `BudgetOptionsEndpoint` for finance budget options (Reads all / Reads a single)
- `ItAsset`, `ItAssetsEndpoint` and `ItAssetModel`, `ItAssetModelsEndpoint` for IT management
- `NodeAttribute`, `NodeAttributesEndpoint`, `JobCatalogNode`, `TreeNodesEndpoint` for job catalog (node attributes and tree nodes with `job_catalog_title`)

### Note

- New query parameters (e.g. `updated_at_gteq`, `company_identifier`, `job_catalog_tree_node_uuids[]`, `search`, `category`, `type_is_payable`, `is_mandatory`, `with_current_training_classes`) and request body fields (e.g. `time_settings_break_configuration_id`, `approved`, `skip_notifications`, `legal_entity_id`) are supported by passing them via `params` or the request `data` to the existing endpoint methods.

## [5.0.1] - 2025-10-31

### Fixed

- fixed typing in `ApiClient.base_url` to `str` intead of `Literal` as the old demo server is deprecated. 

## [5.0.0] - 2025-10-31

### Changed

- support api version `2025-10-01`. Checkout full [changelog](https://apidoc.factorialhr.com/changelog/changelog_2025-10-01)

## [4.1.0] - 2025-08-22

### Added

- fixed some missed exports
- made api models frozen

## [4.0.0] - 2025-08-19

### Added

- enter `httpx.AsyncClient` on enter of `ApiClient`
- pass `**kwargs` from `ApiClient` to `httpx.AsyncClient`
- method to fetch all data from an endpoint
- `anyio` dependency
- nearly all endpoints now supported

### Changed

- return wrapper around pydantic models for list requests, otherwise pydantic model
- use `anyio` instead of `asyncio` to optionally support trio

## [3.0.0] - 2025-02-11

### Added

- oauth2 support
- api version 2025-01-01

### Changed

- returning json instead of pydantic models
- Change repository structure to a src/package style
- Linter. Use ruff instead of black and isort

## [2.0.0] - 2023-10-06

### Added

- some missing url parameters

### Changed

- changed meaning of `kwargs` to be able to pass `timeout` and other parameters to the request. use `data` as the body parameter

## [1.1.0] - 2023-08-07

### Fixed

- renamed `birthday` of employee model to `birthday_on` as it has changed by the api

## [1.0.2] - 2023-03-27

### Added

- added `py.typed` file

## [1.0.1] - 2023-03-27

### Changed

- use `httpx` instead of `aiohttp`

## [1.0.0] - 2023-03-23

### Added

- initial project release