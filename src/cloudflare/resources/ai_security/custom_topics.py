# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.ai_security import custom_topic_update_params
from ...types.ai_security.custom_topic_get_response import CustomTopicGetResponse
from ...types.ai_security.custom_topic_update_response import CustomTopicUpdateResponse

__all__ = ["CustomTopicsResource", "AsyncCustomTopicsResource"]


class CustomTopicsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomTopicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CustomTopicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomTopicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CustomTopicsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        topics: Iterable[custom_topic_update_params.Topic] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomTopicUpdateResponse:
        """
        Set the AI Security for Apps custom topic categories for a zone.

        A maximum of 20 custom topics can be configured per zone. Each topic label must
        be 2–20 characters using only lowercase letters (a–z), digits (0–9), and
        hyphens. Each topic description must be 2–50 printable ASCII characters.

        Changes can take up to a minute to propagate to the zone.

        Args:
          zone_id: Defines the zone.

          topics: Custom topic categories for AI Security for Apps content detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            path_template("/zones/{zone_id}/ai-security/custom-topics", zone_id=zone_id),
            body=maybe_transform({"topics": topics}, custom_topic_update_params.CustomTopicUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomTopicUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomTopicUpdateResponse], ResultWrapper[CustomTopicUpdateResponse]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomTopicGetResponse:
        """
        Get the AI Security for Apps custom topic categories for a zone.

        Args:
          zone_id: Defines the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/ai-security/custom-topics", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomTopicGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomTopicGetResponse], ResultWrapper[CustomTopicGetResponse]),
        )


class AsyncCustomTopicsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomTopicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomTopicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomTopicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCustomTopicsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        topics: Iterable[custom_topic_update_params.Topic] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomTopicUpdateResponse:
        """
        Set the AI Security for Apps custom topic categories for a zone.

        A maximum of 20 custom topics can be configured per zone. Each topic label must
        be 2–20 characters using only lowercase letters (a–z), digits (0–9), and
        hyphens. Each topic description must be 2–50 printable ASCII characters.

        Changes can take up to a minute to propagate to the zone.

        Args:
          zone_id: Defines the zone.

          topics: Custom topic categories for AI Security for Apps content detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            path_template("/zones/{zone_id}/ai-security/custom-topics", zone_id=zone_id),
            body=await async_maybe_transform({"topics": topics}, custom_topic_update_params.CustomTopicUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomTopicUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomTopicUpdateResponse], ResultWrapper[CustomTopicUpdateResponse]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomTopicGetResponse:
        """
        Get the AI Security for Apps custom topic categories for a zone.

        Args:
          zone_id: Defines the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/ai-security/custom-topics", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomTopicGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomTopicGetResponse], ResultWrapper[CustomTopicGetResponse]),
        )


class CustomTopicsResourceWithRawResponse:
    def __init__(self, custom_topics: CustomTopicsResource) -> None:
        self._custom_topics = custom_topics

        self.update = to_raw_response_wrapper(
            custom_topics.update,
        )
        self.get = to_raw_response_wrapper(
            custom_topics.get,
        )


class AsyncCustomTopicsResourceWithRawResponse:
    def __init__(self, custom_topics: AsyncCustomTopicsResource) -> None:
        self._custom_topics = custom_topics

        self.update = async_to_raw_response_wrapper(
            custom_topics.update,
        )
        self.get = async_to_raw_response_wrapper(
            custom_topics.get,
        )


class CustomTopicsResourceWithStreamingResponse:
    def __init__(self, custom_topics: CustomTopicsResource) -> None:
        self._custom_topics = custom_topics

        self.update = to_streamed_response_wrapper(
            custom_topics.update,
        )
        self.get = to_streamed_response_wrapper(
            custom_topics.get,
        )


class AsyncCustomTopicsResourceWithStreamingResponse:
    def __init__(self, custom_topics: AsyncCustomTopicsResource) -> None:
        self._custom_topics = custom_topics

        self.update = async_to_streamed_response_wrapper(
            custom_topics.update,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_topics.get,
        )
