# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

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
from ..._base_client import (
    make_request_options,
)
from ...types.magic_transit import (
    CfInterconnectGetResponse,
    CfInterconnectListResponse,
    CfInterconnectUpdateResponse,
    cf_interconnect_update_params,
)

__all__ = ["CfInterconnects", "AsyncCfInterconnects"]


class CfInterconnects(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CfInterconnectsWithRawResponse:
        return CfInterconnectsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CfInterconnectsWithStreamingResponse:
        return CfInterconnectsWithStreamingResponse(self)

    def update(
        self,
        tunnel_identifier: str,
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

          tunnel_identifier: Identifier

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
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._put(
            f"/accounts/{account_id}/magic/cf_interconnects/{tunnel_identifier}",
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
                post_parser=ResultWrapper._unwrapper,
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectListResponse], ResultWrapper[CfInterconnectListResponse]),
        )

    def get(
        self,
        tunnel_identifier: str,
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

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._get(
            f"/accounts/{account_id}/magic/cf_interconnects/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectGetResponse], ResultWrapper[CfInterconnectGetResponse]),
        )


class AsyncCfInterconnects(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCfInterconnectsWithRawResponse:
        return AsyncCfInterconnectsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCfInterconnectsWithStreamingResponse:
        return AsyncCfInterconnectsWithStreamingResponse(self)

    async def update(
        self,
        tunnel_identifier: str,
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

          tunnel_identifier: Identifier

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
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/cf_interconnects/{tunnel_identifier}",
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
                post_parser=ResultWrapper._unwrapper,
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectListResponse], ResultWrapper[CfInterconnectListResponse]),
        )

    async def get(
        self,
        tunnel_identifier: str,
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

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/cf_interconnects/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectGetResponse], ResultWrapper[CfInterconnectGetResponse]),
        )


class CfInterconnectsWithRawResponse:
    def __init__(self, cf_interconnects: CfInterconnects) -> None:
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


class AsyncCfInterconnectsWithRawResponse:
    def __init__(self, cf_interconnects: AsyncCfInterconnects) -> None:
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


class CfInterconnectsWithStreamingResponse:
    def __init__(self, cf_interconnects: CfInterconnects) -> None:
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


class AsyncCfInterconnectsWithStreamingResponse:
    def __init__(self, cf_interconnects: AsyncCfInterconnects) -> None:
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
