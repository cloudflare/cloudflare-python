# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .resources import (
    ResourcesResource,
    AsyncResourcesResource,
    ResourcesResourceWithRawResponse,
    AsyncResourcesResourceWithRawResponse,
    ResourcesResourceWithStreamingResponse,
    AsyncResourcesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .on_ramps.on_ramps import (
    OnRampsResource,
    AsyncOnRampsResource,
    OnRampsResourceWithRawResponse,
    AsyncOnRampsResourceWithRawResponse,
    OnRampsResourceWithStreamingResponse,
    AsyncOnRampsResourceWithStreamingResponse,
)
from .cloud_integrations import (
    CloudIntegrationsResource,
    AsyncCloudIntegrationsResource,
    CloudIntegrationsResourceWithRawResponse,
    AsyncCloudIntegrationsResourceWithRawResponse,
    CloudIntegrationsResourceWithStreamingResponse,
    AsyncCloudIntegrationsResourceWithStreamingResponse,
)
from .catalog_syncs.catalog_syncs import (
    CatalogSyncsResource,
    AsyncCatalogSyncsResource,
    CatalogSyncsResourceWithRawResponse,
    AsyncCatalogSyncsResourceWithRawResponse,
    CatalogSyncsResourceWithStreamingResponse,
    AsyncCatalogSyncsResourceWithStreamingResponse,
)

__all__ = ["MagicCloudNetworkingResource", "AsyncMagicCloudNetworkingResource"]


class MagicCloudNetworkingResource(SyncAPIResource):
    @cached_property
    def catalog_syncs(self) -> CatalogSyncsResource:
        return CatalogSyncsResource(self._client)

    @cached_property
    def on_ramps(self) -> OnRampsResource:
        return OnRampsResource(self._client)

    @cached_property
    def cloud_integrations(self) -> CloudIntegrationsResource:
        return CloudIntegrationsResource(self._client)

    @cached_property
    def resources(self) -> ResourcesResource:
        return ResourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MagicCloudNetworkingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MagicCloudNetworkingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MagicCloudNetworkingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MagicCloudNetworkingResourceWithStreamingResponse(self)


class AsyncMagicCloudNetworkingResource(AsyncAPIResource):
    @cached_property
    def catalog_syncs(self) -> AsyncCatalogSyncsResource:
        return AsyncCatalogSyncsResource(self._client)

    @cached_property
    def on_ramps(self) -> AsyncOnRampsResource:
        return AsyncOnRampsResource(self._client)

    @cached_property
    def cloud_integrations(self) -> AsyncCloudIntegrationsResource:
        return AsyncCloudIntegrationsResource(self._client)

    @cached_property
    def resources(self) -> AsyncResourcesResource:
        return AsyncResourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMagicCloudNetworkingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMagicCloudNetworkingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMagicCloudNetworkingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMagicCloudNetworkingResourceWithStreamingResponse(self)


class MagicCloudNetworkingResourceWithRawResponse:
    def __init__(self, magic_cloud_networking: MagicCloudNetworkingResource) -> None:
        self._magic_cloud_networking = magic_cloud_networking

    @cached_property
    def catalog_syncs(self) -> CatalogSyncsResourceWithRawResponse:
        return CatalogSyncsResourceWithRawResponse(self._magic_cloud_networking.catalog_syncs)

    @cached_property
    def on_ramps(self) -> OnRampsResourceWithRawResponse:
        return OnRampsResourceWithRawResponse(self._magic_cloud_networking.on_ramps)

    @cached_property
    def cloud_integrations(self) -> CloudIntegrationsResourceWithRawResponse:
        return CloudIntegrationsResourceWithRawResponse(self._magic_cloud_networking.cloud_integrations)

    @cached_property
    def resources(self) -> ResourcesResourceWithRawResponse:
        return ResourcesResourceWithRawResponse(self._magic_cloud_networking.resources)


class AsyncMagicCloudNetworkingResourceWithRawResponse:
    def __init__(self, magic_cloud_networking: AsyncMagicCloudNetworkingResource) -> None:
        self._magic_cloud_networking = magic_cloud_networking

    @cached_property
    def catalog_syncs(self) -> AsyncCatalogSyncsResourceWithRawResponse:
        return AsyncCatalogSyncsResourceWithRawResponse(self._magic_cloud_networking.catalog_syncs)

    @cached_property
    def on_ramps(self) -> AsyncOnRampsResourceWithRawResponse:
        return AsyncOnRampsResourceWithRawResponse(self._magic_cloud_networking.on_ramps)

    @cached_property
    def cloud_integrations(self) -> AsyncCloudIntegrationsResourceWithRawResponse:
        return AsyncCloudIntegrationsResourceWithRawResponse(self._magic_cloud_networking.cloud_integrations)

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithRawResponse:
        return AsyncResourcesResourceWithRawResponse(self._magic_cloud_networking.resources)


class MagicCloudNetworkingResourceWithStreamingResponse:
    def __init__(self, magic_cloud_networking: MagicCloudNetworkingResource) -> None:
        self._magic_cloud_networking = magic_cloud_networking

    @cached_property
    def catalog_syncs(self) -> CatalogSyncsResourceWithStreamingResponse:
        return CatalogSyncsResourceWithStreamingResponse(self._magic_cloud_networking.catalog_syncs)

    @cached_property
    def on_ramps(self) -> OnRampsResourceWithStreamingResponse:
        return OnRampsResourceWithStreamingResponse(self._magic_cloud_networking.on_ramps)

    @cached_property
    def cloud_integrations(self) -> CloudIntegrationsResourceWithStreamingResponse:
        return CloudIntegrationsResourceWithStreamingResponse(self._magic_cloud_networking.cloud_integrations)

    @cached_property
    def resources(self) -> ResourcesResourceWithStreamingResponse:
        return ResourcesResourceWithStreamingResponse(self._magic_cloud_networking.resources)


class AsyncMagicCloudNetworkingResourceWithStreamingResponse:
    def __init__(self, magic_cloud_networking: AsyncMagicCloudNetworkingResource) -> None:
        self._magic_cloud_networking = magic_cloud_networking

    @cached_property
    def catalog_syncs(self) -> AsyncCatalogSyncsResourceWithStreamingResponse:
        return AsyncCatalogSyncsResourceWithStreamingResponse(self._magic_cloud_networking.catalog_syncs)

    @cached_property
    def on_ramps(self) -> AsyncOnRampsResourceWithStreamingResponse:
        return AsyncOnRampsResourceWithStreamingResponse(self._magic_cloud_networking.on_ramps)

    @cached_property
    def cloud_integrations(self) -> AsyncCloudIntegrationsResourceWithStreamingResponse:
        return AsyncCloudIntegrationsResourceWithStreamingResponse(self._magic_cloud_networking.cloud_integrations)

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithStreamingResponse:
        return AsyncResourcesResourceWithStreamingResponse(self._magic_cloud_networking.resources)
