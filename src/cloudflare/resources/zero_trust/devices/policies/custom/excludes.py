# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......pagination import SyncSinglePage, AsyncSinglePage
from ......_base_client import AsyncPaginator, make_request_options
from ......types.zero_trust.devices.split_tunnel_exclude import SplitTunnelExclude
from ......types.zero_trust.devices.split_tunnel_exclude_param import SplitTunnelExcludeParam

__all__ = ["ExcludesResource", "AsyncExcludesResource"]


class ExcludesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExcludesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        policy_id: str,
        *,
        account_id: str,
        body: Iterable[SplitTunnelExcludeParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[SplitTunnelExclude]:
        """
        Sets the list of routes excluded from the WARP client's tunnel for a specific
        device settings profile.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/policy/{policy_id}/exclude",
            page=SyncSinglePage[SplitTunnelExclude],
            body=maybe_transform(body, Iterable[SplitTunnelExcludeParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SplitTunnelExclude,
            method="put",
        )

    def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[SplitTunnelExclude]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel for a specific
        device settings profile.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/policy/{policy_id}/exclude",
            page=SyncSinglePage[SplitTunnelExclude],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SplitTunnelExclude,
        )


class AsyncExcludesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExcludesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    def update(
        self,
        policy_id: str,
        *,
        account_id: str,
        body: Iterable[SplitTunnelExcludeParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SplitTunnelExclude, AsyncSinglePage[SplitTunnelExclude]]:
        """
        Sets the list of routes excluded from the WARP client's tunnel for a specific
        device settings profile.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/policy/{policy_id}/exclude",
            page=AsyncSinglePage[SplitTunnelExclude],
            body=maybe_transform(body, Iterable[SplitTunnelExcludeParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SplitTunnelExclude,
            method="put",
        )

    def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SplitTunnelExclude, AsyncSinglePage[SplitTunnelExclude]]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel for a specific
        device settings profile.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/policy/{policy_id}/exclude",
            page=AsyncSinglePage[SplitTunnelExclude],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SplitTunnelExclude,
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
