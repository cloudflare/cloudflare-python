# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

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
from .....types.zero_trust.dlp.data_tag_categories import data_tag_create_params, data_tag_update_params
from .....types.zero_trust.dlp.data_tag_categories.data_tag_get_response import DataTagGetResponse
from .....types.zero_trust.dlp.data_tag_categories.data_tag_list_response import DataTagListResponse
from .....types.zero_trust.dlp.data_tag_categories.data_tag_create_response import DataTagCreateResponse
from .....types.zero_trust.dlp.data_tag_categories.data_tag_update_response import DataTagUpdateResponse

__all__ = ["DataTagsResource", "AsyncDataTagsResource"]


class DataTagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DataTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DataTagsResourceWithStreamingResponse(self)

    def create(
        self,
        category_id: str,
        *,
        account_id: str,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataTagCreateResponse]:
        """
        Creates a data tag in a category.

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
        return self._post(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags",
                account_id=account_id,
                category_id=category_id,
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                data_tag_create_params.DataTagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagCreateResponse]], ResultWrapper[DataTagCreateResponse]),
        )

    def update(
        self,
        tag_id: str,
        *,
        account_id: str,
        category_id: str,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataTagUpdateResponse]:
        """
        Updates a data tag in a category.

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
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags/{tag_id}",
                account_id=account_id,
                category_id=category_id,
                tag_id=tag_id,
            ),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                data_tag_update_params.DataTagUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagUpdateResponse]], ResultWrapper[DataTagUpdateResponse]),
        )

    def list(
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
    ) -> SyncSinglePage[DataTagListResponse]:
        """
        Lists data tags in a category.

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
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags",
                account_id=account_id,
                category_id=category_id,
            ),
            page=SyncSinglePage[DataTagListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DataTagListResponse,
        )

    def delete(
        self,
        tag_id: str,
        *,
        account_id: str,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a data tag from a category.

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
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags/{tag_id}",
                account_id=account_id,
                category_id=category_id,
                tag_id=tag_id,
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
        tag_id: str,
        *,
        account_id: str,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataTagGetResponse]:
        """
        Gets a data tag from a category.

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
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags/{tag_id}",
                account_id=account_id,
                category_id=category_id,
                tag_id=tag_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagGetResponse]], ResultWrapper[DataTagGetResponse]),
        )


class AsyncDataTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDataTagsResourceWithStreamingResponse(self)

    async def create(
        self,
        category_id: str,
        *,
        account_id: str,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataTagCreateResponse]:
        """
        Creates a data tag in a category.

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
        return await self._post(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags",
                account_id=account_id,
                category_id=category_id,
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                data_tag_create_params.DataTagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagCreateResponse]], ResultWrapper[DataTagCreateResponse]),
        )

    async def update(
        self,
        tag_id: str,
        *,
        account_id: str,
        category_id: str,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataTagUpdateResponse]:
        """
        Updates a data tag in a category.

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
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags/{tag_id}",
                account_id=account_id,
                category_id=category_id,
                tag_id=tag_id,
            ),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                data_tag_update_params.DataTagUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagUpdateResponse]], ResultWrapper[DataTagUpdateResponse]),
        )

    def list(
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
    ) -> AsyncPaginator[DataTagListResponse, AsyncSinglePage[DataTagListResponse]]:
        """
        Lists data tags in a category.

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
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags",
                account_id=account_id,
                category_id=category_id,
            ),
            page=AsyncSinglePage[DataTagListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DataTagListResponse,
        )

    async def delete(
        self,
        tag_id: str,
        *,
        account_id: str,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a data tag from a category.

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
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags/{tag_id}",
                account_id=account_id,
                category_id=category_id,
                tag_id=tag_id,
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
        tag_id: str,
        *,
        account_id: str,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DataTagGetResponse]:
        """
        Gets a data tag from a category.

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
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags/{tag_id}",
                account_id=account_id,
                category_id=category_id,
                tag_id=tag_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DataTagGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DataTagGetResponse]], ResultWrapper[DataTagGetResponse]),
        )


class DataTagsResourceWithRawResponse:
    def __init__(self, data_tags: DataTagsResource) -> None:
        self._data_tags = data_tags

        self.create = to_raw_response_wrapper(
            data_tags.create,
        )
        self.update = to_raw_response_wrapper(
            data_tags.update,
        )
        self.list = to_raw_response_wrapper(
            data_tags.list,
        )
        self.delete = to_raw_response_wrapper(
            data_tags.delete,
        )
        self.get = to_raw_response_wrapper(
            data_tags.get,
        )


class AsyncDataTagsResourceWithRawResponse:
    def __init__(self, data_tags: AsyncDataTagsResource) -> None:
        self._data_tags = data_tags

        self.create = async_to_raw_response_wrapper(
            data_tags.create,
        )
        self.update = async_to_raw_response_wrapper(
            data_tags.update,
        )
        self.list = async_to_raw_response_wrapper(
            data_tags.list,
        )
        self.delete = async_to_raw_response_wrapper(
            data_tags.delete,
        )
        self.get = async_to_raw_response_wrapper(
            data_tags.get,
        )


class DataTagsResourceWithStreamingResponse:
    def __init__(self, data_tags: DataTagsResource) -> None:
        self._data_tags = data_tags

        self.create = to_streamed_response_wrapper(
            data_tags.create,
        )
        self.update = to_streamed_response_wrapper(
            data_tags.update,
        )
        self.list = to_streamed_response_wrapper(
            data_tags.list,
        )
        self.delete = to_streamed_response_wrapper(
            data_tags.delete,
        )
        self.get = to_streamed_response_wrapper(
            data_tags.get,
        )


class AsyncDataTagsResourceWithStreamingResponse:
    def __init__(self, data_tags: AsyncDataTagsResource) -> None:
        self._data_tags = data_tags

        self.create = async_to_streamed_response_wrapper(
            data_tags.create,
        )
        self.update = async_to_streamed_response_wrapper(
            data_tags.update,
        )
        self.list = async_to_streamed_response_wrapper(
            data_tags.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            data_tags.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            data_tags.get,
        )
