# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.email_routing import dns_get_params, dns_edit_params, dns_create_params
from ...types.email_routing.settings import Settings
from ...types.email_routing.dns_record import DNSRecord
from ...types.email_routing.dns_get_response import DNSGetResponse

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

    def create(
        self,
        *,
        zone_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Settings]:
        """Enable you Email Routing zone.

        Add and lock the necessary MX and SPF records.

        Args:
          zone_id: Identifier

          name: Domain of your zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/email/routing/dns",
            body=maybe_transform({"name": name}, dns_create_params.DNSCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Settings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Settings]], ResultWrapper[Settings]),
        )

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[DNSRecord]:
        """Disable your Email Routing zone.

        Also removes additional MX records previously
        required for Email Routing to work.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/email/routing/dns",
            page=SyncSinglePage[DNSRecord],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DNSRecord,
            method="delete",
        )

    def edit(
        self,
        *,
        zone_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Settings]:
        """
        Unlock MX Records previously locked by Email Routing.

        Args:
          zone_id: Identifier

          name: Domain of your zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/email/routing/dns",
            body=maybe_transform({"name": name}, dns_edit_params.DNSEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Settings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Settings]], ResultWrapper[Settings]),
        )

    def get(
        self,
        *,
        zone_id: str,
        subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSGetResponse:
        """
        Show the DNS records needed to configure your Email Routing zone.

        Args:
          zone_id: Identifier

          subdomain: Domain of your zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            DNSGetResponse,
            self._get(
                f"/zones/{zone_id}/email/routing/dns",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"subdomain": subdomain}, dns_get_params.DNSGetParams),
                ),
                cast_to=cast(Any, DNSGetResponse),  # Union types cannot be passed in as arguments in the type system
            ),
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

    async def create(
        self,
        *,
        zone_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Settings]:
        """Enable you Email Routing zone.

        Add and lock the necessary MX and SPF records.

        Args:
          zone_id: Identifier

          name: Domain of your zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/email/routing/dns",
            body=await async_maybe_transform({"name": name}, dns_create_params.DNSCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Settings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Settings]], ResultWrapper[Settings]),
        )

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DNSRecord, AsyncSinglePage[DNSRecord]]:
        """Disable your Email Routing zone.

        Also removes additional MX records previously
        required for Email Routing to work.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/email/routing/dns",
            page=AsyncSinglePage[DNSRecord],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DNSRecord,
            method="delete",
        )

    async def edit(
        self,
        *,
        zone_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Settings]:
        """
        Unlock MX Records previously locked by Email Routing.

        Args:
          zone_id: Identifier

          name: Domain of your zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/email/routing/dns",
            body=await async_maybe_transform({"name": name}, dns_edit_params.DNSEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Settings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Settings]], ResultWrapper[Settings]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSGetResponse:
        """
        Show the DNS records needed to configure your Email Routing zone.

        Args:
          zone_id: Identifier

          subdomain: Domain of your zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            DNSGetResponse,
            await self._get(
                f"/zones/{zone_id}/email/routing/dns",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform({"subdomain": subdomain}, dns_get_params.DNSGetParams),
                ),
                cast_to=cast(Any, DNSGetResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class DNSResourceWithRawResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.create = to_raw_response_wrapper(
            dns.create,
        )
        self.delete = to_raw_response_wrapper(
            dns.delete,
        )
        self.edit = to_raw_response_wrapper(
            dns.edit,
        )
        self.get = to_raw_response_wrapper(
            dns.get,
        )


class AsyncDNSResourceWithRawResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.create = async_to_raw_response_wrapper(
            dns.create,
        )
        self.delete = async_to_raw_response_wrapper(
            dns.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            dns.edit,
        )
        self.get = async_to_raw_response_wrapper(
            dns.get,
        )


class DNSResourceWithStreamingResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.create = to_streamed_response_wrapper(
            dns.create,
        )
        self.delete = to_streamed_response_wrapper(
            dns.delete,
        )
        self.edit = to_streamed_response_wrapper(
            dns.edit,
        )
        self.get = to_streamed_response_wrapper(
            dns.get,
        )


class AsyncDNSResourceWithStreamingResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.create = async_to_streamed_response_wrapper(
            dns.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            dns.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            dns.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            dns.get,
        )
