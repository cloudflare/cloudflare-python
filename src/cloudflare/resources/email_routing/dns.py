# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.email_routing.dns_get_response import DNSGetResponse

from ..._wrappers import ResultWrapper

from typing import Optional, Type

from ..._base_client import make_request_options

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from typing import cast
from typing import cast

__all__ = ["DNSResource", "AsyncDNSResource"]

class DNSResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DNSResourceWithRawResponse:
        return DNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSResourceWithStreamingResponse:
        return DNSResourceWithStreamingResponse(self)

    def get(self,
    zone_identifier: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[DNSGetResponse]:
        """
        Show the DNS records needed to configure your Email Routing zone.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return self._get(
            f"/zones/{zone_identifier}/email/routing/dns",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[DNSGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[DNSGetResponse]], ResultWrapper[DNSGetResponse]),
        )

class AsyncDNSResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDNSResourceWithRawResponse:
        return AsyncDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSResourceWithStreamingResponse:
        return AsyncDNSResourceWithStreamingResponse(self)

    async def get(self,
    zone_identifier: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[DNSGetResponse]:
        """
        Show the DNS records needed to configure your Email Routing zone.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return await self._get(
            f"/zones/{zone_identifier}/email/routing/dns",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[DNSGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[DNSGetResponse]], ResultWrapper[DNSGetResponse]),
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