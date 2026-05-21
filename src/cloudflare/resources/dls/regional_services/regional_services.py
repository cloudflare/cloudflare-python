# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .prefix_bindings import (
    PrefixBindingsResource,
    AsyncPrefixBindingsResource,
    PrefixBindingsResourceWithRawResponse,
    AsyncPrefixBindingsResourceWithRawResponse,
    PrefixBindingsResourceWithStreamingResponse,
    AsyncPrefixBindingsResourceWithStreamingResponse,
)

__all__ = ["RegionalServicesResource", "AsyncRegionalServicesResource"]


class RegionalServicesResource(SyncAPIResource):
    @cached_property
    def prefix_bindings(self) -> PrefixBindingsResource:
        return PrefixBindingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RegionalServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegionalServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionalServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegionalServicesResourceWithStreamingResponse(self)


class AsyncRegionalServicesResource(AsyncAPIResource):
    @cached_property
    def prefix_bindings(self) -> AsyncPrefixBindingsResource:
        return AsyncPrefixBindingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRegionalServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegionalServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionalServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegionalServicesResourceWithStreamingResponse(self)


class RegionalServicesResourceWithRawResponse:
    def __init__(self, regional_services: RegionalServicesResource) -> None:
        self._regional_services = regional_services

    @cached_property
    def prefix_bindings(self) -> PrefixBindingsResourceWithRawResponse:
        return PrefixBindingsResourceWithRawResponse(self._regional_services.prefix_bindings)


class AsyncRegionalServicesResourceWithRawResponse:
    def __init__(self, regional_services: AsyncRegionalServicesResource) -> None:
        self._regional_services = regional_services

    @cached_property
    def prefix_bindings(self) -> AsyncPrefixBindingsResourceWithRawResponse:
        return AsyncPrefixBindingsResourceWithRawResponse(self._regional_services.prefix_bindings)


class RegionalServicesResourceWithStreamingResponse:
    def __init__(self, regional_services: RegionalServicesResource) -> None:
        self._regional_services = regional_services

    @cached_property
    def prefix_bindings(self) -> PrefixBindingsResourceWithStreamingResponse:
        return PrefixBindingsResourceWithStreamingResponse(self._regional_services.prefix_bindings)


class AsyncRegionalServicesResourceWithStreamingResponse:
    def __init__(self, regional_services: AsyncRegionalServicesResource) -> None:
        self._regional_services = regional_services

    @cached_property
    def prefix_bindings(self) -> AsyncPrefixBindingsResourceWithStreamingResponse:
        return AsyncPrefixBindingsResourceWithStreamingResponse(self._regional_services.prefix_bindings)
