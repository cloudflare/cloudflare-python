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
    ExcludeDevicesGetSplitTunnelExcludeListResponse,
    ExcludeDevicesSetSplitTunnelExcludeListResponse,
    ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse,
    ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse,
    exclude_devices_set_split_tunnel_exclude_list_params,
    exclude_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy_params,
)

__all__ = ["Excludes", "AsyncExcludes"]


class Excludes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExcludesWithRawResponse:
        return ExcludesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExcludesWithStreamingResponse:
        return ExcludesWithStreamingResponse(self)

    def devices_get_split_tunnel_exclude_list(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeDevicesGetSplitTunnelExcludeListResponse]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{identifier}/devices/policy/exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ExcludeDevicesGetSplitTunnelExcludeListResponse]],
                ResultWrapper[ExcludeDevicesGetSplitTunnelExcludeListResponse],
            ),
        )

    def devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
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
    ) -> Optional[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel for a specific
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
            f"/accounts/{identifier}/devices/policy/{uuid}/exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse]],
                ResultWrapper[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            ),
        )

    def devices_set_split_tunnel_exclude_list(
        self,
        identifier: object,
        *,
        body: Iterable[exclude_devices_set_split_tunnel_exclude_list_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeDevicesSetSplitTunnelExcludeListResponse]:
        """
        Sets the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{identifier}/devices/policy/exclude",
            body=maybe_transform(
                body, exclude_devices_set_split_tunnel_exclude_list_params.ExcludeDevicesSetSplitTunnelExcludeListParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ExcludeDevicesSetSplitTunnelExcludeListResponse]],
                ResultWrapper[ExcludeDevicesSetSplitTunnelExcludeListResponse],
            ),
        )

    def devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
        self,
        uuid: str,
        *,
        identifier: object,
        body: Iterable[exclude_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse]:
        """
        Sets the list of routes excluded from the WARP client's tunnel for a specific
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
            f"/accounts/{identifier}/devices/policy/{uuid}/exclude",
            body=maybe_transform(
                body,
                exclude_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy_params.ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse]],
                ResultWrapper[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            ),
        )


class AsyncExcludes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExcludesWithRawResponse:
        return AsyncExcludesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExcludesWithStreamingResponse:
        return AsyncExcludesWithStreamingResponse(self)

    async def devices_get_split_tunnel_exclude_list(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeDevicesGetSplitTunnelExcludeListResponse]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{identifier}/devices/policy/exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ExcludeDevicesGetSplitTunnelExcludeListResponse]],
                ResultWrapper[ExcludeDevicesGetSplitTunnelExcludeListResponse],
            ),
        )

    async def devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
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
    ) -> Optional[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel for a specific
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
            f"/accounts/{identifier}/devices/policy/{uuid}/exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse]],
                ResultWrapper[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            ),
        )

    async def devices_set_split_tunnel_exclude_list(
        self,
        identifier: object,
        *,
        body: Iterable[exclude_devices_set_split_tunnel_exclude_list_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeDevicesSetSplitTunnelExcludeListResponse]:
        """
        Sets the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{identifier}/devices/policy/exclude",
            body=maybe_transform(
                body, exclude_devices_set_split_tunnel_exclude_list_params.ExcludeDevicesSetSplitTunnelExcludeListParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ExcludeDevicesSetSplitTunnelExcludeListResponse]],
                ResultWrapper[ExcludeDevicesSetSplitTunnelExcludeListResponse],
            ),
        )

    async def devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
        self,
        uuid: str,
        *,
        identifier: object,
        body: Iterable[exclude_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse]:
        """
        Sets the list of routes excluded from the WARP client's tunnel for a specific
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
            f"/accounts/{identifier}/devices/policy/{uuid}/exclude",
            body=maybe_transform(
                body,
                exclude_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy_params.ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse]],
                ResultWrapper[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            ),
        )


class ExcludesWithRawResponse:
    def __init__(self, excludes: Excludes) -> None:
        self._excludes = excludes

        self.devices_get_split_tunnel_exclude_list = to_raw_response_wrapper(
            excludes.devices_get_split_tunnel_exclude_list,
        )
        self.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy = to_raw_response_wrapper(
            excludes.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy,
        )
        self.devices_set_split_tunnel_exclude_list = to_raw_response_wrapper(
            excludes.devices_set_split_tunnel_exclude_list,
        )
        self.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy = to_raw_response_wrapper(
            excludes.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy,
        )


class AsyncExcludesWithRawResponse:
    def __init__(self, excludes: AsyncExcludes) -> None:
        self._excludes = excludes

        self.devices_get_split_tunnel_exclude_list = async_to_raw_response_wrapper(
            excludes.devices_get_split_tunnel_exclude_list,
        )
        self.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy = async_to_raw_response_wrapper(
            excludes.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy,
        )
        self.devices_set_split_tunnel_exclude_list = async_to_raw_response_wrapper(
            excludes.devices_set_split_tunnel_exclude_list,
        )
        self.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy = async_to_raw_response_wrapper(
            excludes.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy,
        )


class ExcludesWithStreamingResponse:
    def __init__(self, excludes: Excludes) -> None:
        self._excludes = excludes

        self.devices_get_split_tunnel_exclude_list = to_streamed_response_wrapper(
            excludes.devices_get_split_tunnel_exclude_list,
        )
        self.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy = to_streamed_response_wrapper(
            excludes.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy,
        )
        self.devices_set_split_tunnel_exclude_list = to_streamed_response_wrapper(
            excludes.devices_set_split_tunnel_exclude_list,
        )
        self.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy = to_streamed_response_wrapper(
            excludes.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy,
        )


class AsyncExcludesWithStreamingResponse:
    def __init__(self, excludes: AsyncExcludes) -> None:
        self._excludes = excludes

        self.devices_get_split_tunnel_exclude_list = async_to_streamed_response_wrapper(
            excludes.devices_get_split_tunnel_exclude_list,
        )
        self.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy = async_to_streamed_response_wrapper(
            excludes.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy,
        )
        self.devices_set_split_tunnel_exclude_list = async_to_streamed_response_wrapper(
            excludes.devices_set_split_tunnel_exclude_list,
        )
        self.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy = async_to_streamed_response_wrapper(
            excludes.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy,
        )
