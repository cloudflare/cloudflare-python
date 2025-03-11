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
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.radar.robots_txt.top import user_agent_directive_params
from .....types.radar.robots_txt.top.user_agent_directive_response import UserAgentDirectiveResponse

__all__ = ["UserAgentsResource", "AsyncUserAgentsResource"]


class UserAgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UserAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UserAgentsResourceWithStreamingResponse(self)

    def directive(
        self,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        directive: Literal["ALLOW", "DISALLOW"] | NotGiven = NOT_GIVEN,
        domain_category: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> UserAgentDirectiveResponse:
        """
        Retrieves the top user agents on robots.txt files.

        Args:
          date: Array of dates to filter the results.

          directive: Filters results by robots.txt directive.

          domain_category: Filters results by domain category.

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
            "/radar/robots_txt/top/user_agents/directive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "directive": directive,
                        "domain_category": domain_category,
                        "format": format,
                        "limit": limit,
                        "name": name,
                        "user_agent_category": user_agent_category,
                    },
                    user_agent_directive_params.UserAgentDirectiveParams,
                ),
                post_parser=ResultWrapper[UserAgentDirectiveResponse]._unwrapper,
            ),
            cast_to=cast(Type[UserAgentDirectiveResponse], ResultWrapper[UserAgentDirectiveResponse]),
        )


class AsyncUserAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUserAgentsResourceWithStreamingResponse(self)

    async def directive(
        self,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        directive: Literal["ALLOW", "DISALLOW"] | NotGiven = NOT_GIVEN,
        domain_category: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> UserAgentDirectiveResponse:
        """
        Retrieves the top user agents on robots.txt files.

        Args:
          date: Array of dates to filter the results.

          directive: Filters results by robots.txt directive.

          domain_category: Filters results by domain category.

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
            "/radar/robots_txt/top/user_agents/directive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "directive": directive,
                        "domain_category": domain_category,
                        "format": format,
                        "limit": limit,
                        "name": name,
                        "user_agent_category": user_agent_category,
                    },
                    user_agent_directive_params.UserAgentDirectiveParams,
                ),
                post_parser=ResultWrapper[UserAgentDirectiveResponse]._unwrapper,
            ),
            cast_to=cast(Type[UserAgentDirectiveResponse], ResultWrapper[UserAgentDirectiveResponse]),
        )


class UserAgentsResourceWithRawResponse:
    def __init__(self, user_agents: UserAgentsResource) -> None:
        self._user_agents = user_agents

        self.directive = to_raw_response_wrapper(
            user_agents.directive,
        )


class AsyncUserAgentsResourceWithRawResponse:
    def __init__(self, user_agents: AsyncUserAgentsResource) -> None:
        self._user_agents = user_agents

        self.directive = async_to_raw_response_wrapper(
            user_agents.directive,
        )


class UserAgentsResourceWithStreamingResponse:
    def __init__(self, user_agents: UserAgentsResource) -> None:
        self._user_agents = user_agents

        self.directive = to_streamed_response_wrapper(
            user_agents.directive,
        )


class AsyncUserAgentsResourceWithStreamingResponse:
    def __init__(self, user_agents: AsyncUserAgentsResource) -> None:
        self._user_agents = user_agents

        self.directive = async_to_streamed_response_wrapper(
            user_agents.directive,
        )
