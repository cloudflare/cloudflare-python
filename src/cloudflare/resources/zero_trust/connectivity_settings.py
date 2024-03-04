# File generated from our OpenAPI spec by Stainless.

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
from ...types.zero_trust import (
    ConnectivitySettingGetResponse,
    ConnectivitySettingEditResponse,
    connectivity_setting_edit_params,
)

__all__ = ["ConnectivitySettings", "AsyncConnectivitySettings"]


class ConnectivitySettings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectivitySettingsWithRawResponse:
        return ConnectivitySettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectivitySettingsWithStreamingResponse:
        return ConnectivitySettingsWithStreamingResponse(self)

    def edit(
        self,
        *,
        account_id: str,
        icmp_proxy_enabled: bool | NotGiven = NOT_GIVEN,
        offramp_warp_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectivitySettingEditResponse:
        """
        Updates the Zero Trust Connectivity Settings for the given account.

        Args:
          account_id: Cloudflare account ID

          icmp_proxy_enabled: A flag to enable the ICMP proxy for the account network.

          offramp_warp_enabled: A flag to enable WARP to WARP traffic.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            f"/accounts/{account_id}/zerotrust/connectivity_settings",
            body=maybe_transform(
                {
                    "icmp_proxy_enabled": icmp_proxy_enabled,
                    "offramp_warp_enabled": offramp_warp_enabled,
                },
                connectivity_setting_edit_params.ConnectivitySettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConnectivitySettingEditResponse], ResultWrapper[ConnectivitySettingEditResponse]),
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
    ) -> ConnectivitySettingGetResponse:
        """
        Gets the Zero Trust Connectivity Settings for the given account.

        Args:
          account_id: Cloudflare account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/zerotrust/connectivity_settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConnectivitySettingGetResponse], ResultWrapper[ConnectivitySettingGetResponse]),
        )


class AsyncConnectivitySettings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectivitySettingsWithRawResponse:
        return AsyncConnectivitySettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectivitySettingsWithStreamingResponse:
        return AsyncConnectivitySettingsWithStreamingResponse(self)

    async def edit(
        self,
        *,
        account_id: str,
        icmp_proxy_enabled: bool | NotGiven = NOT_GIVEN,
        offramp_warp_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectivitySettingEditResponse:
        """
        Updates the Zero Trust Connectivity Settings for the given account.

        Args:
          account_id: Cloudflare account ID

          icmp_proxy_enabled: A flag to enable the ICMP proxy for the account network.

          offramp_warp_enabled: A flag to enable WARP to WARP traffic.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/zerotrust/connectivity_settings",
            body=await async_maybe_transform(
                {
                    "icmp_proxy_enabled": icmp_proxy_enabled,
                    "offramp_warp_enabled": offramp_warp_enabled,
                },
                connectivity_setting_edit_params.ConnectivitySettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConnectivitySettingEditResponse], ResultWrapper[ConnectivitySettingEditResponse]),
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
    ) -> ConnectivitySettingGetResponse:
        """
        Gets the Zero Trust Connectivity Settings for the given account.

        Args:
          account_id: Cloudflare account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/zerotrust/connectivity_settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConnectivitySettingGetResponse], ResultWrapper[ConnectivitySettingGetResponse]),
        )


class ConnectivitySettingsWithRawResponse:
    def __init__(self, connectivity_settings: ConnectivitySettings) -> None:
        self._connectivity_settings = connectivity_settings

        self.edit = to_raw_response_wrapper(
            connectivity_settings.edit,
        )
        self.get = to_raw_response_wrapper(
            connectivity_settings.get,
        )


class AsyncConnectivitySettingsWithRawResponse:
    def __init__(self, connectivity_settings: AsyncConnectivitySettings) -> None:
        self._connectivity_settings = connectivity_settings

        self.edit = async_to_raw_response_wrapper(
            connectivity_settings.edit,
        )
        self.get = async_to_raw_response_wrapper(
            connectivity_settings.get,
        )


class ConnectivitySettingsWithStreamingResponse:
    def __init__(self, connectivity_settings: ConnectivitySettings) -> None:
        self._connectivity_settings = connectivity_settings

        self.edit = to_streamed_response_wrapper(
            connectivity_settings.edit,
        )
        self.get = to_streamed_response_wrapper(
            connectivity_settings.get,
        )


class AsyncConnectivitySettingsWithStreamingResponse:
    def __init__(self, connectivity_settings: AsyncConnectivitySettings) -> None:
        self._connectivity_settings = connectivity_settings

        self.edit = async_to_streamed_response_wrapper(
            connectivity_settings.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            connectivity_settings.get,
        )
