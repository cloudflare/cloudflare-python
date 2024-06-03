# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .app_configuration import (
    AppConfigurationResource,
    AsyncAppConfigurationResource,
    AppConfigurationResourceWithRawResponse,
    AsyncAppConfigurationResourceWithRawResponse,
    AppConfigurationResourceWithStreamingResponse,
    AsyncAppConfigurationResourceWithStreamingResponse,
)

__all__ = ["SitesResource", "AsyncSitesResource"]


class SitesResource(SyncAPIResource):
    @cached_property
    def app_configuration(self) -> AppConfigurationResource:
        return AppConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> SitesResourceWithRawResponse:
        return SitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SitesResourceWithStreamingResponse:
        return SitesResourceWithStreamingResponse(self)


class AsyncSitesResource(AsyncAPIResource):
    @cached_property
    def app_configuration(self) -> AsyncAppConfigurationResource:
        return AsyncAppConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSitesResourceWithRawResponse:
        return AsyncSitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSitesResourceWithStreamingResponse:
        return AsyncSitesResourceWithStreamingResponse(self)


class SitesResourceWithRawResponse:
    def __init__(self, sites: SitesResource) -> None:
        self._sites = sites

    @cached_property
    def app_configuration(self) -> AppConfigurationResourceWithRawResponse:
        return AppConfigurationResourceWithRawResponse(self._sites.app_configuration)


class AsyncSitesResourceWithRawResponse:
    def __init__(self, sites: AsyncSitesResource) -> None:
        self._sites = sites

    @cached_property
    def app_configuration(self) -> AsyncAppConfigurationResourceWithRawResponse:
        return AsyncAppConfigurationResourceWithRawResponse(self._sites.app_configuration)


class SitesResourceWithStreamingResponse:
    def __init__(self, sites: SitesResource) -> None:
        self._sites = sites

    @cached_property
    def app_configuration(self) -> AppConfigurationResourceWithStreamingResponse:
        return AppConfigurationResourceWithStreamingResponse(self._sites.app_configuration)


class AsyncSitesResourceWithStreamingResponse:
    def __init__(self, sites: AsyncSitesResource) -> None:
        self._sites = sites

    @cached_property
    def app_configuration(self) -> AsyncAppConfigurationResourceWithStreamingResponse:
        return AsyncAppConfigurationResourceWithStreamingResponse(self._sites.app_configuration)
