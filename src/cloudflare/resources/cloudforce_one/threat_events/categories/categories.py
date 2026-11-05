# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

import httpx

from .catalog import (
    CatalogResource,
    AsyncCatalogResource,
    CatalogResourceWithRawResponse,
    AsyncCatalogResourceWithRawResponse,
    CatalogResourceWithStreamingResponse,
    AsyncCatalogResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloudforce_one.threat_events import category_edit_params, category_list_params, category_create_params
from .....types.cloudforce_one.threat_events.category_get_response import CategoryGetResponse
from .....types.cloudforce_one.threat_events.category_edit_response import CategoryEditResponse
from .....types.cloudforce_one.threat_events.category_list_response import CategoryListResponse
from .....types.cloudforce_one.threat_events.category_create_response import CategoryCreateResponse
from .....types.cloudforce_one.threat_events.category_delete_response import CategoryDeleteResponse

__all__ = ["CategoriesResource", "AsyncCategoriesResource"]


class CategoriesResource(SyncAPIResource):
    @cached_property
    def catalog(self) -> CatalogResource:
        return CatalogResource(self._client)

    @cached_property
    def with_raw_response(self) -> CategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CategoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        kill_chain: float,
        name: str,
        mitre_attack: SequenceNotStr[str] | Omit = omit,
        mitre_capec: SequenceNotStr[str] | Omit = omit,
        shortname: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryCreateResponse:
        """Creates an event category for classifying events.

        `name` and `killChain` are
        required.

        Args:
          account_id: Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/categories/create", account_id=account_id),
            body=maybe_transform(
                {
                    "kill_chain": kill_chain,
                    "name": name,
                    "mitre_attack": mitre_attack,
                    "mitre_capec": mitre_capec,
                    "shortname": shortname,
                },
                category_create_params.CategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryCreateResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryListResponse:
        """
        Lists the event categories used by events in the datasets given by `datasetIds`,
        or in the default dataset when `datasetIds` is omitted. Dataset scope values are
        not supported. To list every category, use
        `threat-intel events categories catalog list`.

        Args:
          account_id: Account ID.

          dataset_ids: Array of dataset IDs to query categories from. If not provided, uses the default
              dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/categories", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset_ids": dataset_ids}, category_list_params.CategoryListParams),
            ),
            cast_to=CategoryListResponse,
        )

    @typing_extensions.deprecated("Use DELETE /events/event-categories/by-id/{category_id} before 2026-11-28.")
    def delete(
        self,
        category_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryDeleteResponse:
        """Legacy.

        Use `threat-intel events categories delete`
        (`DELETE /events/event-categories/by-id/{category_id}`) instead. Available
        through 2026-11-28.

        Args:
          account_id: Account ID.

          category_id: Category UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryDeleteResponse,
        )

    @typing_extensions.deprecated("Use PATCH /events/event-categories/by-id/{category_id} before 2026-11-28.")
    def edit(
        self,
        category_id: str,
        *,
        account_id: str,
        kill_chain: float | Omit = omit,
        mitre_attack: SequenceNotStr[str] | Omit = omit,
        mitre_capec: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        shortname: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryEditResponse:
        """Legacy.

        Use `threat-intel events categories update`
        (`PATCH /events/event-categories/by-id/{category_id}`) instead. Available
        through 2026-11-28.

        Args:
          account_id: Account ID.

          category_id: Category UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            body=maybe_transform(
                {
                    "kill_chain": kill_chain,
                    "mitre_attack": mitre_attack,
                    "mitre_capec": mitre_capec,
                    "name": name,
                    "shortname": shortname,
                },
                category_edit_params.CategoryEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryEditResponse,
        )

    @typing_extensions.deprecated("Use GET /events/event-categories/by-id/{category_id} before 2026-11-28.")
    def get(
        self,
        category_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryGetResponse:
        """Legacy.

        Use `threat-intel events categories get`
        (`GET /events/event-categories/by-id/{category_id}`) instead. Available through
        2026-11-28.

        Args:
          account_id: Account ID.

          category_id: Category UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryGetResponse,
        )


class AsyncCategoriesResource(AsyncAPIResource):
    @cached_property
    def catalog(self) -> AsyncCatalogResource:
        return AsyncCatalogResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCategoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        kill_chain: float,
        name: str,
        mitre_attack: SequenceNotStr[str] | Omit = omit,
        mitre_capec: SequenceNotStr[str] | Omit = omit,
        shortname: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryCreateResponse:
        """Creates an event category for classifying events.

        `name` and `killChain` are
        required.

        Args:
          account_id: Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/categories/create", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "kill_chain": kill_chain,
                    "name": name,
                    "mitre_attack": mitre_attack,
                    "mitre_capec": mitre_capec,
                    "shortname": shortname,
                },
                category_create_params.CategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryCreateResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryListResponse:
        """
        Lists the event categories used by events in the datasets given by `datasetIds`,
        or in the default dataset when `datasetIds` is omitted. Dataset scope values are
        not supported. To list every category, use
        `threat-intel events categories catalog list`.

        Args:
          account_id: Account ID.

          dataset_ids: Array of dataset IDs to query categories from. If not provided, uses the default
              dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/categories", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset_ids": dataset_ids}, category_list_params.CategoryListParams
                ),
            ),
            cast_to=CategoryListResponse,
        )

    @typing_extensions.deprecated("Use DELETE /events/event-categories/by-id/{category_id} before 2026-11-28.")
    async def delete(
        self,
        category_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryDeleteResponse:
        """Legacy.

        Use `threat-intel events categories delete`
        (`DELETE /events/event-categories/by-id/{category_id}`) instead. Available
        through 2026-11-28.

        Args:
          account_id: Account ID.

          category_id: Category UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryDeleteResponse,
        )

    @typing_extensions.deprecated("Use PATCH /events/event-categories/by-id/{category_id} before 2026-11-28.")
    async def edit(
        self,
        category_id: str,
        *,
        account_id: str,
        kill_chain: float | Omit = omit,
        mitre_attack: SequenceNotStr[str] | Omit = omit,
        mitre_capec: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        shortname: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryEditResponse:
        """Legacy.

        Use `threat-intel events categories update`
        (`PATCH /events/event-categories/by-id/{category_id}`) instead. Available
        through 2026-11-28.

        Args:
          account_id: Account ID.

          category_id: Category UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            body=await async_maybe_transform(
                {
                    "kill_chain": kill_chain,
                    "mitre_attack": mitre_attack,
                    "mitre_capec": mitre_capec,
                    "name": name,
                    "shortname": shortname,
                },
                category_edit_params.CategoryEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryEditResponse,
        )

    @typing_extensions.deprecated("Use GET /events/event-categories/by-id/{category_id} before 2026-11-28.")
    async def get(
        self,
        category_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryGetResponse:
        """Legacy.

        Use `threat-intel events categories get`
        (`GET /events/event-categories/by-id/{category_id}`) instead. Available through
        2026-11-28.

        Args:
          account_id: Account ID.

          category_id: Category UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryGetResponse,
        )


class CategoriesResourceWithRawResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.create = to_raw_response_wrapper(
            categories.create,
        )
        self.list = to_raw_response_wrapper(
            categories.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                categories.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                categories.edit,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                categories.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def catalog(self) -> CatalogResourceWithRawResponse:
        return CatalogResourceWithRawResponse(self._categories.catalog)


class AsyncCategoriesResourceWithRawResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.create = async_to_raw_response_wrapper(
            categories.create,
        )
        self.list = async_to_raw_response_wrapper(
            categories.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                categories.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                categories.edit,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                categories.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def catalog(self) -> AsyncCatalogResourceWithRawResponse:
        return AsyncCatalogResourceWithRawResponse(self._categories.catalog)


class CategoriesResourceWithStreamingResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.create = to_streamed_response_wrapper(
            categories.create,
        )
        self.list = to_streamed_response_wrapper(
            categories.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                categories.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                categories.edit,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                categories.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def catalog(self) -> CatalogResourceWithStreamingResponse:
        return CatalogResourceWithStreamingResponse(self._categories.catalog)


class AsyncCategoriesResourceWithStreamingResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.create = async_to_streamed_response_wrapper(
            categories.create,
        )
        self.list = async_to_streamed_response_wrapper(
            categories.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                categories.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                categories.edit,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                categories.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def catalog(self) -> AsyncCatalogResourceWithStreamingResponse:
        return AsyncCatalogResourceWithStreamingResponse(self._categories.catalog)
