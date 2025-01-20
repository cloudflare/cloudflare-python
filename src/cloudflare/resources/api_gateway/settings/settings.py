# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .schema_validation import (
    SchemaValidationResource,
    AsyncSchemaValidationResource,
    SchemaValidationResourceWithRawResponse,
    AsyncSchemaValidationResourceWithRawResponse,
    SchemaValidationResourceWithStreamingResponse,
    AsyncSchemaValidationResourceWithStreamingResponse,
)

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def schema_validation(self) -> SchemaValidationResource:
        return SchemaValidationResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationResource:
        return AsyncSchemaValidationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def schema_validation(self) -> SchemaValidationResourceWithRawResponse:
        return SchemaValidationResourceWithRawResponse(self._settings.schema_validation)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationResourceWithRawResponse:
        return AsyncSchemaValidationResourceWithRawResponse(self._settings.schema_validation)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def schema_validation(self) -> SchemaValidationResourceWithStreamingResponse:
        return SchemaValidationResourceWithStreamingResponse(self._settings.schema_validation)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationResourceWithStreamingResponse:
        return AsyncSchemaValidationResourceWithStreamingResponse(self._settings.schema_validation)
