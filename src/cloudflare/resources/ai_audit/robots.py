# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._base_client import make_request_options
from ...types.ai_audit import robot_get_params
from ...types.ai_audit.robot_get_response import RobotGetResponse
from ...types.ai_audit.robot_bulk_get_response import RobotBulkGetResponse

__all__ = ["RobotsResource", "AsyncRobotsResource"]


class RobotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RobotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RobotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RobotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RobotsResourceWithStreamingResponse(self)

    def bulk_get(
        self,
        *,
        zone_id: str,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RobotBulkGetResponse]:
        """
        Fetches and parses robots.txt files for multiple domains within a zone in a
        single request. Each domain must belong to the specified zone. Results are keyed
        by hostname.

        Args:
          body: Array of domain hostnames to fetch robots.txt for. Each domain must end with the
              zone name. Maximum 25 domains per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            path_template("/zones/{zone_id}/ai-audit/robots/bulk", zone_id=zone_id),
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RobotBulkGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RobotBulkGetResponse]], ResultWrapper[RobotBulkGetResponse]),
        )

    def get(
        self,
        *,
        zone_id: str,
        subdomain: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RobotGetResponse]:
        """
        Fetches and parses the robots.txt file for a zone or a specific subdomain within
        the zone. Returns parsed user-agent rules, content signals, and sitemaps.

        Args:
          subdomain: Optional subdomain to fetch robots.txt for. If omitted, fetches robots.txt for
              the zone apex domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/ai-audit/robots", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"subdomain": subdomain}, robot_get_params.RobotGetParams),
                post_parser=ResultWrapper[Optional[RobotGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RobotGetResponse]], ResultWrapper[RobotGetResponse]),
        )


class AsyncRobotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRobotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRobotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRobotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRobotsResourceWithStreamingResponse(self)

    async def bulk_get(
        self,
        *,
        zone_id: str,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RobotBulkGetResponse]:
        """
        Fetches and parses robots.txt files for multiple domains within a zone in a
        single request. Each domain must belong to the specified zone. Results are keyed
        by hostname.

        Args:
          body: Array of domain hostnames to fetch robots.txt for. Each domain must end with the
              zone name. Maximum 25 domains per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            path_template("/zones/{zone_id}/ai-audit/robots/bulk", zone_id=zone_id),
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RobotBulkGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RobotBulkGetResponse]], ResultWrapper[RobotBulkGetResponse]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        subdomain: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RobotGetResponse]:
        """
        Fetches and parses the robots.txt file for a zone or a specific subdomain within
        the zone. Returns parsed user-agent rules, content signals, and sitemaps.

        Args:
          subdomain: Optional subdomain to fetch robots.txt for. If omitted, fetches robots.txt for
              the zone apex domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/ai-audit/robots", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"subdomain": subdomain}, robot_get_params.RobotGetParams),
                post_parser=ResultWrapper[Optional[RobotGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RobotGetResponse]], ResultWrapper[RobotGetResponse]),
        )


class RobotsResourceWithRawResponse:
    def __init__(self, robots: RobotsResource) -> None:
        self._robots = robots

        self.bulk_get = to_raw_response_wrapper(
            robots.bulk_get,
        )
        self.get = to_raw_response_wrapper(
            robots.get,
        )


class AsyncRobotsResourceWithRawResponse:
    def __init__(self, robots: AsyncRobotsResource) -> None:
        self._robots = robots

        self.bulk_get = async_to_raw_response_wrapper(
            robots.bulk_get,
        )
        self.get = async_to_raw_response_wrapper(
            robots.get,
        )


class RobotsResourceWithStreamingResponse:
    def __init__(self, robots: RobotsResource) -> None:
        self._robots = robots

        self.bulk_get = to_streamed_response_wrapper(
            robots.bulk_get,
        )
        self.get = to_streamed_response_wrapper(
            robots.get,
        )


class AsyncRobotsResourceWithStreamingResponse:
    def __init__(self, robots: AsyncRobotsResource) -> None:
        self._robots = robots

        self.bulk_get = async_to_streamed_response_wrapper(
            robots.bulk_get,
        )
        self.get = async_to_streamed_response_wrapper(
            robots.get,
        )
