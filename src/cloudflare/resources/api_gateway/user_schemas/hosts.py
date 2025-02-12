# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.api_gateway.user_schemas import host_list_params
from ....types.api_gateway.user_schemas.host_list_response import HostListResponse

__all__ = ["HostsResource", "AsyncHostsResource"]


class HostsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HostsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[HostListResponse]:
        """
        Retrieve schema hosts in a zone

        Args:
          zone_id: Identifier

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/user_schemas/hosts",
            page=SyncV4PagePaginationArray[HostListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    host_list_params.HostListParams,
                ),
            ),
            model=HostListResponse,
        )


class AsyncHostsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHostsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[HostListResponse, AsyncV4PagePaginationArray[HostListResponse]]:
        """
        Retrieve schema hosts in a zone

        Args:
          zone_id: Identifier

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/user_schemas/hosts",
            page=AsyncV4PagePaginationArray[HostListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    host_list_params.HostListParams,
                ),
            ),
            model=HostListResponse,
        )


class HostsResourceWithRawResponse:
    def __init__(self, hosts: HostsResource) -> None:
        self._hosts = hosts

        self.list = to_raw_response_wrapper(
            hosts.list,
        )


class AsyncHostsResourceWithRawResponse:
    def __init__(self, hosts: AsyncHostsResource) -> None:
        self._hosts = hosts

        self.list = async_to_raw_response_wrapper(
            hosts.list,
        )


class HostsResourceWithStreamingResponse:
    def __init__(self, hosts: HostsResource) -> None:
        self._hosts = hosts

        self.list = to_streamed_response_wrapper(
            hosts.list,
        )


class AsyncHostsResourceWithStreamingResponse:
    def __init__(self, hosts: AsyncHostsResource) -> None:
        self._hosts = hosts

        self.list = async_to_streamed_response_wrapper(
            hosts.list,
        )
