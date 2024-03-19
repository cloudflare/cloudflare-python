# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .content_lists import (
    ContentLists,
    AsyncContentLists,
    ContentListsWithRawResponse,
    AsyncContentListsWithRawResponse,
    ContentListsWithStreamingResponse,
    AsyncContentListsWithStreamingResponse,
)
from .content_lists.content_lists import ContentLists, AsyncContentLists

__all__ = ["IPFSUniversalPaths", "AsyncIPFSUniversalPaths"]


class IPFSUniversalPaths(SyncAPIResource):
    @cached_property
    def content_lists(self) -> ContentLists:
        return ContentLists(self._client)

    @cached_property
    def with_raw_response(self) -> IPFSUniversalPathsWithRawResponse:
        return IPFSUniversalPathsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPFSUniversalPathsWithStreamingResponse:
        return IPFSUniversalPathsWithStreamingResponse(self)


class AsyncIPFSUniversalPaths(AsyncAPIResource):
    @cached_property
    def content_lists(self) -> AsyncContentLists:
        return AsyncContentLists(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIPFSUniversalPathsWithRawResponse:
        return AsyncIPFSUniversalPathsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPFSUniversalPathsWithStreamingResponse:
        return AsyncIPFSUniversalPathsWithStreamingResponse(self)


class IPFSUniversalPathsWithRawResponse:
    def __init__(self, ipfs_universal_paths: IPFSUniversalPaths) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> ContentListsWithRawResponse:
        return ContentListsWithRawResponse(self._ipfs_universal_paths.content_lists)


class AsyncIPFSUniversalPathsWithRawResponse:
    def __init__(self, ipfs_universal_paths: AsyncIPFSUniversalPaths) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> AsyncContentListsWithRawResponse:
        return AsyncContentListsWithRawResponse(self._ipfs_universal_paths.content_lists)


class IPFSUniversalPathsWithStreamingResponse:
    def __init__(self, ipfs_universal_paths: IPFSUniversalPaths) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> ContentListsWithStreamingResponse:
        return ContentListsWithStreamingResponse(self._ipfs_universal_paths.content_lists)


class AsyncIPFSUniversalPathsWithStreamingResponse:
    def __init__(self, ipfs_universal_paths: AsyncIPFSUniversalPaths) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> AsyncContentListsWithStreamingResponse:
        return AsyncContentListsWithStreamingResponse(self._ipfs_universal_paths.content_lists)
