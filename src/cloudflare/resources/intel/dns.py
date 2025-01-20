# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncV4PagePagination, AsyncV4PagePagination
from ...types.intel import dns_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.intel.dns import DNS

__all__ = ["DNSResource", "AsyncDNSResource"]


class DNSResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DNSResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        ipv4: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        start_end_params: dns_list_params.StartEndParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePagination[Optional[DNS]]:
        """
        Gets a list of all the domains that have resolved to a specific IP address.

        Args:
          account_id: Identifier

          page: Requested page within paginated list of results.

          per_page: Maximum number of results requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/intel/dns",
            page=SyncV4PagePagination[Optional[DNS]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ipv4": ipv4,
                        "page": page,
                        "per_page": per_page,
                        "start_end_params": start_end_params,
                    },
                    dns_list_params.DNSListParams,
                ),
            ),
            model=DNS,
        )


class AsyncDNSResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDNSResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        ipv4: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        start_end_params: dns_list_params.StartEndParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Optional[DNS], AsyncV4PagePagination[Optional[DNS]]]:
        """
        Gets a list of all the domains that have resolved to a specific IP address.

        Args:
          account_id: Identifier

          page: Requested page within paginated list of results.

          per_page: Maximum number of results requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/intel/dns",
            page=AsyncV4PagePagination[Optional[DNS]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ipv4": ipv4,
                        "page": page,
                        "per_page": per_page,
                        "start_end_params": start_end_params,
                    },
                    dns_list_params.DNSListParams,
                ),
            ),
            model=DNS,
        )


class DNSResourceWithRawResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.list = to_raw_response_wrapper(
            dns.list,
        )


class AsyncDNSResourceWithRawResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.list = async_to_raw_response_wrapper(
            dns.list,
        )


class DNSResourceWithStreamingResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.list = to_streamed_response_wrapper(
            dns.list,
        )


class AsyncDNSResourceWithStreamingResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.list = async_to_streamed_response_wrapper(
            dns.list,
        )
