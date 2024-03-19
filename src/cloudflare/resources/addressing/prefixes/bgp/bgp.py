# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bindings import (
    Bindings,
    AsyncBindings,
    BindingsWithRawResponse,
    AsyncBindingsWithRawResponse,
    BindingsWithStreamingResponse,
    AsyncBindingsWithStreamingResponse,
)
from .prefixes import (
    Prefixes,
    AsyncPrefixes,
    PrefixesWithRawResponse,
    AsyncPrefixesWithRawResponse,
    PrefixesWithStreamingResponse,
    AsyncPrefixesWithStreamingResponse,
)
from .statuses import (
    Statuses,
    AsyncStatuses,
    StatusesWithRawResponse,
    AsyncStatusesWithRawResponse,
    StatusesWithStreamingResponse,
    AsyncStatusesWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BGP", "AsyncBGP"]


class BGP(SyncAPIResource):
    @cached_property
    def bindings(self) -> Bindings:
        return Bindings(self._client)

    @cached_property
    def prefixes(self) -> Prefixes:
        return Prefixes(self._client)

    @cached_property
    def statuses(self) -> Statuses:
        return Statuses(self._client)

    @cached_property
    def with_raw_response(self) -> BGPWithRawResponse:
        return BGPWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BGPWithStreamingResponse:
        return BGPWithStreamingResponse(self)


class AsyncBGP(AsyncAPIResource):
    @cached_property
    def bindings(self) -> AsyncBindings:
        return AsyncBindings(self._client)

    @cached_property
    def prefixes(self) -> AsyncPrefixes:
        return AsyncPrefixes(self._client)

    @cached_property
    def statuses(self) -> AsyncStatuses:
        return AsyncStatuses(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBGPWithRawResponse:
        return AsyncBGPWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBGPWithStreamingResponse:
        return AsyncBGPWithStreamingResponse(self)


class BGPWithRawResponse:
    def __init__(self, bgp: BGP) -> None:
        self._bgp = bgp

    @cached_property
    def bindings(self) -> BindingsWithRawResponse:
        return BindingsWithRawResponse(self._bgp.bindings)

    @cached_property
    def prefixes(self) -> PrefixesWithRawResponse:
        return PrefixesWithRawResponse(self._bgp.prefixes)

    @cached_property
    def statuses(self) -> StatusesWithRawResponse:
        return StatusesWithRawResponse(self._bgp.statuses)


class AsyncBGPWithRawResponse:
    def __init__(self, bgp: AsyncBGP) -> None:
        self._bgp = bgp

    @cached_property
    def bindings(self) -> AsyncBindingsWithRawResponse:
        return AsyncBindingsWithRawResponse(self._bgp.bindings)

    @cached_property
    def prefixes(self) -> AsyncPrefixesWithRawResponse:
        return AsyncPrefixesWithRawResponse(self._bgp.prefixes)

    @cached_property
    def statuses(self) -> AsyncStatusesWithRawResponse:
        return AsyncStatusesWithRawResponse(self._bgp.statuses)


class BGPWithStreamingResponse:
    def __init__(self, bgp: BGP) -> None:
        self._bgp = bgp

    @cached_property
    def bindings(self) -> BindingsWithStreamingResponse:
        return BindingsWithStreamingResponse(self._bgp.bindings)

    @cached_property
    def prefixes(self) -> PrefixesWithStreamingResponse:
        return PrefixesWithStreamingResponse(self._bgp.prefixes)

    @cached_property
    def statuses(self) -> StatusesWithStreamingResponse:
        return StatusesWithStreamingResponse(self._bgp.statuses)


class AsyncBGPWithStreamingResponse:
    def __init__(self, bgp: AsyncBGP) -> None:
        self._bgp = bgp

    @cached_property
    def bindings(self) -> AsyncBindingsWithStreamingResponse:
        return AsyncBindingsWithStreamingResponse(self._bgp.bindings)

    @cached_property
    def prefixes(self) -> AsyncPrefixesWithStreamingResponse:
        return AsyncPrefixesWithStreamingResponse(self._bgp.prefixes)

    @cached_property
    def statuses(self) -> AsyncStatusesWithStreamingResponse:
        return AsyncStatusesWithStreamingResponse(self._bgp.statuses)
