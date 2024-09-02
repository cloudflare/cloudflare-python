# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .top.top import TopResource, AsyncTopResource

from ...._compat import cached_property

from ....types.radar.robots_txt_domains_response import RobotsTXTDomainsResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Type

from typing_extensions import Literal

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.radar import robots_txt_domains_params
from .top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)
from typing import cast
from typing import cast

__all__ = ["RobotsTXTResource", "AsyncRobotsTXTResource"]


class RobotsTXTResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def with_raw_response(self) -> RobotsTXTResourceWithRawResponse:
        return RobotsTXTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RobotsTXTResourceWithStreamingResponse:
        return RobotsTXTResourceWithStreamingResponse(self)

    def domains(
        self,
        *,
        domain_category: str | NotGiven = NOT_GIVEN,
        domain_name: str | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RobotsTXTDomainsResponse:
        """
        Get the top User-Agents on robots.txt files by domain.

        Args:
          domain_category: Filter domains by category

          domain_name: Filter domains by name

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/robots_txt/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain_category": domain_category,
                        "domain_name": domain_name,
                        "format": format,
                        "limit": limit,
                        "offset": offset,
                    },
                    robots_txt_domains_params.RobotsTXTDomainsParams,
                ),
                post_parser=ResultWrapper[RobotsTXTDomainsResponse]._unwrapper,
            ),
            cast_to=cast(Type[RobotsTXTDomainsResponse], ResultWrapper[RobotsTXTDomainsResponse]),
        )


class AsyncRobotsTXTResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRobotsTXTResourceWithRawResponse:
        return AsyncRobotsTXTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRobotsTXTResourceWithStreamingResponse:
        return AsyncRobotsTXTResourceWithStreamingResponse(self)

    async def domains(
        self,
        *,
        domain_category: str | NotGiven = NOT_GIVEN,
        domain_name: str | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RobotsTXTDomainsResponse:
        """
        Get the top User-Agents on robots.txt files by domain.

        Args:
          domain_category: Filter domains by category

          domain_name: Filter domains by name

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/robots_txt/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain_category": domain_category,
                        "domain_name": domain_name,
                        "format": format,
                        "limit": limit,
                        "offset": offset,
                    },
                    robots_txt_domains_params.RobotsTXTDomainsParams,
                ),
                post_parser=ResultWrapper[RobotsTXTDomainsResponse]._unwrapper,
            ),
            cast_to=cast(Type[RobotsTXTDomainsResponse], ResultWrapper[RobotsTXTDomainsResponse]),
        )


class RobotsTXTResourceWithRawResponse:
    def __init__(self, robots_txt: RobotsTXTResource) -> None:
        self._robots_txt = robots_txt

        self.domains = to_raw_response_wrapper(
            robots_txt.domains,
        )

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._robots_txt.top)


class AsyncRobotsTXTResourceWithRawResponse:
    def __init__(self, robots_txt: AsyncRobotsTXTResource) -> None:
        self._robots_txt = robots_txt

        self.domains = async_to_raw_response_wrapper(
            robots_txt.domains,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._robots_txt.top)


class RobotsTXTResourceWithStreamingResponse:
    def __init__(self, robots_txt: RobotsTXTResource) -> None:
        self._robots_txt = robots_txt

        self.domains = to_streamed_response_wrapper(
            robots_txt.domains,
        )

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._robots_txt.top)


class AsyncRobotsTXTResourceWithStreamingResponse:
    def __init__(self, robots_txt: AsyncRobotsTXTResource) -> None:
        self._robots_txt = robots_txt

        self.domains = async_to_streamed_response_wrapper(
            robots_txt.domains,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._robots_txt.top)
