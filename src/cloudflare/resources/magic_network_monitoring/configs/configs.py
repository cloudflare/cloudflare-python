# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, cast

import httpx

from .full import (
    FullResource,
    AsyncFullResource,
    FullResourceWithRawResponse,
    AsyncFullResourceWithRawResponse,
    FullResourceWithStreamingResponse,
    AsyncFullResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.magic_network_monitoring import config_edit_params, config_create_params, config_update_params
from ....types.magic_network_monitoring.configuration import Configuration

__all__ = ["ConfigsResource", "AsyncConfigsResource"]


class ConfigsResource(SyncAPIResource):
    @cached_property
    def full(self) -> FullResource:
        return FullResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ConfigsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        default_sampling: float,
        name: str,
        router_ips: List[str] | NotGiven = NOT_GIVEN,
        warp_devices: Iterable[config_create_params.WARPDevice] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Create a new network monitoring configuration.

        Args:
          default_sampling: Fallback sampling rate of flow messages being sent in packets per second. This
              should match the packet sampling rate configured on the router.

          name: The account name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/mnm/config",
            body=maybe_transform(
                {
                    "default_sampling": default_sampling,
                    "name": name,
                    "router_ips": router_ips,
                    "warp_devices": warp_devices,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    def update(
        self,
        *,
        account_id: str,
        default_sampling: float,
        name: str,
        router_ips: List[str] | NotGiven = NOT_GIVEN,
        warp_devices: Iterable[config_update_params.WARPDevice] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Update an existing network monitoring configuration, requires the entire
        configuration to be updated at once.

        Args:
          default_sampling: Fallback sampling rate of flow messages being sent in packets per second. This
              should match the packet sampling rate configured on the router.

          name: The account name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/mnm/config",
            body=maybe_transform(
                {
                    "default_sampling": default_sampling,
                    "name": name,
                    "router_ips": router_ips,
                    "warp_devices": warp_devices,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Delete an existing network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            f"/accounts/{account_id}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    def edit(
        self,
        *,
        account_id: str,
        default_sampling: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        router_ips: List[str] | NotGiven = NOT_GIVEN,
        warp_devices: Iterable[config_edit_params.WARPDevice] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Update fields in an existing network monitoring configuration.

        Args:
          default_sampling: Fallback sampling rate of flow messages being sent in packets per second. This
              should match the packet sampling rate configured on the router.

          name: The account name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            f"/accounts/{account_id}/mnm/config",
            body=maybe_transform(
                {
                    "default_sampling": default_sampling,
                    "name": name,
                    "router_ips": router_ips,
                    "warp_devices": warp_devices,
                },
                config_edit_params.ConfigEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
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
    ) -> Configuration:
        """
        Lists default sampling, router IPs and warp devices for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )


class AsyncConfigsResource(AsyncAPIResource):
    @cached_property
    def full(self) -> AsyncFullResource:
        return AsyncFullResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncConfigsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        default_sampling: float,
        name: str,
        router_ips: List[str] | NotGiven = NOT_GIVEN,
        warp_devices: Iterable[config_create_params.WARPDevice] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Create a new network monitoring configuration.

        Args:
          default_sampling: Fallback sampling rate of flow messages being sent in packets per second. This
              should match the packet sampling rate configured on the router.

          name: The account name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/mnm/config",
            body=await async_maybe_transform(
                {
                    "default_sampling": default_sampling,
                    "name": name,
                    "router_ips": router_ips,
                    "warp_devices": warp_devices,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    async def update(
        self,
        *,
        account_id: str,
        default_sampling: float,
        name: str,
        router_ips: List[str] | NotGiven = NOT_GIVEN,
        warp_devices: Iterable[config_update_params.WARPDevice] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Update an existing network monitoring configuration, requires the entire
        configuration to be updated at once.

        Args:
          default_sampling: Fallback sampling rate of flow messages being sent in packets per second. This
              should match the packet sampling rate configured on the router.

          name: The account name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/mnm/config",
            body=await async_maybe_transform(
                {
                    "default_sampling": default_sampling,
                    "name": name,
                    "router_ips": router_ips,
                    "warp_devices": warp_devices,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    async def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Delete an existing network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    async def edit(
        self,
        *,
        account_id: str,
        default_sampling: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        router_ips: List[str] | NotGiven = NOT_GIVEN,
        warp_devices: Iterable[config_edit_params.WARPDevice] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Update fields in an existing network monitoring configuration.

        Args:
          default_sampling: Fallback sampling rate of flow messages being sent in packets per second. This
              should match the packet sampling rate configured on the router.

          name: The account name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/mnm/config",
            body=await async_maybe_transform(
                {
                    "default_sampling": default_sampling,
                    "name": name,
                    "router_ips": router_ips,
                    "warp_devices": warp_devices,
                },
                config_edit_params.ConfigEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
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
    ) -> Configuration:
        """
        Lists default sampling, router IPs and warp devices for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/mnm/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )


class ConfigsResourceWithRawResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.create = to_raw_response_wrapper(
            configs.create,
        )
        self.update = to_raw_response_wrapper(
            configs.update,
        )
        self.delete = to_raw_response_wrapper(
            configs.delete,
        )
        self.edit = to_raw_response_wrapper(
            configs.edit,
        )
        self.get = to_raw_response_wrapper(
            configs.get,
        )

    @cached_property
    def full(self) -> FullResourceWithRawResponse:
        return FullResourceWithRawResponse(self._configs.full)


class AsyncConfigsResourceWithRawResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.create = async_to_raw_response_wrapper(
            configs.create,
        )
        self.update = async_to_raw_response_wrapper(
            configs.update,
        )
        self.delete = async_to_raw_response_wrapper(
            configs.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            configs.edit,
        )
        self.get = async_to_raw_response_wrapper(
            configs.get,
        )

    @cached_property
    def full(self) -> AsyncFullResourceWithRawResponse:
        return AsyncFullResourceWithRawResponse(self._configs.full)


class ConfigsResourceWithStreamingResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.create = to_streamed_response_wrapper(
            configs.create,
        )
        self.update = to_streamed_response_wrapper(
            configs.update,
        )
        self.delete = to_streamed_response_wrapper(
            configs.delete,
        )
        self.edit = to_streamed_response_wrapper(
            configs.edit,
        )
        self.get = to_streamed_response_wrapper(
            configs.get,
        )

    @cached_property
    def full(self) -> FullResourceWithStreamingResponse:
        return FullResourceWithStreamingResponse(self._configs.full)


class AsyncConfigsResourceWithStreamingResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.create = async_to_streamed_response_wrapper(
            configs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            configs.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            configs.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            configs.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            configs.get,
        )

    @cached_property
    def full(self) -> AsyncFullResourceWithStreamingResponse:
        return AsyncFullResourceWithStreamingResponse(self._configs.full)
