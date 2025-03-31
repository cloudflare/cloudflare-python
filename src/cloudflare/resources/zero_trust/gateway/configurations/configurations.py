# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .custom_certificate import (
    CustomCertificateResource,
    AsyncCustomCertificateResource,
    CustomCertificateResourceWithRawResponse,
    AsyncCustomCertificateResourceWithRawResponse,
    CustomCertificateResourceWithStreamingResponse,
    AsyncCustomCertificateResourceWithStreamingResponse,
)
from .....types.zero_trust.gateway import (
    configuration_edit_params,
    configuration_update_params,
)
from .....types.zero_trust.gateway.configuration_get_response import ConfigurationGetResponse
from .....types.zero_trust.gateway.configuration_edit_response import ConfigurationEditResponse
from .....types.zero_trust.gateway.configuration_update_response import ConfigurationUpdateResponse
from .....types.zero_trust.gateway.gateway_configuration_settings_param import GatewayConfigurationSettingsParam

__all__ = ["ConfigurationsResource", "AsyncConfigurationsResource"]


class ConfigurationsResource(SyncAPIResource):
    @cached_property
    def custom_certificate(self) -> CustomCertificateResource:
        return CustomCertificateResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ConfigurationsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        settings: GatewayConfigurationSettingsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigurationUpdateResponse]:
        """
        Updates the current Zero Trust account configuration.

        Args:
          settings: Account settings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/gateway/configuration",
            body=maybe_transform({"settings": settings}, configuration_update_params.ConfigurationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConfigurationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigurationUpdateResponse]], ResultWrapper[ConfigurationUpdateResponse]),
        )

    def edit(
        self,
        *,
        account_id: str,
        settings: GatewayConfigurationSettingsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigurationEditResponse]:
        """Patches the current Zero Trust account configuration.

        This endpoint can update a
        single subcollection of settings such as `antivirus`, `tls_decrypt`,
        `activity_log`, `block_page`, `browser_isolation`, `fips`, `body_scanning`, or
        `certificate`, without updating the entire configuration object. Returns an
        error if any collection of settings is not properly configured.

        Args:
          settings: Account settings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            f"/accounts/{account_id}/gateway/configuration",
            body=maybe_transform({"settings": settings}, configuration_edit_params.ConfigurationEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConfigurationEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigurationEditResponse]], ResultWrapper[ConfigurationEditResponse]),
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
    ) -> Optional[ConfigurationGetResponse]:
        """
        Fetches the current Zero Trust account configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/configuration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConfigurationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigurationGetResponse]], ResultWrapper[ConfigurationGetResponse]),
        )


class AsyncConfigurationsResource(AsyncAPIResource):
    @cached_property
    def custom_certificate(self) -> AsyncCustomCertificateResource:
        return AsyncCustomCertificateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncConfigurationsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        settings: GatewayConfigurationSettingsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigurationUpdateResponse]:
        """
        Updates the current Zero Trust account configuration.

        Args:
          settings: Account settings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/gateway/configuration",
            body=await async_maybe_transform(
                {"settings": settings}, configuration_update_params.ConfigurationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConfigurationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigurationUpdateResponse]], ResultWrapper[ConfigurationUpdateResponse]),
        )

    async def edit(
        self,
        *,
        account_id: str,
        settings: GatewayConfigurationSettingsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigurationEditResponse]:
        """Patches the current Zero Trust account configuration.

        This endpoint can update a
        single subcollection of settings such as `antivirus`, `tls_decrypt`,
        `activity_log`, `block_page`, `browser_isolation`, `fips`, `body_scanning`, or
        `certificate`, without updating the entire configuration object. Returns an
        error if any collection of settings is not properly configured.

        Args:
          settings: Account settings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/gateway/configuration",
            body=await async_maybe_transform({"settings": settings}, configuration_edit_params.ConfigurationEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConfigurationEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigurationEditResponse]], ResultWrapper[ConfigurationEditResponse]),
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
    ) -> Optional[ConfigurationGetResponse]:
        """
        Fetches the current Zero Trust account configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/configuration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConfigurationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigurationGetResponse]], ResultWrapper[ConfigurationGetResponse]),
        )


class ConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = to_raw_response_wrapper(
            configurations.update,
        )
        self.edit = to_raw_response_wrapper(
            configurations.edit,
        )
        self.get = to_raw_response_wrapper(
            configurations.get,
        )

    @cached_property
    def custom_certificate(self) -> CustomCertificateResourceWithRawResponse:
        return CustomCertificateResourceWithRawResponse(self._configurations.custom_certificate)


class AsyncConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = async_to_raw_response_wrapper(
            configurations.update,
        )
        self.edit = async_to_raw_response_wrapper(
            configurations.edit,
        )
        self.get = async_to_raw_response_wrapper(
            configurations.get,
        )

    @cached_property
    def custom_certificate(self) -> AsyncCustomCertificateResourceWithRawResponse:
        return AsyncCustomCertificateResourceWithRawResponse(self._configurations.custom_certificate)


class ConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = to_streamed_response_wrapper(
            configurations.update,
        )
        self.edit = to_streamed_response_wrapper(
            configurations.edit,
        )
        self.get = to_streamed_response_wrapper(
            configurations.get,
        )

    @cached_property
    def custom_certificate(self) -> CustomCertificateResourceWithStreamingResponse:
        return CustomCertificateResourceWithStreamingResponse(self._configurations.custom_certificate)


class AsyncConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = async_to_streamed_response_wrapper(
            configurations.update,
        )
        self.edit = async_to_streamed_response_wrapper(
            configurations.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            configurations.get,
        )

    @cached_property
    def custom_certificate(self) -> AsyncCustomCertificateResourceWithStreamingResponse:
        return AsyncCustomCertificateResourceWithStreamingResponse(self._configurations.custom_certificate)
