# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.ssl.recommendation_get_response import RecommendationGetResponse

__all__ = ["RecommendationsResource", "AsyncRecommendationsResource"]


class RecommendationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecommendationsResourceWithRawResponse:
        return RecommendationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecommendationsResourceWithStreamingResponse:
        return RecommendationsResourceWithStreamingResponse(self)

    def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecommendationGetResponse]:
        """
        Retrieve the SSL/TLS Recommender's recommendation for a zone.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/ssl/recommendation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecommendationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecommendationGetResponse]], ResultWrapper[RecommendationGetResponse]),
        )


class AsyncRecommendationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecommendationsResourceWithRawResponse:
        return AsyncRecommendationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecommendationsResourceWithStreamingResponse:
        return AsyncRecommendationsResourceWithStreamingResponse(self)

    async def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecommendationGetResponse]:
        """
        Retrieve the SSL/TLS Recommender's recommendation for a zone.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/ssl/recommendation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecommendationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecommendationGetResponse]], ResultWrapper[RecommendationGetResponse]),
        )


class RecommendationsResourceWithRawResponse:
    def __init__(self, recommendations: RecommendationsResource) -> None:
        self._recommendations = recommendations

        self.get = to_raw_response_wrapper(
            recommendations.get,
        )


class AsyncRecommendationsResourceWithRawResponse:
    def __init__(self, recommendations: AsyncRecommendationsResource) -> None:
        self._recommendations = recommendations

        self.get = async_to_raw_response_wrapper(
            recommendations.get,
        )


class RecommendationsResourceWithStreamingResponse:
    def __init__(self, recommendations: RecommendationsResource) -> None:
        self._recommendations = recommendations

        self.get = to_streamed_response_wrapper(
            recommendations.get,
        )


class AsyncRecommendationsResourceWithStreamingResponse:
    def __init__(self, recommendations: AsyncRecommendationsResource) -> None:
        self._recommendations = recommendations

        self.get = async_to_streamed_response_wrapper(
            recommendations.get,
        )
