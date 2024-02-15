# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

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
    GreTunnels,
    AsyncGreTunnels,
    GreTunnelsWithRawResponse,
    AsyncGreTunnelsWithRawResponse,
    GreTunnelsWithStreamingResponse,
    AsyncGreTunnelsWithStreamingResponse,
)
from .ipsec_tunnels import (
    IpsecTunnels,
    AsyncIpsecTunnels,
    IpsecTunnelsWithRawResponse,
    AsyncIpsecTunnelsWithRawResponse,
    IpsecTunnelsWithStreamingResponse,
    AsyncIpsecTunnelsWithStreamingResponse,
)
from .cf_interconnects import (
    CfInterconnects,
    AsyncCfInterconnects,
    CfInterconnectsWithRawResponse,
    AsyncCfInterconnectsWithRawResponse,
    CfInterconnectsWithStreamingResponse,
    AsyncCfInterconnectsWithStreamingResponse,
)
from .ipsec_tunnels.ipsec_tunnels import IpsecTunnels, AsyncIpsecTunnels

__all__ = ["Magics", "AsyncMagics"]


class Magics(SyncAPIResource):
    @cached_property
    def cf_interconnects(self) -> CfInterconnects:
        return CfInterconnects(self._client)

    @cached_property
    def gre_tunnels(self) -> GreTunnels:
        return GreTunnels(self._client)

    @cached_property
    def ipsec_tunnels(self) -> IpsecTunnels:
        return IpsecTunnels(self._client)

    @cached_property
    def routes(self) -> Routes:
        return Routes(self._client)

    @cached_property
    def with_raw_response(self) -> MagicsWithRawResponse:
        return MagicsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MagicsWithStreamingResponse:
        return MagicsWithStreamingResponse(self)


class AsyncMagics(AsyncAPIResource):
    @cached_property
    def cf_interconnects(self) -> AsyncCfInterconnects:
        return AsyncCfInterconnects(self._client)

    @cached_property
    def gre_tunnels(self) -> AsyncGreTunnels:
        return AsyncGreTunnels(self._client)

    @cached_property
    def ipsec_tunnels(self) -> AsyncIpsecTunnels:
        return AsyncIpsecTunnels(self._client)

    @cached_property
    def routes(self) -> AsyncRoutes:
        return AsyncRoutes(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMagicsWithRawResponse:
        return AsyncMagicsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMagicsWithStreamingResponse:
        return AsyncMagicsWithStreamingResponse(self)


class MagicsWithRawResponse:
    def __init__(self, magics: Magics) -> None:
        self._magics = magics

    @cached_property
    def cf_interconnects(self) -> CfInterconnectsWithRawResponse:
        return CfInterconnectsWithRawResponse(self._magics.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> GreTunnelsWithRawResponse:
        return GreTunnelsWithRawResponse(self._magics.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> IpsecTunnelsWithRawResponse:
        return IpsecTunnelsWithRawResponse(self._magics.ipsec_tunnels)

    @cached_property
    def routes(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self._magics.routes)


class AsyncMagicsWithRawResponse:
    def __init__(self, magics: AsyncMagics) -> None:
        self._magics = magics

    @cached_property
    def cf_interconnects(self) -> AsyncCfInterconnectsWithRawResponse:
        return AsyncCfInterconnectsWithRawResponse(self._magics.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> AsyncGreTunnelsWithRawResponse:
        return AsyncGreTunnelsWithRawResponse(self._magics.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> AsyncIpsecTunnelsWithRawResponse:
        return AsyncIpsecTunnelsWithRawResponse(self._magics.ipsec_tunnels)

    @cached_property
    def routes(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self._magics.routes)


class MagicsWithStreamingResponse:
    def __init__(self, magics: Magics) -> None:
        self._magics = magics

    @cached_property
    def cf_interconnects(self) -> CfInterconnectsWithStreamingResponse:
        return CfInterconnectsWithStreamingResponse(self._magics.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> GreTunnelsWithStreamingResponse:
        return GreTunnelsWithStreamingResponse(self._magics.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> IpsecTunnelsWithStreamingResponse:
        return IpsecTunnelsWithStreamingResponse(self._magics.ipsec_tunnels)

    @cached_property
    def routes(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self._magics.routes)


class AsyncMagicsWithStreamingResponse:
    def __init__(self, magics: AsyncMagics) -> None:
        self._magics = magics

    @cached_property
    def cf_interconnects(self) -> AsyncCfInterconnectsWithStreamingResponse:
        return AsyncCfInterconnectsWithStreamingResponse(self._magics.cf_interconnects)

    @cached_property
    def gre_tunnels(self) -> AsyncGreTunnelsWithStreamingResponse:
        return AsyncGreTunnelsWithStreamingResponse(self._magics.gre_tunnels)

    @cached_property
    def ipsec_tunnels(self) -> AsyncIpsecTunnelsWithStreamingResponse:
        return AsyncIpsecTunnelsWithStreamingResponse(self._magics.ipsec_tunnels)

    @cached_property
    def routes(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self._magics.routes)
