# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Optional, cast

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
from ..._base_client import make_request_options
from ...types.dns_firewall import reverse_dns_edit_params
from ...types.dns_firewall.reverse_dns_get_response import ReverseDNSGetResponse
from ...types.dns_firewall.reverse_dns_edit_response import ReverseDNSEditResponse

__all__ = ["ReverseDNSResource", "AsyncReverseDNSResource"]


class ReverseDNSResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReverseDNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ReverseDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReverseDNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ReverseDNSResourceWithStreamingResponse(self)

    def edit(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        ptr: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ReverseDNSEditResponse]:
        """
        Update reverse DNS configuration (PTR records) for a DNS Firewall cluster

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          ptr: Map of cluster IP addresses to PTR record contents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return self._patch(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}/reverse_dns",
            body=maybe_transform({"ptr": ptr}, reverse_dns_edit_params.ReverseDNSEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ReverseDNSEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ReverseDNSEditResponse]], ResultWrapper[ReverseDNSEditResponse]),
        )

    def get(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ReverseDNSGetResponse]:
        """
        Show reverse DNS configuration (PTR records) for a DNS Firewall cluster

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return self._get(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}/reverse_dns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ReverseDNSGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ReverseDNSGetResponse]], ResultWrapper[ReverseDNSGetResponse]),
        )


class AsyncReverseDNSResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReverseDNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReverseDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReverseDNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncReverseDNSResourceWithStreamingResponse(self)

    async def edit(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        ptr: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ReverseDNSEditResponse]:
        """
        Update reverse DNS configuration (PTR records) for a DNS Firewall cluster

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          ptr: Map of cluster IP addresses to PTR record contents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}/reverse_dns",
            body=await async_maybe_transform({"ptr": ptr}, reverse_dns_edit_params.ReverseDNSEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ReverseDNSEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ReverseDNSEditResponse]], ResultWrapper[ReverseDNSEditResponse]),
        )

    async def get(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ReverseDNSGetResponse]:
        """
        Show reverse DNS configuration (PTR records) for a DNS Firewall cluster

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}/reverse_dns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ReverseDNSGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ReverseDNSGetResponse]], ResultWrapper[ReverseDNSGetResponse]),
        )


class ReverseDNSResourceWithRawResponse:
    def __init__(self, reverse_dns: ReverseDNSResource) -> None:
        self._reverse_dns = reverse_dns

        self.edit = to_raw_response_wrapper(
            reverse_dns.edit,
        )
        self.get = to_raw_response_wrapper(
            reverse_dns.get,
        )


class AsyncReverseDNSResourceWithRawResponse:
    def __init__(self, reverse_dns: AsyncReverseDNSResource) -> None:
        self._reverse_dns = reverse_dns

        self.edit = async_to_raw_response_wrapper(
            reverse_dns.edit,
        )
        self.get = async_to_raw_response_wrapper(
            reverse_dns.get,
        )


class ReverseDNSResourceWithStreamingResponse:
    def __init__(self, reverse_dns: ReverseDNSResource) -> None:
        self._reverse_dns = reverse_dns

        self.edit = to_streamed_response_wrapper(
            reverse_dns.edit,
        )
        self.get = to_streamed_response_wrapper(
            reverse_dns.get,
        )


class AsyncReverseDNSResourceWithStreamingResponse:
    def __init__(self, reverse_dns: AsyncReverseDNSResource) -> None:
        self._reverse_dns = reverse_dns

        self.edit = async_to_streamed_response_wrapper(
            reverse_dns.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            reverse_dns.get,
        )
