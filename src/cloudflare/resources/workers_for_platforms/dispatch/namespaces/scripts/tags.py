# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_compat import cached_property

from ......types.workers_for_platforms.dispatch.namespaces.scripts.tag_update_response import TagUpdateResponse

from ......_wrappers import ResultWrapper

from typing import List, Optional, Type

from ......_utils import maybe_transform, async_maybe_transform

from ......_base_client import make_request_options, AsyncPaginator

from ......pagination import SyncSinglePage, AsyncSinglePage

from ......types.workers_for_platforms.dispatch.namespaces.scripts.tag_list_response import TagListResponse

from ......_response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......_utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......_types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......types import shared_params
from ......types.workers_for_platforms.dispatch.namespaces.scripts import tag_update_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TagsResource", "AsyncTagsResource"]

class TagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self)

    def update(self,
    script_name: str,
    *,
    account_id: str,
    dispatch_namespace: str,
    body: List[str],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[TagUpdateResponse]:
        """
        Put script tags for a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          body: Tags to help you manage your Workers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not dispatch_namespace:
          raise ValueError(
            f'Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        return self._put(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags",
            body=maybe_transform(body, List[str]),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[TagUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[TagUpdateResponse]], ResultWrapper[TagUpdateResponse]),
        )

    def list(self,
    script_name: str,
    *,
    account_id: str,
    dispatch_namespace: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[TagListResponse]:
        """
        Fetch tags from a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not dispatch_namespace:
          raise ValueError(
            f'Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags",
            page = SyncSinglePage[TagListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=str,
        )

    def delete(self,
    tag: str,
    *,
    account_id: str,
    dispatch_namespace: str,
    script_name: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
        """
        Delete script tag for a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          tag: Tag to help you manage your Worker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not dispatch_namespace:
          raise ValueError(
            f'Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        if not tag:
          raise ValueError(
            f'Expected a non-empty value for `tag` but received {tag!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags/{tag}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

class AsyncTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self)

    async def update(self,
    script_name: str,
    *,
    account_id: str,
    dispatch_namespace: str,
    body: List[str],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[TagUpdateResponse]:
        """
        Put script tags for a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          body: Tags to help you manage your Workers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not dispatch_namespace:
          raise ValueError(
            f'Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags",
            body=await async_maybe_transform(body, List[str]),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[TagUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[TagUpdateResponse]], ResultWrapper[TagUpdateResponse]),
        )

    def list(self,
    script_name: str,
    *,
    account_id: str,
    dispatch_namespace: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[TagListResponse, AsyncSinglePage[TagListResponse]]:
        """
        Fetch tags from a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not dispatch_namespace:
          raise ValueError(
            f'Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags",
            page = AsyncSinglePage[TagListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=str,
        )

    async def delete(self,
    tag: str,
    *,
    account_id: str,
    dispatch_namespace: str,
    script_name: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
        """
        Delete script tag for a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          tag: Tag to help you manage your Worker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not dispatch_namespace:
          raise ValueError(
            f'Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        if not tag:
          raise ValueError(
            f'Expected a non-empty value for `tag` but received {tag!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags/{tag}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

class TagsResourceWithRawResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.update = to_raw_response_wrapper(
            tags.update,
        )
        self.list = to_raw_response_wrapper(
            tags.list,
        )
        self.delete = to_raw_response_wrapper(
            tags.delete,
        )

class AsyncTagsResourceWithRawResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.update = async_to_raw_response_wrapper(
            tags.update,
        )
        self.list = async_to_raw_response_wrapper(
            tags.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tags.delete,
        )

class TagsResourceWithStreamingResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.update = to_streamed_response_wrapper(
            tags.update,
        )
        self.list = to_streamed_response_wrapper(
            tags.list,
        )
        self.delete = to_streamed_response_wrapper(
            tags.delete,
        )

class AsyncTagsResourceWithStreamingResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.update = async_to_streamed_response_wrapper(
            tags.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tags.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tags.delete,
        )