# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

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
from ...._base_client import (
    make_request_options,
)
from ....types.zero_trust.gateway import (
    ConfigurationGetResponse,
    ConfigurationEditResponse,
    ConfigurationUpdateResponse,
    configuration_edit_params,
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
        *,
        account_id: str,
        settings: configuration_update_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationUpdateResponse:
        """
        Updates the current Zero Trust account configuration.

        Args:
          settings: account settings.

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationUpdateResponse], ResultWrapper[ConfigurationUpdateResponse]),
        )

    def edit(
        self,
        *,
        account_id: str,
        settings: configuration_edit_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationEditResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationEditResponse], ResultWrapper[ConfigurationEditResponse]),
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
    ) -> ConfigurationGetResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationGetResponse], ResultWrapper[ConfigurationGetResponse]),
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
        *,
        account_id: str,
        settings: configuration_update_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationUpdateResponse:
        """
        Updates the current Zero Trust account configuration.

        Args:
          settings: account settings.

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationUpdateResponse], ResultWrapper[ConfigurationUpdateResponse]),
        )

    async def edit(
        self,
        *,
        account_id: str,
        settings: configuration_edit_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationEditResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationEditResponse], ResultWrapper[ConfigurationEditResponse]),
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
    ) -> ConfigurationGetResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationGetResponse], ResultWrapper[ConfigurationGetResponse]),
        )


class ConfigurationsWithRawResponse:
    def __init__(self, configurations: Configurations) -> None:
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


class AsyncConfigurationsWithRawResponse:
    def __init__(self, configurations: AsyncConfigurations) -> None:
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


class ConfigurationsWithStreamingResponse:
    def __init__(self, configurations: Configurations) -> None:
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


class AsyncConfigurationsWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurations) -> None:
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
