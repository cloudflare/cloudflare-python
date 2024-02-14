# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .routings import (
    Routings,
    AsyncRoutings,
    RoutingsWithRawResponse,
    AsyncRoutingsWithRawResponse,
    RoutingsWithStreamingResponse,
    AsyncRoutingsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .routings.routings import Routings, AsyncRoutings

__all__ = ["Emails", "AsyncEmails"]


class Emails(SyncAPIResource):
    @cached_property
    def routings(self) -> Routings:
        return Routings(self._client)

    @cached_property
    def with_raw_response(self) -> EmailsWithRawResponse:
        return EmailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsWithStreamingResponse:
        return EmailsWithStreamingResponse(self)


class AsyncEmails(AsyncAPIResource):
    @cached_property
    def routings(self) -> AsyncRoutings:
        return AsyncRoutings(self._client)

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
    def routings(self) -> RoutingsWithRawResponse:
        return RoutingsWithRawResponse(self._emails.routings)


class AsyncEmailsWithRawResponse:
    def __init__(self, emails: AsyncEmails) -> None:
        self._emails = emails

    @cached_property
    def routings(self) -> AsyncRoutingsWithRawResponse:
        return AsyncRoutingsWithRawResponse(self._emails.routings)


class EmailsWithStreamingResponse:
    def __init__(self, emails: Emails) -> None:
        self._emails = emails

    @cached_property
    def routings(self) -> RoutingsWithStreamingResponse:
        return RoutingsWithStreamingResponse(self._emails.routings)


class AsyncEmailsWithStreamingResponse:
    def __init__(self, emails: AsyncEmails) -> None:
        self._emails = emails

    @cached_property
    def routings(self) -> AsyncRoutingsWithStreamingResponse:
        return AsyncRoutingsWithStreamingResponse(self._emails.routings)
