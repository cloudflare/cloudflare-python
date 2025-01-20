# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

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
from ......types.web3.hostnames.ipfs_universal_paths.content_lists import entry_create_params, entry_update_params
from ......types.web3.hostnames.ipfs_universal_paths.content_lists.entry_get_response import EntryGetResponse
from ......types.web3.hostnames.ipfs_universal_paths.content_lists.entry_list_response import EntryListResponse
from ......types.web3.hostnames.ipfs_universal_paths.content_lists.entry_create_response import EntryCreateResponse
from ......types.web3.hostnames.ipfs_universal_paths.content_lists.entry_delete_response import EntryDeleteResponse
from ......types.web3.hostnames.ipfs_universal_paths.content_lists.entry_update_response import EntryUpdateResponse

__all__ = ["EntriesResource", "AsyncEntriesResource"]


class EntriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EntriesResourceWithStreamingResponse(self)

    def create(
        self,
        identifier: str,
        *,
        zone_id: str,
        content: str,
        type: Literal["cid", "content_path"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryCreateResponse:
        """
        Create IPFS Universal Path Gateway Content List Entry

        Args:
          zone_id: Identifier

          identifier: Identifier

          content: CID or content path of content to block.

          type: Type of content list entry to block.

          description: An optional description of the content list entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._post(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
            body=maybe_transform(
                {
                    "content": content,
                    "type": type,
                    "description": description,
                },
                entry_create_params.EntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EntryCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[EntryCreateResponse], ResultWrapper[EntryCreateResponse]),
        )

    def update(
        self,
        content_list_entry_identifier: str,
        *,
        zone_id: str,
        identifier: str,
        content: str,
        type: Literal["cid", "content_path"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryUpdateResponse:
        """
        Edit IPFS Universal Path Gateway Content List Entry

        Args:
          zone_id: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          content: CID or content path of content to block.

          type: Type of content list entry to block.

          description: An optional description of the content list entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return self._put(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            body=maybe_transform(
                {
                    "content": content,
                    "type": type,
                    "description": description,
                },
                entry_update_params.EntryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EntryUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[EntryUpdateResponse], ResultWrapper[EntryUpdateResponse]),
        )

    def list(
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
    ) -> Optional[EntryListResponse]:
        """
        List IPFS Universal Path Gateway Content List Entries

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
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EntryListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryListResponse]], ResultWrapper[EntryListResponse]),
        )

    def delete(
        self,
        content_list_entry_identifier: str,
        *,
        zone_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryDeleteResponse]:
        """
        Delete IPFS Universal Path Gateway Content List Entry

        Args:
          zone_id: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return self._delete(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EntryDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryDeleteResponse]], ResultWrapper[EntryDeleteResponse]),
        )

    def get(
        self,
        content_list_entry_identifier: str,
        *,
        zone_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryGetResponse:
        """
        IPFS Universal Path Gateway Content List Entry Details

        Args:
          zone_id: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return self._get(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EntryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[EntryGetResponse], ResultWrapper[EntryGetResponse]),
        )


class AsyncEntriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEntriesResourceWithStreamingResponse(self)

    async def create(
        self,
        identifier: str,
        *,
        zone_id: str,
        content: str,
        type: Literal["cid", "content_path"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryCreateResponse:
        """
        Create IPFS Universal Path Gateway Content List Entry

        Args:
          zone_id: Identifier

          identifier: Identifier

          content: CID or content path of content to block.

          type: Type of content list entry to block.

          description: An optional description of the content list entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._post(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "type": type,
                    "description": description,
                },
                entry_create_params.EntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EntryCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[EntryCreateResponse], ResultWrapper[EntryCreateResponse]),
        )

    async def update(
        self,
        content_list_entry_identifier: str,
        *,
        zone_id: str,
        identifier: str,
        content: str,
        type: Literal["cid", "content_path"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryUpdateResponse:
        """
        Edit IPFS Universal Path Gateway Content List Entry

        Args:
          zone_id: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          content: CID or content path of content to block.

          type: Type of content list entry to block.

          description: An optional description of the content list entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return await self._put(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "type": type,
                    "description": description,
                },
                entry_update_params.EntryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EntryUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[EntryUpdateResponse], ResultWrapper[EntryUpdateResponse]),
        )

    async def list(
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
    ) -> Optional[EntryListResponse]:
        """
        List IPFS Universal Path Gateway Content List Entries

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
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EntryListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryListResponse]], ResultWrapper[EntryListResponse]),
        )

    async def delete(
        self,
        content_list_entry_identifier: str,
        *,
        zone_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryDeleteResponse]:
        """
        Delete IPFS Universal Path Gateway Content List Entry

        Args:
          zone_id: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return await self._delete(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EntryDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryDeleteResponse]], ResultWrapper[EntryDeleteResponse]),
        )

    async def get(
        self,
        content_list_entry_identifier: str,
        *,
        zone_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryGetResponse:
        """
        IPFS Universal Path Gateway Content List Entry Details

        Args:
          zone_id: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return await self._get(
            f"/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EntryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[EntryGetResponse], ResultWrapper[EntryGetResponse]),
        )


class EntriesResourceWithRawResponse:
    def __init__(self, entries: EntriesResource) -> None:
        self._entries = entries

        self.create = to_raw_response_wrapper(
            entries.create,
        )
        self.update = to_raw_response_wrapper(
            entries.update,
        )
        self.list = to_raw_response_wrapper(
            entries.list,
        )
        self.delete = to_raw_response_wrapper(
            entries.delete,
        )
        self.get = to_raw_response_wrapper(
            entries.get,
        )


class AsyncEntriesResourceWithRawResponse:
    def __init__(self, entries: AsyncEntriesResource) -> None:
        self._entries = entries

        self.create = async_to_raw_response_wrapper(
            entries.create,
        )
        self.update = async_to_raw_response_wrapper(
            entries.update,
        )
        self.list = async_to_raw_response_wrapper(
            entries.list,
        )
        self.delete = async_to_raw_response_wrapper(
            entries.delete,
        )
        self.get = async_to_raw_response_wrapper(
            entries.get,
        )


class EntriesResourceWithStreamingResponse:
    def __init__(self, entries: EntriesResource) -> None:
        self._entries = entries

        self.create = to_streamed_response_wrapper(
            entries.create,
        )
        self.update = to_streamed_response_wrapper(
            entries.update,
        )
        self.list = to_streamed_response_wrapper(
            entries.list,
        )
        self.delete = to_streamed_response_wrapper(
            entries.delete,
        )
        self.get = to_streamed_response_wrapper(
            entries.get,
        )


class AsyncEntriesResourceWithStreamingResponse:
    def __init__(self, entries: AsyncEntriesResource) -> None:
        self._entries = entries

        self.create = async_to_streamed_response_wrapper(
            entries.create,
        )
        self.update = async_to_streamed_response_wrapper(
            entries.update,
        )
        self.list = async_to_streamed_response_wrapper(
            entries.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            entries.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            entries.get,
        )
