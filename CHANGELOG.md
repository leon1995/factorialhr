# Changelog

All notable changes to factorialhr module will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0)

## [Unreleased]

## [4.1.1] - 2025-08-23

### Fixed

- fixed some typing of models

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