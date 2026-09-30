# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .registries.registries import (
    RegistriesResource,
    AsyncRegistriesResource,
    RegistriesResourceWithRawResponse,
    AsyncRegistriesResourceWithRawResponse,
    RegistriesResourceWithStreamingResponse,
    AsyncRegistriesResourceWithStreamingResponse,
)
from .applications.applications import (
    ApplicationsResource,
    AsyncApplicationsResource,
    ApplicationsResourceWithRawResponse,
    AsyncApplicationsResourceWithRawResponse,
    ApplicationsResourceWithStreamingResponse,
    AsyncApplicationsResourceWithStreamingResponse,
)

__all__ = ["ContainersResource", "AsyncContainersResource"]


class ContainersResource(SyncAPIResource):
    @cached_property
    def applications(self) -> ApplicationsResource:
        return ApplicationsResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def registries(self) -> RegistriesResource:
        return RegistriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContainersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ContainersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContainersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ContainersResourceWithStreamingResponse(self)


class AsyncContainersResource(AsyncAPIResource):
    @cached_property
    def applications(self) -> AsyncApplicationsResource:
        return AsyncApplicationsResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def registries(self) -> AsyncRegistriesResource:
        return AsyncRegistriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContainersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContainersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContainersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncContainersResourceWithStreamingResponse(self)


class ContainersResourceWithRawResponse:
    def __init__(self, containers: ContainersResource) -> None:
        self._containers = containers

    @cached_property
    def applications(self) -> ApplicationsResourceWithRawResponse:
        return ApplicationsResourceWithRawResponse(self._containers.applications)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._containers.images)

    @cached_property
    def registries(self) -> RegistriesResourceWithRawResponse:
        return RegistriesResourceWithRawResponse(self._containers.registries)


class AsyncContainersResourceWithRawResponse:
    def __init__(self, containers: AsyncContainersResource) -> None:
        self._containers = containers

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithRawResponse:
        return AsyncApplicationsResourceWithRawResponse(self._containers.applications)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._containers.images)

    @cached_property
    def registries(self) -> AsyncRegistriesResourceWithRawResponse:
        return AsyncRegistriesResourceWithRawResponse(self._containers.registries)


class ContainersResourceWithStreamingResponse:
    def __init__(self, containers: ContainersResource) -> None:
        self._containers = containers

    @cached_property
    def applications(self) -> ApplicationsResourceWithStreamingResponse:
        return ApplicationsResourceWithStreamingResponse(self._containers.applications)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._containers.images)

    @cached_property
    def registries(self) -> RegistriesResourceWithStreamingResponse:
        return RegistriesResourceWithStreamingResponse(self._containers.registries)


class AsyncContainersResourceWithStreamingResponse:
    def __init__(self, containers: AsyncContainersResource) -> None:
        self._containers = containers

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithStreamingResponse:
        return AsyncApplicationsResourceWithStreamingResponse(self._containers.applications)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._containers.images)

    @cached_property
    def registries(self) -> AsyncRegistriesResourceWithStreamingResponse:
        return AsyncRegistriesResourceWithStreamingResponse(self._containers.registries)
