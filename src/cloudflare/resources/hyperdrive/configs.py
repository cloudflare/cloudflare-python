# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.hyperdrive import (
    Hyperdrive,
    ConfigurationParam,
    ConfigDeleteResponse,
    config_edit_params,
    config_create_params,
    config_update_params,
)

__all__ = ["Configs", "AsyncConfigs"]


class Configs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        origin: ConfigurationParam,
        caching: config_create_params.Caching | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Hyperdrive]:
        """
        Creates and returns a new Hyperdrive configuration.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/hyperdrive/configs",
            body=maybe_transform(
                {
                    "name": name,
                    "origin": origin,
                    "caching": caching,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Hyperdrive]], ResultWrapper[Hyperdrive]),
        )

    def update(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        name: str,
        origin: ConfigurationParam,
        caching: config_update_params.Caching | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Hyperdrive]:
        """
        Updates and returns the specified Hyperdrive configuration.

        Args:
          account_id: Identifier

          hyperdrive_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return self._put(
            f"/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "origin": origin,
                    "caching": caching,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Hyperdrive]], ResultWrapper[Hyperdrive]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Hyperdrive]:
        """
        Returns a list of Hyperdrives

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/hyperdrive/configs",
            page=SyncSinglePage[Hyperdrive],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Hyperdrive,
        )

    def delete(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigDeleteResponse:
        """
        Deletes the specified Hyperdrive.

        Args:
          account_id: Identifier

          hyperdrive_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return cast(
            ConfigDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def edit(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        caching: config_edit_params.Caching | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        origin: ConfigurationParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Hyperdrive]:
        """Patches and returns the specified Hyperdrive configuration.

        Updates to the
        origin and caching settings are applied with an all-or-nothing approach.

        Args:
          account_id: Identifier

          hyperdrive_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return self._patch(
            f"/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
            body=maybe_transform(
                {
                    "caching": caching,
                    "name": name,
                    "origin": origin,
                },
                config_edit_params.ConfigEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Hyperdrive]], ResultWrapper[Hyperdrive]),
        )

    def get(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Hyperdrive]:
        """
        Returns the specified Hyperdrive configuration.

        Args:
          account_id: Identifier

          hyperdrive_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return self._get(
            f"/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Hyperdrive]], ResultWrapper[Hyperdrive]),
        )


class AsyncConfigs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        origin: ConfigurationParam,
        caching: config_create_params.Caching | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Hyperdrive]:
        """
        Creates and returns a new Hyperdrive configuration.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/hyperdrive/configs",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "origin": origin,
                    "caching": caching,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Hyperdrive]], ResultWrapper[Hyperdrive]),
        )

    async def update(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        name: str,
        origin: ConfigurationParam,
        caching: config_update_params.Caching | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Hyperdrive]:
        """
        Updates and returns the specified Hyperdrive configuration.

        Args:
          account_id: Identifier

          hyperdrive_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return await self._put(
            f"/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "origin": origin,
                    "caching": caching,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Hyperdrive]], ResultWrapper[Hyperdrive]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Hyperdrive, AsyncSinglePage[Hyperdrive]]:
        """
        Returns a list of Hyperdrives

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/hyperdrive/configs",
            page=AsyncSinglePage[Hyperdrive],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Hyperdrive,
        )

    async def delete(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigDeleteResponse:
        """
        Deletes the specified Hyperdrive.

        Args:
          account_id: Identifier

          hyperdrive_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return cast(
            ConfigDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def edit(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        caching: config_edit_params.Caching | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        origin: ConfigurationParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Hyperdrive]:
        """Patches and returns the specified Hyperdrive configuration.

        Updates to the
        origin and caching settings are applied with an all-or-nothing approach.

        Args:
          account_id: Identifier

          hyperdrive_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
            body=await async_maybe_transform(
                {
                    "caching": caching,
                    "name": name,
                    "origin": origin,
                },
                config_edit_params.ConfigEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Hyperdrive]], ResultWrapper[Hyperdrive]),
        )

    async def get(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Hyperdrive]:
        """
        Returns the specified Hyperdrive configuration.

        Args:
          account_id: Identifier

          hyperdrive_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return await self._get(
            f"/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Hyperdrive]], ResultWrapper[Hyperdrive]),
        )


class ConfigsWithRawResponse:
    def __init__(self, configs: Configs) -> None:
        self._configs = configs

        self.create = to_raw_response_wrapper(
            configs.create,
        )
        self.update = to_raw_response_wrapper(
            configs.update,
        )
        self.list = to_raw_response_wrapper(
            configs.list,
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


class AsyncConfigsWithRawResponse:
    def __init__(self, configs: AsyncConfigs) -> None:
        self._configs = configs

        self.create = async_to_raw_response_wrapper(
            configs.create,
        )
        self.update = async_to_raw_response_wrapper(
            configs.update,
        )
        self.list = async_to_raw_response_wrapper(
            configs.list,
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


class ConfigsWithStreamingResponse:
    def __init__(self, configs: Configs) -> None:
        self._configs = configs

        self.create = to_streamed_response_wrapper(
            configs.create,
        )
        self.update = to_streamed_response_wrapper(
            configs.update,
        )
        self.list = to_streamed_response_wrapper(
            configs.list,
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


class AsyncConfigsWithStreamingResponse:
    def __init__(self, configs: AsyncConfigs) -> None:
        self._configs = configs

        self.create = async_to_streamed_response_wrapper(
            configs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            configs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            configs.list,
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
