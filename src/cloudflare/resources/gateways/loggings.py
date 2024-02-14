# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.gateways import (
    LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse,
    LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse,
    logging_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account_params,
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
from ...types.gateways import logging_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Loggings", "AsyncLoggings"]


class Loggings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoggingsWithRawResponse:
        return LoggingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoggingsWithStreamingResponse:
        return LoggingsWithStreamingResponse(self)

    def zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse:
        """
        Fetches the current logging settings for Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/gateway/logging",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse],
                ResultWrapper[LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse],
            ),
        )

    def zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
        self,
        account_id: object,
        *,
        redact_pii: bool | NotGiven = NOT_GIVEN,
        settings_by_rule_type: logging_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account_params.SettingsByRuleType
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse:
        """
        Updates logging settings for the current Zero Trust account.

        Args:
          redact_pii: Redact personally identifiable information from activity logging (PII fields
              are: source IP, user email, user ID, device ID, URL, referrer, user agent).

          settings_by_rule_type: Logging settings by rule type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_id}/gateway/logging",
            body=maybe_transform(
                {
                    "redact_pii": redact_pii,
                    "settings_by_rule_type": settings_by_rule_type,
                },
                logging_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account_params.LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse],
                ResultWrapper[LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse],
            ),
        )


class AsyncLoggings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoggingsWithRawResponse:
        return AsyncLoggingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoggingsWithStreamingResponse:
        return AsyncLoggingsWithStreamingResponse(self)

    async def zero_trust_accounts_get_logging_settings_for_the_zero_trust_account(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse:
        """
        Fetches the current logging settings for Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/gateway/logging",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse],
                ResultWrapper[LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse],
            ),
        )

    async def zero_trust_accounts_update_logging_settings_for_the_zero_trust_account(
        self,
        account_id: object,
        *,
        redact_pii: bool | NotGiven = NOT_GIVEN,
        settings_by_rule_type: logging_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account_params.SettingsByRuleType
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse:
        """
        Updates logging settings for the current Zero Trust account.

        Args:
          redact_pii: Redact personally identifiable information from activity logging (PII fields
              are: source IP, user email, user ID, device ID, URL, referrer, user agent).

          settings_by_rule_type: Logging settings by rule type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_id}/gateway/logging",
            body=maybe_transform(
                {
                    "redact_pii": redact_pii,
                    "settings_by_rule_type": settings_by_rule_type,
                },
                logging_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account_params.LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse],
                ResultWrapper[LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse],
            ),
        )


class LoggingsWithRawResponse:
    def __init__(self, loggings: Loggings) -> None:
        self._loggings = loggings

        self.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account = to_raw_response_wrapper(
            loggings.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account,
        )
        self.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account = to_raw_response_wrapper(
            loggings.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account,
        )


class AsyncLoggingsWithRawResponse:
    def __init__(self, loggings: AsyncLoggings) -> None:
        self._loggings = loggings

        self.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account = async_to_raw_response_wrapper(
            loggings.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account,
        )
        self.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account = async_to_raw_response_wrapper(
            loggings.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account,
        )


class LoggingsWithStreamingResponse:
    def __init__(self, loggings: Loggings) -> None:
        self._loggings = loggings

        self.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account = to_streamed_response_wrapper(
            loggings.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account,
        )
        self.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account = to_streamed_response_wrapper(
            loggings.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account,
        )


class AsyncLoggingsWithStreamingResponse:
    def __init__(self, loggings: AsyncLoggings) -> None:
        self._loggings = loggings

        self.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account = async_to_streamed_response_wrapper(
            loggings.zero_trust_accounts_get_logging_settings_for_the_zero_trust_account,
        )
        self.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account = (
            async_to_streamed_response_wrapper(
                loggings.zero_trust_accounts_update_logging_settings_for_the_zero_trust_account,
            )
        )
