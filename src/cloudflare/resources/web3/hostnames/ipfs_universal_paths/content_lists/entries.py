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
from ......_base_client import (
    make_request_options,
)
from ......types.web3.hostnames.ipfs_universal_paths.content_lists import (
    EntryListResponse,
    EntryDeleteResponse,
    DwebConfigContentListEntry,
    entry_create_params,
    entry_update_params,
)

__all__ = ["Entries", "AsyncEntries"]


class Entries(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntriesWithRawResponse:
        return EntriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntriesWithStreamingResponse:
        return EntriesWithStreamingResponse(self)

    def create(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        content: str,
        type: Literal["cid", "content_path"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DwebConfigContentListEntry:
        """
        Create IPFS Universal Path Gateway Content List Entry

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content: CID or content path of content to block.

          type: Type of content list entry to block.

          description: An optional description of the content list entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigContentListEntry], ResultWrapper[DwebConfigContentListEntry]),
        )

    def update(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
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
    ) -> DwebConfigContentListEntry:
        """
        Edit IPFS Universal Path Gateway Content List Entry

        Args:
          zone_identifier: Identifier

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
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return self._put(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigContentListEntry], ResultWrapper[DwebConfigContentListEntry]),
        )

    def list(
        self,
        identifier: str,
        *,
        zone_identifier: str,
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
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryListResponse]], ResultWrapper[EntryListResponse]),
        )

    def delete(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
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
          zone_identifier: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return self._delete(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryDeleteResponse]], ResultWrapper[EntryDeleteResponse]),
        )

    def get(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DwebConfigContentListEntry:
        """
        IPFS Universal Path Gateway Content List Entry Details

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigContentListEntry], ResultWrapper[DwebConfigContentListEntry]),
        )


class AsyncEntries(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntriesWithRawResponse:
        return AsyncEntriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntriesWithStreamingResponse:
        return AsyncEntriesWithStreamingResponse(self)

    async def create(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        content: str,
        type: Literal["cid", "content_path"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DwebConfigContentListEntry:
        """
        Create IPFS Universal Path Gateway Content List Entry

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content: CID or content path of content to block.

          type: Type of content list entry to block.

          description: An optional description of the content list entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigContentListEntry], ResultWrapper[DwebConfigContentListEntry]),
        )

    async def update(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
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
    ) -> DwebConfigContentListEntry:
        """
        Edit IPFS Universal Path Gateway Content List Entry

        Args:
          zone_identifier: Identifier

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
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return await self._put(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigContentListEntry], ResultWrapper[DwebConfigContentListEntry]),
        )

    async def list(
        self,
        identifier: str,
        *,
        zone_identifier: str,
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
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryListResponse]], ResultWrapper[EntryListResponse]),
        )

    async def delete(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
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
          zone_identifier: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return await self._delete(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryDeleteResponse]], ResultWrapper[EntryDeleteResponse]),
        )

    async def get(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DwebConfigContentListEntry:
        """
        IPFS Universal Path Gateway Content List Entry Details

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return await self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DwebConfigContentListEntry], ResultWrapper[DwebConfigContentListEntry]),
        )


class EntriesWithRawResponse:
    def __init__(self, entries: Entries) -> None:
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


class AsyncEntriesWithRawResponse:
    def __init__(self, entries: AsyncEntries) -> None:
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


class EntriesWithStreamingResponse:
    def __init__(self, entries: Entries) -> None:
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


class AsyncEntriesWithStreamingResponse:
    def __init__(self, entries: AsyncEntries) -> None:
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
