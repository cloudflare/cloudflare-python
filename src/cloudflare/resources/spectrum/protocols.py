# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.spectrum.protocol_list_response import ProtocolListResponse

__all__ = ["ProtocolsResource", "AsyncProtocolsResource"]


class ProtocolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProtocolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ProtocolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProtocolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ProtocolsResourceWithStreamingResponse(self)

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
    ) -> SyncSinglePage[ProtocolListResponse]:
        """
        Retrieves a list of Spectrum application protocols available for a zone.

        Args:
          zone_id: Zone identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/spectrum/protocols", zone_id=zone_id),
            page=SyncSinglePage[ProtocolListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProtocolListResponse,
        )


class AsyncProtocolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProtocolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProtocolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProtocolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncProtocolsResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[ProtocolListResponse, AsyncSinglePage[ProtocolListResponse]]:
        """
        Retrieves a list of Spectrum application protocols available for a zone.

        Args:
          zone_id: Zone identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/spectrum/protocols", zone_id=zone_id),
            page=AsyncSinglePage[ProtocolListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProtocolListResponse,
        )


class ProtocolsResourceWithRawResponse:
    def __init__(self, protocols: ProtocolsResource) -> None:
        self._protocols = protocols

        self.list = to_raw_response_wrapper(
            protocols.list,
        )


class AsyncProtocolsResourceWithRawResponse:
    def __init__(self, protocols: AsyncProtocolsResource) -> None:
        self._protocols = protocols

        self.list = async_to_raw_response_wrapper(
            protocols.list,
        )


class ProtocolsResourceWithStreamingResponse:
    def __init__(self, protocols: ProtocolsResource) -> None:
        self._protocols = protocols

        self.list = to_streamed_response_wrapper(
            protocols.list,
        )


class AsyncProtocolsResourceWithStreamingResponse:
    def __init__(self, protocols: AsyncProtocolsResource) -> None:
        self._protocols = protocols

        self.list = async_to_streamed_response_wrapper(
            protocols.list,
        )
