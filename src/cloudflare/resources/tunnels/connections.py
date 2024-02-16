# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.tunnels import ConnectionDeleteResponse

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
from ...types.tunnels import connection_delete_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Connections", "AsyncConnections"]


class Connections(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectionsWithRawResponse:
        return ConnectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionsWithStreamingResponse:
        return ConnectionsWithStreamingResponse(self)

    def delete(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionDeleteResponse:
        """Removes connections that are in a disconnected or pending reconnect state.

        We
        recommend running this command after shutting down a tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            ConnectionDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/tunnels/{tunnel_id}/connections",
                body=maybe_transform(body, connection_delete_params.ConnectionDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConnectionDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncConnections(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectionsWithRawResponse:
        return AsyncConnectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionsWithStreamingResponse:
        return AsyncConnectionsWithStreamingResponse(self)

    async def delete(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionDeleteResponse:
        """Removes connections that are in a disconnected or pending reconnect state.

        We
        recommend running this command after shutting down a tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            ConnectionDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/tunnels/{tunnel_id}/connections",
                body=maybe_transform(body, connection_delete_params.ConnectionDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConnectionDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ConnectionsWithRawResponse:
    def __init__(self, connections: Connections) -> None:
        self._connections = connections

        self.delete = to_raw_response_wrapper(
            connections.delete,
        )


class AsyncConnectionsWithRawResponse:
    def __init__(self, connections: AsyncConnections) -> None:
        self._connections = connections

        self.delete = async_to_raw_response_wrapper(
            connections.delete,
        )


class ConnectionsWithStreamingResponse:
    def __init__(self, connections: Connections) -> None:
        self._connections = connections

        self.delete = to_streamed_response_wrapper(
            connections.delete,
        )


class AsyncConnectionsWithStreamingResponse:
    def __init__(self, connections: AsyncConnections) -> None:
        self._connections = connections

        self.delete = async_to_streamed_response_wrapper(
            connections.delete,
        )
