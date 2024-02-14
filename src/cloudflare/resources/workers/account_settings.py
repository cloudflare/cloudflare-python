# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.workers import (
    AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse,
    AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse,
)

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.workers import account_setting_worker_account_settings_create_worker_account_settings_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["AccountSettings", "AsyncAccountSettings"]


class AccountSettings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountSettingsWithRawResponse:
        return AccountSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountSettingsWithStreamingResponse:
        return AccountSettingsWithStreamingResponse(self)

    def worker_account_settings_create_worker_account_settings(
        self,
        account_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse:
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
                body,
                account_setting_worker_account_settings_create_worker_account_settings_params.AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse],
                ResultWrapper[AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse],
            ),
        )

    def worker_account_settings_fetch_worker_account_settings(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse],
                ResultWrapper[AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse],
            ),
        )


class AsyncAccountSettings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountSettingsWithRawResponse:
        return AsyncAccountSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountSettingsWithStreamingResponse:
        return AsyncAccountSettingsWithStreamingResponse(self)

    async def worker_account_settings_create_worker_account_settings(
        self,
        account_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse:
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
            body=maybe_transform(
                body,
                account_setting_worker_account_settings_create_worker_account_settings_params.AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse],
                ResultWrapper[AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse],
            ),
        )

    async def worker_account_settings_fetch_worker_account_settings(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse],
                ResultWrapper[AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse],
            ),
        )


class AccountSettingsWithRawResponse:
    def __init__(self, account_settings: AccountSettings) -> None:
        self._account_settings = account_settings

        self.worker_account_settings_create_worker_account_settings = to_raw_response_wrapper(
            account_settings.worker_account_settings_create_worker_account_settings,
        )
        self.worker_account_settings_fetch_worker_account_settings = to_raw_response_wrapper(
            account_settings.worker_account_settings_fetch_worker_account_settings,
        )


class AsyncAccountSettingsWithRawResponse:
    def __init__(self, account_settings: AsyncAccountSettings) -> None:
        self._account_settings = account_settings

        self.worker_account_settings_create_worker_account_settings = async_to_raw_response_wrapper(
            account_settings.worker_account_settings_create_worker_account_settings,
        )
        self.worker_account_settings_fetch_worker_account_settings = async_to_raw_response_wrapper(
            account_settings.worker_account_settings_fetch_worker_account_settings,
        )


class AccountSettingsWithStreamingResponse:
    def __init__(self, account_settings: AccountSettings) -> None:
        self._account_settings = account_settings

        self.worker_account_settings_create_worker_account_settings = to_streamed_response_wrapper(
            account_settings.worker_account_settings_create_worker_account_settings,
        )
        self.worker_account_settings_fetch_worker_account_settings = to_streamed_response_wrapper(
            account_settings.worker_account_settings_fetch_worker_account_settings,
        )


class AsyncAccountSettingsWithStreamingResponse:
    def __init__(self, account_settings: AsyncAccountSettings) -> None:
        self._account_settings = account_settings

        self.worker_account_settings_create_worker_account_settings = async_to_streamed_response_wrapper(
            account_settings.worker_account_settings_create_worker_account_settings,
        )
        self.worker_account_settings_fetch_worker_account_settings = async_to_streamed_response_wrapper(
            account_settings.worker_account_settings_fetch_worker_account_settings,
        )
