# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .apps import (
    AppsResource,
    AsyncAppsResource,
    AppsResourceWithRawResponse,
    AsyncAppsResourceWithRawResponse,
    AppsResourceWithStreamingResponse,
    AsyncAppsResourceWithStreamingResponse,
)
from .routes import (
    RoutesResource,
    AsyncRoutesResource,
    RoutesResourceWithRawResponse,
    AsyncRoutesResourceWithRawResponse,
    RoutesResourceWithStreamingResponse,
    AsyncRoutesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .gre_tunnels import (
    GRETunnelsResource,
    AsyncGRETunnelsResource,
    GRETunnelsResourceWithRawResponse,
    AsyncGRETunnelsResourceWithRawResponse,
    GRETunnelsResourceWithStreamingResponse,
    AsyncGRETunnelsResourceWithStreamingResponse,
)
from .pcaps.pcaps import (
    PCAPsResource,
    AsyncPCAPsResource,
    PCAPsResourceWithRawResponse,
    AsyncPCAPsResourceWithRawResponse,
    PCAPsResourceWithStreamingResponse,
    AsyncPCAPsResourceWithStreamingResponse,
)
from .sites.sites import (
    SitesResource,
    AsyncSitesResource,
    SitesResourceWithRawResponse,
    AsyncSitesResourceWithRawResponse,
    SitesResourceWithStreamingResponse,
    AsyncSitesResourceWithStreamingResponse,
)
from .ipsec_tunnels import (
    IPSECTunnelsResource,
    AsyncIPSECTunnelsResource,
    IPSECTunnelsResourceWithRawResponse,
    AsyncIPSECTunnelsResourceWithRawResponse,
    IPSECTunnelsResourceWithStreamingResponse,
    AsyncIPSECTunnelsResourceWithStreamingResponse,
)
from .cf_interconnects import (
    CfInterconnectsResource,
    AsyncCfInterconnectsResource,
    CfInterconnectsResourceWithRawResponse,
    AsyncCfInterconnectsResourceWithRawResponse,
    CfInterconnectsResourceWithStreamingResponse,
    AsyncCfInterconnectsResourceWithStreamingResponse,
)
from .connectors.connectors import (
    ConnectorsResource,
    AsyncConnectorsResource,
    ConnectorsResourceWithRawResponse,
    AsyncConnectorsResourceWithRawResponse,
    ConnectorsResourceWithStreamingResponse,
    AsyncConnectorsResourceWithStreamingResponse,
)

__all__ = ["MagicTransitResource", "AsyncMagicTransitResource"]


class MagicTransitResource(SyncAPIResource):
    @cached_property
    def apps(self) -> AppsResource:
        return AppsResource(self._client)

    @cached_property
    def cf_interconnects(self) -> CfInterconnectsResource:
        return CfInterconnectsResource(self._client)

    @cached_property
    def gre_tunnels(self) -> GRETunnelsResource:
        return GRETunnelsResource(self._client)

    @cached_property
    def ipsec_tunnels(self) -> IPSECTunnelsResource:
        return IPSECTunnelsResource(self._client)

    @cached_property
    def routes(self) -> RoutesResource:
        return RoutesResource(self._client)

    @cached_property
    def sites(self) -> SitesResource:
        return SitesResource(self._client)

    @cached_property
    def connectors(self) -> ConnectorsResource:
        return ConnectorsResource(self._client)

    @cached_property
    def pcaps(self) -> PCAPsResource:
        return PCAPsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MagicTransitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MagicTransitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MagicTransitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MagicTransitResourceWithStreamingResponse(self)


class AsyncMagicTransitResource(AsyncAPIResource):
    @cached_property
    def apps(self) -> AsyncAppsResource:
        return AsyncAppsResource(self._client)

    @cached_property
    def cf_interconnects(self) -> AsyncCfInterconnectsResource:
        return AsyncCfInterconnectsResource(self._client)

    @cached_property
    def gre_tunnels(self) -> AsyncGRETunnelsResource:
        return AsyncGRETunnelsResource(self._client)

    @cached_property
    def ipsec_tunnels(self) -> AsyncIPSECTunnelsResource:
        return AsyncIPSECTunnelsResource(self._client)

    @cached_property
    def routes(self) -> AsyncRoutesResource:
        return AsyncRoutesResource(self._client)

    @cached_property
    def sites(self) -> AsyncSitesResource:
        return AsyncSitesResource(self._client)

    @cached_property
    def connectors(self) -> AsyncConnectorsResource:
        return AsyncConnectorsResource(self._client)

    @cached_property
    def pcaps(self) -> AsyncPCAPsResource:
        return AsyncPCAPsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMagicTransitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMagicTransitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMagicTransitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMagicTransitResourceWithStreamingResponse(self)


class MagicTransitResourceWithRawResponse:
    def __init__(self, magic_transit: MagicTransitResource) -> None:
        self._magic_transit = magic_transit

    @cached_property
    def apps(self) -> AppsResourceWithRawResponse:
        return AppsResourceWithRawResponse(self._magic_transit.apps)

    @cached_property
    def cf_interconnects(self) -> CfInterconnectsResourceWithRawResponse:
        return CfInterconnectsResourceWithRawResponse(self._magic_transit.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> GRETunnelsResourceWithRawResponse:
        return GRETunnelsResourceWithRawResponse(self._magic_transit.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> IPSECTunnelsResourceWithRawResponse:
        return IPSECTunnelsResourceWithRawResponse(self._magic_transit.ipsec_tunnels)

    @cached_property
    def routes(self) -> RoutesResourceWithRawResponse:
        return RoutesResourceWithRawResponse(self._magic_transit.routes)

    @cached_property
    def sites(self) -> SitesResourceWithRawResponse:
        return SitesResourceWithRawResponse(self._magic_transit.sites)

    @cached_property
    def connectors(self) -> ConnectorsResourceWithRawResponse:
        return ConnectorsResourceWithRawResponse(self._magic_transit.connectors)

    @cached_property
    def pcaps(self) -> PCAPsResourceWithRawResponse:
        return PCAPsResourceWithRawResponse(self._magic_transit.pcaps)


class AsyncMagicTransitResourceWithRawResponse:
    def __init__(self, magic_transit: AsyncMagicTransitResource) -> None:
        self._magic_transit = magic_transit

    @cached_property
    def apps(self) -> AsyncAppsResourceWithRawResponse:
        return AsyncAppsResourceWithRawResponse(self._magic_transit.apps)

    @cached_property
    def cf_interconnects(self) -> AsyncCfInterconnectsResourceWithRawResponse:
        return AsyncCfInterconnectsResourceWithRawResponse(self._magic_transit.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> AsyncGRETunnelsResourceWithRawResponse:
        return AsyncGRETunnelsResourceWithRawResponse(self._magic_transit.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> AsyncIPSECTunnelsResourceWithRawResponse:
        return AsyncIPSECTunnelsResourceWithRawResponse(self._magic_transit.ipsec_tunnels)

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithRawResponse:
        return AsyncRoutesResourceWithRawResponse(self._magic_transit.routes)

    @cached_property
    def sites(self) -> AsyncSitesResourceWithRawResponse:
        return AsyncSitesResourceWithRawResponse(self._magic_transit.sites)

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithRawResponse:
        return AsyncConnectorsResourceWithRawResponse(self._magic_transit.connectors)

    @cached_property
    def pcaps(self) -> AsyncPCAPsResourceWithRawResponse:
        return AsyncPCAPsResourceWithRawResponse(self._magic_transit.pcaps)


class MagicTransitResourceWithStreamingResponse:
    def __init__(self, magic_transit: MagicTransitResource) -> None:
        self._magic_transit = magic_transit

    @cached_property
    def apps(self) -> AppsResourceWithStreamingResponse:
        return AppsResourceWithStreamingResponse(self._magic_transit.apps)

    @cached_property
    def cf_interconnects(self) -> CfInterconnectsResourceWithStreamingResponse:
        return CfInterconnectsResourceWithStreamingResponse(self._magic_transit.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> GRETunnelsResourceWithStreamingResponse:
        return GRETunnelsResourceWithStreamingResponse(self._magic_transit.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> IPSECTunnelsResourceWithStreamingResponse:
        return IPSECTunnelsResourceWithStreamingResponse(self._magic_transit.ipsec_tunnels)

    @cached_property
    def routes(self) -> RoutesResourceWithStreamingResponse:
        return RoutesResourceWithStreamingResponse(self._magic_transit.routes)

    @cached_property
    def sites(self) -> SitesResourceWithStreamingResponse:
        return SitesResourceWithStreamingResponse(self._magic_transit.sites)

    @cached_property
    def connectors(self) -> ConnectorsResourceWithStreamingResponse:
        return ConnectorsResourceWithStreamingResponse(self._magic_transit.connectors)

    @cached_property
    def pcaps(self) -> PCAPsResourceWithStreamingResponse:
        return PCAPsResourceWithStreamingResponse(self._magic_transit.pcaps)


class AsyncMagicTransitResourceWithStreamingResponse:
    def __init__(self, magic_transit: AsyncMagicTransitResource) -> None:
        self._magic_transit = magic_transit

    @cached_property
    def apps(self) -> AsyncAppsResourceWithStreamingResponse:
        return AsyncAppsResourceWithStreamingResponse(self._magic_transit.apps)

    @cached_property
    def cf_interconnects(self) -> AsyncCfInterconnectsResourceWithStreamingResponse:
        return AsyncCfInterconnectsResourceWithStreamingResponse(self._magic_transit.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> AsyncGRETunnelsResourceWithStreamingResponse:
        return AsyncGRETunnelsResourceWithStreamingResponse(self._magic_transit.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> AsyncIPSECTunnelsResourceWithStreamingResponse:
        return AsyncIPSECTunnelsResourceWithStreamingResponse(self._magic_transit.ipsec_tunnels)

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithStreamingResponse:
        return AsyncRoutesResourceWithStreamingResponse(self._magic_transit.routes)

    @cached_property
    def sites(self) -> AsyncSitesResourceWithStreamingResponse:
        return AsyncSitesResourceWithStreamingResponse(self._magic_transit.sites)

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithStreamingResponse:
        return AsyncConnectorsResourceWithStreamingResponse(self._magic_transit.connectors)

    @cached_property
    def pcaps(self) -> AsyncPCAPsResourceWithStreamingResponse:
        return AsyncPCAPsResourceWithStreamingResponse(self._magic_transit.pcaps)
