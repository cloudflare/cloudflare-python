# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sites import (
    Sites,
    AsyncSites,
    SitesWithRawResponse,
    AsyncSitesWithRawResponse,
    SitesWithStreamingResponse,
    AsyncSitesWithStreamingResponse,
)
from .routes import (
    Routes,
    AsyncRoutes,
    RoutesWithRawResponse,
    AsyncRoutesWithRawResponse,
    RoutesWithStreamingResponse,
    AsyncRoutesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .gre_tunnels import (
    GRETunnels,
    AsyncGRETunnels,
    GRETunnelsWithRawResponse,
    AsyncGRETunnelsWithRawResponse,
    GRETunnelsWithStreamingResponse,
    AsyncGRETunnelsWithStreamingResponse,
)
from .sites.sites import Sites, AsyncSites
from .ipsec_tunnels import (
    IPSECTunnels,
    AsyncIPSECTunnels,
    IPSECTunnelsWithRawResponse,
    AsyncIPSECTunnelsWithRawResponse,
    IPSECTunnelsWithStreamingResponse,
    AsyncIPSECTunnelsWithStreamingResponse,
)
from .cf_interconnects import (
    CfInterconnects,
    AsyncCfInterconnects,
    CfInterconnectsWithRawResponse,
    AsyncCfInterconnectsWithRawResponse,
    CfInterconnectsWithStreamingResponse,
    AsyncCfInterconnectsWithStreamingResponse,
)

__all__ = ["MagicTransit", "AsyncMagicTransit"]


class MagicTransit(SyncAPIResource):
    @cached_property
    def cf_interconnects(self) -> CfInterconnects:
        return CfInterconnects(self._client)

    @cached_property
    def gre_tunnels(self) -> GRETunnels:
        return GRETunnels(self._client)

    @cached_property
    def ipsec_tunnels(self) -> IPSECTunnels:
        return IPSECTunnels(self._client)

    @cached_property
    def routes(self) -> Routes:
        return Routes(self._client)

    @cached_property
    def sites(self) -> Sites:
        return Sites(self._client)

    @cached_property
    def with_raw_response(self) -> MagicTransitWithRawResponse:
        return MagicTransitWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MagicTransitWithStreamingResponse:
        return MagicTransitWithStreamingResponse(self)


class AsyncMagicTransit(AsyncAPIResource):
    @cached_property
    def cf_interconnects(self) -> AsyncCfInterconnects:
        return AsyncCfInterconnects(self._client)

    @cached_property
    def gre_tunnels(self) -> AsyncGRETunnels:
        return AsyncGRETunnels(self._client)

    @cached_property
    def ipsec_tunnels(self) -> AsyncIPSECTunnels:
        return AsyncIPSECTunnels(self._client)

    @cached_property
    def routes(self) -> AsyncRoutes:
        return AsyncRoutes(self._client)

    @cached_property
    def sites(self) -> AsyncSites:
        return AsyncSites(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMagicTransitWithRawResponse:
        return AsyncMagicTransitWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMagicTransitWithStreamingResponse:
        return AsyncMagicTransitWithStreamingResponse(self)


class MagicTransitWithRawResponse:
    def __init__(self, magic_transit: MagicTransit) -> None:
        self._magic_transit = magic_transit

    @cached_property
    def cf_interconnects(self) -> CfInterconnectsWithRawResponse:
        return CfInterconnectsWithRawResponse(self._magic_transit.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> GRETunnelsWithRawResponse:
        return GRETunnelsWithRawResponse(self._magic_transit.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> IPSECTunnelsWithRawResponse:
        return IPSECTunnelsWithRawResponse(self._magic_transit.ipsec_tunnels)

    @cached_property
    def routes(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self._magic_transit.routes)

    @cached_property
    def sites(self) -> SitesWithRawResponse:
        return SitesWithRawResponse(self._magic_transit.sites)


class AsyncMagicTransitWithRawResponse:
    def __init__(self, magic_transit: AsyncMagicTransit) -> None:
        self._magic_transit = magic_transit

    @cached_property
    def cf_interconnects(self) -> AsyncCfInterconnectsWithRawResponse:
        return AsyncCfInterconnectsWithRawResponse(self._magic_transit.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> AsyncGRETunnelsWithRawResponse:
        return AsyncGRETunnelsWithRawResponse(self._magic_transit.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> AsyncIPSECTunnelsWithRawResponse:
        return AsyncIPSECTunnelsWithRawResponse(self._magic_transit.ipsec_tunnels)

    @cached_property
    def routes(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self._magic_transit.routes)

    @cached_property
    def sites(self) -> AsyncSitesWithRawResponse:
        return AsyncSitesWithRawResponse(self._magic_transit.sites)


class MagicTransitWithStreamingResponse:
    def __init__(self, magic_transit: MagicTransit) -> None:
        self._magic_transit = magic_transit

    @cached_property
    def cf_interconnects(self) -> CfInterconnectsWithStreamingResponse:
        return CfInterconnectsWithStreamingResponse(self._magic_transit.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> GRETunnelsWithStreamingResponse:
        return GRETunnelsWithStreamingResponse(self._magic_transit.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> IPSECTunnelsWithStreamingResponse:
        return IPSECTunnelsWithStreamingResponse(self._magic_transit.ipsec_tunnels)

    @cached_property
    def routes(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self._magic_transit.routes)

    @cached_property
    def sites(self) -> SitesWithStreamingResponse:
        return SitesWithStreamingResponse(self._magic_transit.sites)


class AsyncMagicTransitWithStreamingResponse:
    def __init__(self, magic_transit: AsyncMagicTransit) -> None:
        self._magic_transit = magic_transit

    @cached_property
    def cf_interconnects(self) -> AsyncCfInterconnectsWithStreamingResponse:
        return AsyncCfInterconnectsWithStreamingResponse(self._magic_transit.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> AsyncGRETunnelsWithStreamingResponse:
        return AsyncGRETunnelsWithStreamingResponse(self._magic_transit.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> AsyncIPSECTunnelsWithStreamingResponse:
        return AsyncIPSECTunnelsWithStreamingResponse(self._magic_transit.ipsec_tunnels)

    @cached_property
    def routes(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self._magic_transit.routes)

    @cached_property
    def sites(self) -> AsyncSitesWithStreamingResponse:
        return AsyncSitesWithStreamingResponse(self._magic_transit.sites)
