# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import make_request_options
from ......types.zero_trust.devices.split_tunnel_exclude_param import SplitTunnelExcludeParam
from ......types.zero_trust.devices.policies.default.exclude_get_response import ExcludeGetResponse
from ......types.zero_trust.devices.policies.default.exclude_update_response import ExcludeUpdateResponse

__all__ = ["ExcludesResource", "AsyncExcludesResource"]


class ExcludesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExcludesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ExcludesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExcludesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ExcludesResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        body: Iterable[SplitTunnelExcludeParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeUpdateResponse]:
        """
        Sets the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/devices/policy/exclude",
            body=maybe_transform(body, Iterable[SplitTunnelExcludeParam]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ExcludeUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ExcludeUpdateResponse]], ResultWrapper[ExcludeUpdateResponse]),
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeGetResponse]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/policy/exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ExcludeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ExcludeGetResponse]], ResultWrapper[ExcludeGetResponse]),
        )


class AsyncExcludesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExcludesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExcludesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExcludesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncExcludesResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        body: Iterable[SplitTunnelExcludeParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeUpdateResponse]:
        """
        Sets the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/devices/policy/exclude",
            body=await async_maybe_transform(body, Iterable[SplitTunnelExcludeParam]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ExcludeUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ExcludeUpdateResponse]], ResultWrapper[ExcludeUpdateResponse]),
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeGetResponse]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/policy/exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ExcludeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ExcludeGetResponse]], ResultWrapper[ExcludeGetResponse]),
        )


class ExcludesResourceWithRawResponse:
    def __init__(self, excludes: ExcludesResource) -> None:
        self._excludes = excludes

        self.update = to_raw_response_wrapper(
            excludes.update,
        )
        self.get = to_raw_response_wrapper(
            excludes.get,
        )


class AsyncExcludesResourceWithRawResponse:
    def __init__(self, excludes: AsyncExcludesResource) -> None:
        self._excludes = excludes

        self.update = async_to_raw_response_wrapper(
            excludes.update,
        )
        self.get = async_to_raw_response_wrapper(
            excludes.get,
        )


class ExcludesResourceWithStreamingResponse:
    def __init__(self, excludes: ExcludesResource) -> None:
        self._excludes = excludes

        self.update = to_streamed_response_wrapper(
            excludes.update,
        )
        self.get = to_streamed_response_wrapper(
            excludes.get,
        )


class AsyncExcludesResourceWithStreamingResponse:
    def __init__(self, excludes: AsyncExcludesResource) -> None:
        self._excludes = excludes

        self.update = async_to_streamed_response_wrapper(
            excludes.update,
        )
        self.get = async_to_streamed_response_wrapper(
            excludes.get,
        )
