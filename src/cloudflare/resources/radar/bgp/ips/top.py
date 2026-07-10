# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
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
from .....types.radar.bgp.ips import top_ases_params
from .....types.radar.bgp.ips.top_ases_response import TopAsesResponse

__all__ = ["TopResource", "AsyncTopResource"]


class TopResource(SyncAPIResource):
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

    def ases(
        self,
        *,
        country: str | Omit = omit,
        date: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit: int | Omit = omit,
        metric: Literal["v4_24s", "v6_48s"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopAsesResponse:
        """
        Returns the top-N autonomous systems by announced IP space at the nearest 8-hour
        RIB boundary at or before the requested date. The snapped boundary is returned
        as `anchor_ts`.

        Args:
          country: Optional ISO 3166-1 alpha-2 country filter. Omit for global top-N.

          date: Filters results by the specified datetime (ISO 8601).

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          metric: Ranking metric: IPv4 /24 count or IPv6 /48 count.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/ips/top/ases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "metric": metric,
                    },
                    top_ases_params.TopAsesParams,
                ),
                post_parser=ResultWrapper[TopAsesResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopAsesResponse], ResultWrapper[TopAsesResponse]),
        )


class AsyncTopResource(AsyncAPIResource):
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

    async def ases(
        self,
        *,
        country: str | Omit = omit,
        date: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit: int | Omit = omit,
        metric: Literal["v4_24s", "v6_48s"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopAsesResponse:
        """
        Returns the top-N autonomous systems by announced IP space at the nearest 8-hour
        RIB boundary at or before the requested date. The snapped boundary is returned
        as `anchor_ts`.

        Args:
          country: Optional ISO 3166-1 alpha-2 country filter. Omit for global top-N.

          date: Filters results by the specified datetime (ISO 8601).

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          metric: Ranking metric: IPv4 /24 count or IPv6 /48 count.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/ips/top/ases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "metric": metric,
                    },
                    top_ases_params.TopAsesParams,
                ),
                post_parser=ResultWrapper[TopAsesResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopAsesResponse], ResultWrapper[TopAsesResponse]),
        )


class TopResourceWithRawResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.ases = to_raw_response_wrapper(
            top.ases,
        )


class AsyncTopResourceWithRawResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.ases = async_to_raw_response_wrapper(
            top.ases,
        )


class TopResourceWithStreamingResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.ases = to_streamed_response_wrapper(
            top.ases,
        )


class AsyncTopResourceWithStreamingResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.ases = async_to_streamed_response_wrapper(
            top.ases,
        )
