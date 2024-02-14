# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zaraz.history import ConfigGetResponse

from typing import Type, Iterable

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.zaraz.history import config_get_params
from ...._wrappers import ResultWrapper
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

    def get(
        self,
        zone_id: str,
        *,
        ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigGetResponse:
        """
        Gets a history of published Zaraz configurations by ID(s) for a zone.

        Args:
          zone_id: Identifier

          ids: Comma separated list of Zaraz configuration IDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/zaraz/history/configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, config_get_params.ConfigGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigGetResponse], ResultWrapper[ConfigGetResponse]),
        )


class AsyncConfigs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self)

    async def get(
        self,
        zone_id: str,
        *,
        ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigGetResponse:
        """
        Gets a history of published Zaraz configurations by ID(s) for a zone.

        Args:
          zone_id: Identifier

          ids: Comma separated list of Zaraz configuration IDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/zaraz/history/configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, config_get_params.ConfigGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigGetResponse], ResultWrapper[ConfigGetResponse]),
        )


class ConfigsWithRawResponse:
    def __init__(self, configs: Configs) -> None:
        self._configs = configs

        self.get = to_raw_response_wrapper(
            configs.get,
        )


class AsyncConfigsWithRawResponse:
    def __init__(self, configs: AsyncConfigs) -> None:
        self._configs = configs

        self.get = async_to_raw_response_wrapper(
            configs.get,
        )


class ConfigsWithStreamingResponse:
    def __init__(self, configs: Configs) -> None:
        self._configs = configs

        self.get = to_streamed_response_wrapper(
            configs.get,
        )


class AsyncConfigsWithStreamingResponse:
    def __init__(self, configs: AsyncConfigs) -> None:
        self._configs = configs

        self.get = async_to_streamed_response_wrapper(
            configs.get,
        )
