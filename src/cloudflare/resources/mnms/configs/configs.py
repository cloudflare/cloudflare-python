# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from .fulls import (
    Fulls,
    AsyncFulls,
    FullsWithRawResponse,
    AsyncFullsWithRawResponse,
    FullsWithStreamingResponse,
    AsyncFullsWithStreamingResponse,
)
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
from ....types.mnms import (
    ConfigDeleteResponse,
    ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse,
    ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse,
    ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse,
    ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse,
)
from ...._base_client import (
    make_request_options,
)

__all__ = ["Configs", "AsyncConfigs"]


class Configs(SyncAPIResource):
    @cached_property
    def fulls(self) -> Fulls:
        return Fulls(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self)

    def delete(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigDeleteResponse:
        """
        Delete an existing network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/accounts/{account_identifier}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigDeleteResponse], ResultWrapper[ConfigDeleteResponse]),
        )

    def magic_network_monitoring_configuration_create_account_configuration(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse:
        """
        Create a new network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_identifier}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse],
                ResultWrapper[ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse],
            ),
        )

    def magic_network_monitoring_configuration_list_account_configuration(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse:
        """
        Lists default sampling and router IPs for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_identifier}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse],
                ResultWrapper[ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse],
            ),
        )

    def magic_network_monitoring_configuration_update_account_configuration_fields(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse:
        """
        Update fields in an existing network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/accounts/{account_identifier}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse],
                ResultWrapper[ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse],
            ),
        )

    def magic_network_monitoring_configuration_update_an_entire_account_configuration(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse:
        """
        Update an existing network monitoring configuration, requires the entire
        configuration to be updated at once.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_identifier}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse],
                ResultWrapper[ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse],
            ),
        )


class AsyncConfigs(AsyncAPIResource):
    @cached_property
    def fulls(self) -> AsyncFulls:
        return AsyncFulls(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self)

    async def delete(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigDeleteResponse:
        """
        Delete an existing network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/accounts/{account_identifier}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigDeleteResponse], ResultWrapper[ConfigDeleteResponse]),
        )

    async def magic_network_monitoring_configuration_create_account_configuration(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse:
        """
        Create a new network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_identifier}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse],
                ResultWrapper[ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse],
            ),
        )

    async def magic_network_monitoring_configuration_list_account_configuration(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse:
        """
        Lists default sampling and router IPs for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_identifier}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse],
                ResultWrapper[ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse],
            ),
        )

    async def magic_network_monitoring_configuration_update_account_configuration_fields(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse:
        """
        Update fields in an existing network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/accounts/{account_identifier}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse],
                ResultWrapper[ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse],
            ),
        )

    async def magic_network_monitoring_configuration_update_an_entire_account_configuration(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse:
        """
        Update an existing network monitoring configuration, requires the entire
        configuration to be updated at once.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_identifier}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse],
                ResultWrapper[ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse],
            ),
        )


class ConfigsWithRawResponse:
    def __init__(self, configs: Configs) -> None:
        self._configs = configs

        self.delete = to_raw_response_wrapper(
            configs.delete,
        )
        self.magic_network_monitoring_configuration_create_account_configuration = to_raw_response_wrapper(
            configs.magic_network_monitoring_configuration_create_account_configuration,
        )
        self.magic_network_monitoring_configuration_list_account_configuration = to_raw_response_wrapper(
            configs.magic_network_monitoring_configuration_list_account_configuration,
        )
        self.magic_network_monitoring_configuration_update_account_configuration_fields = to_raw_response_wrapper(
            configs.magic_network_monitoring_configuration_update_account_configuration_fields,
        )
        self.magic_network_monitoring_configuration_update_an_entire_account_configuration = to_raw_response_wrapper(
            configs.magic_network_monitoring_configuration_update_an_entire_account_configuration,
        )

    @cached_property
    def fulls(self) -> FullsWithRawResponse:
        return FullsWithRawResponse(self._configs.fulls)


class AsyncConfigsWithRawResponse:
    def __init__(self, configs: AsyncConfigs) -> None:
        self._configs = configs

        self.delete = async_to_raw_response_wrapper(
            configs.delete,
        )
        self.magic_network_monitoring_configuration_create_account_configuration = async_to_raw_response_wrapper(
            configs.magic_network_monitoring_configuration_create_account_configuration,
        )
        self.magic_network_monitoring_configuration_list_account_configuration = async_to_raw_response_wrapper(
            configs.magic_network_monitoring_configuration_list_account_configuration,
        )
        self.magic_network_monitoring_configuration_update_account_configuration_fields = async_to_raw_response_wrapper(
            configs.magic_network_monitoring_configuration_update_account_configuration_fields,
        )
        self.magic_network_monitoring_configuration_update_an_entire_account_configuration = (
            async_to_raw_response_wrapper(
                configs.magic_network_monitoring_configuration_update_an_entire_account_configuration,
            )
        )

    @cached_property
    def fulls(self) -> AsyncFullsWithRawResponse:
        return AsyncFullsWithRawResponse(self._configs.fulls)


class ConfigsWithStreamingResponse:
    def __init__(self, configs: Configs) -> None:
        self._configs = configs

        self.delete = to_streamed_response_wrapper(
            configs.delete,
        )
        self.magic_network_monitoring_configuration_create_account_configuration = to_streamed_response_wrapper(
            configs.magic_network_monitoring_configuration_create_account_configuration,
        )
        self.magic_network_monitoring_configuration_list_account_configuration = to_streamed_response_wrapper(
            configs.magic_network_monitoring_configuration_list_account_configuration,
        )
        self.magic_network_monitoring_configuration_update_account_configuration_fields = to_streamed_response_wrapper(
            configs.magic_network_monitoring_configuration_update_account_configuration_fields,
        )
        self.magic_network_monitoring_configuration_update_an_entire_account_configuration = (
            to_streamed_response_wrapper(
                configs.magic_network_monitoring_configuration_update_an_entire_account_configuration,
            )
        )

    @cached_property
    def fulls(self) -> FullsWithStreamingResponse:
        return FullsWithStreamingResponse(self._configs.fulls)


class AsyncConfigsWithStreamingResponse:
    def __init__(self, configs: AsyncConfigs) -> None:
        self._configs = configs

        self.delete = async_to_streamed_response_wrapper(
            configs.delete,
        )
        self.magic_network_monitoring_configuration_create_account_configuration = async_to_streamed_response_wrapper(
            configs.magic_network_monitoring_configuration_create_account_configuration,
        )
        self.magic_network_monitoring_configuration_list_account_configuration = async_to_streamed_response_wrapper(
            configs.magic_network_monitoring_configuration_list_account_configuration,
        )
        self.magic_network_monitoring_configuration_update_account_configuration_fields = (
            async_to_streamed_response_wrapper(
                configs.magic_network_monitoring_configuration_update_account_configuration_fields,
            )
        )
        self.magic_network_monitoring_configuration_update_an_entire_account_configuration = (
            async_to_streamed_response_wrapper(
                configs.magic_network_monitoring_configuration_update_an_entire_account_configuration,
            )
        )

    @cached_property
    def fulls(self) -> AsyncFullsWithStreamingResponse:
        return AsyncFullsWithStreamingResponse(self._configs.fulls)
