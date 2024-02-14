# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.cfd_tunnels import ConnectorGetResponse

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
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Connectors", "AsyncConnectors"]


class Connectors(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectorsWithRawResponse:
        return ConnectorsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorsWithStreamingResponse:
        return ConnectorsWithStreamingResponse(self)

    def get(
        self,
        connector_id: str,
        *,
        account_id: str,
        tunnel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectorGetResponse:
        """
        Fetches connector and connection details for a Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          connector_id: UUID of the Cloudflare Tunnel client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConnectorGetResponse], ResultWrapper[ConnectorGetResponse]),
        )


class AsyncConnectors(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectorsWithRawResponse:
        return AsyncConnectorsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorsWithStreamingResponse:
        return AsyncConnectorsWithStreamingResponse(self)

    async def get(
        self,
        connector_id: str,
        *,
        account_id: str,
        tunnel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectorGetResponse:
        """
        Fetches connector and connection details for a Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          connector_id: UUID of the Cloudflare Tunnel client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConnectorGetResponse], ResultWrapper[ConnectorGetResponse]),
        )


class ConnectorsWithRawResponse:
    def __init__(self, connectors: Connectors) -> None:
        self._connectors = connectors

        self.get = to_raw_response_wrapper(
            connectors.get,
        )


class AsyncConnectorsWithRawResponse:
    def __init__(self, connectors: AsyncConnectors) -> None:
        self._connectors = connectors

        self.get = async_to_raw_response_wrapper(
            connectors.get,
        )


class ConnectorsWithStreamingResponse:
    def __init__(self, connectors: Connectors) -> None:
        self._connectors = connectors

        self.get = to_streamed_response_wrapper(
            connectors.get,
        )


class AsyncConnectorsWithStreamingResponse:
    def __init__(self, connectors: AsyncConnectors) -> None:
        self._connectors = connectors

        self.get = async_to_streamed_response_wrapper(
            connectors.get,
        )
