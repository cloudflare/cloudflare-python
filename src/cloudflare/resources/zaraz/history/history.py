# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .configs import Configs, AsyncConfigs

from ...._compat import cached_property

from ....types.zaraz import HistoryUpdateResponse, HistoryListResponse

from typing import Type

from typing_extensions import Literal

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
from ....types.zaraz import history_update_params
from ....types.zaraz import history_list_params
from .configs import (
    Configs,
    AsyncConfigs,
    ConfigsWithRawResponse,
    AsyncConfigsWithRawResponse,
    ConfigsWithStreamingResponse,
    AsyncConfigsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["History", "AsyncHistory"]


class History(SyncAPIResource):
    @cached_property
    def configs(self) -> Configs:
        return Configs(self._client)

    @cached_property
    def with_raw_response(self) -> HistoryWithRawResponse:
        return HistoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryWithStreamingResponse:
        return HistoryWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        body: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoryUpdateResponse:
        """
        Restores a historical published Zaraz configuration by ID for a zone.

        Args:
          zone_id: Identifier

          body: ID of the Zaraz configuration to restore.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/settings/zaraz/history",
            body=maybe_transform(body, history_update_params.HistoryUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HistoryUpdateResponse], ResultWrapper[HistoryUpdateResponse]),
        )

    def list(
        self,
        zone_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_field: Literal["id", "user_id", "description", "created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["DESC", "ASC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoryListResponse:
        """
        Lists a history of published Zaraz configuration records for a zone.

        Args:
          zone_id: Identifier

          limit: Maximum amount of results to list. Default value is 10.

          offset: Ordinal number to start listing the results with. Default value is 0.

          sort_field: The field to sort by. Default is updated_at.

          sort_order: Sorting order. Default is DESC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/zaraz/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "sort_field": sort_field,
                        "sort_order": sort_order,
                    },
                    history_list_params.HistoryListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HistoryListResponse], ResultWrapper[HistoryListResponse]),
        )


class AsyncHistory(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigs:
        return AsyncConfigs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHistoryWithRawResponse:
        return AsyncHistoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryWithStreamingResponse:
        return AsyncHistoryWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        body: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoryUpdateResponse:
        """
        Restores a historical published Zaraz configuration by ID for a zone.

        Args:
          zone_id: Identifier

          body: ID of the Zaraz configuration to restore.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/settings/zaraz/history",
            body=maybe_transform(body, history_update_params.HistoryUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HistoryUpdateResponse], ResultWrapper[HistoryUpdateResponse]),
        )

    async def list(
        self,
        zone_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_field: Literal["id", "user_id", "description", "created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["DESC", "ASC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoryListResponse:
        """
        Lists a history of published Zaraz configuration records for a zone.

        Args:
          zone_id: Identifier

          limit: Maximum amount of results to list. Default value is 10.

          offset: Ordinal number to start listing the results with. Default value is 0.

          sort_field: The field to sort by. Default is updated_at.

          sort_order: Sorting order. Default is DESC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/zaraz/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "sort_field": sort_field,
                        "sort_order": sort_order,
                    },
                    history_list_params.HistoryListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HistoryListResponse], ResultWrapper[HistoryListResponse]),
        )


class HistoryWithRawResponse:
    def __init__(self, history: History) -> None:
        self._history = history

        self.update = to_raw_response_wrapper(
            history.update,
        )
        self.list = to_raw_response_wrapper(
            history.list,
        )

    @cached_property
    def configs(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self._history.configs)


class AsyncHistoryWithRawResponse:
    def __init__(self, history: AsyncHistory) -> None:
        self._history = history

        self.update = async_to_raw_response_wrapper(
            history.update,
        )
        self.list = async_to_raw_response_wrapper(
            history.list,
        )

    @cached_property
    def configs(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self._history.configs)


class HistoryWithStreamingResponse:
    def __init__(self, history: History) -> None:
        self._history = history

        self.update = to_streamed_response_wrapper(
            history.update,
        )
        self.list = to_streamed_response_wrapper(
            history.list,
        )

    @cached_property
    def configs(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self._history.configs)


class AsyncHistoryWithStreamingResponse:
    def __init__(self, history: AsyncHistory) -> None:
        self._history = history

        self.update = async_to_streamed_response_wrapper(
            history.update,
        )
        self.list = async_to_streamed_response_wrapper(
            history.list,
        )

    @cached_property
    def configs(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self._history.configs)
