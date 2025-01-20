# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .upload import (
    UploadResource,
    AsyncUploadResource,
    UploadResourceWithRawResponse,
    AsyncUploadResourceWithRawResponse,
    UploadResourceWithStreamingResponse,
    AsyncUploadResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def upload(self) -> UploadResource:
        return UploadResource(self._client)

    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AssetsResourceWithStreamingResponse(self)


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def upload(self) -> AsyncUploadResource:
        return AsyncUploadResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAssetsResourceWithStreamingResponse(self)


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

    @cached_property
    def upload(self) -> UploadResourceWithRawResponse:
        return UploadResourceWithRawResponse(self._assets.upload)


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

    @cached_property
    def upload(self) -> AsyncUploadResourceWithRawResponse:
        return AsyncUploadResourceWithRawResponse(self._assets.upload)


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

    @cached_property
    def upload(self) -> UploadResourceWithStreamingResponse:
        return UploadResourceWithStreamingResponse(self._assets.upload)


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

    @cached_property
    def upload(self) -> AsyncUploadResourceWithStreamingResponse:
        return AsyncUploadResourceWithStreamingResponse(self._assets.upload)
