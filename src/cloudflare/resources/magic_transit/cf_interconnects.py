# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.magic_transit.cf_interconnect_update_response import CfInterconnectUpdateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import Type

from ...types.magic_transit.cf_interconnect_list_response import CfInterconnectListResponse

from ...types.magic_transit.cf_interconnect_get_response import CfInterconnectGetResponse

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ...types.magic_transit import cf_interconnect_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.magic_transit import cf_interconnect_update_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CfInterconnectsResource", "AsyncCfInterconnectsResource"]


class CfInterconnectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CfInterconnectsResourceWithRawResponse:
        return CfInterconnectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CfInterconnectsResourceWithStreamingResponse:
        return CfInterconnectsResourceWithStreamingResponse(self)

    def update(
        self,
        cf_interconnect_id: str,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        gre: cf_interconnect_update_params.GRE | NotGiven = NOT_GIVEN,
        health_check: cf_interconnect_update_params.HealthCheck | NotGiven = NOT_GIVEN,
        interface_address: str | NotGiven = NOT_GIVEN,
        mtu: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CfInterconnectUpdateResponse:
        """Updates a specific interconnect associated with an account.

        Use
        `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_id: Identifier

          cf_interconnect_id: Identifier

          description: An optional description of the interconnect.

          gre: The configuration specific to GRE interconnects.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          mtu: The Maximum Transmission Unit (MTU) in bytes for the interconnect. The minimum
              value is 576.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf_interconnect_id:
            raise ValueError(f"Expected a non-empty value for `cf_interconnect_id` but received {cf_interconnect_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "gre": gre,
                    "health_check": health_check,
                    "interface_address": interface_address,
                    "mtu": mtu,
                },
                cf_interconnect_update_params.CfInterconnectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CfInterconnectUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectUpdateResponse], ResultWrapper[CfInterconnectUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CfInterconnectListResponse:
        """
        Lists interconnects associated with an account.

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
            f"/accounts/{account_id}/magic/cf_interconnects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CfInterconnectListResponse]._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectListResponse], ResultWrapper[CfInterconnectListResponse]),
        )

    def get(
        self,
        cf_interconnect_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CfInterconnectGetResponse:
        """
        Lists details for a specific interconnect.

        Args:
          account_id: Identifier

          cf_interconnect_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf_interconnect_id:
            raise ValueError(f"Expected a non-empty value for `cf_interconnect_id` but received {cf_interconnect_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CfInterconnectGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectGetResponse], ResultWrapper[CfInterconnectGetResponse]),
        )


class AsyncCfInterconnectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCfInterconnectsResourceWithRawResponse:
        return AsyncCfInterconnectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCfInterconnectsResourceWithStreamingResponse:
        return AsyncCfInterconnectsResourceWithStreamingResponse(self)

    async def update(
        self,
        cf_interconnect_id: str,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        gre: cf_interconnect_update_params.GRE | NotGiven = NOT_GIVEN,
        health_check: cf_interconnect_update_params.HealthCheck | NotGiven = NOT_GIVEN,
        interface_address: str | NotGiven = NOT_GIVEN,
        mtu: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CfInterconnectUpdateResponse:
        """Updates a specific interconnect associated with an account.

        Use
        `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_id: Identifier

          cf_interconnect_id: Identifier

          description: An optional description of the interconnect.

          gre: The configuration specific to GRE interconnects.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          mtu: The Maximum Transmission Unit (MTU) in bytes for the interconnect. The minimum
              value is 576.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf_interconnect_id:
            raise ValueError(f"Expected a non-empty value for `cf_interconnect_id` but received {cf_interconnect_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "gre": gre,
                    "health_check": health_check,
                    "interface_address": interface_address,
                    "mtu": mtu,
                },
                cf_interconnect_update_params.CfInterconnectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CfInterconnectUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectUpdateResponse], ResultWrapper[CfInterconnectUpdateResponse]),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CfInterconnectListResponse:
        """
        Lists interconnects associated with an account.

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
            f"/accounts/{account_id}/magic/cf_interconnects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CfInterconnectListResponse]._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectListResponse], ResultWrapper[CfInterconnectListResponse]),
        )

    async def get(
        self,
        cf_interconnect_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CfInterconnectGetResponse:
        """
        Lists details for a specific interconnect.

        Args:
          account_id: Identifier

          cf_interconnect_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf_interconnect_id:
            raise ValueError(f"Expected a non-empty value for `cf_interconnect_id` but received {cf_interconnect_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CfInterconnectGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectGetResponse], ResultWrapper[CfInterconnectGetResponse]),
        )


class CfInterconnectsResourceWithRawResponse:
    def __init__(self, cf_interconnects: CfInterconnectsResource) -> None:
        self._cf_interconnects = cf_interconnects

        self.update = to_raw_response_wrapper(
            cf_interconnects.update,
        )
        self.list = to_raw_response_wrapper(
            cf_interconnects.list,
        )
        self.get = to_raw_response_wrapper(
            cf_interconnects.get,
        )


class AsyncCfInterconnectsResourceWithRawResponse:
    def __init__(self, cf_interconnects: AsyncCfInterconnectsResource) -> None:
        self._cf_interconnects = cf_interconnects

        self.update = async_to_raw_response_wrapper(
            cf_interconnects.update,
        )
        self.list = async_to_raw_response_wrapper(
            cf_interconnects.list,
        )
        self.get = async_to_raw_response_wrapper(
            cf_interconnects.get,
        )


class CfInterconnectsResourceWithStreamingResponse:
    def __init__(self, cf_interconnects: CfInterconnectsResource) -> None:
        self._cf_interconnects = cf_interconnects

        self.update = to_streamed_response_wrapper(
            cf_interconnects.update,
        )
        self.list = to_streamed_response_wrapper(
            cf_interconnects.list,
        )
        self.get = to_streamed_response_wrapper(
            cf_interconnects.get,
        )


class AsyncCfInterconnectsResourceWithStreamingResponse:
    def __init__(self, cf_interconnects: AsyncCfInterconnectsResource) -> None:
        self._cf_interconnects = cf_interconnects

        self.update = async_to_streamed_response_wrapper(
            cf_interconnects.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cf_interconnects.list,
        )
        self.get = async_to_streamed_response_wrapper(
            cf_interconnects.get,
        )
