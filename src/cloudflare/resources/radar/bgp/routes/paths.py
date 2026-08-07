# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
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
from .....types.radar.bgp.routes import path_list_params
from .....types.radar.bgp.routes.path_list_response import PathListResponse

__all__ = ["PathsResource", "AsyncPathsResource"]


class PathsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PathsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PathsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PathsResourceWithStreamingResponse(self)

    def list(
        self,
        asn: int,
        *,
        collector: str | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: Literal["IPv4", "IPv6"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PathListResponse:
        """
        Retrieves the paths an AS uses to reach the tier-1 clique, derived from
        RouteViews RIB snapshots. Each entry is an ordered AS-path segment (from the
        queried AS toward a tier-1) with the number of observed paths and peers, and the
        collectors that observed it. By default segments are merged across all active
        collectors; pass "collector" to scope to one. The response also includes an
        "asnInfo" map (keyed by ASN) with the name and country for every ASN in the
        returned segments plus the queried ASN (best-effort; null when unavailable).

        Args:
          asn: Single Autonomous System Number (ASN) as integer.

          collector: Scope to a single RouteViews collector (e.g. "route-views3"). Omit to merge
              across all active collectors (identical path segments are deduplicated,
              observation counts summed, and every contributing collector listed).

          format: Format in which results will be returned.

          ip_version: Address family of the observed paths. Defaults to IPv4.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/radar/bgp/routes/paths/{asn}", asn=asn),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collector": collector,
                        "format": format,
                        "ip_version": ip_version,
                    },
                    path_list_params.PathListParams,
                ),
                post_parser=ResultWrapper[PathListResponse]._unwrapper,
            ),
            cast_to=cast(Type[PathListResponse], ResultWrapper[PathListResponse]),
        )


class AsyncPathsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPathsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPathsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPathsResourceWithStreamingResponse(self)

    async def list(
        self,
        asn: int,
        *,
        collector: str | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: Literal["IPv4", "IPv6"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PathListResponse:
        """
        Retrieves the paths an AS uses to reach the tier-1 clique, derived from
        RouteViews RIB snapshots. Each entry is an ordered AS-path segment (from the
        queried AS toward a tier-1) with the number of observed paths and peers, and the
        collectors that observed it. By default segments are merged across all active
        collectors; pass "collector" to scope to one. The response also includes an
        "asnInfo" map (keyed by ASN) with the name and country for every ASN in the
        returned segments plus the queried ASN (best-effort; null when unavailable).

        Args:
          asn: Single Autonomous System Number (ASN) as integer.

          collector: Scope to a single RouteViews collector (e.g. "route-views3"). Omit to merge
              across all active collectors (identical path segments are deduplicated,
              observation counts summed, and every contributing collector listed).

          format: Format in which results will be returned.

          ip_version: Address family of the observed paths. Defaults to IPv4.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/radar/bgp/routes/paths/{asn}", asn=asn),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "collector": collector,
                        "format": format,
                        "ip_version": ip_version,
                    },
                    path_list_params.PathListParams,
                ),
                post_parser=ResultWrapper[PathListResponse]._unwrapper,
            ),
            cast_to=cast(Type[PathListResponse], ResultWrapper[PathListResponse]),
        )


class PathsResourceWithRawResponse:
    def __init__(self, paths: PathsResource) -> None:
        self._paths = paths

        self.list = to_raw_response_wrapper(
            paths.list,
        )


class AsyncPathsResourceWithRawResponse:
    def __init__(self, paths: AsyncPathsResource) -> None:
        self._paths = paths

        self.list = async_to_raw_response_wrapper(
            paths.list,
        )


class PathsResourceWithStreamingResponse:
    def __init__(self, paths: PathsResource) -> None:
        self._paths = paths

        self.list = to_streamed_response_wrapper(
            paths.list,
        )


class AsyncPathsResourceWithStreamingResponse:
    def __init__(self, paths: AsyncPathsResource) -> None:
        self._paths = paths

        self.list = async_to_streamed_response_wrapper(
            paths.list,
        )
