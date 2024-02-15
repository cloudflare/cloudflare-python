# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .verifies import (
    Verifies,
    AsyncVerifies,
    VerifiesWithRawResponse,
    AsyncVerifiesWithRawResponse,
    VerifiesWithStreamingResponse,
    AsyncVerifiesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .availabilities import (
    Availabilities,
    AsyncAvailabilities,
    AvailabilitiesWithRawResponse,
    AsyncAvailabilitiesWithRawResponse,
    AvailabilitiesWithStreamingResponse,
    AsyncAvailabilitiesWithStreamingResponse,
)

__all__ = ["CustomNs", "AsyncCustomNs"]


class CustomNs(SyncAPIResource):
    @cached_property
    def availabilities(self) -> Availabilities:
        return Availabilities(self._client)

    @cached_property
    def verifies(self) -> Verifies:
        return Verifies(self._client)

    @cached_property
    def with_raw_response(self) -> CustomNsWithRawResponse:
        return CustomNsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomNsWithStreamingResponse:
        return CustomNsWithStreamingResponse(self)


class AsyncCustomNs(AsyncAPIResource):
    @cached_property
    def availabilities(self) -> AsyncAvailabilities:
        return AsyncAvailabilities(self._client)

    @cached_property
    def verifies(self) -> AsyncVerifies:
        return AsyncVerifies(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomNsWithRawResponse:
        return AsyncCustomNsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomNsWithStreamingResponse:
        return AsyncCustomNsWithStreamingResponse(self)


class CustomNsWithRawResponse:
    def __init__(self, custom_ns: CustomNs) -> None:
        self._custom_ns = custom_ns

    @cached_property
    def availabilities(self) -> AvailabilitiesWithRawResponse:
        return AvailabilitiesWithRawResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> VerifiesWithRawResponse:
        return VerifiesWithRawResponse(self._custom_ns.verifies)


class AsyncCustomNsWithRawResponse:
    def __init__(self, custom_ns: AsyncCustomNs) -> None:
        self._custom_ns = custom_ns

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesWithRawResponse:
        return AsyncAvailabilitiesWithRawResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> AsyncVerifiesWithRawResponse:
        return AsyncVerifiesWithRawResponse(self._custom_ns.verifies)


class CustomNsWithStreamingResponse:
    def __init__(self, custom_ns: CustomNs) -> None:
        self._custom_ns = custom_ns

    @cached_property
    def availabilities(self) -> AvailabilitiesWithStreamingResponse:
        return AvailabilitiesWithStreamingResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> VerifiesWithStreamingResponse:
        return VerifiesWithStreamingResponse(self._custom_ns.verifies)


class AsyncCustomNsWithStreamingResponse:
    def __init__(self, custom_ns: AsyncCustomNs) -> None:
        self._custom_ns = custom_ns

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesWithStreamingResponse:
        return AsyncAvailabilitiesWithStreamingResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> AsyncVerifiesWithStreamingResponse:
        return AsyncVerifiesWithStreamingResponse(self._custom_ns.verifies)
