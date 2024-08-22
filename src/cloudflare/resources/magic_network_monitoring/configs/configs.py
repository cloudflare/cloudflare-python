# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .full import FullResource, AsyncFullResource

from ...._compat import cached_property

from ....types.magic_network_monitoring.configuration import Configuration

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Type

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.magic_network_monitoring import config_create_params
from ....types.magic_network_monitoring import config_update_params
from ....types.magic_network_monitoring import config_edit_params
from .full import FullResource, AsyncFullResource, FullResourceWithRawResponse, AsyncFullResourceWithRawResponse, FullResourceWithStreamingResponse, AsyncFullResourceWithStreamingResponse
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

__all__ = ["ConfigsResource", "AsyncConfigsResource"]

class ConfigsResource(SyncAPIResource):
    @cached_property
    def full(self) -> FullResource:
        return FullResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigsResourceWithRawResponse:
        return ConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigsResourceWithStreamingResponse:
        return ConfigsResourceWithStreamingResponse(self)

    def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Create a new network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/mnm/config",
            body=maybe_transform(body, config_create_params.ConfigCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Configuration]._unwrapper),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    def update(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Update an existing network monitoring configuration, requires the entire
        configuration to be updated at once.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/mnm/config",
            body=maybe_transform(body, config_update_params.ConfigUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Configuration]._unwrapper),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    def delete(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Delete an existing network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/mnm/config",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Configuration]._unwrapper),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    def edit(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Update fields in an existing network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._patch(
            f"/accounts/{account_id}/mnm/config",
            body=maybe_transform(body, config_edit_params.ConfigEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Configuration]._unwrapper),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Lists default sampling and router IPs for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/mnm/config",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Configuration]._unwrapper),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

class AsyncConfigsResource(AsyncAPIResource):
    @cached_property
    def full(self) -> AsyncFullResource:
        return AsyncFullResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigsResourceWithRawResponse:
        return AsyncConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsResourceWithStreamingResponse:
        return AsyncConfigsResourceWithStreamingResponse(self)

    async def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Create a new network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/mnm/config",
            body=await async_maybe_transform(body, config_create_params.ConfigCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Configuration]._unwrapper),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    async def update(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Update an existing network monitoring configuration, requires the entire
        configuration to be updated at once.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/mnm/config",
            body=await async_maybe_transform(body, config_update_params.ConfigUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Configuration]._unwrapper),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    async def delete(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Delete an existing network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/mnm/config",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Configuration]._unwrapper),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    async def edit(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Update fields in an existing network monitoring configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._patch(
            f"/accounts/{account_id}/mnm/config",
            body=await async_maybe_transform(body, config_edit_params.ConfigEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Configuration]._unwrapper),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

    async def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Lists default sampling and router IPs for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/mnm/config",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Configuration]._unwrapper),
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