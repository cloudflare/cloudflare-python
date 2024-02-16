# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.intels import (
    DNSPassiveDNSByIPGetPassiveDNSByIPResponse,
    dns_passive_dns_by_ip_get_passive_dns_by_ip_params,
)

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.intels import dns_passive_dns_by_ip_get_passive_dns_by_ip_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["DNS", "AsyncDNS"]


class DNS(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DNSWithRawResponse:
        return DNSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSWithStreamingResponse:
        return DNSWithStreamingResponse(self)

    def passive_dns_by_ip_get_passive_dns_by_ip(
        self,
        account_id: str,
        *,
        ipv4: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        start_end_params: dns_passive_dns_by_ip_get_passive_dns_by_ip_params.StartEndParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSPassiveDNSByIPGetPassiveDNSByIPResponse:
        """
        Get Passive DNS by IP

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
        return self._get(
            f"/accounts/{account_id}/intel/dns",
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
                    dns_passive_dns_by_ip_get_passive_dns_by_ip_params.DNSPassiveDNSByIPGetPassiveDNSByIPParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DNSPassiveDNSByIPGetPassiveDNSByIPResponse],
                ResultWrapper[DNSPassiveDNSByIPGetPassiveDNSByIPResponse],
            ),
        )


class AsyncDNS(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDNSWithRawResponse:
        return AsyncDNSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSWithStreamingResponse:
        return AsyncDNSWithStreamingResponse(self)

    async def passive_dns_by_ip_get_passive_dns_by_ip(
        self,
        account_id: str,
        *,
        ipv4: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        start_end_params: dns_passive_dns_by_ip_get_passive_dns_by_ip_params.StartEndParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSPassiveDNSByIPGetPassiveDNSByIPResponse:
        """
        Get Passive DNS by IP

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
        return await self._get(
            f"/accounts/{account_id}/intel/dns",
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
                    dns_passive_dns_by_ip_get_passive_dns_by_ip_params.DNSPassiveDNSByIPGetPassiveDNSByIPParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DNSPassiveDNSByIPGetPassiveDNSByIPResponse],
                ResultWrapper[DNSPassiveDNSByIPGetPassiveDNSByIPResponse],
            ),
        )


class DNSWithRawResponse:
    def __init__(self, dns: DNS) -> None:
        self._dns = dns

        self.passive_dns_by_ip_get_passive_dns_by_ip = to_raw_response_wrapper(
            dns.passive_dns_by_ip_get_passive_dns_by_ip,
        )


class AsyncDNSWithRawResponse:
    def __init__(self, dns: AsyncDNS) -> None:
        self._dns = dns

        self.passive_dns_by_ip_get_passive_dns_by_ip = async_to_raw_response_wrapper(
            dns.passive_dns_by_ip_get_passive_dns_by_ip,
        )


class DNSWithStreamingResponse:
    def __init__(self, dns: DNS) -> None:
        self._dns = dns

        self.passive_dns_by_ip_get_passive_dns_by_ip = to_streamed_response_wrapper(
            dns.passive_dns_by_ip_get_passive_dns_by_ip,
        )


class AsyncDNSWithStreamingResponse:
    def __init__(self, dns: AsyncDNS) -> None:
        self._dns = dns

        self.passive_dns_by_ip_get_passive_dns_by_ip = async_to_streamed_response_wrapper(
            dns.passive_dns_by_ip_get_passive_dns_by_ip,
        )
