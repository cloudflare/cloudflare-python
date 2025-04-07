# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from .query import (
    QueryResource,
    AsyncQueryResource,
    QueryResourceWithRawResponse,
    AsyncQueryResourceWithRawResponse,
    QueryResourceWithStreamingResponse,
    AsyncQueryResourceWithStreamingResponse,
)
from .values import (
    ValuesResource,
    AsyncValuesResource,
    ValuesResourceWithRawResponse,
    AsyncValuesResourceWithRawResponse,
    ValuesResourceWithStreamingResponse,
    AsyncValuesResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TelemetryResource", "AsyncTelemetryResource"]


class TelemetryResource(SyncAPIResource):
    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def query(self) -> QueryResource:
        return QueryResource(self._client)

    @cached_property
    def values(self) -> ValuesResource:
        return ValuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TelemetryResourceWithStreamingResponse(self)


class AsyncTelemetryResource(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def query(self) -> AsyncQueryResource:
        return AsyncQueryResource(self._client)

    @cached_property
    def values(self) -> AsyncValuesResource:
        return AsyncValuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTelemetryResourceWithStreamingResponse(self)


class TelemetryResourceWithRawResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._telemetry.keys)

    @cached_property
    def query(self) -> QueryResourceWithRawResponse:
        return QueryResourceWithRawResponse(self._telemetry.query)

    @cached_property
    def values(self) -> ValuesResourceWithRawResponse:
        return ValuesResourceWithRawResponse(self._telemetry.values)


class AsyncTelemetryResourceWithRawResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._telemetry.keys)

    @cached_property
    def query(self) -> AsyncQueryResourceWithRawResponse:
        return AsyncQueryResourceWithRawResponse(self._telemetry.query)

    @cached_property
    def values(self) -> AsyncValuesResourceWithRawResponse:
        return AsyncValuesResourceWithRawResponse(self._telemetry.values)


class TelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._telemetry.keys)

    @cached_property
    def query(self) -> QueryResourceWithStreamingResponse:
        return QueryResourceWithStreamingResponse(self._telemetry.query)

    @cached_property
    def values(self) -> ValuesResourceWithStreamingResponse:
        return ValuesResourceWithStreamingResponse(self._telemetry.values)


class AsyncTelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._telemetry.keys)

    @cached_property
    def query(self) -> AsyncQueryResourceWithStreamingResponse:
        return AsyncQueryResourceWithStreamingResponse(self._telemetry.query)

    @cached_property
    def values(self) -> AsyncValuesResourceWithStreamingResponse:
        return AsyncValuesResourceWithStreamingResponse(self._telemetry.values)
