# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.devices import device_get_params, device_list_params
from ....types.zero_trust.devices.device_get_response import DeviceGetResponse
from ....types.zero_trust.devices.device_list_response import DeviceListResponse

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
        id: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        active_registrations: Literal["include", "only", "exclude"] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        include: str | NotGiven = NOT_GIVEN,
        last_seen_user: device_list_params.LastSeenUser | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        seen_after: str | NotGiven = NOT_GIVEN,
        seen_before: str | NotGiven = NOT_GIVEN,
        sort_by: Literal[
            "name", "id", "client_version", "last_seen_user.email", "last_seen_at", "active_registrations", "created_at"
        ]
        | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPagination[DeviceListResponse]:
        """
        Lists WARP devices.

        Args:
          id: Filter by a one or more device IDs.

          active_registrations: Include or exclude devices with active registrations. The default is "only" -
              return only devices with active registrations.

          cursor: Opaque token indicating the starting position when requesting the next set of
              records. A cursor value can be obtained from the result_info.cursor field in the
              response.

          include: Comma-separated list of additional information that should be included in the
              device response. Supported values are: "last_seen_registration.policy".

          per_page: The maximum number of devices to return in a single response.

          search: Search by device details.

          seen_after: Filter by the last_seen timestamp - returns only devices last seen after this
              timestamp.

          seen_before: Filter by the last_seen timestamp - returns only devices last seen before this
              timestamp.

          sort_by: The device field to order results by.

          sort_order: Sort direction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/physical-devices",
            page=SyncCursorPagination[DeviceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "active_registrations": active_registrations,
                        "cursor": cursor,
                        "include": include,
                        "last_seen_user": last_seen_user,
                        "per_page": per_page,
                        "search": search,
                        "seen_after": seen_after,
                        "seen_before": seen_before,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    device_list_params.DeviceListParams,
                ),
            ),
            model=DeviceListResponse,
        )

    def delete(
        self,
        device_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a WARP device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._delete(
            f"/accounts/{account_id}/devices/physical-devices/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        device_id: str,
        *,
        account_id: str,
        include: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceGetResponse:
        """
        Fetches a single WARP device.

        Args:
          include: Comma-separated list of additional information that should be included in the
              device response. Supported values are: "last_seen_registration.policy".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/physical-devices/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, device_get_params.DeviceGetParams),
                post_parser=ResultWrapper[DeviceGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DeviceGetResponse], ResultWrapper[DeviceGetResponse]),
        )

    def revoke(
        self,
        device_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Revokes all WARP registrations associated with the specified device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._post(
            f"/accounts/{account_id}/devices/physical-devices/{device_id}/revoke",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
        id: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        active_registrations: Literal["include", "only", "exclude"] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        include: str | NotGiven = NOT_GIVEN,
        last_seen_user: device_list_params.LastSeenUser | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        seen_after: str | NotGiven = NOT_GIVEN,
        seen_before: str | NotGiven = NOT_GIVEN,
        sort_by: Literal[
            "name", "id", "client_version", "last_seen_user.email", "last_seen_at", "active_registrations", "created_at"
        ]
        | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DeviceListResponse, AsyncCursorPagination[DeviceListResponse]]:
        """
        Lists WARP devices.

        Args:
          id: Filter by a one or more device IDs.

          active_registrations: Include or exclude devices with active registrations. The default is "only" -
              return only devices with active registrations.

          cursor: Opaque token indicating the starting position when requesting the next set of
              records. A cursor value can be obtained from the result_info.cursor field in the
              response.

          include: Comma-separated list of additional information that should be included in the
              device response. Supported values are: "last_seen_registration.policy".

          per_page: The maximum number of devices to return in a single response.

          search: Search by device details.

          seen_after: Filter by the last_seen timestamp - returns only devices last seen after this
              timestamp.

          seen_before: Filter by the last_seen timestamp - returns only devices last seen before this
              timestamp.

          sort_by: The device field to order results by.

          sort_order: Sort direction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/physical-devices",
            page=AsyncCursorPagination[DeviceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "active_registrations": active_registrations,
                        "cursor": cursor,
                        "include": include,
                        "last_seen_user": last_seen_user,
                        "per_page": per_page,
                        "search": search,
                        "seen_after": seen_after,
                        "seen_before": seen_before,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    device_list_params.DeviceListParams,
                ),
            ),
            model=DeviceListResponse,
        )

    async def delete(
        self,
        device_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a WARP device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/devices/physical-devices/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        device_id: str,
        *,
        account_id: str,
        include: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceGetResponse:
        """
        Fetches a single WARP device.

        Args:
          include: Comma-separated list of additional information that should be included in the
              device response. Supported values are: "last_seen_registration.policy".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/physical-devices/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, device_get_params.DeviceGetParams),
                post_parser=ResultWrapper[DeviceGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DeviceGetResponse], ResultWrapper[DeviceGetResponse]),
        )

    async def revoke(
        self,
        device_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Revokes all WARP registrations associated with the specified device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._post(
            f"/accounts/{account_id}/devices/physical-devices/{device_id}/revoke",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class DevicesResourceWithRawResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.list = to_raw_response_wrapper(
            devices.list,
        )
        self.delete = to_raw_response_wrapper(
            devices.delete,
        )
        self.get = to_raw_response_wrapper(
            devices.get,
        )
        self.revoke = to_raw_response_wrapper(
            devices.revoke,
        )


class AsyncDevicesResourceWithRawResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.list = async_to_raw_response_wrapper(
            devices.list,
        )
        self.delete = async_to_raw_response_wrapper(
            devices.delete,
        )
        self.get = async_to_raw_response_wrapper(
            devices.get,
        )
        self.revoke = async_to_raw_response_wrapper(
            devices.revoke,
        )


class DevicesResourceWithStreamingResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.list = to_streamed_response_wrapper(
            devices.list,
        )
        self.delete = to_streamed_response_wrapper(
            devices.delete,
        )
        self.get = to_streamed_response_wrapper(
            devices.get,
        )
        self.revoke = to_streamed_response_wrapper(
            devices.revoke,
        )


class AsyncDevicesResourceWithStreamingResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.list = async_to_streamed_response_wrapper(
            devices.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            devices.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            devices.get,
        )
        self.revoke = async_to_streamed_response_wrapper(
            devices.revoke,
        )
