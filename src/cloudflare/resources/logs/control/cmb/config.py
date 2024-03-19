# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

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
from ....._base_client import (
    make_request_options,
)
from .....types.logs.control.cmb import LogcontrolCmbConfig, ConfigDeleteResponse, config_create_params

__all__ = ["Config", "AsyncConfig"]


class Config(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigWithRawResponse:
        return ConfigWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigWithStreamingResponse:
        return ConfigWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        regions: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LogcontrolCmbConfig]:
        """
        Updates CMB config.

        Args:
          account_id: Identifier

          regions: Comma-separated list of regions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/logs/control/cmb/config",
            body=maybe_transform({"regions": regions}, config_create_params.ConfigCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogcontrolCmbConfig]], ResultWrapper[LogcontrolCmbConfig]),
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
    ) -> Optional[ConfigDeleteResponse]:
        """
        Deletes CMB config.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[ConfigDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/logs/control/cmb/config",
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
    ) -> Optional[LogcontrolCmbConfig]:
        """
        Gets CMB config.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/logs/control/cmb/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogcontrolCmbConfig]], ResultWrapper[LogcontrolCmbConfig]),
        )


class AsyncConfig(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigWithRawResponse:
        return AsyncConfigWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigWithStreamingResponse:
        return AsyncConfigWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        regions: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LogcontrolCmbConfig]:
        """
        Updates CMB config.

        Args:
          account_id: Identifier

          regions: Comma-separated list of regions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/logs/control/cmb/config",
            body=await async_maybe_transform({"regions": regions}, config_create_params.ConfigCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogcontrolCmbConfig]], ResultWrapper[LogcontrolCmbConfig]),
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
    ) -> Optional[ConfigDeleteResponse]:
        """
        Deletes CMB config.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[ConfigDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/logs/control/cmb/config",
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
    ) -> Optional[LogcontrolCmbConfig]:
        """
        Gets CMB config.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/logs/control/cmb/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogcontrolCmbConfig]], ResultWrapper[LogcontrolCmbConfig]),
        )


class ConfigWithRawResponse:
    def __init__(self, config: Config) -> None:
        self._config = config

        self.create = to_raw_response_wrapper(
            config.create,
        )
        self.delete = to_raw_response_wrapper(
            config.delete,
        )
        self.get = to_raw_response_wrapper(
            config.get,
        )


class AsyncConfigWithRawResponse:
    def __init__(self, config: AsyncConfig) -> None:
        self._config = config

        self.create = async_to_raw_response_wrapper(
            config.create,
        )
        self.delete = async_to_raw_response_wrapper(
            config.delete,
        )
        self.get = async_to_raw_response_wrapper(
            config.get,
        )


class ConfigWithStreamingResponse:
    def __init__(self, config: Config) -> None:
        self._config = config

        self.create = to_streamed_response_wrapper(
            config.create,
        )
        self.delete = to_streamed_response_wrapper(
            config.delete,
        )
        self.get = to_streamed_response_wrapper(
            config.get,
        )


class AsyncConfigWithStreamingResponse:
    def __init__(self, config: AsyncConfig) -> None:
        self._config = config

        self.create = async_to_streamed_response_wrapper(
            config.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            config.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            config.get,
        )
