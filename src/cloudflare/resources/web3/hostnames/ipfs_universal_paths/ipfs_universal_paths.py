# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .content_lists.content_lists import ContentListsResource, AsyncContentListsResource

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .content_lists import (
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
        return IPFSUniversalPathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPFSUniversalPathsResourceWithStreamingResponse:
        return IPFSUniversalPathsResourceWithStreamingResponse(self)


class AsyncIPFSUniversalPathsResource(AsyncAPIResource):
    @cached_property
    def content_lists(self) -> AsyncContentListsResource:
        return AsyncContentListsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIPFSUniversalPathsResourceWithRawResponse:
        return AsyncIPFSUniversalPathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPFSUniversalPathsResourceWithStreamingResponse:
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
