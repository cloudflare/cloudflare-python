# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .services import (
    ServicesResource,
    AsyncServicesResource,
    ServicesResourceWithRawResponse,
    AsyncServicesResourceWithRawResponse,
    ServicesResourceWithStreamingResponse,
    AsyncServicesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DirectoryResource", "AsyncDirectoryResource"]


class DirectoryResource(SyncAPIResource):
    @cached_property
    def services(self) -> ServicesResource:
        return ServicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DirectoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DirectoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DirectoryResourceWithStreamingResponse(self)


class AsyncDirectoryResource(AsyncAPIResource):
    @cached_property
    def services(self) -> AsyncServicesResource:
        return AsyncServicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDirectoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDirectoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDirectoryResourceWithStreamingResponse(self)


class DirectoryResourceWithRawResponse:
    def __init__(self, directory: DirectoryResource) -> None:
        self._directory = directory

    @cached_property
    def services(self) -> ServicesResourceWithRawResponse:
        return ServicesResourceWithRawResponse(self._directory.services)


class AsyncDirectoryResourceWithRawResponse:
    def __init__(self, directory: AsyncDirectoryResource) -> None:
        self._directory = directory

    @cached_property
    def services(self) -> AsyncServicesResourceWithRawResponse:
        return AsyncServicesResourceWithRawResponse(self._directory.services)


class DirectoryResourceWithStreamingResponse:
    def __init__(self, directory: DirectoryResource) -> None:
        self._directory = directory

    @cached_property
    def services(self) -> ServicesResourceWithStreamingResponse:
        return ServicesResourceWithStreamingResponse(self._directory.services)


class AsyncDirectoryResourceWithStreamingResponse:
    def __init__(self, directory: AsyncDirectoryResource) -> None:
        self._directory = directory

    @cached_property
    def services(self) -> AsyncServicesResourceWithStreamingResponse:
        return AsyncServicesResourceWithStreamingResponse(self._directory.services)
