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
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ChallengesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChallengesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ChallengesResourceWithStreamingResponse(self)


class AsyncChallengesResource(AsyncAPIResource):
    @cached_property
    def widgets(self) -> AsyncWidgetsResource:
        return AsyncWidgetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChallengesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChallengesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChallengesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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
