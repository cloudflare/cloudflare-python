# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .routing import (
    Routing,
    AsyncRouting,
    RoutingWithRawResponse,
    AsyncRoutingWithRawResponse,
    RoutingWithStreamingResponse,
    AsyncRoutingWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .routing.routing import Routing, AsyncRouting

__all__ = ["EmailRouting", "AsyncEmailRouting"]


class EmailRouting(SyncAPIResource):
    @cached_property
    def routing(self) -> Routing:
        return Routing(self._client)

    @cached_property
    def with_raw_response(self) -> EmailRoutingWithRawResponse:
        return EmailRoutingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailRoutingWithStreamingResponse:
        return EmailRoutingWithStreamingResponse(self)


class AsyncEmailRouting(AsyncAPIResource):
    @cached_property
    def routing(self) -> AsyncRouting:
        return AsyncRouting(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailRoutingWithRawResponse:
        return AsyncEmailRoutingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailRoutingWithStreamingResponse:
        return AsyncEmailRoutingWithStreamingResponse(self)


class EmailRoutingWithRawResponse:
    def __init__(self, email_routing: EmailRouting) -> None:
        self._email_routing = email_routing

    @cached_property
    def routing(self) -> RoutingWithRawResponse:
        return RoutingWithRawResponse(self._email_routing.routing)


class AsyncEmailRoutingWithRawResponse:
    def __init__(self, email_routing: AsyncEmailRouting) -> None:
        self._email_routing = email_routing

    @cached_property
    def routing(self) -> AsyncRoutingWithRawResponse:
        return AsyncRoutingWithRawResponse(self._email_routing.routing)


class EmailRoutingWithStreamingResponse:
    def __init__(self, email_routing: EmailRouting) -> None:
        self._email_routing = email_routing

    @cached_property
    def routing(self) -> RoutingWithStreamingResponse:
        return RoutingWithStreamingResponse(self._email_routing.routing)


class AsyncEmailRoutingWithStreamingResponse:
    def __init__(self, email_routing: AsyncEmailRouting) -> None:
        self._email_routing = email_routing

    @cached_property
    def routing(self) -> AsyncRoutingWithStreamingResponse:
        return AsyncRoutingWithStreamingResponse(self._email_routing.routing)
