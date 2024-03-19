# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .dex import (
    DEX,
    AsyncDEX,
    DEXWithRawResponse,
    AsyncDEXWithRawResponse,
    DEXWithStreamingResponse,
    AsyncDEXWithStreamingResponse,
)
from .dlp import (
    DLP,
    AsyncDLP,
    DLPWithRawResponse,
    AsyncDLPWithRawResponse,
    DLPWithStreamingResponse,
    AsyncDLPWithStreamingResponse,
)
from .seats import (
    Seats,
    AsyncSeats,
    SeatsWithRawResponse,
    AsyncSeatsWithRawResponse,
    SeatsWithStreamingResponse,
    AsyncSeatsWithStreamingResponse,
)
from .access import (
    Access,
    AsyncAccess,
    AccessWithRawResponse,
    AsyncAccessWithRawResponse,
    AccessWithStreamingResponse,
    AsyncAccessWithStreamingResponse,
)
from .devices import (
    Devices,
    AsyncDevices,
    DevicesWithRawResponse,
    AsyncDevicesWithRawResponse,
    DevicesWithStreamingResponse,
    AsyncDevicesWithStreamingResponse,
)
from .dex.dex import DEX, AsyncDEX
from .dlp.dlp import DLP, AsyncDLP
from .gateway import (
    Gateway,
    AsyncGateway,
    GatewayWithRawResponse,
    AsyncGatewayWithRawResponse,
    GatewayWithStreamingResponse,
    AsyncGatewayWithStreamingResponse,
)
from .tunnels import (
    Tunnels,
    AsyncTunnels,
    TunnelsWithRawResponse,
    AsyncTunnelsWithRawResponse,
    TunnelsWithStreamingResponse,
    AsyncTunnelsWithStreamingResponse,
)
from .networks import (
    Networks,
    AsyncNetworks,
    NetworksWithRawResponse,
    AsyncNetworksWithRawResponse,
    NetworksWithStreamingResponse,
    AsyncNetworksWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .access.access import Access, AsyncAccess
from .organizations import (
    Organizations,
    AsyncOrganizations,
    OrganizationsWithRawResponse,
    AsyncOrganizationsWithRawResponse,
    OrganizationsWithStreamingResponse,
    AsyncOrganizationsWithStreamingResponse,
)
from .devices.devices import Devices, AsyncDevices
from .gateway.gateway import Gateway, AsyncGateway
from .tunnels.tunnels import Tunnels, AsyncTunnels
from .networks.networks import Networks, AsyncNetworks
from .identity_providers import (
    IdentityProviders,
    AsyncIdentityProviders,
    IdentityProvidersWithRawResponse,
    AsyncIdentityProvidersWithRawResponse,
    IdentityProvidersWithStreamingResponse,
    AsyncIdentityProvidersWithStreamingResponse,
)
from .connectivity_settings import (
    ConnectivitySettings,
    AsyncConnectivitySettings,
    ConnectivitySettingsWithRawResponse,
    AsyncConnectivitySettingsWithRawResponse,
    ConnectivitySettingsWithStreamingResponse,
    AsyncConnectivitySettingsWithStreamingResponse,
)

__all__ = ["ZeroTrust", "AsyncZeroTrust"]


class ZeroTrust(SyncAPIResource):
    @cached_property
    def devices(self) -> Devices:
        return Devices(self._client)

    @cached_property
    def identity_providers(self) -> IdentityProviders:
        return IdentityProviders(self._client)

    @cached_property
    def organizations(self) -> Organizations:
        return Organizations(self._client)

    @cached_property
    def seats(self) -> Seats:
        return Seats(self._client)

    @cached_property
    def access(self) -> Access:
        return Access(self._client)

    @cached_property
    def dex(self) -> DEX:
        return DEX(self._client)

    @cached_property
    def tunnels(self) -> Tunnels:
        return Tunnels(self._client)

    @cached_property
    def connectivity_settings(self) -> ConnectivitySettings:
        return ConnectivitySettings(self._client)

    @cached_property
    def dlp(self) -> DLP:
        return DLP(self._client)

    @cached_property
    def gateway(self) -> Gateway:
        return Gateway(self._client)

    @cached_property
    def networks(self) -> Networks:
        return Networks(self._client)

    @cached_property
    def with_raw_response(self) -> ZeroTrustWithRawResponse:
        return ZeroTrustWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZeroTrustWithStreamingResponse:
        return ZeroTrustWithStreamingResponse(self)


class AsyncZeroTrust(AsyncAPIResource):
    @cached_property
    def devices(self) -> AsyncDevices:
        return AsyncDevices(self._client)

    @cached_property
    def identity_providers(self) -> AsyncIdentityProviders:
        return AsyncIdentityProviders(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizations:
        return AsyncOrganizations(self._client)

    @cached_property
    def seats(self) -> AsyncSeats:
        return AsyncSeats(self._client)

    @cached_property
    def access(self) -> AsyncAccess:
        return AsyncAccess(self._client)

    @cached_property
    def dex(self) -> AsyncDEX:
        return AsyncDEX(self._client)

    @cached_property
    def tunnels(self) -> AsyncTunnels:
        return AsyncTunnels(self._client)

    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettings:
        return AsyncConnectivitySettings(self._client)

    @cached_property
    def dlp(self) -> AsyncDLP:
        return AsyncDLP(self._client)

    @cached_property
    def gateway(self) -> AsyncGateway:
        return AsyncGateway(self._client)

    @cached_property
    def networks(self) -> AsyncNetworks:
        return AsyncNetworks(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZeroTrustWithRawResponse:
        return AsyncZeroTrustWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZeroTrustWithStreamingResponse:
        return AsyncZeroTrustWithStreamingResponse(self)


class ZeroTrustWithRawResponse:
    def __init__(self, zero_trust: ZeroTrust) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def devices(self) -> DevicesWithRawResponse:
        return DevicesWithRawResponse(self._zero_trust.devices)

    @cached_property
    def identity_providers(self) -> IdentityProvidersWithRawResponse:
        return IdentityProvidersWithRawResponse(self._zero_trust.identity_providers)

    @cached_property
    def organizations(self) -> OrganizationsWithRawResponse:
        return OrganizationsWithRawResponse(self._zero_trust.organizations)

    @cached_property
    def seats(self) -> SeatsWithRawResponse:
        return SeatsWithRawResponse(self._zero_trust.seats)

    @cached_property
    def access(self) -> AccessWithRawResponse:
        return AccessWithRawResponse(self._zero_trust.access)

    @cached_property
    def dex(self) -> DEXWithRawResponse:
        return DEXWithRawResponse(self._zero_trust.dex)

    @cached_property
    def tunnels(self) -> TunnelsWithRawResponse:
        return TunnelsWithRawResponse(self._zero_trust.tunnels)

    @cached_property
    def connectivity_settings(self) -> ConnectivitySettingsWithRawResponse:
        return ConnectivitySettingsWithRawResponse(self._zero_trust.connectivity_settings)

    @cached_property
    def dlp(self) -> DLPWithRawResponse:
        return DLPWithRawResponse(self._zero_trust.dlp)

    @cached_property
    def gateway(self) -> GatewayWithRawResponse:
        return GatewayWithRawResponse(self._zero_trust.gateway)

    @cached_property
    def networks(self) -> NetworksWithRawResponse:
        return NetworksWithRawResponse(self._zero_trust.networks)


class AsyncZeroTrustWithRawResponse:
    def __init__(self, zero_trust: AsyncZeroTrust) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def devices(self) -> AsyncDevicesWithRawResponse:
        return AsyncDevicesWithRawResponse(self._zero_trust.devices)

    @cached_property
    def identity_providers(self) -> AsyncIdentityProvidersWithRawResponse:
        return AsyncIdentityProvidersWithRawResponse(self._zero_trust.identity_providers)

    @cached_property
    def organizations(self) -> AsyncOrganizationsWithRawResponse:
        return AsyncOrganizationsWithRawResponse(self._zero_trust.organizations)

    @cached_property
    def seats(self) -> AsyncSeatsWithRawResponse:
        return AsyncSeatsWithRawResponse(self._zero_trust.seats)

    @cached_property
    def access(self) -> AsyncAccessWithRawResponse:
        return AsyncAccessWithRawResponse(self._zero_trust.access)

    @cached_property
    def dex(self) -> AsyncDEXWithRawResponse:
        return AsyncDEXWithRawResponse(self._zero_trust.dex)

    @cached_property
    def tunnels(self) -> AsyncTunnelsWithRawResponse:
        return AsyncTunnelsWithRawResponse(self._zero_trust.tunnels)

    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettingsWithRawResponse:
        return AsyncConnectivitySettingsWithRawResponse(self._zero_trust.connectivity_settings)

    @cached_property
    def dlp(self) -> AsyncDLPWithRawResponse:
        return AsyncDLPWithRawResponse(self._zero_trust.dlp)

    @cached_property
    def gateway(self) -> AsyncGatewayWithRawResponse:
        return AsyncGatewayWithRawResponse(self._zero_trust.gateway)

    @cached_property
    def networks(self) -> AsyncNetworksWithRawResponse:
        return AsyncNetworksWithRawResponse(self._zero_trust.networks)


class ZeroTrustWithStreamingResponse:
    def __init__(self, zero_trust: ZeroTrust) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def devices(self) -> DevicesWithStreamingResponse:
        return DevicesWithStreamingResponse(self._zero_trust.devices)

    @cached_property
    def identity_providers(self) -> IdentityProvidersWithStreamingResponse:
        return IdentityProvidersWithStreamingResponse(self._zero_trust.identity_providers)

    @cached_property
    def organizations(self) -> OrganizationsWithStreamingResponse:
        return OrganizationsWithStreamingResponse(self._zero_trust.organizations)

    @cached_property
    def seats(self) -> SeatsWithStreamingResponse:
        return SeatsWithStreamingResponse(self._zero_trust.seats)

    @cached_property
    def access(self) -> AccessWithStreamingResponse:
        return AccessWithStreamingResponse(self._zero_trust.access)

    @cached_property
    def dex(self) -> DEXWithStreamingResponse:
        return DEXWithStreamingResponse(self._zero_trust.dex)

    @cached_property
    def tunnels(self) -> TunnelsWithStreamingResponse:
        return TunnelsWithStreamingResponse(self._zero_trust.tunnels)

    @cached_property
    def connectivity_settings(self) -> ConnectivitySettingsWithStreamingResponse:
        return ConnectivitySettingsWithStreamingResponse(self._zero_trust.connectivity_settings)

    @cached_property
    def dlp(self) -> DLPWithStreamingResponse:
        return DLPWithStreamingResponse(self._zero_trust.dlp)

    @cached_property
    def gateway(self) -> GatewayWithStreamingResponse:
        return GatewayWithStreamingResponse(self._zero_trust.gateway)

    @cached_property
    def networks(self) -> NetworksWithStreamingResponse:
        return NetworksWithStreamingResponse(self._zero_trust.networks)


class AsyncZeroTrustWithStreamingResponse:
    def __init__(self, zero_trust: AsyncZeroTrust) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def devices(self) -> AsyncDevicesWithStreamingResponse:
        return AsyncDevicesWithStreamingResponse(self._zero_trust.devices)

    @cached_property
    def identity_providers(self) -> AsyncIdentityProvidersWithStreamingResponse:
        return AsyncIdentityProvidersWithStreamingResponse(self._zero_trust.identity_providers)

    @cached_property
    def organizations(self) -> AsyncOrganizationsWithStreamingResponse:
        return AsyncOrganizationsWithStreamingResponse(self._zero_trust.organizations)

    @cached_property
    def seats(self) -> AsyncSeatsWithStreamingResponse:
        return AsyncSeatsWithStreamingResponse(self._zero_trust.seats)

    @cached_property
    def access(self) -> AsyncAccessWithStreamingResponse:
        return AsyncAccessWithStreamingResponse(self._zero_trust.access)

    @cached_property
    def dex(self) -> AsyncDEXWithStreamingResponse:
        return AsyncDEXWithStreamingResponse(self._zero_trust.dex)

    @cached_property
    def tunnels(self) -> AsyncTunnelsWithStreamingResponse:
        return AsyncTunnelsWithStreamingResponse(self._zero_trust.tunnels)

    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettingsWithStreamingResponse:
        return AsyncConnectivitySettingsWithStreamingResponse(self._zero_trust.connectivity_settings)

    @cached_property
    def dlp(self) -> AsyncDLPWithStreamingResponse:
        return AsyncDLPWithStreamingResponse(self._zero_trust.dlp)

    @cached_property
    def gateway(self) -> AsyncGatewayWithStreamingResponse:
        return AsyncGatewayWithStreamingResponse(self._zero_trust.gateway)

    @cached_property
    def networks(self) -> AsyncNetworksWithStreamingResponse:
        return AsyncNetworksWithStreamingResponse(self._zero_trust.networks)
