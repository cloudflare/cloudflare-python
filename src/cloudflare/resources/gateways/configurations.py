# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.gateways import (
    ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse,
    ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse,
    ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse,
    configuration_zero_trust_accounts_patch_zero_trust_account_configuration_params,
    configuration_zero_trust_accounts_update_zero_trust_account_configuration_params,
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
from ...types.gateways import configuration_zero_trust_accounts_patch_zero_trust_account_configuration_params
from ...types.gateways import configuration_zero_trust_accounts_update_zero_trust_account_configuration_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Configurations", "AsyncConfigurations"]


class Configurations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationsWithRawResponse:
        return ConfigurationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsWithStreamingResponse:
        return ConfigurationsWithStreamingResponse(self)

    def zero_trust_accounts_get_zero_trust_account_configuration(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse:
        """
        Fetches the current Zero Trust account configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/gateway/configuration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse],
                ResultWrapper[ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse],
            ),
        )

    def zero_trust_accounts_patch_zero_trust_account_configuration(
        self,
        account_id: object,
        *,
        settings: configuration_zero_trust_accounts_patch_zero_trust_account_configuration_params.Settings
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse:
        """Patches the current Zero Trust account configuration.

        This endpoint can update a
        single subcollection of settings such as `antivirus`, `tls_decrypt`,
        `activity_log`, `block_page`, `browser_isolation`, `fips`, `body_scanning`, or
        `custom_certificate`, without updating the entire configuration object. Returns
        an error if any collection of settings is not properly configured.

        Args:
          settings: account settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/accounts/{account_id}/gateway/configuration",
            body=maybe_transform(
                {"settings": settings},
                configuration_zero_trust_accounts_patch_zero_trust_account_configuration_params.ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse],
                ResultWrapper[ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse],
            ),
        )

    def zero_trust_accounts_update_zero_trust_account_configuration(
        self,
        account_id: object,
        *,
        settings: configuration_zero_trust_accounts_update_zero_trust_account_configuration_params.Settings
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse:
        """
        Updates the current Zero Trust account configuration.

        Args:
          settings: account settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_id}/gateway/configuration",
            body=maybe_transform(
                {"settings": settings},
                configuration_zero_trust_accounts_update_zero_trust_account_configuration_params.ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse],
                ResultWrapper[ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse],
            ),
        )


class AsyncConfigurations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigurationsWithRawResponse:
        return AsyncConfigurationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationsWithStreamingResponse:
        return AsyncConfigurationsWithStreamingResponse(self)

    async def zero_trust_accounts_get_zero_trust_account_configuration(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse:
        """
        Fetches the current Zero Trust account configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/gateway/configuration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse],
                ResultWrapper[ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse],
            ),
        )

    async def zero_trust_accounts_patch_zero_trust_account_configuration(
        self,
        account_id: object,
        *,
        settings: configuration_zero_trust_accounts_patch_zero_trust_account_configuration_params.Settings
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse:
        """Patches the current Zero Trust account configuration.

        This endpoint can update a
        single subcollection of settings such as `antivirus`, `tls_decrypt`,
        `activity_log`, `block_page`, `browser_isolation`, `fips`, `body_scanning`, or
        `custom_certificate`, without updating the entire configuration object. Returns
        an error if any collection of settings is not properly configured.

        Args:
          settings: account settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/accounts/{account_id}/gateway/configuration",
            body=maybe_transform(
                {"settings": settings},
                configuration_zero_trust_accounts_patch_zero_trust_account_configuration_params.ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse],
                ResultWrapper[ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse],
            ),
        )

    async def zero_trust_accounts_update_zero_trust_account_configuration(
        self,
        account_id: object,
        *,
        settings: configuration_zero_trust_accounts_update_zero_trust_account_configuration_params.Settings
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse:
        """
        Updates the current Zero Trust account configuration.

        Args:
          settings: account settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_id}/gateway/configuration",
            body=maybe_transform(
                {"settings": settings},
                configuration_zero_trust_accounts_update_zero_trust_account_configuration_params.ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse],
                ResultWrapper[ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse],
            ),
        )


class ConfigurationsWithRawResponse:
    def __init__(self, configurations: Configurations) -> None:
        self._configurations = configurations

        self.zero_trust_accounts_get_zero_trust_account_configuration = to_raw_response_wrapper(
            configurations.zero_trust_accounts_get_zero_trust_account_configuration,
        )
        self.zero_trust_accounts_patch_zero_trust_account_configuration = to_raw_response_wrapper(
            configurations.zero_trust_accounts_patch_zero_trust_account_configuration,
        )
        self.zero_trust_accounts_update_zero_trust_account_configuration = to_raw_response_wrapper(
            configurations.zero_trust_accounts_update_zero_trust_account_configuration,
        )


class AsyncConfigurationsWithRawResponse:
    def __init__(self, configurations: AsyncConfigurations) -> None:
        self._configurations = configurations

        self.zero_trust_accounts_get_zero_trust_account_configuration = async_to_raw_response_wrapper(
            configurations.zero_trust_accounts_get_zero_trust_account_configuration,
        )
        self.zero_trust_accounts_patch_zero_trust_account_configuration = async_to_raw_response_wrapper(
            configurations.zero_trust_accounts_patch_zero_trust_account_configuration,
        )
        self.zero_trust_accounts_update_zero_trust_account_configuration = async_to_raw_response_wrapper(
            configurations.zero_trust_accounts_update_zero_trust_account_configuration,
        )


class ConfigurationsWithStreamingResponse:
    def __init__(self, configurations: Configurations) -> None:
        self._configurations = configurations

        self.zero_trust_accounts_get_zero_trust_account_configuration = to_streamed_response_wrapper(
            configurations.zero_trust_accounts_get_zero_trust_account_configuration,
        )
        self.zero_trust_accounts_patch_zero_trust_account_configuration = to_streamed_response_wrapper(
            configurations.zero_trust_accounts_patch_zero_trust_account_configuration,
        )
        self.zero_trust_accounts_update_zero_trust_account_configuration = to_streamed_response_wrapper(
            configurations.zero_trust_accounts_update_zero_trust_account_configuration,
        )


class AsyncConfigurationsWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurations) -> None:
        self._configurations = configurations

        self.zero_trust_accounts_get_zero_trust_account_configuration = async_to_streamed_response_wrapper(
            configurations.zero_trust_accounts_get_zero_trust_account_configuration,
        )
        self.zero_trust_accounts_patch_zero_trust_account_configuration = async_to_streamed_response_wrapper(
            configurations.zero_trust_accounts_patch_zero_trust_account_configuration,
        )
        self.zero_trust_accounts_update_zero_trust_account_configuration = async_to_streamed_response_wrapper(
            configurations.zero_trust_accounts_update_zero_trust_account_configuration,
        )
