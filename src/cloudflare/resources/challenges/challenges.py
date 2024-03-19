# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .widgets import (
    Widgets,
    AsyncWidgets,
    WidgetsWithRawResponse,
    AsyncWidgetsWithRawResponse,
    WidgetsWithStreamingResponse,
    AsyncWidgetsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Challenges", "AsyncChallenges"]


class Challenges(SyncAPIResource):
    @cached_property
    def widgets(self) -> Widgets:
        return Widgets(self._client)

    @cached_property
    def with_raw_response(self) -> ChallengesWithRawResponse:
        return ChallengesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChallengesWithStreamingResponse:
        return ChallengesWithStreamingResponse(self)


class AsyncChallenges(AsyncAPIResource):
    @cached_property
    def widgets(self) -> AsyncWidgets:
        return AsyncWidgets(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChallengesWithRawResponse:
        return AsyncChallengesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChallengesWithStreamingResponse:
        return AsyncChallengesWithStreamingResponse(self)


class ChallengesWithRawResponse:
    def __init__(self, challenges: Challenges) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> WidgetsWithRawResponse:
        return WidgetsWithRawResponse(self._challenges.widgets)


class AsyncChallengesWithRawResponse:
    def __init__(self, challenges: AsyncChallenges) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> AsyncWidgetsWithRawResponse:
        return AsyncWidgetsWithRawResponse(self._challenges.widgets)


class ChallengesWithStreamingResponse:
    def __init__(self, challenges: Challenges) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> WidgetsWithStreamingResponse:
        return WidgetsWithStreamingResponse(self._challenges.widgets)


class AsyncChallengesWithStreamingResponse:
    def __init__(self, challenges: AsyncChallenges) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> AsyncWidgetsWithStreamingResponse:
        return AsyncWidgetsWithStreamingResponse(self._challenges.widgets)
