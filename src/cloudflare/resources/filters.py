# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import (
    FilterUpdateResponse,
    FilterDeleteResponse,
    FilterFiltersCreateFiltersResponse,
    FilterFiltersListFiltersResponse,
    FilterFiltersUpdateFiltersResponse,
    FilterGetResponse,
)

from typing import Type, Optional

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import filter_update_params
from ..types import filter_filters_create_filters_params
from ..types import filter_filters_list_filters_params
from ..types import filter_filters_update_filters_params
from .._wrappers import ResultWrapper
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
        id: str,
        *,
        zone_identifier: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterUpdateResponse]:
        """
        Updates an existing filter.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/zones/{zone_identifier}/filters/{id}",
            body=maybe_transform(body, filter_update_params.FilterUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterUpdateResponse]], ResultWrapper[FilterUpdateResponse]),
        )

    def delete(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterDeleteResponse]:
        """
        Deletes an existing filter.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/zones/{zone_identifier}/filters/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterDeleteResponse]], ResultWrapper[FilterDeleteResponse]),
        )

    def filters_create_filters(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterFiltersCreateFiltersResponse]:
        """
        Creates one or more filters.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/filters",
            body=maybe_transform(body, filter_filters_create_filters_params.FilterFiltersCreateFiltersParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FilterFiltersCreateFiltersResponse]], ResultWrapper[FilterFiltersCreateFiltersResponse]
            ),
        )

    def filters_list_filters(
        self,
        zone_identifier: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        paused: bool | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterFiltersListFiltersResponse]:
        """Fetches filters in a zone.

        You can filter the results using several optional
        parameters.

        Args:
          zone_identifier: Identifier

          description: A case-insensitive string to find in the description.

          expression: A case-insensitive string to find in the expression.

          page: Page number of paginated results.

          paused: When true, indicates that the filter is currently paused.

          per_page: Number of filters per page.

          ref: The filter ref (a short reference tag) to search for. Must be an exact match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/filters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "description": description,
                        "expression": expression,
                        "page": page,
                        "paused": paused,
                        "per_page": per_page,
                        "ref": ref,
                    },
                    filter_filters_list_filters_params.FilterFiltersListFiltersParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FilterFiltersListFiltersResponse]], ResultWrapper[FilterFiltersListFiltersResponse]
            ),
        )

    def filters_update_filters(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterFiltersUpdateFiltersResponse]:
        """
        Updates one or more existing filters.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._put(
            f"/zones/{zone_identifier}/filters",
            body=maybe_transform(body, filter_filters_update_filters_params.FilterFiltersUpdateFiltersParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FilterFiltersUpdateFiltersResponse]], ResultWrapper[FilterFiltersUpdateFiltersResponse]
            ),
        )

    def get(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterGetResponse]:
        """
        Fetches the details of a filter.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/zones/{zone_identifier}/filters/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterGetResponse]], ResultWrapper[FilterGetResponse]),
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
        id: str,
        *,
        zone_identifier: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterUpdateResponse]:
        """
        Updates an existing filter.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/zones/{zone_identifier}/filters/{id}",
            body=maybe_transform(body, filter_update_params.FilterUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterUpdateResponse]], ResultWrapper[FilterUpdateResponse]),
        )

    async def delete(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterDeleteResponse]:
        """
        Deletes an existing filter.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/zones/{zone_identifier}/filters/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterDeleteResponse]], ResultWrapper[FilterDeleteResponse]),
        )

    async def filters_create_filters(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterFiltersCreateFiltersResponse]:
        """
        Creates one or more filters.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/filters",
            body=maybe_transform(body, filter_filters_create_filters_params.FilterFiltersCreateFiltersParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FilterFiltersCreateFiltersResponse]], ResultWrapper[FilterFiltersCreateFiltersResponse]
            ),
        )

    async def filters_list_filters(
        self,
        zone_identifier: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        paused: bool | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterFiltersListFiltersResponse]:
        """Fetches filters in a zone.

        You can filter the results using several optional
        parameters.

        Args:
          zone_identifier: Identifier

          description: A case-insensitive string to find in the description.

          expression: A case-insensitive string to find in the expression.

          page: Page number of paginated results.

          paused: When true, indicates that the filter is currently paused.

          per_page: Number of filters per page.

          ref: The filter ref (a short reference tag) to search for. Must be an exact match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/filters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "description": description,
                        "expression": expression,
                        "page": page,
                        "paused": paused,
                        "per_page": per_page,
                        "ref": ref,
                    },
                    filter_filters_list_filters_params.FilterFiltersListFiltersParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FilterFiltersListFiltersResponse]], ResultWrapper[FilterFiltersListFiltersResponse]
            ),
        )

    async def filters_update_filters(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterFiltersUpdateFiltersResponse]:
        """
        Updates one or more existing filters.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._put(
            f"/zones/{zone_identifier}/filters",
            body=maybe_transform(body, filter_filters_update_filters_params.FilterFiltersUpdateFiltersParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FilterFiltersUpdateFiltersResponse]], ResultWrapper[FilterFiltersUpdateFiltersResponse]
            ),
        )

    async def get(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FilterGetResponse]:
        """
        Fetches the details of a filter.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/zones/{zone_identifier}/filters/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterGetResponse]], ResultWrapper[FilterGetResponse]),
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
        self.filters_create_filters = to_raw_response_wrapper(
            filters.filters_create_filters,
        )
        self.filters_list_filters = to_raw_response_wrapper(
            filters.filters_list_filters,
        )
        self.filters_update_filters = to_raw_response_wrapper(
            filters.filters_update_filters,
        )
        self.get = to_raw_response_wrapper(
            filters.get,
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
        self.filters_create_filters = async_to_raw_response_wrapper(
            filters.filters_create_filters,
        )
        self.filters_list_filters = async_to_raw_response_wrapper(
            filters.filters_list_filters,
        )
        self.filters_update_filters = async_to_raw_response_wrapper(
            filters.filters_update_filters,
        )
        self.get = async_to_raw_response_wrapper(
            filters.get,
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
        self.filters_create_filters = to_streamed_response_wrapper(
            filters.filters_create_filters,
        )
        self.filters_list_filters = to_streamed_response_wrapper(
            filters.filters_list_filters,
        )
        self.filters_update_filters = to_streamed_response_wrapper(
            filters.filters_update_filters,
        )
        self.get = to_streamed_response_wrapper(
            filters.get,
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
        self.filters_create_filters = async_to_streamed_response_wrapper(
            filters.filters_create_filters,
        )
        self.filters_list_filters = async_to_streamed_response_wrapper(
            filters.filters_list_filters,
        )
        self.filters_update_filters = async_to_streamed_response_wrapper(
            filters.filters_update_filters,
        )
        self.get = async_to_streamed_response_wrapper(
            filters.get,
        )
