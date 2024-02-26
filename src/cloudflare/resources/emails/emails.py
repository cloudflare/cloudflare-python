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

__all__ = ["Emails", "AsyncEmails"]


class Emails(SyncAPIResource):
    @cached_property
    def routing(self) -> Routing:
        return Routing(self._client)

    @cached_property
    def with_raw_response(self) -> EmailsWithRawResponse:
        return EmailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsWithStreamingResponse:
        return EmailsWithStreamingResponse(self)


class AsyncEmails(AsyncAPIResource):
    @cached_property
    def routing(self) -> AsyncRouting:
        return AsyncRouting(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailsWithRawResponse:
        return AsyncEmailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsWithStreamingResponse:
        return AsyncEmailsWithStreamingResponse(self)


class EmailsWithRawResponse:
    def __init__(self, emails: Emails) -> None:
        self._emails = emails

    @cached_property
    def routing(self) -> RoutingWithRawResponse:
        return RoutingWithRawResponse(self._emails.routing)


class AsyncEmailsWithRawResponse:
    def __init__(self, emails: AsyncEmails) -> None:
        self._emails = emails

    @cached_property
    def routing(self) -> AsyncRoutingWithRawResponse:
        return AsyncRoutingWithRawResponse(self._emails.routing)


class EmailsWithStreamingResponse:
    def __init__(self, emails: Emails) -> None:
        self._emails = emails

    @cached_property
    def routing(self) -> RoutingWithStreamingResponse:
        return RoutingWithStreamingResponse(self._emails.routing)


class AsyncEmailsWithStreamingResponse:
    def __init__(self, emails: AsyncEmails) -> None:
        self._emails = emails

    @cached_property
    def routing(self) -> AsyncRoutingWithStreamingResponse:
        return AsyncRoutingWithStreamingResponse(self._emails.routing)
