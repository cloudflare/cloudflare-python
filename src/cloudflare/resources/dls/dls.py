# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .regions import (
    RegionsResource,
    AsyncRegionsResource,
    RegionsResourceWithRawResponse,
    AsyncRegionsResourceWithRawResponse,
    RegionsResourceWithStreamingResponse,
    AsyncRegionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .regional_services.regional_services import (
    RegionalServicesResource,
    AsyncRegionalServicesResource,
    RegionalServicesResourceWithRawResponse,
    AsyncRegionalServicesResourceWithRawResponse,
    RegionalServicesResourceWithStreamingResponse,
    AsyncRegionalServicesResourceWithStreamingResponse,
)

__all__ = ["DLSResource", "AsyncDLSResource"]


class DLSResource(SyncAPIResource):
    @cached_property
    def regions(self) -> RegionsResource:
        return RegionsResource(self._client)

    @cached_property
    def regional_services(self) -> RegionalServicesResource:
        return RegionalServicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DLSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DLSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DLSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DLSResourceWithStreamingResponse(self)


class AsyncDLSResource(AsyncAPIResource):
    @cached_property
    def regions(self) -> AsyncRegionsResource:
        return AsyncRegionsResource(self._client)

    @cached_property
    def regional_services(self) -> AsyncRegionalServicesResource:
        return AsyncRegionalServicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDLSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDLSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDLSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDLSResourceWithStreamingResponse(self)


class DLSResourceWithRawResponse:
    def __init__(self, dls: DLSResource) -> None:
        self._dls = dls

    @cached_property
    def regions(self) -> RegionsResourceWithRawResponse:
        return RegionsResourceWithRawResponse(self._dls.regions)

    @cached_property
    def regional_services(self) -> RegionalServicesResourceWithRawResponse:
        return RegionalServicesResourceWithRawResponse(self._dls.regional_services)


class AsyncDLSResourceWithRawResponse:
    def __init__(self, dls: AsyncDLSResource) -> None:
        self._dls = dls

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithRawResponse:
        return AsyncRegionsResourceWithRawResponse(self._dls.regions)

    @cached_property
    def regional_services(self) -> AsyncRegionalServicesResourceWithRawResponse:
        return AsyncRegionalServicesResourceWithRawResponse(self._dls.regional_services)


class DLSResourceWithStreamingResponse:
    def __init__(self, dls: DLSResource) -> None:
        self._dls = dls

    @cached_property
    def regions(self) -> RegionsResourceWithStreamingResponse:
        return RegionsResourceWithStreamingResponse(self._dls.regions)

    @cached_property
    def regional_services(self) -> RegionalServicesResourceWithStreamingResponse:
        return RegionalServicesResourceWithStreamingResponse(self._dls.regional_services)


class AsyncDLSResourceWithStreamingResponse:
    def __init__(self, dls: AsyncDLSResource) -> None:
        self._dls = dls

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithStreamingResponse:
        return AsyncRegionsResourceWithStreamingResponse(self._dls.regions)

    @cached_property
    def regional_services(self) -> AsyncRegionalServicesResourceWithStreamingResponse:
        return AsyncRegionalServicesResourceWithStreamingResponse(self._dls.regional_services)
