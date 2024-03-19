# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .flag import (
    Flag,
    AsyncFlag,
    FlagWithRawResponse,
    AsyncFlagWithRawResponse,
    FlagWithStreamingResponse,
    AsyncFlagWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Retention", "AsyncRetention"]


class Retention(SyncAPIResource):
    @cached_property
    def flag(self) -> Flag:
        return Flag(self._client)

    @cached_property
    def with_raw_response(self) -> RetentionWithRawResponse:
        return RetentionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetentionWithStreamingResponse:
        return RetentionWithStreamingResponse(self)


class AsyncRetention(AsyncAPIResource):
    @cached_property
    def flag(self) -> AsyncFlag:
        return AsyncFlag(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRetentionWithRawResponse:
        return AsyncRetentionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetentionWithStreamingResponse:
        return AsyncRetentionWithStreamingResponse(self)


class RetentionWithRawResponse:
    def __init__(self, retention: Retention) -> None:
        self._retention = retention

    @cached_property
    def flag(self) -> FlagWithRawResponse:
        return FlagWithRawResponse(self._retention.flag)


class AsyncRetentionWithRawResponse:
    def __init__(self, retention: AsyncRetention) -> None:
        self._retention = retention

    @cached_property
    def flag(self) -> AsyncFlagWithRawResponse:
        return AsyncFlagWithRawResponse(self._retention.flag)


class RetentionWithStreamingResponse:
    def __init__(self, retention: Retention) -> None:
        self._retention = retention

    @cached_property
    def flag(self) -> FlagWithStreamingResponse:
        return FlagWithStreamingResponse(self._retention.flag)


class AsyncRetentionWithStreamingResponse:
    def __init__(self, retention: AsyncRetention) -> None:
        self._retention = retention

    @cached_property
    def flag(self) -> AsyncFlagWithStreamingResponse:
        return AsyncFlagWithStreamingResponse(self._retention.flag)
