# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._base_client import make_request_options
from ...types.workers import account_setting_update_params
from ...types.workers.account_setting_get_response import AccountSettingGetResponse
from ...types.workers.account_setting_update_response import AccountSettingUpdateResponse

__all__ = ["AccountSettingsResource", "AsyncAccountSettingsResource"]


class AccountSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AccountSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AccountSettingsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        default_usage_model: str | NotGiven = NOT_GIVEN,
        green_compute: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccountSettingUpdateResponse]:
        """
        Creates Worker account settings for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/workers/account-settings",
            body=maybe_transform(
                {
                    "default_usage_model": default_usage_model,
                    "green_compute": green_compute,
                },
                account_setting_update_params.AccountSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountSettingUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountSettingUpdateResponse]], ResultWrapper[AccountSettingUpdateResponse]),
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
    ) -> Optional[AccountSettingGetResponse]:
        """
        Fetches Worker account settings for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/account-settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountSettingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountSettingGetResponse]], ResultWrapper[AccountSettingGetResponse]),
        )


class AsyncAccountSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAccountSettingsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        default_usage_model: str | NotGiven = NOT_GIVEN,
        green_compute: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccountSettingUpdateResponse]:
        """
        Creates Worker account settings for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/account-settings",
            body=await async_maybe_transform(
                {
                    "default_usage_model": default_usage_model,
                    "green_compute": green_compute,
                },
                account_setting_update_params.AccountSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountSettingUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountSettingUpdateResponse]], ResultWrapper[AccountSettingUpdateResponse]),
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
    ) -> Optional[AccountSettingGetResponse]:
        """
        Fetches Worker account settings for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/account-settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountSettingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountSettingGetResponse]], ResultWrapper[AccountSettingGetResponse]),
        )


class AccountSettingsResourceWithRawResponse:
    def __init__(self, account_settings: AccountSettingsResource) -> None:
        self._account_settings = account_settings

        self.update = to_raw_response_wrapper(
            account_settings.update,
        )
        self.get = to_raw_response_wrapper(
            account_settings.get,
        )


class AsyncAccountSettingsResourceWithRawResponse:
    def __init__(self, account_settings: AsyncAccountSettingsResource) -> None:
        self._account_settings = account_settings

        self.update = async_to_raw_response_wrapper(
            account_settings.update,
        )
        self.get = async_to_raw_response_wrapper(
            account_settings.get,
        )


class AccountSettingsResourceWithStreamingResponse:
    def __init__(self, account_settings: AccountSettingsResource) -> None:
        self._account_settings = account_settings

        self.update = to_streamed_response_wrapper(
            account_settings.update,
        )
        self.get = to_streamed_response_wrapper(
            account_settings.get,
        )


class AsyncAccountSettingsResourceWithStreamingResponse:
    def __init__(self, account_settings: AsyncAccountSettingsResource) -> None:
        self._account_settings = account_settings

        self.update = async_to_streamed_response_wrapper(
            account_settings.update,
        )
        self.get = async_to_streamed_response_wrapper(
            account_settings.get,
        )
