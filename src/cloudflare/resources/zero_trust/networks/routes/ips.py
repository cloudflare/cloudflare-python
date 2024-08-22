# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.zero_trust.networks.teamnet import Teamnet

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from ....._base_client import make_request_options

from typing import Type

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.zero_trust.networks.routes import ip_get_params
from typing import cast
from typing import cast

__all__ = ["IPsResource", "AsyncIPsResource"]

class IPsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPsResourceWithRawResponse:
        return IPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPsResourceWithStreamingResponse:
        return IPsResourceWithStreamingResponse(self)

    def get(self,
    ip: str,
    *,
    account_id: str,
    virtual_network_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Teamnet:
        """
        Fetches routes that contain the given IP address.

        Args:
          account_id: Cloudflare account ID

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not ip:
          raise ValueError(
            f'Expected a non-empty value for `ip` but received {ip!r}'
          )
        return self._get(
            f"/accounts/{account_id}/teamnet/routes/ip/{ip}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "virtual_network_id": virtual_network_id
            }, ip_get_params.IPGetParams), post_parser=ResultWrapper[Teamnet]._unwrapper),
            cast_to=cast(Type[Teamnet], ResultWrapper[Teamnet]),
        )

class AsyncIPsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPsResourceWithRawResponse:
        return AsyncIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPsResourceWithStreamingResponse:
        return AsyncIPsResourceWithStreamingResponse(self)

    async def get(self,
    ip: str,
    *,
    account_id: str,
    virtual_network_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Teamnet:
        """
        Fetches routes that contain the given IP address.

        Args:
          account_id: Cloudflare account ID

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not ip:
          raise ValueError(
            f'Expected a non-empty value for `ip` but received {ip!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/teamnet/routes/ip/{ip}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "virtual_network_id": virtual_network_id
            }, ip_get_params.IPGetParams), post_parser=ResultWrapper[Teamnet]._unwrapper),
            cast_to=cast(Type[Teamnet], ResultWrapper[Teamnet]),
        )

class IPsResourceWithRawResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.get = to_raw_response_wrapper(
            ips.get,
        )

class AsyncIPsResourceWithRawResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.get = async_to_raw_response_wrapper(
            ips.get,
        )

class IPsResourceWithStreamingResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.get = to_streamed_response_wrapper(
            ips.get,
        )

class AsyncIPsResourceWithStreamingResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.get = async_to_streamed_response_wrapper(
            ips.get,
        )