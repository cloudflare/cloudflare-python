# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import date
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.radar import agent_readiness_summary_params
from ..._base_client import make_request_options
from ...types.radar.agent_readiness_summary_response import AgentReadinessSummaryResponse

__all__ = ["AgentReadinessResource", "AsyncAgentReadinessResource"]


class AgentReadinessResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentReadinessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AgentReadinessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentReadinessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AgentReadinessResourceWithStreamingResponse(self)

    def summary(
        self,
        dimension: Literal["CHECK"],
        *,
        date: Union[str, date] | Omit = omit,
        domain_category: SequenceNotStr[str] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentReadinessSummaryResponse:
        """
        Returns a summary of AI agent readiness scores across scanned domains, grouped
        by the specified dimension. Data is sourced from weekly bulk scans. All values
        are raw domain counts.

        Args:
          dimension: Specifies the agent readiness data dimension by which to group the results.

          date: Filters results by the specified date.

          domain_category: Filters results by domain category.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            path_template("/radar/agent_readiness/summary/{dimension}", dimension=dimension),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "domain_category": domain_category,
                        "format": format,
                        "name": name,
                    },
                    agent_readiness_summary_params.AgentReadinessSummaryParams,
                ),
                post_parser=ResultWrapper[AgentReadinessSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[AgentReadinessSummaryResponse], ResultWrapper[AgentReadinessSummaryResponse]),
        )


class AsyncAgentReadinessResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentReadinessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentReadinessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentReadinessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAgentReadinessResourceWithStreamingResponse(self)

    async def summary(
        self,
        dimension: Literal["CHECK"],
        *,
        date: Union[str, date] | Omit = omit,
        domain_category: SequenceNotStr[str] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentReadinessSummaryResponse:
        """
        Returns a summary of AI agent readiness scores across scanned domains, grouped
        by the specified dimension. Data is sourced from weekly bulk scans. All values
        are raw domain counts.

        Args:
          dimension: Specifies the agent readiness data dimension by which to group the results.

          date: Filters results by the specified date.

          domain_category: Filters results by domain category.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            path_template("/radar/agent_readiness/summary/{dimension}", dimension=dimension),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "domain_category": domain_category,
                        "format": format,
                        "name": name,
                    },
                    agent_readiness_summary_params.AgentReadinessSummaryParams,
                ),
                post_parser=ResultWrapper[AgentReadinessSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[AgentReadinessSummaryResponse], ResultWrapper[AgentReadinessSummaryResponse]),
        )


class AgentReadinessResourceWithRawResponse:
    def __init__(self, agent_readiness: AgentReadinessResource) -> None:
        self._agent_readiness = agent_readiness

        self.summary = to_raw_response_wrapper(
            agent_readiness.summary,
        )


class AsyncAgentReadinessResourceWithRawResponse:
    def __init__(self, agent_readiness: AsyncAgentReadinessResource) -> None:
        self._agent_readiness = agent_readiness

        self.summary = async_to_raw_response_wrapper(
            agent_readiness.summary,
        )


class AgentReadinessResourceWithStreamingResponse:
    def __init__(self, agent_readiness: AgentReadinessResource) -> None:
        self._agent_readiness = agent_readiness

        self.summary = to_streamed_response_wrapper(
            agent_readiness.summary,
        )


class AsyncAgentReadinessResourceWithStreamingResponse:
    def __init__(self, agent_readiness: AsyncAgentReadinessResource) -> None:
        self._agent_readiness = agent_readiness

        self.summary = async_to_streamed_response_wrapper(
            agent_readiness.summary,
        )
