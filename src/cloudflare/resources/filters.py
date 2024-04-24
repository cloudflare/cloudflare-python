# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from ..pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.filters import filter_list_params, filter_create_params, filter_update_params
from ..types.filters.firewall_filter import FirewallFilter
from ..types.filters.filter_create_response import FilterCreateResponse

__all__ = ["FiltersResource", "AsyncFiltersResource"]


class FiltersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FiltersResourceWithRawResponse:
        return FiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiltersResourceWithStreamingResponse:
        return FiltersResourceWithStreamingResponse(self)

    def create(
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
    ) -> Optional[FilterCreateResponse]:
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
            body=maybe_transform(body, filter_create_params.FilterCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FilterCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterCreateResponse]], ResultWrapper[FilterCreateResponse]),
        )

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
    ) -> FirewallFilter:
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
                post_parser=ResultWrapper[FirewallFilter]._unwrapper,
            ),
            cast_to=cast(Type[FirewallFilter], ResultWrapper[FirewallFilter]),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        id: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncV4PagePaginationArray[FirewallFilter]:
        """Fetches filters in a zone.

        You can filter the results using several optional
        parameters.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the filter.

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
        return self._get_api_list(
            f"/zones/{zone_identifier}/filters",
            page=SyncV4PagePaginationArray[FirewallFilter],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "description": description,
                        "expression": expression,
                        "page": page,
                        "paused": paused,
                        "per_page": per_page,
                        "ref": ref,
                    },
                    filter_list_params.FilterListParams,
                ),
            ),
            model=FirewallFilter,
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
    ) -> FirewallFilter:
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
                post_parser=ResultWrapper[FirewallFilter]._unwrapper,
            ),
            cast_to=cast(Type[FirewallFilter], ResultWrapper[FirewallFilter]),
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
    ) -> FirewallFilter:
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
                post_parser=ResultWrapper[FirewallFilter]._unwrapper,
            ),
            cast_to=cast(Type[FirewallFilter], ResultWrapper[FirewallFilter]),
        )


class AsyncFiltersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFiltersResourceWithRawResponse:
        return AsyncFiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiltersResourceWithStreamingResponse:
        return AsyncFiltersResourceWithStreamingResponse(self)

    async def create(
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
    ) -> Optional[FilterCreateResponse]:
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
            body=await async_maybe_transform(body, filter_create_params.FilterCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FilterCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterCreateResponse]], ResultWrapper[FilterCreateResponse]),
        )

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
    ) -> FirewallFilter:
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
            body=await async_maybe_transform(body, filter_update_params.FilterUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FirewallFilter]._unwrapper,
            ),
            cast_to=cast(Type[FirewallFilter], ResultWrapper[FirewallFilter]),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        id: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[FirewallFilter, AsyncV4PagePaginationArray[FirewallFilter]]:
        """Fetches filters in a zone.

        You can filter the results using several optional
        parameters.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the filter.

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
        return self._get_api_list(
            f"/zones/{zone_identifier}/filters",
            page=AsyncV4PagePaginationArray[FirewallFilter],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "description": description,
                        "expression": expression,
                        "page": page,
                        "paused": paused,
                        "per_page": per_page,
                        "ref": ref,
                    },
                    filter_list_params.FilterListParams,
                ),
            ),
            model=FirewallFilter,
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
    ) -> FirewallFilter:
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
                post_parser=ResultWrapper[FirewallFilter]._unwrapper,
            ),
            cast_to=cast(Type[FirewallFilter], ResultWrapper[FirewallFilter]),
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
    ) -> FirewallFilter:
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
                post_parser=ResultWrapper[FirewallFilter]._unwrapper,
            ),
            cast_to=cast(Type[FirewallFilter], ResultWrapper[FirewallFilter]),
        )


class FiltersResourceWithRawResponse:
    def __init__(self, filters: FiltersResource) -> None:
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
        self.get = to_raw_response_wrapper(
            filters.get,
        )


class AsyncFiltersResourceWithRawResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
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
        self.get = async_to_raw_response_wrapper(
            filters.get,
        )


class FiltersResourceWithStreamingResponse:
    def __init__(self, filters: FiltersResource) -> None:
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
        self.get = to_streamed_response_wrapper(
            filters.get,
        )


class AsyncFiltersResourceWithStreamingResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
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
        self.get = async_to_streamed_response_wrapper(
            filters.get,
        )
