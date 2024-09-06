# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.intel.ip_get_response import IPGetResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options

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
from ...types import shared_params
from ...types.intel import ip_get_params
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

    def get(
        self,
        *,
        account_id: str,
        ipv4: str | NotGiven = NOT_GIVEN,
        ipv6: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPGetResponse]:
        """
        Get IP Overview

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ipv4": ipv4,
                        "ipv6": ipv6,
                    },
                    ip_get_params.IPGetParams,
                ),
                post_parser=ResultWrapper[Optional[IPGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IPGetResponse]], ResultWrapper[IPGetResponse]),
        )


class AsyncIPsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPsResourceWithRawResponse:
        return AsyncIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPsResourceWithStreamingResponse:
        return AsyncIPsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        ipv4: str | NotGiven = NOT_GIVEN,
        ipv6: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPGetResponse]:
        """
        Get IP Overview

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ipv4": ipv4,
                        "ipv6": ipv6,
                    },
                    ip_get_params.IPGetParams,
                ),
                post_parser=ResultWrapper[Optional[IPGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IPGetResponse]], ResultWrapper[IPGetResponse]),
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
