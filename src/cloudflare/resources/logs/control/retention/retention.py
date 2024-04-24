# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .flag import (
    FlagResource,
    AsyncFlagResource,
    FlagResourceWithRawResponse,
    AsyncFlagResourceWithRawResponse,
    FlagResourceWithStreamingResponse,
    AsyncFlagResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RetentionResource", "AsyncRetentionResource"]


class RetentionResource(SyncAPIResource):
    @cached_property
    def flag(self) -> FlagResource:
        return FlagResource(self._client)

    @cached_property
    def with_raw_response(self) -> RetentionResourceWithRawResponse:
        return RetentionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetentionResourceWithStreamingResponse:
        return RetentionResourceWithStreamingResponse(self)


class AsyncRetentionResource(AsyncAPIResource):
    @cached_property
    def flag(self) -> AsyncFlagResource:
        return AsyncFlagResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRetentionResourceWithRawResponse:
        return AsyncRetentionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetentionResourceWithStreamingResponse:
        return AsyncRetentionResourceWithStreamingResponse(self)


class RetentionResourceWithRawResponse:
    def __init__(self, retention: RetentionResource) -> None:
        self._retention = retention

    @cached_property
    def flag(self) -> FlagResourceWithRawResponse:
        return FlagResourceWithRawResponse(self._retention.flag)


class AsyncRetentionResourceWithRawResponse:
    def __init__(self, retention: AsyncRetentionResource) -> None:
        self._retention = retention

    @cached_property
    def flag(self) -> AsyncFlagResourceWithRawResponse:
        return AsyncFlagResourceWithRawResponse(self._retention.flag)


class RetentionResourceWithStreamingResponse:
    def __init__(self, retention: RetentionResource) -> None:
        self._retention = retention

    @cached_property
    def flag(self) -> FlagResourceWithStreamingResponse:
        return FlagResourceWithStreamingResponse(self._retention.flag)


class AsyncRetentionResourceWithStreamingResponse:
    def __init__(self, retention: AsyncRetentionResource) -> None:
        self._retention = retention

    @cached_property
    def flag(self) -> AsyncFlagResourceWithStreamingResponse:
        return AsyncFlagResourceWithStreamingResponse(self._retention.flag)
