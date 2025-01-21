# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from .entries import (
    EntriesResource,
    AsyncEntriesResource,
    EntriesResourceWithRawResponse,
    AsyncEntriesResourceWithRawResponse,
    EntriesResourceWithStreamingResponse,
    AsyncEntriesResourceWithStreamingResponse,
)
from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import make_request_options
from ......types.web3.hostnames.ipfs_universal_paths import content_list_update_params
from ......types.web3.hostnames.ipfs_universal_paths.content_list import ContentList

__all__ = ["ContentListsResource", "AsyncContentListsResource"]


class ContentListsResource(SyncAPIResource):
    @cached_property
    def entries(self) -> EntriesResource:
        return EntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContentListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ContentListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ContentListsResourceWithStreamingResponse(self)

    def update(
        self,
        identifier: str,
        *,
        zone_id: str,
        action: Literal["block"],
        entries: Iterable[content_list_update_params.Entry],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentList:
        """
        Update IPFS Universal Path Gateway Content List

        Args:
          zone_id: Identifier

          identifier: Identifier

          action: Behavior of the content list.

          entries: Content list entries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._put(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list",
            body=maybe_transform(
                {
                    "action": action,
                    "entries": entries,
                },
                content_list_update_params.ContentListUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ContentList]._unwrapper,
            ),
            cast_to=cast(Type[ContentList], ResultWrapper[ContentList]),
        )

    def get(
        self,
        identifier: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentList:
        """
        IPFS Universal Path Gateway Content List Details

        Args:
          zone_id: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ContentList]._unwrapper,
            ),
            cast_to=cast(Type[ContentList], ResultWrapper[ContentList]),
        )


class AsyncContentListsResource(AsyncAPIResource):
    @cached_property
    def entries(self) -> AsyncEntriesResource:
        return AsyncEntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContentListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncContentListsResourceWithStreamingResponse(self)

    async def update(
        self,
        identifier: str,
        *,
        zone_id: str,
        action: Literal["block"],
        entries: Iterable[content_list_update_params.Entry],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentList:
        """
        Update IPFS Universal Path Gateway Content List

        Args:
          zone_id: Identifier

          identifier: Identifier

          action: Behavior of the content list.

          entries: Content list entries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._put(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "entries": entries,
                },
                content_list_update_params.ContentListUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ContentList]._unwrapper,
            ),
            cast_to=cast(Type[ContentList], ResultWrapper[ContentList]),
        )

    async def get(
        self,
        identifier: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentList:
        """
        IPFS Universal Path Gateway Content List Details

        Args:
          zone_id: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ContentList]._unwrapper,
            ),
            cast_to=cast(Type[ContentList], ResultWrapper[ContentList]),
        )


class ContentListsResourceWithRawResponse:
    def __init__(self, content_lists: ContentListsResource) -> None:
        self._content_lists = content_lists

        self.update = to_raw_response_wrapper(
            content_lists.update,
        )
        self.get = to_raw_response_wrapper(
            content_lists.get,
        )

    @cached_property
    def entries(self) -> EntriesResourceWithRawResponse:
        return EntriesResourceWithRawResponse(self._content_lists.entries)


class AsyncContentListsResourceWithRawResponse:
    def __init__(self, content_lists: AsyncContentListsResource) -> None:
        self._content_lists = content_lists

        self.update = async_to_raw_response_wrapper(
            content_lists.update,
        )
        self.get = async_to_raw_response_wrapper(
            content_lists.get,
        )

    @cached_property
    def entries(self) -> AsyncEntriesResourceWithRawResponse:
        return AsyncEntriesResourceWithRawResponse(self._content_lists.entries)


class ContentListsResourceWithStreamingResponse:
    def __init__(self, content_lists: ContentListsResource) -> None:
        self._content_lists = content_lists

        self.update = to_streamed_response_wrapper(
            content_lists.update,
        )
        self.get = to_streamed_response_wrapper(
            content_lists.get,
        )

    @cached_property
    def entries(self) -> EntriesResourceWithStreamingResponse:
        return EntriesResourceWithStreamingResponse(self._content_lists.entries)


class AsyncContentListsResourceWithStreamingResponse:
    def __init__(self, content_lists: AsyncContentListsResource) -> None:
        self._content_lists = content_lists

        self.update = async_to_streamed_response_wrapper(
            content_lists.update,
        )
        self.get = async_to_streamed_response_wrapper(
            content_lists.get,
        )

    @cached_property
    def entries(self) -> AsyncEntriesResourceWithStreamingResponse:
        return AsyncEntriesResourceWithStreamingResponse(self._content_lists.entries)
