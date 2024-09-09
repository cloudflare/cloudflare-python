# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .widgets import (
    WidgetsResource,
    AsyncWidgetsResource,
    WidgetsResourceWithRawResponse,
    AsyncWidgetsResourceWithRawResponse,
    WidgetsResourceWithStreamingResponse,
    AsyncWidgetsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ChallengesResource", "AsyncChallengesResource"]


class ChallengesResource(SyncAPIResource):
    @cached_property
    def widgets(self) -> WidgetsResource:
        return WidgetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChallengesResourceWithRawResponse:
        return ChallengesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChallengesResourceWithStreamingResponse:
        return ChallengesResourceWithStreamingResponse(self)


class AsyncChallengesResource(AsyncAPIResource):
    @cached_property
    def widgets(self) -> AsyncWidgetsResource:
        return AsyncWidgetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChallengesResourceWithRawResponse:
        return AsyncChallengesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChallengesResourceWithStreamingResponse:
        return AsyncChallengesResourceWithStreamingResponse(self)


class ChallengesResourceWithRawResponse:
    def __init__(self, challenges: ChallengesResource) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> WidgetsResourceWithRawResponse:
        return WidgetsResourceWithRawResponse(self._challenges.widgets)


class AsyncChallengesResourceWithRawResponse:
    def __init__(self, challenges: AsyncChallengesResource) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> AsyncWidgetsResourceWithRawResponse:
        return AsyncWidgetsResourceWithRawResponse(self._challenges.widgets)


class ChallengesResourceWithStreamingResponse:
    def __init__(self, challenges: ChallengesResource) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> WidgetsResourceWithStreamingResponse:
        return WidgetsResourceWithStreamingResponse(self._challenges.widgets)


class AsyncChallengesResourceWithStreamingResponse:
    def __init__(self, challenges: AsyncChallengesResource) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> AsyncWidgetsResourceWithStreamingResponse:
        return AsyncWidgetsResourceWithStreamingResponse(self._challenges.widgets)
