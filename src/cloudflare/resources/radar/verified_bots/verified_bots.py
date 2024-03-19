# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .top import (
    Top,
    AsyncTop,
    TopWithRawResponse,
    AsyncTopWithRawResponse,
    TopWithStreamingResponse,
    AsyncTopWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["VerifiedBots", "AsyncVerifiedBots"]


class VerifiedBots(SyncAPIResource):
    @cached_property
    def top(self) -> Top:
        return Top(self._client)

    @cached_property
    def with_raw_response(self) -> VerifiedBotsWithRawResponse:
        return VerifiedBotsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifiedBotsWithStreamingResponse:
        return VerifiedBotsWithStreamingResponse(self)


class AsyncVerifiedBots(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTop:
        return AsyncTop(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVerifiedBotsWithRawResponse:
        return AsyncVerifiedBotsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifiedBotsWithStreamingResponse:
        return AsyncVerifiedBotsWithStreamingResponse(self)


class VerifiedBotsWithRawResponse:
    def __init__(self, verified_bots: VerifiedBots) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def top(self) -> TopWithRawResponse:
        return TopWithRawResponse(self._verified_bots.top)


class AsyncVerifiedBotsWithRawResponse:
    def __init__(self, verified_bots: AsyncVerifiedBots) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def top(self) -> AsyncTopWithRawResponse:
        return AsyncTopWithRawResponse(self._verified_bots.top)


class VerifiedBotsWithStreamingResponse:
    def __init__(self, verified_bots: VerifiedBots) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def top(self) -> TopWithStreamingResponse:
        return TopWithStreamingResponse(self._verified_bots.top)


class AsyncVerifiedBotsWithStreamingResponse:
    def __init__(self, verified_bots: AsyncVerifiedBots) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def top(self) -> AsyncTopWithStreamingResponse:
        return AsyncTopWithStreamingResponse(self._verified_bots.top)
