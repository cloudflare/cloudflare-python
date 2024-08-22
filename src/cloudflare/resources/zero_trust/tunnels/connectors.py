# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.tunnels.client import Client

from ...._wrappers import ResultWrapper

from ...._base_client import make_request_options

from typing import Type

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from typing import cast
from typing import cast

__all__ = ["ConnectorsResource", "AsyncConnectorsResource"]

class ConnectorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectorsResourceWithRawResponse:
        return ConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorsResourceWithStreamingResponse:
        return ConnectorsResourceWithStreamingResponse(self)

    def get(self,
    connector_id: str,
    *,
    account_id: str,
    tunnel_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Client:
        """
        Fetches connector and connection details for a Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          connector_id: UUID of the Cloudflare Tunnel connector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}'
          )
        if not connector_id:
          raise ValueError(
            f'Expected a non-empty value for `connector_id` but received {connector_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Client]._unwrapper),
            cast_to=cast(Type[Client], ResultWrapper[Client]),
        )

class AsyncConnectorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectorsResourceWithRawResponse:
        return AsyncConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorsResourceWithStreamingResponse:
        return AsyncConnectorsResourceWithStreamingResponse(self)

    async def get(self,
    connector_id: str,
    *,
    account_id: str,
    tunnel_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Client:
        """
        Fetches connector and connection details for a Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          connector_id: UUID of the Cloudflare Tunnel connector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}'
          )
        if not connector_id:
          raise ValueError(
            f'Expected a non-empty value for `connector_id` but received {connector_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Client]._unwrapper),
            cast_to=cast(Type[Client], ResultWrapper[Client]),
        )

class ConnectorsResourceWithRawResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.get = to_raw_response_wrapper(
            connectors.get,
        )

class AsyncConnectorsResourceWithRawResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.get = async_to_raw_response_wrapper(
            connectors.get,
        )

class ConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.get = to_streamed_response_wrapper(
            connectors.get,
        )

class AsyncConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.get = async_to_streamed_response_wrapper(
            connectors.get,
        )