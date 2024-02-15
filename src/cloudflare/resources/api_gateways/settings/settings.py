# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .schema_validation import (
    SchemaValidation,
    AsyncSchemaValidation,
    SchemaValidationWithRawResponse,
    AsyncSchemaValidationWithRawResponse,
    SchemaValidationWithStreamingResponse,
    AsyncSchemaValidationWithStreamingResponse,
)

__all__ = ["Settings", "AsyncSettings"]


class Settings(SyncAPIResource):
    @cached_property
    def schema_validation(self) -> SchemaValidation:
        return SchemaValidation(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self)


class AsyncSettings(AsyncAPIResource):
    @cached_property
    def schema_validation(self) -> AsyncSchemaValidation:
        return AsyncSchemaValidation(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self)


class SettingsWithRawResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @cached_property
    def schema_validation(self) -> SchemaValidationWithRawResponse:
        return SchemaValidationWithRawResponse(self._settings.schema_validation)


class AsyncSettingsWithRawResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationWithRawResponse:
        return AsyncSchemaValidationWithRawResponse(self._settings.schema_validation)


class SettingsWithStreamingResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @cached_property
    def schema_validation(self) -> SchemaValidationWithStreamingResponse:
        return SchemaValidationWithStreamingResponse(self._settings.schema_validation)


class AsyncSettingsWithStreamingResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationWithStreamingResponse:
        return AsyncSchemaValidationWithStreamingResponse(self._settings.schema_validation)
