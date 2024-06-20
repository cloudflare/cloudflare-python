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
from ...types.magic_transit import gre_tunnel_create_params
from ...types.magic_transit.gre_tunnel_list_response import GRETunnelListResponse
from ...types.magic_transit.gre_tunnel_create_response import GRETunnelCreateResponse

__all__ = ["GRETunnelsResource", "AsyncGRETunnelsResource"]


class GRETunnelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GRETunnelsResourceWithRawResponse:
        return GRETunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GRETunnelsResourceWithStreamingResponse:
        return GRETunnelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GRETunnelCreateResponse:
        """Creates new GRE tunnels.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/gre_tunnels",
            body=maybe_transform(body, gre_tunnel_create_params.GRETunnelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[GRETunnelCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[GRETunnelCreateResponse], ResultWrapper[GRETunnelCreateResponse]),
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
    ) -> GRETunnelListResponse:
        """
        Lists GRE tunnels associated with an account.

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
            f"/accounts/{account_id}/magic/gre_tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[GRETunnelListResponse]._unwrapper,
            ),
            cast_to=cast(Type[GRETunnelListResponse], ResultWrapper[GRETunnelListResponse]),
        )


class AsyncGRETunnelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGRETunnelsResourceWithRawResponse:
        return AsyncGRETunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGRETunnelsResourceWithStreamingResponse:
        return AsyncGRETunnelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GRETunnelCreateResponse:
        """Creates new GRE tunnels.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/gre_tunnels",
            body=await async_maybe_transform(body, gre_tunnel_create_params.GRETunnelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[GRETunnelCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[GRETunnelCreateResponse], ResultWrapper[GRETunnelCreateResponse]),
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
    ) -> GRETunnelListResponse:
        """
        Lists GRE tunnels associated with an account.

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
            f"/accounts/{account_id}/magic/gre_tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[GRETunnelListResponse]._unwrapper,
            ),
            cast_to=cast(Type[GRETunnelListResponse], ResultWrapper[GRETunnelListResponse]),
        )


class GRETunnelsResourceWithRawResponse:
    def __init__(self, gre_tunnels: GRETunnelsResource) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = to_raw_response_wrapper(
            gre_tunnels.create,
        )
        self.list = to_raw_response_wrapper(
            gre_tunnels.list,
        )


class AsyncGRETunnelsResourceWithRawResponse:
    def __init__(self, gre_tunnels: AsyncGRETunnelsResource) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = async_to_raw_response_wrapper(
            gre_tunnels.create,
        )
        self.list = async_to_raw_response_wrapper(
            gre_tunnels.list,
        )


class GRETunnelsResourceWithStreamingResponse:
    def __init__(self, gre_tunnels: GRETunnelsResource) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = to_streamed_response_wrapper(
            gre_tunnels.create,
        )
        self.list = to_streamed_response_wrapper(
            gre_tunnels.list,
        )


class AsyncGRETunnelsResourceWithStreamingResponse:
    def __init__(self, gre_tunnels: AsyncGRETunnelsResource) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = async_to_streamed_response_wrapper(
            gre_tunnels.create,
        )
        self.list = async_to_streamed_response_wrapper(
            gre_tunnels.list,
        )
