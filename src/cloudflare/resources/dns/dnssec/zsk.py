# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.dns.dnssec.zsk_list_response import ZskListResponse

__all__ = ["ZskResource", "AsyncZskResource"]


class ZskResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ZskResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ZskResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZskResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ZskResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[ZskListResponse]:
        """
        List the Zone Signing Keys (ZSKs) that DNSSEC uses for the zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/dnssec/zsk", zone_id=zone_id),
            page=SyncSinglePage[ZskListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ZskListResponse,
        )


class AsyncZskResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncZskResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZskResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZskResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncZskResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ZskListResponse, AsyncSinglePage[ZskListResponse]]:
        """
        List the Zone Signing Keys (ZSKs) that DNSSEC uses for the zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/dnssec/zsk", zone_id=zone_id),
            page=AsyncSinglePage[ZskListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ZskListResponse,
        )


class ZskResourceWithRawResponse:
    def __init__(self, zsk: ZskResource) -> None:
        self._zsk = zsk

        self.list = to_raw_response_wrapper(
            zsk.list,
        )


class AsyncZskResourceWithRawResponse:
    def __init__(self, zsk: AsyncZskResource) -> None:
        self._zsk = zsk

        self.list = async_to_raw_response_wrapper(
            zsk.list,
        )


class ZskResourceWithStreamingResponse:
    def __init__(self, zsk: ZskResource) -> None:
        self._zsk = zsk

        self.list = to_streamed_response_wrapper(
            zsk.list,
        )


class AsyncZskResourceWithStreamingResponse:
    def __init__(self, zsk: AsyncZskResource) -> None:
        self._zsk = zsk

        self.list = async_to_streamed_response_wrapper(
            zsk.list,
        )
