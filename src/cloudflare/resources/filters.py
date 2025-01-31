# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Type, cast

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
from ..pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from .._base_client import AsyncPaginator, make_request_options
from ..types.filters import filter_list_params, filter_create_params, filter_update_params
from ..types.filters.firewall_filter import FirewallFilter

__all__ = ["FiltersResource", "AsyncFiltersResource"]


class FiltersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FiltersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiltersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FiltersResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    def create(
        self,
        *,
        zone_id: str,
        expression: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[FirewallFilter]:
        """
        Creates one or more filters.

        Args:
          zone_id: Identifier

          expression: The filter expression. For more information, refer to
              [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/filters",
            page=SyncSinglePage[FirewallFilter],
            body=maybe_transform({"expression": expression}, filter_create_params.FilterCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=FirewallFilter,
            method="post",
        )

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    def update(
        self,
        filter_id: str,
        *,
        zone_id: str,
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
          zone_id: Identifier

          filter_id: The unique identifier of the filter.

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
            f"/zones/{zone_id}/filters/{filter_id}",
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

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    def list(
        self,
        *,
        zone_id: str,
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
          zone_id: Identifier

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
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/filters",
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

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
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
    ) -> FirewallFilter:
        """
        Deletes an existing filter.

        Args:
          zone_id: Identifier

          filter_id: The unique identifier of the filter.

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
            f"/zones/{zone_id}/filters/{filter_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FirewallFilter]._unwrapper,
            ),
            cast_to=cast(Type[FirewallFilter], ResultWrapper[FirewallFilter]),
        )

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    def bulk_delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[FirewallFilter]:
        """
        Deletes one or more existing filters.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/filters",
            page=SyncSinglePage[FirewallFilter],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=FirewallFilter,
            method="delete",
        )

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    def bulk_update(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[FirewallFilter]:
        """
        Updates one or more existing filters.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/filters",
            page=SyncSinglePage[FirewallFilter],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=FirewallFilter,
            method="put",
        )

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    def get(
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
    ) -> FirewallFilter:
        """
        Fetches the details of a filter.

        Args:
          zone_id: Identifier

          filter_id: The unique identifier of the filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not filter_id:
            raise ValueError(f"Expected a non-empty value for `filter_id` but received {filter_id!r}")
        return self._get(
            f"/zones/{zone_id}/filters/{filter_id}",
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiltersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFiltersResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    def create(
        self,
        *,
        zone_id: str,
        expression: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[FirewallFilter, AsyncSinglePage[FirewallFilter]]:
        """
        Creates one or more filters.

        Args:
          zone_id: Identifier

          expression: The filter expression. For more information, refer to
              [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/filters",
            page=AsyncSinglePage[FirewallFilter],
            body=maybe_transform({"expression": expression}, filter_create_params.FilterCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=FirewallFilter,
            method="post",
        )

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    async def update(
        self,
        filter_id: str,
        *,
        zone_id: str,
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
          zone_id: Identifier

          filter_id: The unique identifier of the filter.

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
            f"/zones/{zone_id}/filters/{filter_id}",
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

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    def list(
        self,
        *,
        zone_id: str,
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
          zone_id: Identifier

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
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/filters",
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

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
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
    ) -> FirewallFilter:
        """
        Deletes an existing filter.

        Args:
          zone_id: Identifier

          filter_id: The unique identifier of the filter.

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
            f"/zones/{zone_id}/filters/{filter_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FirewallFilter]._unwrapper,
            ),
            cast_to=cast(Type[FirewallFilter], ResultWrapper[FirewallFilter]),
        )

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    def bulk_delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[FirewallFilter, AsyncSinglePage[FirewallFilter]]:
        """
        Deletes one or more existing filters.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/filters",
            page=AsyncSinglePage[FirewallFilter],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=FirewallFilter,
            method="delete",
        )

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    def bulk_update(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[FirewallFilter, AsyncSinglePage[FirewallFilter]]:
        """
        Updates one or more existing filters.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/filters",
            page=AsyncSinglePage[FirewallFilter],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=FirewallFilter,
            method="put",
        )

    @typing_extensions.deprecated(
        "The Filters API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#firewall-rules-api-and-filters-api for full details."
    )
    async def get(
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
    ) -> FirewallFilter:
        """
        Fetches the details of a filter.

        Args:
          zone_id: Identifier

          filter_id: The unique identifier of the filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not filter_id:
            raise ValueError(f"Expected a non-empty value for `filter_id` but received {filter_id!r}")
        return await self._get(
            f"/zones/{zone_id}/filters/{filter_id}",
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

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                filters.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                filters.update  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                filters.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                filters.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                filters.bulk_delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                filters.bulk_update  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                filters.get  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncFiltersResourceWithRawResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
        self._filters = filters

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                filters.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                filters.update  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                filters.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                filters.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                filters.bulk_delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                filters.bulk_update  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                filters.get  # pyright: ignore[reportDeprecated],
            )
        )


class FiltersResourceWithStreamingResponse:
    def __init__(self, filters: FiltersResource) -> None:
        self._filters = filters

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                filters.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                filters.update  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                filters.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                filters.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                filters.bulk_delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                filters.bulk_update  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                filters.get  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncFiltersResourceWithStreamingResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
        self._filters = filters

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                filters.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                filters.update  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                filters.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                filters.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                filters.bulk_delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                filters.bulk_update  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                filters.get  # pyright: ignore[reportDeprecated],
            )
        )
