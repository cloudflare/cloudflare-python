# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.logs.control.cmb.cmb_config import CmbConfig

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ....._base_client import make_request_options

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.logs.control.cmb import config_create_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ConfigResource", "AsyncConfigResource"]

class ConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self)

    def create(self,
    *,
    account_id: str,
    regions: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CmbConfig]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/logs/control/cmb/config",
            body=maybe_transform({
                "regions": regions
            }, config_create_params.ConfigCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CmbConfig]]._unwrapper),
            cast_to=cast(Type[Optional[CmbConfig]], ResultWrapper[CmbConfig]),
        )

    def delete(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/logs/control/cmb/config",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CmbConfig]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/logs/control/cmb/config",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CmbConfig]]._unwrapper),
            cast_to=cast(Type[Optional[CmbConfig]], ResultWrapper[CmbConfig]),
        )

class AsyncConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self)

    async def create(self,
    *,
    account_id: str,
    regions: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CmbConfig]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/logs/control/cmb/config",
            body=await async_maybe_transform({
                "regions": regions
            }, config_create_params.ConfigCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CmbConfig]]._unwrapper),
            cast_to=cast(Type[Optional[CmbConfig]], ResultWrapper[CmbConfig]),
        )

    async def delete(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/logs/control/cmb/config",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CmbConfig]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/logs/control/cmb/config",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CmbConfig]]._unwrapper),
            cast_to=cast(Type[Optional[CmbConfig]], ResultWrapper[CmbConfig]),
        )

class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
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

class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
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

class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
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

class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
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