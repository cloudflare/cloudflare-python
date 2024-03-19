# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._base_client import (
    make_request_options,
)
from ...types.workers import (
    WorkersFilters,
    FilterListResponse,
    FilterCreateResponse,
    FilterDeleteResponse,
    filter_create_params,
    filter_update_params,
)

__all__ = ["Filters", "AsyncFilters"]


class Filters(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FiltersWithRawResponse:
        return FiltersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiltersWithStreamingResponse:
        return FiltersWithStreamingResponse(self)

    def create(
        self,
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
    ) -> Optional[FilterCreateResponse]:
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
                filter_create_params.FilterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterCreateResponse]], ResultWrapper[FilterCreateResponse]),
        )

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
    ) -> WorkersFilters:
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
            cast_to=cast(Type[WorkersFilters], ResultWrapper[WorkersFilters]),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FilterListResponse:
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
            cast_to=cast(Type[FilterListResponse], ResultWrapper[FilterListResponse]),
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


class AsyncFilters(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFiltersWithRawResponse:
        return AsyncFiltersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiltersWithStreamingResponse:
        return AsyncFiltersWithStreamingResponse(self)

    async def create(
        self,
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
    ) -> Optional[FilterCreateResponse]:
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
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "pattern": pattern,
                },
                filter_create_params.FilterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterCreateResponse]], ResultWrapper[FilterCreateResponse]),
        )

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
    ) -> WorkersFilters:
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
            body=await async_maybe_transform(
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
            cast_to=cast(Type[WorkersFilters], ResultWrapper[WorkersFilters]),
        )

    async def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FilterListResponse:
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
            cast_to=cast(Type[FilterListResponse], ResultWrapper[FilterListResponse]),
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


class FiltersWithRawResponse:
    def __init__(self, filters: Filters) -> None:
        self._filters = filters

        self.create = to_raw_response_wrapper(
            filters.create,
        )
        self.update = to_raw_response_wrapper(
            filters.update,
        )
        self.list = to_raw_response_wrapper(
            filters.list,
        )
        self.delete = to_raw_response_wrapper(
            filters.delete,
        )


class AsyncFiltersWithRawResponse:
    def __init__(self, filters: AsyncFilters) -> None:
        self._filters = filters

        self.create = async_to_raw_response_wrapper(
            filters.create,
        )
        self.update = async_to_raw_response_wrapper(
            filters.update,
        )
        self.list = async_to_raw_response_wrapper(
            filters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            filters.delete,
        )


class FiltersWithStreamingResponse:
    def __init__(self, filters: Filters) -> None:
        self._filters = filters

        self.create = to_streamed_response_wrapper(
            filters.create,
        )
        self.update = to_streamed_response_wrapper(
            filters.update,
        )
        self.list = to_streamed_response_wrapper(
            filters.list,
        )
        self.delete = to_streamed_response_wrapper(
            filters.delete,
        )


class AsyncFiltersWithStreamingResponse:
    def __init__(self, filters: AsyncFilters) -> None:
        self._filters = filters

        self.create = async_to_streamed_response_wrapper(
            filters.create,
        )
        self.update = async_to_streamed_response_wrapper(
            filters.update,
        )
        self.list = async_to_streamed_response_wrapper(
            filters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            filters.delete,
        )
