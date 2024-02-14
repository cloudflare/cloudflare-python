# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.hyperdrive import (
    ConfigCreateResponse,
    ConfigUpdateResponse,
    ConfigListResponse,
    ConfigDeleteResponse,
    ConfigGetResponse,
)

from typing import Type, Optional

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.hyperdrive import config_create_params
from ...types.hyperdrive import config_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

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
        account_id: str,
        *,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigCreateResponse]:
        """
        Creates and returns a new Hyperdrive configuration.

        Args:
          account_id: Identifier

          password: The password required to access your origin database. This value is write-only
              and never returned by the API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/hyperdrive/configs",
            body=maybe_transform({"password": password}, config_create_params.ConfigCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigCreateResponse]], ResultWrapper[ConfigCreateResponse]),
        )

    def update(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigUpdateResponse]:
        """
        Updates and returns the specified Hyperdrive configuration.

        Args:
          account_id: Identifier

          hyperdrive_id: Identifier

          password: The password required to access your origin database. This value is write-only
              and never returned by the API.

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
            body=maybe_transform({"password": password}, config_update_params.ConfigUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigUpdateResponse]], ResultWrapper[ConfigUpdateResponse]),
        )

    def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigListResponse:
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
        return self._get(
            f"/accounts/{account_id}/hyperdrive/configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigListResponse], ResultWrapper[ConfigListResponse]),
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
    ) -> Optional[ConfigDeleteResponse]:
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
            Optional[ConfigDeleteResponse],
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
    ) -> Optional[ConfigGetResponse]:
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
            cast_to=cast(Type[Optional[ConfigGetResponse]], ResultWrapper[ConfigGetResponse]),
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
        account_id: str,
        *,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigCreateResponse]:
        """
        Creates and returns a new Hyperdrive configuration.

        Args:
          account_id: Identifier

          password: The password required to access your origin database. This value is write-only
              and never returned by the API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/hyperdrive/configs",
            body=maybe_transform({"password": password}, config_create_params.ConfigCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigCreateResponse]], ResultWrapper[ConfigCreateResponse]),
        )

    async def update(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigUpdateResponse]:
        """
        Updates and returns the specified Hyperdrive configuration.

        Args:
          account_id: Identifier

          hyperdrive_id: Identifier

          password: The password required to access your origin database. This value is write-only
              and never returned by the API.

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
            body=maybe_transform({"password": password}, config_update_params.ConfigUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigUpdateResponse]], ResultWrapper[ConfigUpdateResponse]),
        )

    async def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigListResponse:
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
        return await self._get(
            f"/accounts/{account_id}/hyperdrive/configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigListResponse], ResultWrapper[ConfigListResponse]),
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
    ) -> Optional[ConfigDeleteResponse]:
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
            Optional[ConfigDeleteResponse],
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
    ) -> Optional[ConfigGetResponse]:
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
            cast_to=cast(Type[Optional[ConfigGetResponse]], ResultWrapper[ConfigGetResponse]),
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
        self.get = async_to_streamed_response_wrapper(
            configs.get,
        )
