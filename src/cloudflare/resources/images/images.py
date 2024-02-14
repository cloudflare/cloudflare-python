# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .v1s.v1s import V1s, AsyncV1s

from ..._compat import cached_property

from .v2s.v2s import V2s, AsyncV2s

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .v1s import (
    V1s,
    AsyncV1s,
    V1sWithRawResponse,
    AsyncV1sWithRawResponse,
    V1sWithStreamingResponse,
    AsyncV1sWithStreamingResponse,
)
from .v2s import (
    V2s,
    AsyncV2s,
    V2sWithRawResponse,
    AsyncV2sWithRawResponse,
    V2sWithStreamingResponse,
    AsyncV2sWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Images", "AsyncImages"]


class Images(SyncAPIResource):
    @cached_property
    def v1s(self) -> V1s:
        return V1s(self._client)

    @cached_property
    def v2s(self) -> V2s:
        return V2s(self._client)

    @cached_property
    def with_raw_response(self) -> ImagesWithRawResponse:
        return ImagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesWithStreamingResponse:
        return ImagesWithStreamingResponse(self)


class AsyncImages(AsyncAPIResource):
    @cached_property
    def v1s(self) -> AsyncV1s:
        return AsyncV1s(self._client)

    @cached_property
    def v2s(self) -> AsyncV2s:
        return AsyncV2s(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncImagesWithRawResponse:
        return AsyncImagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesWithStreamingResponse:
        return AsyncImagesWithStreamingResponse(self)


class ImagesWithRawResponse:
    def __init__(self, images: Images) -> None:
        self._images = images

    @cached_property
    def v1s(self) -> V1sWithRawResponse:
        return V1sWithRawResponse(self._images.v1s)

    @cached_property
    def v2s(self) -> V2sWithRawResponse:
        return V2sWithRawResponse(self._images.v2s)


class AsyncImagesWithRawResponse:
    def __init__(self, images: AsyncImages) -> None:
        self._images = images

    @cached_property
    def v1s(self) -> AsyncV1sWithRawResponse:
        return AsyncV1sWithRawResponse(self._images.v1s)

    @cached_property
    def v2s(self) -> AsyncV2sWithRawResponse:
        return AsyncV2sWithRawResponse(self._images.v2s)


class ImagesWithStreamingResponse:
    def __init__(self, images: Images) -> None:
        self._images = images

    @cached_property
    def v1s(self) -> V1sWithStreamingResponse:
        return V1sWithStreamingResponse(self._images.v1s)

    @cached_property
    def v2s(self) -> V2sWithStreamingResponse:
        return V2sWithStreamingResponse(self._images.v2s)


class AsyncImagesWithStreamingResponse:
    def __init__(self, images: AsyncImages) -> None:
        self._images = images

    @cached_property
    def v1s(self) -> AsyncV1sWithStreamingResponse:
        return AsyncV1sWithStreamingResponse(self._images.v1s)

    @cached_property
    def v2s(self) -> AsyncV2sWithStreamingResponse:
        return AsyncV2sWithStreamingResponse(self._images.v2s)
