# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
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
from .....types.zero_trust.tunnels.warp_connector import failover_update_params

__all__ = ["FailoverResource", "AsyncFailoverResource"]


class FailoverResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FailoverResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FailoverResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FailoverResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FailoverResourceWithStreamingResponse(self)

    def update(
        self,
        tunnel_id: str,
        *,
        account_id: str | None = None,
        client_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Triggers a manual failover for a specific WARP Connector Tunnel, setting the
        specified client as the active connector. The tunnel must be configured for high
        availability (HA) and the client must be linked to the tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          client_id: UUID of the Cloudflare Tunnel connector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}/failover", account_id=account_id, tunnel_id=tunnel_id
            ),
            body=maybe_transform({"client_id": client_id}, failover_update_params.FailoverUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncFailoverResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFailoverResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFailoverResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFailoverResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFailoverResourceWithStreamingResponse(self)

    async def update(
        self,
        tunnel_id: str,
        *,
        account_id: str | None = None,
        client_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Triggers a manual failover for a specific WARP Connector Tunnel, setting the
        specified client as the active connector. The tunnel must be configured for high
        availability (HA) and the client must be linked to the tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          client_id: UUID of the Cloudflare Tunnel connector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}/failover", account_id=account_id, tunnel_id=tunnel_id
            ),
            body=await async_maybe_transform({"client_id": client_id}, failover_update_params.FailoverUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class FailoverResourceWithRawResponse:
    def __init__(self, failover: FailoverResource) -> None:
        self._failover = failover

        self.update = to_raw_response_wrapper(
            failover.update,
        )


class AsyncFailoverResourceWithRawResponse:
    def __init__(self, failover: AsyncFailoverResource) -> None:
        self._failover = failover

        self.update = async_to_raw_response_wrapper(
            failover.update,
        )


class FailoverResourceWithStreamingResponse:
    def __init__(self, failover: FailoverResource) -> None:
        self._failover = failover

        self.update = to_streamed_response_wrapper(
            failover.update,
        )


class AsyncFailoverResourceWithStreamingResponse:
    def __init__(self, failover: AsyncFailoverResource) -> None:
        self._failover = failover

        self.update = async_to_streamed_response_wrapper(
            failover.update,
        )
