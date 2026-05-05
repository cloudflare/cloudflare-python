# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .applications import (
    ApplicationsResource,
    AsyncApplicationsResource,
    ApplicationsResourceWithRawResponse,
    AsyncApplicationsResourceWithRawResponse,
    ApplicationsResourceWithStreamingResponse,
    AsyncApplicationsResourceWithStreamingResponse,
)

__all__ = ["ResourceLibraryResource", "AsyncResourceLibraryResource"]


class ResourceLibraryResource(SyncAPIResource):
    @cached_property
    def applications(self) -> ApplicationsResource:
        return ApplicationsResource(self._client)

    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResourceLibraryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ResourceLibraryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceLibraryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ResourceLibraryResourceWithStreamingResponse(self)


class AsyncResourceLibraryResource(AsyncAPIResource):
    @cached_property
    def applications(self) -> AsyncApplicationsResource:
        return AsyncApplicationsResource(self._client)

    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResourceLibraryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResourceLibraryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceLibraryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncResourceLibraryResourceWithStreamingResponse(self)


class ResourceLibraryResourceWithRawResponse:
    def __init__(self, resource_library: ResourceLibraryResource) -> None:
        self._resource_library = resource_library

    @cached_property
    def applications(self) -> ApplicationsResourceWithRawResponse:
        return ApplicationsResourceWithRawResponse(self._resource_library.applications)

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._resource_library.categories)


class AsyncResourceLibraryResourceWithRawResponse:
    def __init__(self, resource_library: AsyncResourceLibraryResource) -> None:
        self._resource_library = resource_library

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithRawResponse:
        return AsyncApplicationsResourceWithRawResponse(self._resource_library.applications)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._resource_library.categories)


class ResourceLibraryResourceWithStreamingResponse:
    def __init__(self, resource_library: ResourceLibraryResource) -> None:
        self._resource_library = resource_library

    @cached_property
    def applications(self) -> ApplicationsResourceWithStreamingResponse:
        return ApplicationsResourceWithStreamingResponse(self._resource_library.applications)

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._resource_library.categories)


class AsyncResourceLibraryResourceWithStreamingResponse:
    def __init__(self, resource_library: AsyncResourceLibraryResource) -> None:
        self._resource_library = resource_library

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithStreamingResponse:
        return AsyncApplicationsResourceWithStreamingResponse(self._resource_library.applications)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._resource_library.categories)
