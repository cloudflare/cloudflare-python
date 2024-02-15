# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

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
from ...types.cfd_tunnels import (
    ConfigurationCloudflareTunnelConfigurationGetConfigurationResponse,
    ConfigurationCloudflareTunnelConfigurationPutConfigurationResponse,
    configuration_cloudflare_tunnel_configuration_put_configuration_params,
)

__all__ = ["Configurations", "AsyncConfigurations"]


class Configurations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationsWithRawResponse:
        return ConfigurationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsWithStreamingResponse:
        return ConfigurationsWithStreamingResponse(self)

    def cloudflare_tunnel_configuration_get_configuration(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationCloudflareTunnelConfigurationGetConfigurationResponse:
        """
        Gets the configuration for a remotely-managed tunnel

        Args:
          account_id: Identifier

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            ConfigurationCloudflareTunnelConfigurationGetConfigurationResponse,
            self._get(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigurationCloudflareTunnelConfigurationGetConfigurationResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def cloudflare_tunnel_configuration_put_configuration(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        config: configuration_cloudflare_tunnel_configuration_put_configuration_params.Config | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationCloudflareTunnelConfigurationPutConfigurationResponse:
        """
        Adds or updates the configuration for a remotely-managed tunnel.

        Args:
          account_id: Identifier

          tunnel_id: UUID of the tunnel.

          config: The tunnel configuration and ingress rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            ConfigurationCloudflareTunnelConfigurationPutConfigurationResponse,
            self._put(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations",
                body=maybe_transform(
                    {"config": config},
                    configuration_cloudflare_tunnel_configuration_put_configuration_params.ConfigurationCloudflareTunnelConfigurationPutConfigurationParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigurationCloudflareTunnelConfigurationPutConfigurationResponse]
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

    async def cloudflare_tunnel_configuration_get_configuration(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationCloudflareTunnelConfigurationGetConfigurationResponse:
        """
        Gets the configuration for a remotely-managed tunnel

        Args:
          account_id: Identifier

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            ConfigurationCloudflareTunnelConfigurationGetConfigurationResponse,
            await self._get(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigurationCloudflareTunnelConfigurationGetConfigurationResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def cloudflare_tunnel_configuration_put_configuration(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        config: configuration_cloudflare_tunnel_configuration_put_configuration_params.Config | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationCloudflareTunnelConfigurationPutConfigurationResponse:
        """
        Adds or updates the configuration for a remotely-managed tunnel.

        Args:
          account_id: Identifier

          tunnel_id: UUID of the tunnel.

          config: The tunnel configuration and ingress rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            ConfigurationCloudflareTunnelConfigurationPutConfigurationResponse,
            await self._put(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations",
                body=maybe_transform(
                    {"config": config},
                    configuration_cloudflare_tunnel_configuration_put_configuration_params.ConfigurationCloudflareTunnelConfigurationPutConfigurationParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigurationCloudflareTunnelConfigurationPutConfigurationResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ConfigurationsWithRawResponse:
    def __init__(self, configurations: Configurations) -> None:
        self._configurations = configurations

        self.cloudflare_tunnel_configuration_get_configuration = to_raw_response_wrapper(
            configurations.cloudflare_tunnel_configuration_get_configuration,
        )
        self.cloudflare_tunnel_configuration_put_configuration = to_raw_response_wrapper(
            configurations.cloudflare_tunnel_configuration_put_configuration,
        )


class AsyncConfigurationsWithRawResponse:
    def __init__(self, configurations: AsyncConfigurations) -> None:
        self._configurations = configurations

        self.cloudflare_tunnel_configuration_get_configuration = async_to_raw_response_wrapper(
            configurations.cloudflare_tunnel_configuration_get_configuration,
        )
        self.cloudflare_tunnel_configuration_put_configuration = async_to_raw_response_wrapper(
            configurations.cloudflare_tunnel_configuration_put_configuration,
        )


class ConfigurationsWithStreamingResponse:
    def __init__(self, configurations: Configurations) -> None:
        self._configurations = configurations

        self.cloudflare_tunnel_configuration_get_configuration = to_streamed_response_wrapper(
            configurations.cloudflare_tunnel_configuration_get_configuration,
        )
        self.cloudflare_tunnel_configuration_put_configuration = to_streamed_response_wrapper(
            configurations.cloudflare_tunnel_configuration_put_configuration,
        )


class AsyncConfigurationsWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurations) -> None:
        self._configurations = configurations

        self.cloudflare_tunnel_configuration_get_configuration = async_to_streamed_response_wrapper(
            configurations.cloudflare_tunnel_configuration_get_configuration,
        )
        self.cloudflare_tunnel_configuration_put_configuration = async_to_streamed_response_wrapper(
            configurations.cloudflare_tunnel_configuration_put_configuration,
        )
