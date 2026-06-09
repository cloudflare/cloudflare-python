# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
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
from .....types.zero_trust.tunnels.warp_connector import configuration_update_params
from .....types.zero_trust.tunnels.warp_connector.configuration_get_response import ConfigurationGetResponse
from .....types.zero_trust.tunnels.warp_connector.configuration_update_response import ConfigurationUpdateResponse

__all__ = ["ConfigurationsResource", "AsyncConfigurationsResource"]


class ConfigurationsResource(SyncAPIResource):
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
        tunnel_id: str,
        *,
        account_id: str,
        ha_mode: Literal["none", "disabled", "aws", "local"],
        config: Optional[configuration_update_params.Config] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ConfigurationUpdateResponse]:
        """
        Adds or updates the high-availability configuration for a WARP Connector tunnel.

        Args:
          account_id: Identifier.

          tunnel_id: UUID of the tunnel.

          ha_mode: High-availability mode for the WARP Connector tunnel. `none` means HA is enabled
              but no provider is configured yet (newly created tunnels default to this).
              `disabled` means HA is explicitly turned off. `aws` uses AWS ENI move for
              failover. `local` uses virtual IPs (VIPs) on the local interface.

          config: Provider-specific configuration. Required shape depends on ha_mode. For `aws`,
              must contain `fnr_id`. For `local`, must contain `vips`. For `none` and
              `disabled`, must be empty or omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}/configurations",
                account_id=account_id,
                tunnel_id=tunnel_id,
            ),
            body=maybe_transform(
                {
                    "ha_mode": ha_mode,
                    "config": config,
                },
                configuration_update_params.ConfigurationUpdateParams,
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

    def get(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ConfigurationGetResponse]:
        """
        Gets the high-availability configuration for a WARP Connector tunnel.

        Args:
          account_id: Identifier.

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
        return self._get(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}/configurations",
                account_id=account_id,
                tunnel_id=tunnel_id,
            ),
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
        tunnel_id: str,
        *,
        account_id: str,
        ha_mode: Literal["none", "disabled", "aws", "local"],
        config: Optional[configuration_update_params.Config] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ConfigurationUpdateResponse]:
        """
        Adds or updates the high-availability configuration for a WARP Connector tunnel.

        Args:
          account_id: Identifier.

          tunnel_id: UUID of the tunnel.

          ha_mode: High-availability mode for the WARP Connector tunnel. `none` means HA is enabled
              but no provider is configured yet (newly created tunnels default to this).
              `disabled` means HA is explicitly turned off. `aws` uses AWS ENI move for
              failover. `local` uses virtual IPs (VIPs) on the local interface.

          config: Provider-specific configuration. Required shape depends on ha_mode. For `aws`,
              must contain `fnr_id`. For `local`, must contain `vips`. For `none` and
              `disabled`, must be empty or omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}/configurations",
                account_id=account_id,
                tunnel_id=tunnel_id,
            ),
            body=await async_maybe_transform(
                {
                    "ha_mode": ha_mode,
                    "config": config,
                },
                configuration_update_params.ConfigurationUpdateParams,
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

    async def get(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ConfigurationGetResponse]:
        """
        Gets the high-availability configuration for a WARP Connector tunnel.

        Args:
          account_id: Identifier.

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
        return await self._get(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}/configurations",
                account_id=account_id,
                tunnel_id=tunnel_id,
            ),
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
        self.get = to_raw_response_wrapper(
            configurations.get,
        )


class AsyncConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = async_to_raw_response_wrapper(
            configurations.update,
        )
        self.get = async_to_raw_response_wrapper(
            configurations.get,
        )


class ConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = to_streamed_response_wrapper(
            configurations.update,
        )
        self.get = to_streamed_response_wrapper(
            configurations.get,
        )


class AsyncConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = async_to_streamed_response_wrapper(
            configurations.update,
        )
        self.get = async_to_streamed_response_wrapper(
            configurations.get,
        )
