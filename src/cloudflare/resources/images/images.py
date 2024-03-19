# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1 import (
    V1,
    AsyncV1,
    V1WithRawResponse,
    AsyncV1WithRawResponse,
    V1WithStreamingResponse,
    AsyncV1WithStreamingResponse,
)
from .v2 import (
    V2,
    AsyncV2,
    V2WithRawResponse,
    AsyncV2WithRawResponse,
    V2WithStreamingResponse,
    AsyncV2WithStreamingResponse,
)
from .v1.v1 import V1, AsyncV1
from .v2.v2 import V2, AsyncV2
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Images", "AsyncImages"]


class Images(SyncAPIResource):
    @cached_property
    def v1(self) -> V1:
        return V1(self._client)

    @cached_property
    def v2(self) -> V2:
        return V2(self._client)

    @cached_property
    def with_raw_response(self) -> ImagesWithRawResponse:
        return ImagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesWithStreamingResponse:
        return ImagesWithStreamingResponse(self)


class AsyncImages(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1:
        return AsyncV1(self._client)

    @cached_property
    def v2(self) -> AsyncV2:
        return AsyncV2(self._client)

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
    def v1(self) -> V1WithRawResponse:
        return V1WithRawResponse(self._images.v1)

    @cached_property
    def v2(self) -> V2WithRawResponse:
        return V2WithRawResponse(self._images.v2)


class AsyncImagesWithRawResponse:
    def __init__(self, images: AsyncImages) -> None:
        self._images = images

    @cached_property
    def v1(self) -> AsyncV1WithRawResponse:
        return AsyncV1WithRawResponse(self._images.v1)

    @cached_property
    def v2(self) -> AsyncV2WithRawResponse:
        return AsyncV2WithRawResponse(self._images.v2)


class ImagesWithStreamingResponse:
    def __init__(self, images: Images) -> None:
        self._images = images

    @cached_property
    def v1(self) -> V1WithStreamingResponse:
        return V1WithStreamingResponse(self._images.v1)

    @cached_property
    def v2(self) -> V2WithStreamingResponse:
        return V2WithStreamingResponse(self._images.v2)


class AsyncImagesWithStreamingResponse:
    def __init__(self, images: AsyncImages) -> None:
        self._images = images

    @cached_property
    def v1(self) -> AsyncV1WithStreamingResponse:
        return AsyncV1WithStreamingResponse(self._images.v1)

    @cached_property
    def v2(self) -> AsyncV2WithStreamingResponse:
        return AsyncV2WithStreamingResponse(self._images.v2)
