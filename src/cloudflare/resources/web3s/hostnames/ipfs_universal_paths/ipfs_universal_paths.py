# File generated from our OpenAPI spec by Stainless.

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

__all__ = ["IpfsUniversalPaths", "AsyncIpfsUniversalPaths"]


class IpfsUniversalPaths(SyncAPIResource):
    @cached_property
    def content_lists(self) -> ContentLists:
        return ContentLists(self._client)

    @cached_property
    def with_raw_response(self) -> IpfsUniversalPathsWithRawResponse:
        return IpfsUniversalPathsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IpfsUniversalPathsWithStreamingResponse:
        return IpfsUniversalPathsWithStreamingResponse(self)


class AsyncIpfsUniversalPaths(AsyncAPIResource):
    @cached_property
    def content_lists(self) -> AsyncContentLists:
        return AsyncContentLists(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIpfsUniversalPathsWithRawResponse:
        return AsyncIpfsUniversalPathsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIpfsUniversalPathsWithStreamingResponse:
        return AsyncIpfsUniversalPathsWithStreamingResponse(self)


class IpfsUniversalPathsWithRawResponse:
    def __init__(self, ipfs_universal_paths: IpfsUniversalPaths) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> ContentListsWithRawResponse:
        return ContentListsWithRawResponse(self._ipfs_universal_paths.content_lists)


class AsyncIpfsUniversalPathsWithRawResponse:
    def __init__(self, ipfs_universal_paths: AsyncIpfsUniversalPaths) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> AsyncContentListsWithRawResponse:
        return AsyncContentListsWithRawResponse(self._ipfs_universal_paths.content_lists)


class IpfsUniversalPathsWithStreamingResponse:
    def __init__(self, ipfs_universal_paths: IpfsUniversalPaths) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> ContentListsWithStreamingResponse:
        return ContentListsWithStreamingResponse(self._ipfs_universal_paths.content_lists)


class AsyncIpfsUniversalPathsWithStreamingResponse:
    def __init__(self, ipfs_universal_paths: AsyncIpfsUniversalPaths) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> AsyncContentListsWithStreamingResponse:
        return AsyncContentListsWithStreamingResponse(self._ipfs_universal_paths.content_lists)
