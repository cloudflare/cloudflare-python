# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from .data_tags import (
    DataTagsResource,
    AsyncDataTagsResource,
    DataTagsResourceWithRawResponse,
    AsyncDataTagsResourceWithRawResponse,
    DataTagsResourceWithStreamingResponse,
    AsyncDataTagsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.dlp import data_tag_category_create_params, data_tag_category_update_params
from .....types.zero_trust.dlp.data_tag_category_get_response import DataTagCategoryGetResponse
from .....types.zero_trust.dlp.data_tag_category_list_response import DataTagCategoryListResponse
from .....types.zero_trust.dlp.data_tag_category_create_response import DataTagCategoryCreateResponse
from .....types.zero_trust.dlp.data_tag_category_update_response import DataTagCategoryUpdateResponse

__all__ = ["DataTagCategoriesResource", "AsyncDataTagCategoriesResource"]


class DataTagCategoriesResource(SyncAPIResource):
    @cached_property
    def data_tags(self) -> DataTagsResource:
        return DataTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataTagCategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DataTagCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataTagCategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DataTagCategoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        description: Optional[str] | Omit = omit,
        tags: Iterable[data_tag_category_create_params.Tag] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataTagCategoryCreateResponse]:
        """
        Creates a data tag category, optionally from a template.

        Args:
          tags: Tags to create with the category. Mutually exclusive with `template_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/dlp/data_tag_categories", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "tags": tags,
                    "template_id": template_id,
                },
                data_tag_category_create_params.DataTagCategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagCategoryCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagCategoryCreateResponse]], ResultWrapper[DataTagCategoryCreateResponse]),
        )

    def update(
        self,
        category_id: str,
        *,
        account_id: str,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        tags: Optional[Iterable[data_tag_category_update_params.Tag]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataTagCategoryUpdateResponse]:
        """
        Updates a data tag category and its tags.

        Args:
          tags: The desired final state of tags.

              - `None` (omitted): no tag changes.
              - `Some([])`: delete all tags.
              - `Some([...])`: desired final set + order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "tags": tags,
                },
                data_tag_category_update_params.DataTagCategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagCategoryUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagCategoryUpdateResponse]], ResultWrapper[DataTagCategoryUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[DataTagCategoryListResponse]:
        """
        Lists data tag categories configured for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/data_tag_categories", account_id=account_id),
            page=SyncSinglePage[DataTagCategoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DataTagCategoryListResponse,
        )

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
    ) -> object:
        """
        Deletes a data tag category and its tags.

        Args:
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
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

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
    ) -> Optional[DataTagCategoryGetResponse]:
        """
        Gets a data tag category and its tags.

        Args:
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
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagCategoryGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagCategoryGetResponse]], ResultWrapper[DataTagCategoryGetResponse]),
        )


class AsyncDataTagCategoriesResource(AsyncAPIResource):
    @cached_property
    def data_tags(self) -> AsyncDataTagsResource:
        return AsyncDataTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataTagCategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataTagCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataTagCategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDataTagCategoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        description: Optional[str] | Omit = omit,
        tags: Iterable[data_tag_category_create_params.Tag] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataTagCategoryCreateResponse]:
        """
        Creates a data tag category, optionally from a template.

        Args:
          tags: Tags to create with the category. Mutually exclusive with `template_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/dlp/data_tag_categories", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "tags": tags,
                    "template_id": template_id,
                },
                data_tag_category_create_params.DataTagCategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagCategoryCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagCategoryCreateResponse]], ResultWrapper[DataTagCategoryCreateResponse]),
        )

    async def update(
        self,
        category_id: str,
        *,
        account_id: str,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        tags: Optional[Iterable[data_tag_category_update_params.Tag]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataTagCategoryUpdateResponse]:
        """
        Updates a data tag category and its tags.

        Args:
          tags: The desired final state of tags.

              - `None` (omitted): no tag changes.
              - `Some([])`: delete all tags.
              - `Some([...])`: desired final set + order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "tags": tags,
                },
                data_tag_category_update_params.DataTagCategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagCategoryUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagCategoryUpdateResponse]], ResultWrapper[DataTagCategoryUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DataTagCategoryListResponse, AsyncSinglePage[DataTagCategoryListResponse]]:
        """
        Lists data tag categories configured for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dlp/data_tag_categories", account_id=account_id),
            page=AsyncSinglePage[DataTagCategoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DataTagCategoryListResponse,
        )

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
    ) -> object:
        """
        Deletes a data tag category and its tags.

        Args:
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
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

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
    ) -> Optional[DataTagCategoryGetResponse]:
        """
        Gets a data tag category and its tags.

        Args:
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
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}",
                account_id=account_id,
                category_id=category_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagCategoryGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagCategoryGetResponse]], ResultWrapper[DataTagCategoryGetResponse]),
        )


class DataTagCategoriesResourceWithRawResponse:
    def __init__(self, data_tag_categories: DataTagCategoriesResource) -> None:
        self._data_tag_categories = data_tag_categories

        self.create = to_raw_response_wrapper(
            data_tag_categories.create,
        )
        self.update = to_raw_response_wrapper(
            data_tag_categories.update,
        )
        self.list = to_raw_response_wrapper(
            data_tag_categories.list,
        )
        self.delete = to_raw_response_wrapper(
            data_tag_categories.delete,
        )
        self.get = to_raw_response_wrapper(
            data_tag_categories.get,
        )

    @cached_property
    def data_tags(self) -> DataTagsResourceWithRawResponse:
        return DataTagsResourceWithRawResponse(self._data_tag_categories.data_tags)


class AsyncDataTagCategoriesResourceWithRawResponse:
    def __init__(self, data_tag_categories: AsyncDataTagCategoriesResource) -> None:
        self._data_tag_categories = data_tag_categories

        self.create = async_to_raw_response_wrapper(
            data_tag_categories.create,
        )
        self.update = async_to_raw_response_wrapper(
            data_tag_categories.update,
        )
        self.list = async_to_raw_response_wrapper(
            data_tag_categories.list,
        )
        self.delete = async_to_raw_response_wrapper(
            data_tag_categories.delete,
        )
        self.get = async_to_raw_response_wrapper(
            data_tag_categories.get,
        )

    @cached_property
    def data_tags(self) -> AsyncDataTagsResourceWithRawResponse:
        return AsyncDataTagsResourceWithRawResponse(self._data_tag_categories.data_tags)


class DataTagCategoriesResourceWithStreamingResponse:
    def __init__(self, data_tag_categories: DataTagCategoriesResource) -> None:
        self._data_tag_categories = data_tag_categories

        self.create = to_streamed_response_wrapper(
            data_tag_categories.create,
        )
        self.update = to_streamed_response_wrapper(
            data_tag_categories.update,
        )
        self.list = to_streamed_response_wrapper(
            data_tag_categories.list,
        )
        self.delete = to_streamed_response_wrapper(
            data_tag_categories.delete,
        )
        self.get = to_streamed_response_wrapper(
            data_tag_categories.get,
        )

    @cached_property
    def data_tags(self) -> DataTagsResourceWithStreamingResponse:
        return DataTagsResourceWithStreamingResponse(self._data_tag_categories.data_tags)


class AsyncDataTagCategoriesResourceWithStreamingResponse:
    def __init__(self, data_tag_categories: AsyncDataTagCategoriesResource) -> None:
        self._data_tag_categories = data_tag_categories

        self.create = async_to_streamed_response_wrapper(
            data_tag_categories.create,
        )
        self.update = async_to_streamed_response_wrapper(
            data_tag_categories.update,
        )
        self.list = async_to_streamed_response_wrapper(
            data_tag_categories.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            data_tag_categories.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            data_tag_categories.get,
        )

    @cached_property
    def data_tags(self) -> AsyncDataTagsResourceWithStreamingResponse:
        return AsyncDataTagsResourceWithStreamingResponse(self._data_tag_categories.data_tags)
