# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import date
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from .user_agents import (
    UserAgentsResource,
    AsyncUserAgentsResource,
    UserAgentsResourceWithRawResponse,
    AsyncUserAgentsResourceWithRawResponse,
    UserAgentsResourceWithStreamingResponse,
    AsyncUserAgentsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.radar.robots_txt import top_domain_categories_params
from .....types.radar.robots_txt.top_domain_categories_response import TopDomainCategoriesResponse

__all__ = ["TopResource", "AsyncTopResource"]


class TopResource(SyncAPIResource):
    @cached_property
    def user_agents(self) -> UserAgentsResource:
        return UserAgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TopResourceWithStreamingResponse(self)

    def domain_categories(
        self,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        user_agent_category: Literal["AI"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopDomainCategoriesResponse:
        """
        Retrieves the top domain categories by the number of robots.txt files parsed.

        Args:
          date: Array of dates to filter the results.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          user_agent_category: Filters results by user agent category.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/robots_txt/top/domain_categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "name": name,
                        "user_agent_category": user_agent_category,
                    },
                    top_domain_categories_params.TopDomainCategoriesParams,
                ),
                post_parser=ResultWrapper[TopDomainCategoriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopDomainCategoriesResponse], ResultWrapper[TopDomainCategoriesResponse]),
        )


class AsyncTopResource(AsyncAPIResource):
    @cached_property
    def user_agents(self) -> AsyncUserAgentsResource:
        return AsyncUserAgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTopResourceWithStreamingResponse(self)

    async def domain_categories(
        self,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        user_agent_category: Literal["AI"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopDomainCategoriesResponse:
        """
        Retrieves the top domain categories by the number of robots.txt files parsed.

        Args:
          date: Array of dates to filter the results.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          user_agent_category: Filters results by user agent category.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/robots_txt/top/domain_categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "name": name,
                        "user_agent_category": user_agent_category,
                    },
                    top_domain_categories_params.TopDomainCategoriesParams,
                ),
                post_parser=ResultWrapper[TopDomainCategoriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopDomainCategoriesResponse], ResultWrapper[TopDomainCategoriesResponse]),
        )


class TopResourceWithRawResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.domain_categories = to_raw_response_wrapper(
            top.domain_categories,
        )

    @cached_property
    def user_agents(self) -> UserAgentsResourceWithRawResponse:
        return UserAgentsResourceWithRawResponse(self._top.user_agents)


class AsyncTopResourceWithRawResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.domain_categories = async_to_raw_response_wrapper(
            top.domain_categories,
        )

    @cached_property
    def user_agents(self) -> AsyncUserAgentsResourceWithRawResponse:
        return AsyncUserAgentsResourceWithRawResponse(self._top.user_agents)


class TopResourceWithStreamingResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.domain_categories = to_streamed_response_wrapper(
            top.domain_categories,
        )

    @cached_property
    def user_agents(self) -> UserAgentsResourceWithStreamingResponse:
        return UserAgentsResourceWithStreamingResponse(self._top.user_agents)


class AsyncTopResourceWithStreamingResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.domain_categories = async_to_streamed_response_wrapper(
            top.domain_categories,
        )

    @cached_property
    def user_agents(self) -> AsyncUserAgentsResourceWithStreamingResponse:
        return AsyncUserAgentsResourceWithStreamingResponse(self._top.user_agents)
