# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
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
from ...types.api_gateways import (
    ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse,
    ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse,
    configuration_api_shield_settings_set_configuration_properties_params,
    configuration_api_shield_settings_get_information_about_specific_configuration_properties_params,
)

__all__ = ["Configurations", "AsyncConfigurations"]


class Configurations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationsWithRawResponse:
        return ConfigurationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsWithStreamingResponse:
        return ConfigurationsWithStreamingResponse(self)

    def api_shield_settings_get_information_about_specific_configuration_properties(
        self,
        zone_id: str,
        *,
        properties: List[Literal["auth_id_characteristics"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse:
        """
        Retrieve information about specific configuration properties

        Args:
          zone_id: Identifier

          properties: Requests information about certain properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/configuration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"properties": properties},
                    configuration_api_shield_settings_get_information_about_specific_configuration_properties_params.ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse],
                ResultWrapper[ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse],
            ),
        )

    def api_shield_settings_set_configuration_properties(
        self,
        zone_id: str,
        *,
        auth_id_characteristics: Iterable[
            configuration_api_shield_settings_set_configuration_properties_params.AuthIDCharacteristic
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse:
        """
        Set configuration properties

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse,
            self._put(
                f"/zones/{zone_id}/api_gateway/configuration",
                body=maybe_transform(
                    {"auth_id_characteristics": auth_id_characteristics},
                    configuration_api_shield_settings_set_configuration_properties_params.ConfigurationAPIShieldSettingsSetConfigurationPropertiesParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncConfigurations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigurationsWithRawResponse:
        return AsyncConfigurationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationsWithStreamingResponse:
        return AsyncConfigurationsWithStreamingResponse(self)

    async def api_shield_settings_get_information_about_specific_configuration_properties(
        self,
        zone_id: str,
        *,
        properties: List[Literal["auth_id_characteristics"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse:
        """
        Retrieve information about specific configuration properties

        Args:
          zone_id: Identifier

          properties: Requests information about certain properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/configuration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"properties": properties},
                    configuration_api_shield_settings_get_information_about_specific_configuration_properties_params.ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse],
                ResultWrapper[ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse],
            ),
        )

    async def api_shield_settings_set_configuration_properties(
        self,
        zone_id: str,
        *,
        auth_id_characteristics: Iterable[
            configuration_api_shield_settings_set_configuration_properties_params.AuthIDCharacteristic
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse:
        """
        Set configuration properties

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse,
            await self._put(
                f"/zones/{zone_id}/api_gateway/configuration",
                body=maybe_transform(
                    {"auth_id_characteristics": auth_id_characteristics},
                    configuration_api_shield_settings_set_configuration_properties_params.ConfigurationAPIShieldSettingsSetConfigurationPropertiesParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ConfigurationsWithRawResponse:
    def __init__(self, configurations: Configurations) -> None:
        self._configurations = configurations

        self.api_shield_settings_get_information_about_specific_configuration_properties = to_raw_response_wrapper(
            configurations.api_shield_settings_get_information_about_specific_configuration_properties,
        )
        self.api_shield_settings_set_configuration_properties = to_raw_response_wrapper(
            configurations.api_shield_settings_set_configuration_properties,
        )


class AsyncConfigurationsWithRawResponse:
    def __init__(self, configurations: AsyncConfigurations) -> None:
        self._configurations = configurations

        self.api_shield_settings_get_information_about_specific_configuration_properties = (
            async_to_raw_response_wrapper(
                configurations.api_shield_settings_get_information_about_specific_configuration_properties,
            )
        )
        self.api_shield_settings_set_configuration_properties = async_to_raw_response_wrapper(
            configurations.api_shield_settings_set_configuration_properties,
        )


class ConfigurationsWithStreamingResponse:
    def __init__(self, configurations: Configurations) -> None:
        self._configurations = configurations

        self.api_shield_settings_get_information_about_specific_configuration_properties = to_streamed_response_wrapper(
            configurations.api_shield_settings_get_information_about_specific_configuration_properties,
        )
        self.api_shield_settings_set_configuration_properties = to_streamed_response_wrapper(
            configurations.api_shield_settings_set_configuration_properties,
        )


class AsyncConfigurationsWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurations) -> None:
        self._configurations = configurations

        self.api_shield_settings_get_information_about_specific_configuration_properties = (
            async_to_streamed_response_wrapper(
                configurations.api_shield_settings_get_information_about_specific_configuration_properties,
            )
        )
        self.api_shield_settings_set_configuration_properties = async_to_streamed_response_wrapper(
            configurations.api_shield_settings_set_configuration_properties,
        )
