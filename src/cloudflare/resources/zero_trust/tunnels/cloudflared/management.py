# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.zero_trust.tunnels.cloudflared import management_create_params
from .....types.zero_trust.tunnels.cloudflared.management_create_response import ManagementCreateResponse

__all__ = ["ManagementResource", "AsyncManagementResource"]


class ManagementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ManagementResourceWithStreamingResponse(self)

    def create(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        resources: List[Literal["logs"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Gets a management token used to access the management resources (i.e.

        Streaming
        Logs) of a tunnel.

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
        return self._post(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/management",
            body=maybe_transform({"resources": resources}, management_create_params.ManagementCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ManagementCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncManagementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncManagementResourceWithStreamingResponse(self)

    async def create(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        resources: List[Literal["logs"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Gets a management token used to access the management resources (i.e.

        Streaming
        Logs) of a tunnel.

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
        return await self._post(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/management",
            body=await async_maybe_transform({"resources": resources}, management_create_params.ManagementCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ManagementCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class ManagementResourceWithRawResponse:
    def __init__(self, management: ManagementResource) -> None:
        self._management = management

        self.create = to_raw_response_wrapper(
            management.create,
        )


class AsyncManagementResourceWithRawResponse:
    def __init__(self, management: AsyncManagementResource) -> None:
        self._management = management

        self.create = async_to_raw_response_wrapper(
            management.create,
        )


class ManagementResourceWithStreamingResponse:
    def __init__(self, management: ManagementResource) -> None:
        self._management = management

        self.create = to_streamed_response_wrapper(
            management.create,
        )


class AsyncManagementResourceWithStreamingResponse:
    def __init__(self, management: AsyncManagementResource) -> None:
        self._management = management

        self.create = async_to_streamed_response_wrapper(
            management.create,
        )
