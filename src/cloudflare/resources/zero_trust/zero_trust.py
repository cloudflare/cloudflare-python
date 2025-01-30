# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .seats import (
    SeatsResource,
    AsyncSeatsResource,
    SeatsResourceWithRawResponse,
    AsyncSeatsResourceWithRawResponse,
    SeatsResourceWithStreamingResponse,
    AsyncSeatsResourceWithStreamingResponse,
)
from .dex.dex import (
    DEXResource,
    AsyncDEXResource,
    DEXResourceWithRawResponse,
    AsyncDEXResourceWithRawResponse,
    DEXResourceWithStreamingResponse,
    AsyncDEXResourceWithStreamingResponse,
)
from .dlp.dlp import (
    DLPResource,
    AsyncDLPResource,
    DLPResourceWithRawResponse,
    AsyncDLPResourceWithRawResponse,
    DLPResourceWithStreamingResponse,
    AsyncDLPResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .access.access import (
    AccessResource,
    AsyncAccessResource,
    AccessResourceWithRawResponse,
    AsyncAccessResourceWithRawResponse,
    AccessResourceWithStreamingResponse,
    AsyncAccessResourceWithStreamingResponse,
)
from .devices.devices import (
    DevicesResource,
    AsyncDevicesResource,
    DevicesResourceWithRawResponse,
    AsyncDevicesResourceWithRawResponse,
    DevicesResourceWithStreamingResponse,
    AsyncDevicesResourceWithStreamingResponse,
)
from .gateway.gateway import (
    GatewayResource,
    AsyncGatewayResource,
    GatewayResourceWithRawResponse,
    AsyncGatewayResourceWithRawResponse,
    GatewayResourceWithStreamingResponse,
    AsyncGatewayResourceWithStreamingResponse,
)
from .tunnels.tunnels import (
    TunnelsResource,
    AsyncTunnelsResource,
    TunnelsResourceWithRawResponse,
    AsyncTunnelsResourceWithRawResponse,
    TunnelsResourceWithStreamingResponse,
    AsyncTunnelsResourceWithStreamingResponse,
)
from .networks.networks import (
    NetworksResource,
    AsyncNetworksResource,
    NetworksResourceWithRawResponse,
    AsyncNetworksResourceWithRawResponse,
    NetworksResourceWithStreamingResponse,
    AsyncNetworksResourceWithStreamingResponse,
)
from .connectivity_settings import (
    ConnectivitySettingsResource,
    AsyncConnectivitySettingsResource,
    ConnectivitySettingsResourceWithRawResponse,
    AsyncConnectivitySettingsResourceWithRawResponse,
    ConnectivitySettingsResourceWithStreamingResponse,
    AsyncConnectivitySettingsResourceWithStreamingResponse,
)
from .risk_scoring.risk_scoring import (
    RiskScoringResource,
    AsyncRiskScoringResource,
    RiskScoringResourceWithRawResponse,
    AsyncRiskScoringResourceWithRawResponse,
    RiskScoringResourceWithStreamingResponse,
    AsyncRiskScoringResourceWithStreamingResponse,
)
from .organizations.organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from .identity_providers.identity_providers import (
    IdentityProvidersResource,
    AsyncIdentityProvidersResource,
    IdentityProvidersResourceWithRawResponse,
    AsyncIdentityProvidersResourceWithRawResponse,
    IdentityProvidersResourceWithStreamingResponse,
    AsyncIdentityProvidersResourceWithStreamingResponse,
)

__all__ = ["ZeroTrustResource", "AsyncZeroTrustResource"]


class ZeroTrustResource(SyncAPIResource):
    @cached_property
    def devices(self) -> DevicesResource:
        return DevicesResource(self._client)

    @cached_property
    def identity_providers(self) -> IdentityProvidersResource:
        return IdentityProvidersResource(self._client)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def seats(self) -> SeatsResource:
        return SeatsResource(self._client)

    @cached_property
    def access(self) -> AccessResource:
        return AccessResource(self._client)

    @cached_property
    def dex(self) -> DEXResource:
        return DEXResource(self._client)

    @cached_property
    def tunnels(self) -> TunnelsResource:
        return TunnelsResource(self._client)

    @cached_property
    def connectivity_settings(self) -> ConnectivitySettingsResource:
        return ConnectivitySettingsResource(self._client)

    @cached_property
    def dlp(self) -> DLPResource:
        return DLPResource(self._client)

    @cached_property
    def gateway(self) -> GatewayResource:
        return GatewayResource(self._client)

    @cached_property
    def networks(self) -> NetworksResource:
        return NetworksResource(self._client)

    @cached_property
    def risk_scoring(self) -> RiskScoringResource:
        return RiskScoringResource(self._client)

    @cached_property
    def with_raw_response(self) -> ZeroTrustResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ZeroTrustResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZeroTrustResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ZeroTrustResourceWithStreamingResponse(self)


class AsyncZeroTrustResource(AsyncAPIResource):
    @cached_property
    def devices(self) -> AsyncDevicesResource:
        return AsyncDevicesResource(self._client)

    @cached_property
    def identity_providers(self) -> AsyncIdentityProvidersResource:
        return AsyncIdentityProvidersResource(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def seats(self) -> AsyncSeatsResource:
        return AsyncSeatsResource(self._client)

    @cached_property
    def access(self) -> AsyncAccessResource:
        return AsyncAccessResource(self._client)

    @cached_property
    def dex(self) -> AsyncDEXResource:
        return AsyncDEXResource(self._client)

    @cached_property
    def tunnels(self) -> AsyncTunnelsResource:
        return AsyncTunnelsResource(self._client)

    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettingsResource:
        return AsyncConnectivitySettingsResource(self._client)

    @cached_property
    def dlp(self) -> AsyncDLPResource:
        return AsyncDLPResource(self._client)

    @cached_property
    def gateway(self) -> AsyncGatewayResource:
        return AsyncGatewayResource(self._client)

    @cached_property
    def networks(self) -> AsyncNetworksResource:
        return AsyncNetworksResource(self._client)

    @cached_property
    def risk_scoring(self) -> AsyncRiskScoringResource:
        return AsyncRiskScoringResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZeroTrustResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZeroTrustResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZeroTrustResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncZeroTrustResourceWithStreamingResponse(self)


class ZeroTrustResourceWithRawResponse:
    def __init__(self, zero_trust: ZeroTrustResource) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def devices(self) -> DevicesResourceWithRawResponse:
        return DevicesResourceWithRawResponse(self._zero_trust.devices)

    @cached_property
    def identity_providers(self) -> IdentityProvidersResourceWithRawResponse:
        return IdentityProvidersResourceWithRawResponse(self._zero_trust.identity_providers)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._zero_trust.organizations)

    @cached_property
    def seats(self) -> SeatsResourceWithRawResponse:
        return SeatsResourceWithRawResponse(self._zero_trust.seats)

    @cached_property
    def access(self) -> AccessResourceWithRawResponse:
        return AccessResourceWithRawResponse(self._zero_trust.access)

    @cached_property
    def dex(self) -> DEXResourceWithRawResponse:
        return DEXResourceWithRawResponse(self._zero_trust.dex)

    @cached_property
    def tunnels(self) -> TunnelsResourceWithRawResponse:
        return TunnelsResourceWithRawResponse(self._zero_trust.tunnels)

    @cached_property
    def connectivity_settings(self) -> ConnectivitySettingsResourceWithRawResponse:
        return ConnectivitySettingsResourceWithRawResponse(self._zero_trust.connectivity_settings)

    @cached_property
    def dlp(self) -> DLPResourceWithRawResponse:
        return DLPResourceWithRawResponse(self._zero_trust.dlp)

    @cached_property
    def gateway(self) -> GatewayResourceWithRawResponse:
        return GatewayResourceWithRawResponse(self._zero_trust.gateway)

    @cached_property
    def networks(self) -> NetworksResourceWithRawResponse:
        return NetworksResourceWithRawResponse(self._zero_trust.networks)

    @cached_property
    def risk_scoring(self) -> RiskScoringResourceWithRawResponse:
        return RiskScoringResourceWithRawResponse(self._zero_trust.risk_scoring)


class AsyncZeroTrustResourceWithRawResponse:
    def __init__(self, zero_trust: AsyncZeroTrustResource) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def devices(self) -> AsyncDevicesResourceWithRawResponse:
        return AsyncDevicesResourceWithRawResponse(self._zero_trust.devices)

    @cached_property
    def identity_providers(self) -> AsyncIdentityProvidersResourceWithRawResponse:
        return AsyncIdentityProvidersResourceWithRawResponse(self._zero_trust.identity_providers)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._zero_trust.organizations)

    @cached_property
    def seats(self) -> AsyncSeatsResourceWithRawResponse:
        return AsyncSeatsResourceWithRawResponse(self._zero_trust.seats)

    @cached_property
    def access(self) -> AsyncAccessResourceWithRawResponse:
        return AsyncAccessResourceWithRawResponse(self._zero_trust.access)

    @cached_property
    def dex(self) -> AsyncDEXResourceWithRawResponse:
        return AsyncDEXResourceWithRawResponse(self._zero_trust.dex)

    @cached_property
    def tunnels(self) -> AsyncTunnelsResourceWithRawResponse:
        return AsyncTunnelsResourceWithRawResponse(self._zero_trust.tunnels)

    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettingsResourceWithRawResponse:
        return AsyncConnectivitySettingsResourceWithRawResponse(self._zero_trust.connectivity_settings)

    @cached_property
    def dlp(self) -> AsyncDLPResourceWithRawResponse:
        return AsyncDLPResourceWithRawResponse(self._zero_trust.dlp)

    @cached_property
    def gateway(self) -> AsyncGatewayResourceWithRawResponse:
        return AsyncGatewayResourceWithRawResponse(self._zero_trust.gateway)

    @cached_property
    def networks(self) -> AsyncNetworksResourceWithRawResponse:
        return AsyncNetworksResourceWithRawResponse(self._zero_trust.networks)

    @cached_property
    def risk_scoring(self) -> AsyncRiskScoringResourceWithRawResponse:
        return AsyncRiskScoringResourceWithRawResponse(self._zero_trust.risk_scoring)


class ZeroTrustResourceWithStreamingResponse:
    def __init__(self, zero_trust: ZeroTrustResource) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def devices(self) -> DevicesResourceWithStreamingResponse:
        return DevicesResourceWithStreamingResponse(self._zero_trust.devices)

    @cached_property
    def identity_providers(self) -> IdentityProvidersResourceWithStreamingResponse:
        return IdentityProvidersResourceWithStreamingResponse(self._zero_trust.identity_providers)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._zero_trust.organizations)

    @cached_property
    def seats(self) -> SeatsResourceWithStreamingResponse:
        return SeatsResourceWithStreamingResponse(self._zero_trust.seats)

    @cached_property
    def access(self) -> AccessResourceWithStreamingResponse:
        return AccessResourceWithStreamingResponse(self._zero_trust.access)

    @cached_property
    def dex(self) -> DEXResourceWithStreamingResponse:
        return DEXResourceWithStreamingResponse(self._zero_trust.dex)

    @cached_property
    def tunnels(self) -> TunnelsResourceWithStreamingResponse:
        return TunnelsResourceWithStreamingResponse(self._zero_trust.tunnels)

    @cached_property
    def connectivity_settings(self) -> ConnectivitySettingsResourceWithStreamingResponse:
        return ConnectivitySettingsResourceWithStreamingResponse(self._zero_trust.connectivity_settings)

    @cached_property
    def dlp(self) -> DLPResourceWithStreamingResponse:
        return DLPResourceWithStreamingResponse(self._zero_trust.dlp)

    @cached_property
    def gateway(self) -> GatewayResourceWithStreamingResponse:
        return GatewayResourceWithStreamingResponse(self._zero_trust.gateway)

    @cached_property
    def networks(self) -> NetworksResourceWithStreamingResponse:
        return NetworksResourceWithStreamingResponse(self._zero_trust.networks)

    @cached_property
    def risk_scoring(self) -> RiskScoringResourceWithStreamingResponse:
        return RiskScoringResourceWithStreamingResponse(self._zero_trust.risk_scoring)


class AsyncZeroTrustResourceWithStreamingResponse:
    def __init__(self, zero_trust: AsyncZeroTrustResource) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def devices(self) -> AsyncDevicesResourceWithStreamingResponse:
        return AsyncDevicesResourceWithStreamingResponse(self._zero_trust.devices)

    @cached_property
    def identity_providers(self) -> AsyncIdentityProvidersResourceWithStreamingResponse:
        return AsyncIdentityProvidersResourceWithStreamingResponse(self._zero_trust.identity_providers)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._zero_trust.organizations)

    @cached_property
    def seats(self) -> AsyncSeatsResourceWithStreamingResponse:
        return AsyncSeatsResourceWithStreamingResponse(self._zero_trust.seats)

    @cached_property
    def access(self) -> AsyncAccessResourceWithStreamingResponse:
        return AsyncAccessResourceWithStreamingResponse(self._zero_trust.access)

    @cached_property
    def dex(self) -> AsyncDEXResourceWithStreamingResponse:
        return AsyncDEXResourceWithStreamingResponse(self._zero_trust.dex)

    @cached_property
    def tunnels(self) -> AsyncTunnelsResourceWithStreamingResponse:
        return AsyncTunnelsResourceWithStreamingResponse(self._zero_trust.tunnels)

    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettingsResourceWithStreamingResponse:
        return AsyncConnectivitySettingsResourceWithStreamingResponse(self._zero_trust.connectivity_settings)

    @cached_property
    def dlp(self) -> AsyncDLPResourceWithStreamingResponse:
        return AsyncDLPResourceWithStreamingResponse(self._zero_trust.dlp)

    @cached_property
    def gateway(self) -> AsyncGatewayResourceWithStreamingResponse:
        return AsyncGatewayResourceWithStreamingResponse(self._zero_trust.gateway)

    @cached_property
    def networks(self) -> AsyncNetworksResourceWithStreamingResponse:
        return AsyncNetworksResourceWithStreamingResponse(self._zero_trust.networks)

    @cached_property
    def risk_scoring(self) -> AsyncRiskScoringResourceWithStreamingResponse:
        return AsyncRiskScoringResourceWithStreamingResponse(self._zero_trust.risk_scoring)
