# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .directory.directory import (
    DirectoryResource,
    AsyncDirectoryResource,
    DirectoryResourceWithRawResponse,
    AsyncDirectoryResourceWithRawResponse,
    DirectoryResourceWithStreamingResponse,
    AsyncDirectoryResourceWithStreamingResponse,
)

__all__ = ["ConnectivityResource", "AsyncConnectivityResource"]


class ConnectivityResource(SyncAPIResource):
    @cached_property
    def directory(self) -> DirectoryResource:
        return DirectoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ConnectivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ConnectivityResourceWithStreamingResponse(self)


class AsyncConnectivityResource(AsyncAPIResource):
    @cached_property
    def directory(self) -> AsyncDirectoryResource:
        return AsyncDirectoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncConnectivityResourceWithStreamingResponse(self)


class ConnectivityResourceWithRawResponse:
    def __init__(self, connectivity: ConnectivityResource) -> None:
        self._connectivity = connectivity

    @cached_property
    def directory(self) -> DirectoryResourceWithRawResponse:
        return DirectoryResourceWithRawResponse(self._connectivity.directory)


class AsyncConnectivityResourceWithRawResponse:
    def __init__(self, connectivity: AsyncConnectivityResource) -> None:
        self._connectivity = connectivity

    @cached_property
    def directory(self) -> AsyncDirectoryResourceWithRawResponse:
        return AsyncDirectoryResourceWithRawResponse(self._connectivity.directory)


class ConnectivityResourceWithStreamingResponse:
    def __init__(self, connectivity: ConnectivityResource) -> None:
        self._connectivity = connectivity

    @cached_property
    def directory(self) -> DirectoryResourceWithStreamingResponse:
        return DirectoryResourceWithStreamingResponse(self._connectivity.directory)


class AsyncConnectivityResourceWithStreamingResponse:
    def __init__(self, connectivity: AsyncConnectivityResource) -> None:
        self._connectivity = connectivity

    @cached_property
    def directory(self) -> AsyncDirectoryResourceWithStreamingResponse:
        return AsyncDirectoryResourceWithStreamingResponse(self._connectivity.directory)
