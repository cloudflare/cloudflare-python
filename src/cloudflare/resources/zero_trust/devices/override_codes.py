# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.devices.override_code_get_response import OverrideCodeGetResponse

__all__ = ["OverrideCodesResource", "AsyncOverrideCodesResource"]


class OverrideCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OverrideCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OverrideCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OverrideCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OverrideCodesResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def list(
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
    ) -> SyncSinglePage[object]:
        """Fetches a one-time use admin override code for a device.

        This relies on the
        **Admin Override** setting being enabled in your device configuration. Not
        supported when
        [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/)
        is enabled for the account. **Deprecated:** please use GET
        /accounts/{account_id}/devices/registrations/{registration_id}/override_codes
        instead.

        Args:
          device_id: Registration ID. Equal to Device ID except for accounts which enabled
              [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/{device_id}/override_codes",
            page=SyncSinglePage[object],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=object,
        )

    def get(
        self,
        registration_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OverrideCodeGetResponse:
        """Fetches one-time use admin override codes for a registration.

        This relies on the
        **Admin Override** setting being enabled in your device configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not registration_id:
            raise ValueError(f"Expected a non-empty value for `registration_id` but received {registration_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/registrations/{registration_id}/override_codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OverrideCodeGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OverrideCodeGetResponse], ResultWrapper[OverrideCodeGetResponse]),
        )


class AsyncOverrideCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOverrideCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOverrideCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOverrideCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOverrideCodesResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def list(
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
    ) -> AsyncPaginator[object, AsyncSinglePage[object]]:
        """Fetches a one-time use admin override code for a device.

        This relies on the
        **Admin Override** setting being enabled in your device configuration. Not
        supported when
        [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/)
        is enabled for the account. **Deprecated:** please use GET
        /accounts/{account_id}/devices/registrations/{registration_id}/override_codes
        instead.

        Args:
          device_id: Registration ID. Equal to Device ID except for accounts which enabled
              [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/{device_id}/override_codes",
            page=AsyncSinglePage[object],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=object,
        )

    async def get(
        self,
        registration_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OverrideCodeGetResponse:
        """Fetches one-time use admin override codes for a registration.

        This relies on the
        **Admin Override** setting being enabled in your device configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not registration_id:
            raise ValueError(f"Expected a non-empty value for `registration_id` but received {registration_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/registrations/{registration_id}/override_codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OverrideCodeGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OverrideCodeGetResponse], ResultWrapper[OverrideCodeGetResponse]),
        )


class OverrideCodesResourceWithRawResponse:
    def __init__(self, override_codes: OverrideCodesResource) -> None:
        self._override_codes = override_codes

        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                override_codes.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = to_raw_response_wrapper(
            override_codes.get,
        )


class AsyncOverrideCodesResourceWithRawResponse:
    def __init__(self, override_codes: AsyncOverrideCodesResource) -> None:
        self._override_codes = override_codes

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                override_codes.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = async_to_raw_response_wrapper(
            override_codes.get,
        )


class OverrideCodesResourceWithStreamingResponse:
    def __init__(self, override_codes: OverrideCodesResource) -> None:
        self._override_codes = override_codes

        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                override_codes.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = to_streamed_response_wrapper(
            override_codes.get,
        )


class AsyncOverrideCodesResourceWithStreamingResponse:
    def __init__(self, override_codes: AsyncOverrideCodesResource) -> None:
        self._override_codes = override_codes

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                override_codes.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = async_to_streamed_response_wrapper(
            override_codes.get,
        )
