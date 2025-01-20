# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncV4PagePagination, AsyncV4PagePagination
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.dex.commands import device_list_params
from .....types.zero_trust.dex.commands.device_list_response import DeviceListResponse

__all__ = ["DevicesResource", "AsyncDevicesResource"]


class DevicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DevicesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        page: float,
        per_page: float,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePagination[Optional[DeviceListResponse]]:
        """
        List devices with WARP client support for remote captures which have been
        connected in the last 1 hour.

        Args:
          page: Page number of paginated results

          per_page: Number of items per page

          search: Filter devices by name or email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dex/commands/devices",
            page=SyncV4PagePagination[Optional[DeviceListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    device_list_params.DeviceListParams,
                ),
            ),
            model=DeviceListResponse,
        )


class AsyncDevicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDevicesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        page: float,
        per_page: float,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Optional[DeviceListResponse], AsyncV4PagePagination[Optional[DeviceListResponse]]]:
        """
        List devices with WARP client support for remote captures which have been
        connected in the last 1 hour.

        Args:
          page: Page number of paginated results

          per_page: Number of items per page

          search: Filter devices by name or email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dex/commands/devices",
            page=AsyncV4PagePagination[Optional[DeviceListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    device_list_params.DeviceListParams,
                ),
            ),
            model=DeviceListResponse,
        )


class DevicesResourceWithRawResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.list = to_raw_response_wrapper(
            devices.list,
        )


class AsyncDevicesResourceWithRawResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.list = async_to_raw_response_wrapper(
            devices.list,
        )


class DevicesResourceWithStreamingResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.list = to_streamed_response_wrapper(
            devices.list,
        )


class AsyncDevicesResourceWithStreamingResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.list = async_to_streamed_response_wrapper(
            devices.list,
        )
