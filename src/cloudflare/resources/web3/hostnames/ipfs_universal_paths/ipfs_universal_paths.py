# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .content_lists.content_lists import (
    ContentListsResource,
    AsyncContentListsResource,
    ContentListsResourceWithRawResponse,
    AsyncContentListsResourceWithRawResponse,
    ContentListsResourceWithStreamingResponse,
    AsyncContentListsResourceWithStreamingResponse,
)

__all__ = ["IPFSUniversalPathsResource", "AsyncIPFSUniversalPathsResource"]


class IPFSUniversalPathsResource(SyncAPIResource):
    @cached_property
    def content_lists(self) -> ContentListsResource:
        return ContentListsResource(self._client)

    @cached_property
    def with_raw_response(self) -> IPFSUniversalPathsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IPFSUniversalPathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPFSUniversalPathsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IPFSUniversalPathsResourceWithStreamingResponse(self)


class AsyncIPFSUniversalPathsResource(AsyncAPIResource):
    @cached_property
    def content_lists(self) -> AsyncContentListsResource:
        return AsyncContentListsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIPFSUniversalPathsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPFSUniversalPathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPFSUniversalPathsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIPFSUniversalPathsResourceWithStreamingResponse(self)


class IPFSUniversalPathsResourceWithRawResponse:
    def __init__(self, ipfs_universal_paths: IPFSUniversalPathsResource) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> ContentListsResourceWithRawResponse:
        return ContentListsResourceWithRawResponse(self._ipfs_universal_paths.content_lists)


class AsyncIPFSUniversalPathsResourceWithRawResponse:
    def __init__(self, ipfs_universal_paths: AsyncIPFSUniversalPathsResource) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> AsyncContentListsResourceWithRawResponse:
        return AsyncContentListsResourceWithRawResponse(self._ipfs_universal_paths.content_lists)


class IPFSUniversalPathsResourceWithStreamingResponse:
    def __init__(self, ipfs_universal_paths: IPFSUniversalPathsResource) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> ContentListsResourceWithStreamingResponse:
        return ContentListsResourceWithStreamingResponse(self._ipfs_universal_paths.content_lists)


class AsyncIPFSUniversalPathsResourceWithStreamingResponse:
    def __init__(self, ipfs_universal_paths: AsyncIPFSUniversalPathsResource) -> None:
        self._ipfs_universal_paths = ipfs_universal_paths

    @cached_property
    def content_lists(self) -> AsyncContentListsResourceWithStreamingResponse:
        return AsyncContentListsResourceWithStreamingResponse(self._ipfs_universal_paths.content_lists)
