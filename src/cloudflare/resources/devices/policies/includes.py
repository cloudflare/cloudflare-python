# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.devices.policies import (
    IncludeDevicesGetSplitTunnelIncludeListResponse,
    IncludeDevicesSetSplitTunnelIncludeListResponse,
    IncludeDevicesGetSplitTunnelIncludeListForADeviceSettingsPolicyResponse,
    IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyResponse,
    include_devices_set_split_tunnel_include_list_params,
    include_devices_set_split_tunnel_include_list_for_a_device_settings_policy_params,
)

__all__ = ["Includes", "AsyncIncludes"]


class Includes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IncludesWithRawResponse:
        return IncludesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncludesWithStreamingResponse:
        return IncludesWithStreamingResponse(self)

    def devices_get_split_tunnel_include_list(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeDevicesGetSplitTunnelIncludeListResponse]:
        """
        Fetches the list of routes included in the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{identifier}/devices/policy/include",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IncludeDevicesGetSplitTunnelIncludeListResponse]],
                ResultWrapper[IncludeDevicesGetSplitTunnelIncludeListResponse],
            ),
        )

    def devices_get_split_tunnel_include_list_for_a_device_settings_policy(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeDevicesGetSplitTunnelIncludeListForADeviceSettingsPolicyResponse]:
        """
        Fetches the list of routes included in the WARP client's tunnel for a specific
        device settings profile.

        Args:
          uuid: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/accounts/{identifier}/devices/policy/{uuid}/include",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IncludeDevicesGetSplitTunnelIncludeListForADeviceSettingsPolicyResponse]],
                ResultWrapper[IncludeDevicesGetSplitTunnelIncludeListForADeviceSettingsPolicyResponse],
            ),
        )

    def devices_set_split_tunnel_include_list(
        self,
        identifier: object,
        *,
        body: Iterable[include_devices_set_split_tunnel_include_list_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeDevicesSetSplitTunnelIncludeListResponse]:
        """
        Sets the list of routes included in the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{identifier}/devices/policy/include",
            body=maybe_transform(
                body, include_devices_set_split_tunnel_include_list_params.IncludeDevicesSetSplitTunnelIncludeListParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IncludeDevicesSetSplitTunnelIncludeListResponse]],
                ResultWrapper[IncludeDevicesSetSplitTunnelIncludeListResponse],
            ),
        )

    def devices_set_split_tunnel_include_list_for_a_device_settings_policy(
        self,
        uuid: str,
        *,
        identifier: object,
        body: Iterable[include_devices_set_split_tunnel_include_list_for_a_device_settings_policy_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyResponse]:
        """
        Sets the list of routes included in the WARP client's tunnel for a specific
        device settings profile.

        Args:
          uuid: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._put(
            f"/accounts/{identifier}/devices/policy/{uuid}/include",
            body=maybe_transform(
                body,
                include_devices_set_split_tunnel_include_list_for_a_device_settings_policy_params.IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyResponse]],
                ResultWrapper[IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyResponse],
            ),
        )


class AsyncIncludes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIncludesWithRawResponse:
        return AsyncIncludesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncludesWithStreamingResponse:
        return AsyncIncludesWithStreamingResponse(self)

    async def devices_get_split_tunnel_include_list(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeDevicesGetSplitTunnelIncludeListResponse]:
        """
        Fetches the list of routes included in the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{identifier}/devices/policy/include",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IncludeDevicesGetSplitTunnelIncludeListResponse]],
                ResultWrapper[IncludeDevicesGetSplitTunnelIncludeListResponse],
            ),
        )

    async def devices_get_split_tunnel_include_list_for_a_device_settings_policy(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeDevicesGetSplitTunnelIncludeListForADeviceSettingsPolicyResponse]:
        """
        Fetches the list of routes included in the WARP client's tunnel for a specific
        device settings profile.

        Args:
          uuid: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/accounts/{identifier}/devices/policy/{uuid}/include",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IncludeDevicesGetSplitTunnelIncludeListForADeviceSettingsPolicyResponse]],
                ResultWrapper[IncludeDevicesGetSplitTunnelIncludeListForADeviceSettingsPolicyResponse],
            ),
        )

    async def devices_set_split_tunnel_include_list(
        self,
        identifier: object,
        *,
        body: Iterable[include_devices_set_split_tunnel_include_list_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeDevicesSetSplitTunnelIncludeListResponse]:
        """
        Sets the list of routes included in the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{identifier}/devices/policy/include",
            body=maybe_transform(
                body, include_devices_set_split_tunnel_include_list_params.IncludeDevicesSetSplitTunnelIncludeListParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IncludeDevicesSetSplitTunnelIncludeListResponse]],
                ResultWrapper[IncludeDevicesSetSplitTunnelIncludeListResponse],
            ),
        )

    async def devices_set_split_tunnel_include_list_for_a_device_settings_policy(
        self,
        uuid: str,
        *,
        identifier: object,
        body: Iterable[include_devices_set_split_tunnel_include_list_for_a_device_settings_policy_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyResponse]:
        """
        Sets the list of routes included in the WARP client's tunnel for a specific
        device settings profile.

        Args:
          uuid: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._put(
            f"/accounts/{identifier}/devices/policy/{uuid}/include",
            body=maybe_transform(
                body,
                include_devices_set_split_tunnel_include_list_for_a_device_settings_policy_params.IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyResponse]],
                ResultWrapper[IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyResponse],
            ),
        )


class IncludesWithRawResponse:
    def __init__(self, includes: Includes) -> None:
        self._includes = includes

        self.devices_get_split_tunnel_include_list = to_raw_response_wrapper(
            includes.devices_get_split_tunnel_include_list,
        )
        self.devices_get_split_tunnel_include_list_for_a_device_settings_policy = to_raw_response_wrapper(
            includes.devices_get_split_tunnel_include_list_for_a_device_settings_policy,
        )
        self.devices_set_split_tunnel_include_list = to_raw_response_wrapper(
            includes.devices_set_split_tunnel_include_list,
        )
        self.devices_set_split_tunnel_include_list_for_a_device_settings_policy = to_raw_response_wrapper(
            includes.devices_set_split_tunnel_include_list_for_a_device_settings_policy,
        )


class AsyncIncludesWithRawResponse:
    def __init__(self, includes: AsyncIncludes) -> None:
        self._includes = includes

        self.devices_get_split_tunnel_include_list = async_to_raw_response_wrapper(
            includes.devices_get_split_tunnel_include_list,
        )
        self.devices_get_split_tunnel_include_list_for_a_device_settings_policy = async_to_raw_response_wrapper(
            includes.devices_get_split_tunnel_include_list_for_a_device_settings_policy,
        )
        self.devices_set_split_tunnel_include_list = async_to_raw_response_wrapper(
            includes.devices_set_split_tunnel_include_list,
        )
        self.devices_set_split_tunnel_include_list_for_a_device_settings_policy = async_to_raw_response_wrapper(
            includes.devices_set_split_tunnel_include_list_for_a_device_settings_policy,
        )


class IncludesWithStreamingResponse:
    def __init__(self, includes: Includes) -> None:
        self._includes = includes

        self.devices_get_split_tunnel_include_list = to_streamed_response_wrapper(
            includes.devices_get_split_tunnel_include_list,
        )
        self.devices_get_split_tunnel_include_list_for_a_device_settings_policy = to_streamed_response_wrapper(
            includes.devices_get_split_tunnel_include_list_for_a_device_settings_policy,
        )
        self.devices_set_split_tunnel_include_list = to_streamed_response_wrapper(
            includes.devices_set_split_tunnel_include_list,
        )
        self.devices_set_split_tunnel_include_list_for_a_device_settings_policy = to_streamed_response_wrapper(
            includes.devices_set_split_tunnel_include_list_for_a_device_settings_policy,
        )


class AsyncIncludesWithStreamingResponse:
    def __init__(self, includes: AsyncIncludes) -> None:
        self._includes = includes

        self.devices_get_split_tunnel_include_list = async_to_streamed_response_wrapper(
            includes.devices_get_split_tunnel_include_list,
        )
        self.devices_get_split_tunnel_include_list_for_a_device_settings_policy = async_to_streamed_response_wrapper(
            includes.devices_get_split_tunnel_include_list_for_a_device_settings_policy,
        )
        self.devices_set_split_tunnel_include_list = async_to_streamed_response_wrapper(
            includes.devices_set_split_tunnel_include_list,
        )
        self.devices_set_split_tunnel_include_list_for_a_device_settings_policy = async_to_streamed_response_wrapper(
            includes.devices_set_split_tunnel_include_list_for_a_device_settings_policy,
        )
