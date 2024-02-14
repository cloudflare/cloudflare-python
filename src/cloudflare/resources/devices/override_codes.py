# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.devices import OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse

__all__ = ["OverrideCodes", "AsyncOverrideCodes"]


class OverrideCodes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OverrideCodesWithRawResponse:
        return OverrideCodesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OverrideCodesWithStreamingResponse:
        return OverrideCodesWithStreamingResponse(self)

    def devices_list_admin_override_code_for_device(
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
    ) -> Optional[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse]:
        """Fetches a one-time use admin override code for a device.

        This relies on the
        **Admin Override** setting being enabled in your device configuration.

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
            f"/accounts/{identifier}/devices/{uuid}/override_codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse]],
                ResultWrapper[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse],
            ),
        )


class AsyncOverrideCodes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOverrideCodesWithRawResponse:
        return AsyncOverrideCodesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOverrideCodesWithStreamingResponse:
        return AsyncOverrideCodesWithStreamingResponse(self)

    async def devices_list_admin_override_code_for_device(
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
    ) -> Optional[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse]:
        """Fetches a one-time use admin override code for a device.

        This relies on the
        **Admin Override** setting being enabled in your device configuration.

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
            f"/accounts/{identifier}/devices/{uuid}/override_codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse]],
                ResultWrapper[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse],
            ),
        )


class OverrideCodesWithRawResponse:
    def __init__(self, override_codes: OverrideCodes) -> None:
        self._override_codes = override_codes

        self.devices_list_admin_override_code_for_device = to_raw_response_wrapper(
            override_codes.devices_list_admin_override_code_for_device,
        )


class AsyncOverrideCodesWithRawResponse:
    def __init__(self, override_codes: AsyncOverrideCodes) -> None:
        self._override_codes = override_codes

        self.devices_list_admin_override_code_for_device = async_to_raw_response_wrapper(
            override_codes.devices_list_admin_override_code_for_device,
        )


class OverrideCodesWithStreamingResponse:
    def __init__(self, override_codes: OverrideCodes) -> None:
        self._override_codes = override_codes

        self.devices_list_admin_override_code_for_device = to_streamed_response_wrapper(
            override_codes.devices_list_admin_override_code_for_device,
        )


class AsyncOverrideCodesWithStreamingResponse:
    def __init__(self, override_codes: AsyncOverrideCodes) -> None:
        self._override_codes = override_codes

        self.devices_list_admin_override_code_for_device = async_to_streamed_response_wrapper(
            override_codes.devices_list_admin_override_code_for_device,
        )
