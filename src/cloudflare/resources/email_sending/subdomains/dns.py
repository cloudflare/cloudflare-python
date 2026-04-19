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
from ....types.email_routing.dns_record import DNSRecord

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

    def get(
        self,
        subdomain_id: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[DNSRecord]:
        """
        Returns the expected DNS records for a sending subdomain.

        Args:
          zone_id: Identifier.

          subdomain_id: Sending subdomain identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not subdomain_id:
            raise ValueError(f"Expected a non-empty value for `subdomain_id` but received {subdomain_id!r}")
        return self._get_api_list(
            path_template(
                "/zones/{zone_id}/email/sending/subdomains/{subdomain_id}/dns",
                zone_id=zone_id,
                subdomain_id=subdomain_id,
            ),
            page=SyncSinglePage[DNSRecord],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DNSRecord,
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

    def get(
        self,
        subdomain_id: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DNSRecord, AsyncSinglePage[DNSRecord]]:
        """
        Returns the expected DNS records for a sending subdomain.

        Args:
          zone_id: Identifier.

          subdomain_id: Sending subdomain identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not subdomain_id:
            raise ValueError(f"Expected a non-empty value for `subdomain_id` but received {subdomain_id!r}")
        return self._get_api_list(
            path_template(
                "/zones/{zone_id}/email/sending/subdomains/{subdomain_id}/dns",
                zone_id=zone_id,
                subdomain_id=subdomain_id,
            ),
            page=AsyncSinglePage[DNSRecord],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DNSRecord,
        )


class DNSResourceWithRawResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.get = to_raw_response_wrapper(
            dns.get,
        )


class AsyncDNSResourceWithRawResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.get = async_to_raw_response_wrapper(
            dns.get,
        )


class DNSResourceWithStreamingResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.get = to_streamed_response_wrapper(
            dns.get,
        )


class AsyncDNSResourceWithStreamingResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.get = async_to_streamed_response_wrapper(
            dns.get,
        )
