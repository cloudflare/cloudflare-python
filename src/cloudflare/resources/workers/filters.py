# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.workers import (
    FilterUpdateResponse,
    FilterDeleteResponse,
    FilterWorkerFiltersDeprecatedCreateFilterResponse,
    FilterWorkerFiltersDeprecatedListFiltersResponse,
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
from ...types.workers import filter_update_params
from ...types.workers import filter_worker_filters_deprecated_create_filter_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Filters", "AsyncFilters"]


class Filters(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FiltersWithRawResponse:
        return FiltersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiltersWithStreamingResponse:
        return FiltersWithStreamingResponse(self)

    def update(
        self,
        filter_id: str,
        *,
        zone_id: str,
        enabled: bool,
        pattern: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FilterUpdateResponse:
        """
        Update Filter

        Args:
          zone_id: Identifier

          filter_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not filter_id:
            raise ValueError(f"Expected a non-empty value for `filter_id` but received {filter_id!r}")
        return self._put(
            f"/zones/{zone_id}/workers/filters/{filter_id}",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "pattern": pattern,
                },
                filter_update_params.FilterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[FilterUpdateResponse], ResultWrapper[FilterUpdateResponse]),
        )

    def delete(
        self,
        filter_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterDeleteResponse]:
        """
        Delete Filter

        Args:
          zone_id: Identifier

          filter_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not filter_id:
            raise ValueError(f"Expected a non-empty value for `filter_id` but received {filter_id!r}")
        return self._delete(
            f"/zones/{zone_id}/workers/filters/{filter_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterDeleteResponse]], ResultWrapper[FilterDeleteResponse]),
        )

    def worker_filters_deprecated_create_filter(
        self,
        zone_id: str,
        *,
        enabled: bool,
        pattern: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterWorkerFiltersDeprecatedCreateFilterResponse]:
        """
        Create Filter

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/workers/filters",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "pattern": pattern,
                },
                filter_worker_filters_deprecated_create_filter_params.FilterWorkerFiltersDeprecatedCreateFilterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FilterWorkerFiltersDeprecatedCreateFilterResponse]],
                ResultWrapper[FilterWorkerFiltersDeprecatedCreateFilterResponse],
            ),
        )

    def worker_filters_deprecated_list_filters(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FilterWorkerFiltersDeprecatedListFiltersResponse:
        """
        List Filters

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/workers/filters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[FilterWorkerFiltersDeprecatedListFiltersResponse],
                ResultWrapper[FilterWorkerFiltersDeprecatedListFiltersResponse],
            ),
        )


class AsyncFilters(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFiltersWithRawResponse:
        return AsyncFiltersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiltersWithStreamingResponse:
        return AsyncFiltersWithStreamingResponse(self)

    async def update(
        self,
        filter_id: str,
        *,
        zone_id: str,
        enabled: bool,
        pattern: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FilterUpdateResponse:
        """
        Update Filter

        Args:
          zone_id: Identifier

          filter_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not filter_id:
            raise ValueError(f"Expected a non-empty value for `filter_id` but received {filter_id!r}")
        return await self._put(
            f"/zones/{zone_id}/workers/filters/{filter_id}",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "pattern": pattern,
                },
                filter_update_params.FilterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[FilterUpdateResponse], ResultWrapper[FilterUpdateResponse]),
        )

    async def delete(
        self,
        filter_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterDeleteResponse]:
        """
        Delete Filter

        Args:
          zone_id: Identifier

          filter_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not filter_id:
            raise ValueError(f"Expected a non-empty value for `filter_id` but received {filter_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/workers/filters/{filter_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterDeleteResponse]], ResultWrapper[FilterDeleteResponse]),
        )

    async def worker_filters_deprecated_create_filter(
        self,
        zone_id: str,
        *,
        enabled: bool,
        pattern: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterWorkerFiltersDeprecatedCreateFilterResponse]:
        """
        Create Filter

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/workers/filters",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "pattern": pattern,
                },
                filter_worker_filters_deprecated_create_filter_params.FilterWorkerFiltersDeprecatedCreateFilterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FilterWorkerFiltersDeprecatedCreateFilterResponse]],
                ResultWrapper[FilterWorkerFiltersDeprecatedCreateFilterResponse],
            ),
        )

    async def worker_filters_deprecated_list_filters(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FilterWorkerFiltersDeprecatedListFiltersResponse:
        """
        List Filters

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/workers/filters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[FilterWorkerFiltersDeprecatedListFiltersResponse],
                ResultWrapper[FilterWorkerFiltersDeprecatedListFiltersResponse],
            ),
        )


class FiltersWithRawResponse:
    def __init__(self, filters: Filters) -> None:
        self._filters = filters

        self.update = to_raw_response_wrapper(
            filters.update,
        )
        self.delete = to_raw_response_wrapper(
            filters.delete,
        )
        self.worker_filters_deprecated_create_filter = to_raw_response_wrapper(
            filters.worker_filters_deprecated_create_filter,
        )
        self.worker_filters_deprecated_list_filters = to_raw_response_wrapper(
            filters.worker_filters_deprecated_list_filters,
        )


class AsyncFiltersWithRawResponse:
    def __init__(self, filters: AsyncFilters) -> None:
        self._filters = filters

        self.update = async_to_raw_response_wrapper(
            filters.update,
        )
        self.delete = async_to_raw_response_wrapper(
            filters.delete,
        )
        self.worker_filters_deprecated_create_filter = async_to_raw_response_wrapper(
            filters.worker_filters_deprecated_create_filter,
        )
        self.worker_filters_deprecated_list_filters = async_to_raw_response_wrapper(
            filters.worker_filters_deprecated_list_filters,
        )


class FiltersWithStreamingResponse:
    def __init__(self, filters: Filters) -> None:
        self._filters = filters

        self.update = to_streamed_response_wrapper(
            filters.update,
        )
        self.delete = to_streamed_response_wrapper(
            filters.delete,
        )
        self.worker_filters_deprecated_create_filter = to_streamed_response_wrapper(
            filters.worker_filters_deprecated_create_filter,
        )
        self.worker_filters_deprecated_list_filters = to_streamed_response_wrapper(
            filters.worker_filters_deprecated_list_filters,
        )


class AsyncFiltersWithStreamingResponse:
    def __init__(self, filters: AsyncFilters) -> None:
        self._filters = filters

        self.update = async_to_streamed_response_wrapper(
            filters.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            filters.delete,
        )
        self.worker_filters_deprecated_create_filter = async_to_streamed_response_wrapper(
            filters.worker_filters_deprecated_create_filter,
        )
        self.worker_filters_deprecated_list_filters = async_to_streamed_response_wrapper(
            filters.worker_filters_deprecated_list_filters,
        )
