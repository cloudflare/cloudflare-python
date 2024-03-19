# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .routing import (
    Routing,
    AsyncRouting,
    RoutingWithRawResponse,
    AsyncRoutingWithRawResponse,
    RoutingWithStreamingResponse,
    AsyncRoutingWithStreamingResponse,
)
from .security import (
    Security,
    AsyncSecurity,
    SecurityWithRawResponse,
    AsyncSecurityWithRawResponse,
    SecurityWithStreamingResponse,
    AsyncSecurityWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .routing.routing import Routing, AsyncRouting
from .security.security import Security, AsyncSecurity

__all__ = ["Email", "AsyncEmail"]


class Email(SyncAPIResource):
    @cached_property
    def routing(self) -> Routing:
        return Routing(self._client)

    @cached_property
    def security(self) -> Security:
        return Security(self._client)

    @cached_property
    def with_raw_response(self) -> EmailWithRawResponse:
        return EmailWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailWithStreamingResponse:
        return EmailWithStreamingResponse(self)


class AsyncEmail(AsyncAPIResource):
    @cached_property
    def routing(self) -> AsyncRouting:
        return AsyncRouting(self._client)

    @cached_property
    def security(self) -> AsyncSecurity:
        return AsyncSecurity(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailWithRawResponse:
        return AsyncEmailWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailWithStreamingResponse:
        return AsyncEmailWithStreamingResponse(self)


class EmailWithRawResponse:
    def __init__(self, email: Email) -> None:
        self._email = email

    @cached_property
    def routing(self) -> RoutingWithRawResponse:
        return RoutingWithRawResponse(self._email.routing)

    @cached_property
    def security(self) -> SecurityWithRawResponse:
        return SecurityWithRawResponse(self._email.security)


class AsyncEmailWithRawResponse:
    def __init__(self, email: AsyncEmail) -> None:
        self._email = email

    @cached_property
    def routing(self) -> AsyncRoutingWithRawResponse:
        return AsyncRoutingWithRawResponse(self._email.routing)

    @cached_property
    def security(self) -> AsyncSecurityWithRawResponse:
        return AsyncSecurityWithRawResponse(self._email.security)


class EmailWithStreamingResponse:
    def __init__(self, email: Email) -> None:
        self._email = email

    @cached_property
    def routing(self) -> RoutingWithStreamingResponse:
        return RoutingWithStreamingResponse(self._email.routing)

    @cached_property
    def security(self) -> SecurityWithStreamingResponse:
        return SecurityWithStreamingResponse(self._email.security)


class AsyncEmailWithStreamingResponse:
    def __init__(self, email: AsyncEmail) -> None:
        self._email = email

    @cached_property
    def routing(self) -> AsyncRoutingWithStreamingResponse:
        return AsyncRoutingWithStreamingResponse(self._email.routing)

    @cached_property
    def security(self) -> AsyncSecurityWithStreamingResponse:
        return AsyncSecurityWithStreamingResponse(self._email.security)
