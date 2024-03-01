# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.zero_trust.tunnels import (
    ConfigurationListResponse,
    ConfigurationUpdateResponse,
    configuration_update_params,
)

__all__ = ["Configurations", "AsyncConfigurations"]


class Configurations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationsWithRawResponse:
        return ConfigurationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsWithStreamingResponse:
        return ConfigurationsWithStreamingResponse(self)

    def update(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        config: configuration_update_params.Config | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationUpdateResponse:
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
            ConfigurationUpdateResponse,
            self._put(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations",
                body=maybe_transform({"config": config}, configuration_update_params.ConfigurationUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigurationUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
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
    ) -> ConfigurationListResponse:
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
            ConfigurationListResponse,
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
                    Any, ResultWrapper[ConfigurationListResponse]
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

    async def update(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        config: configuration_update_params.Config | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationUpdateResponse:
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
            ConfigurationUpdateResponse,
            await self._put(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations",
                body=maybe_transform({"config": config}, configuration_update_params.ConfigurationUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigurationUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
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
    ) -> ConfigurationListResponse:
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
            ConfigurationListResponse,
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
                    Any, ResultWrapper[ConfigurationListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ConfigurationsWithRawResponse:
    def __init__(self, configurations: Configurations) -> None:
        self._configurations = configurations

        self.update = to_raw_response_wrapper(
            configurations.update,
        )
        self.list = to_raw_response_wrapper(
            configurations.list,
        )


class AsyncConfigurationsWithRawResponse:
    def __init__(self, configurations: AsyncConfigurations) -> None:
        self._configurations = configurations

        self.update = async_to_raw_response_wrapper(
            configurations.update,
        )
        self.list = async_to_raw_response_wrapper(
            configurations.list,
        )


class ConfigurationsWithStreamingResponse:
    def __init__(self, configurations: Configurations) -> None:
        self._configurations = configurations

        self.update = to_streamed_response_wrapper(
            configurations.update,
        )
        self.list = to_streamed_response_wrapper(
            configurations.list,
        )


class AsyncConfigurationsWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurations) -> None:
        self._configurations = configurations

        self.update = async_to_streamed_response_wrapper(
            configurations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            configurations.list,
        )
