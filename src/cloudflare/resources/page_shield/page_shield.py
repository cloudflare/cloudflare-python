# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .policies import (
    Policies,
    AsyncPolicies,
    PoliciesWithRawResponse,
    AsyncPoliciesWithRawResponse,
    PoliciesWithStreamingResponse,
    AsyncPoliciesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .connections import (
    Connections,
    AsyncConnections,
    ConnectionsWithRawResponse,
    AsyncConnectionsWithRawResponse,
    ConnectionsWithStreamingResponse,
    AsyncConnectionsWithStreamingResponse,
)

__all__ = ["PageShield", "AsyncPageShield"]


class PageShield(SyncAPIResource):
    @cached_property
    def connections(self) -> Connections:
        return Connections(self._client)

    @cached_property
    def policies(self) -> Policies:
        return Policies(self._client)

    @cached_property
    def with_raw_response(self) -> PageShieldWithRawResponse:
        return PageShieldWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PageShieldWithStreamingResponse:
        return PageShieldWithStreamingResponse(self)


class AsyncPageShield(AsyncAPIResource):
    @cached_property
    def connections(self) -> AsyncConnections:
        return AsyncConnections(self._client)

    @cached_property
    def policies(self) -> AsyncPolicies:
        return AsyncPolicies(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPageShieldWithRawResponse:
        return AsyncPageShieldWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPageShieldWithStreamingResponse:
        return AsyncPageShieldWithStreamingResponse(self)


class PageShieldWithRawResponse:
    def __init__(self, page_shield: PageShield) -> None:
        self._page_shield = page_shield

    @cached_property
    def connections(self) -> ConnectionsWithRawResponse:
        return ConnectionsWithRawResponse(self._page_shield.connections)

    @cached_property
    def policies(self) -> PoliciesWithRawResponse:
        return PoliciesWithRawResponse(self._page_shield.policies)


class AsyncPageShieldWithRawResponse:
    def __init__(self, page_shield: AsyncPageShield) -> None:
        self._page_shield = page_shield

    @cached_property
    def connections(self) -> AsyncConnectionsWithRawResponse:
        return AsyncConnectionsWithRawResponse(self._page_shield.connections)

    @cached_property
    def policies(self) -> AsyncPoliciesWithRawResponse:
        return AsyncPoliciesWithRawResponse(self._page_shield.policies)


class PageShieldWithStreamingResponse:
    def __init__(self, page_shield: PageShield) -> None:
        self._page_shield = page_shield

    @cached_property
    def connections(self) -> ConnectionsWithStreamingResponse:
        return ConnectionsWithStreamingResponse(self._page_shield.connections)

    @cached_property
    def policies(self) -> PoliciesWithStreamingResponse:
        return PoliciesWithStreamingResponse(self._page_shield.policies)


class AsyncPageShieldWithStreamingResponse:
    def __init__(self, page_shield: AsyncPageShield) -> None:
        self._page_shield = page_shield

    @cached_property
    def connections(self) -> AsyncConnectionsWithStreamingResponse:
        return AsyncConnectionsWithStreamingResponse(self._page_shield.connections)

    @cached_property
    def policies(self) -> AsyncPoliciesWithStreamingResponse:
        return AsyncPoliciesWithStreamingResponse(self._page_shield.policies)
