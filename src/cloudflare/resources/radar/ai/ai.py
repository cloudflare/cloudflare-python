# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bots.bots import (
    BotsResource,
    AsyncBotsResource,
    BotsResourceWithRawResponse,
    AsyncBotsResourceWithRawResponse,
    BotsResourceWithStreamingResponse,
    AsyncBotsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .timeseries_groups import (
    TimeseriesGroupsResource,
    AsyncTimeseriesGroupsResource,
    TimeseriesGroupsResourceWithRawResponse,
    AsyncTimeseriesGroupsResourceWithRawResponse,
    TimeseriesGroupsResourceWithStreamingResponse,
    AsyncTimeseriesGroupsResourceWithStreamingResponse,
)
from .inference.inference import (
    InferenceResource,
    AsyncInferenceResource,
    InferenceResourceWithRawResponse,
    AsyncInferenceResourceWithRawResponse,
    InferenceResourceWithStreamingResponse,
    AsyncInferenceResourceWithStreamingResponse,
)

__all__ = ["AIResource", "AsyncAIResource"]


class AIResource(SyncAPIResource):
    @cached_property
    def inference(self) -> InferenceResource:
        return InferenceResource(self._client)

    @cached_property
    def bots(self) -> BotsResource:
        return BotsResource(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResource:
        return TimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AIResourceWithStreamingResponse(self)


class AsyncAIResource(AsyncAPIResource):
    @cached_property
    def inference(self) -> AsyncInferenceResource:
        return AsyncInferenceResource(self._client)

    @cached_property
    def bots(self) -> AsyncBotsResource:
        return AsyncBotsResource(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResource:
        return AsyncTimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAIResourceWithStreamingResponse(self)


class AIResourceWithRawResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

    @cached_property
    def inference(self) -> InferenceResourceWithRawResponse:
        return InferenceResourceWithRawResponse(self._ai.inference)

    @cached_property
    def bots(self) -> BotsResourceWithRawResponse:
        return BotsResourceWithRawResponse(self._ai.bots)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._ai.timeseries_groups)


class AsyncAIResourceWithRawResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

    @cached_property
    def inference(self) -> AsyncInferenceResourceWithRawResponse:
        return AsyncInferenceResourceWithRawResponse(self._ai.inference)

    @cached_property
    def bots(self) -> AsyncBotsResourceWithRawResponse:
        return AsyncBotsResourceWithRawResponse(self._ai.bots)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._ai.timeseries_groups)


class AIResourceWithStreamingResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

    @cached_property
    def inference(self) -> InferenceResourceWithStreamingResponse:
        return InferenceResourceWithStreamingResponse(self._ai.inference)

    @cached_property
    def bots(self) -> BotsResourceWithStreamingResponse:
        return BotsResourceWithStreamingResponse(self._ai.bots)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._ai.timeseries_groups)


class AsyncAIResourceWithStreamingResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

    @cached_property
    def inference(self) -> AsyncInferenceResourceWithStreamingResponse:
        return AsyncInferenceResourceWithStreamingResponse(self._ai.inference)

    @cached_property
    def bots(self) -> AsyncBotsResourceWithStreamingResponse:
        return AsyncBotsResourceWithStreamingResponse(self._ai.bots)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._ai.timeseries_groups)
