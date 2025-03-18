# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        ai,
        d1,
        kv,
        r2,
        acm,
        dns,
        iam,
        ips,
        rum,
        ssl,
        argo,
        logs,
        user,
        web3,
        cache,
        calls,
        intel,
        pages,
        radar,
        rules,
        speed,
        zaraz,
        zones,
        images,
        queues,
        stream,
        billing,
        filters,
        logpush,
        workers,
        accounts,
        alerting,
        firewall,
        rulesets,
        snippets,
        spectrum,
        hostnames,
        registrar,
        turnstile,
        vectorize,
        workflows,
        addressing,
        ai_gateway,
        audit_logs,
        hyperdrive,
        page_rules,
        zero_trust,
        api_gateway,
        botnet_feed,
        diagnostics,
        memberships,
        page_shield,
        rate_limits,
        url_scanner,
        custom_pages,
        dns_firewall,
        healthchecks,
        security_txt,
        abuse_reports,
        email_routing,
        magic_transit,
        waiting_rooms,
        bot_management,
        cloudforce_one,
        dcv_delegation,
        email_security,
        load_balancers,
        cloud_connector,
        durable_objects,
        request_tracers,
        security_center,
        brand_protection,
        content_scanning,
        custom_hostnames,
        resource_sharing,
        browser_rendering,
        mtls_certificates,
        url_normalization,
        custom_nameservers,
        managed_transforms,
        client_certificates,
        custom_certificates,
        keyless_certificates,
        network_interconnects,
        workers_for_platforms,
        magic_cloud_networking,
        origin_ca_certificates,
        origin_tls_client_auth,
        certificate_authorities,
        leaked_credential_checks,
        magic_network_monitoring,
        origin_post_quantum_encryption,
    )
    from .resources.ips import IPsResource, AsyncIPsResource
    from .resources.ai.ai import AIResource, AsyncAIResource
    from .resources.d1.d1 import D1Resource, AsyncD1Resource
    from .resources.kv.kv import KVResource, AsyncKVResource
    from .resources.r2.r2 import R2Resource, AsyncR2Resource
    from .resources.acm.acm import ACMResource, AsyncACMResource
    from .resources.dns.dns import DNSResource, AsyncDNSResource
    from .resources.filters import FiltersResource, AsyncFiltersResource
    from .resources.iam.iam import IAMResource, AsyncIAMResource
    from .resources.rum.rum import RUMResource, AsyncRUMResource
    from .resources.ssl.ssl import SSLResource, AsyncSSLResource
    from .resources.argo.argo import ArgoResource, AsyncArgoResource
    from .resources.logs.logs import LogsResource, AsyncLogsResource
    from .resources.user.user import UserResource, AsyncUserResource
    from .resources.web3.web3 import Web3Resource, AsyncWeb3Resource
    from .resources.audit_logs import AuditLogsResource, AsyncAuditLogsResource
    from .resources.page_rules import PageRulesResource, AsyncPageRulesResource
    from .resources.cache.cache import CacheResource, AsyncCacheResource
    from .resources.calls.calls import CallsResource, AsyncCallsResource
    from .resources.intel.intel import IntelResource, AsyncIntelResource
    from .resources.memberships import MembershipsResource, AsyncMembershipsResource
    from .resources.pages.pages import PagesResource, AsyncPagesResource
    from .resources.radar.radar import RadarResource, AsyncRadarResource
    from .resources.rate_limits import RateLimitsResource, AsyncRateLimitsResource
    from .resources.rules.rules import RulesResource, AsyncRulesResource
    from .resources.speed.speed import SpeedResource, AsyncSpeedResource
    from .resources.zaraz.zaraz import ZarazResource, AsyncZarazResource
    from .resources.zones.zones import ZonesResource, AsyncZonesResource
    from .resources.custom_pages import CustomPagesResource, AsyncCustomPagesResource
    from .resources.security_txt import SecurityTXTResource, AsyncSecurityTXTResource
    from .resources.abuse_reports import AbuseReportsResource, AsyncAbuseReportsResource
    from .resources.images.images import ImagesResource, AsyncImagesResource
    from .resources.queues.queues import QueuesResource, AsyncQueuesResource
    from .resources.stream.stream import StreamResource, AsyncStreamResource
    from .resources.bot_management import BotManagementResource, AsyncBotManagementResource
    from .resources.dcv_delegation import DCVDelegationResource, AsyncDCVDelegationResource
    from .resources.billing.billing import BillingResource, AsyncBillingResource
    from .resources.logpush.logpush import LogpushResource, AsyncLogpushResource
    from .resources.workers.workers import WorkersResource, AsyncWorkersResource
    from .resources.brand_protection import BrandProtectionResource, AsyncBrandProtectionResource
    from .resources.accounts.accounts import AccountsResource, AsyncAccountsResource
    from .resources.alerting.alerting import AlertingResource, AsyncAlertingResource
    from .resources.firewall.firewall import FirewallResource, AsyncFirewallResource
    from .resources.rulesets.rulesets import RulesetsResource, AsyncRulesetsResource
    from .resources.snippets.snippets import SnippetsResource, AsyncSnippetsResource
    from .resources.spectrum.spectrum import SpectrumResource, AsyncSpectrumResource
    from .resources.url_normalization import URLNormalizationResource, AsyncURLNormalizationResource
    from .resources.custom_nameservers import CustomNameserversResource, AsyncCustomNameserversResource
    from .resources.managed_transforms import ManagedTransformsResource, AsyncManagedTransformsResource
    from .resources.client_certificates import ClientCertificatesResource, AsyncClientCertificatesResource
    from .resources.hostnames.hostnames import HostnamesResource, AsyncHostnamesResource
    from .resources.registrar.registrar import RegistrarResource, AsyncRegistrarResource
    from .resources.turnstile.turnstile import TurnstileResource, AsyncTurnstileResource
    from .resources.vectorize.vectorize import VectorizeResource, AsyncVectorizeResource
    from .resources.workflows.workflows import WorkflowsResource, AsyncWorkflowsResource
    from .resources.keyless_certificates import KeylessCertificatesResource, AsyncKeylessCertificatesResource
    from .resources.addressing.addressing import AddressingResource, AsyncAddressingResource
    from .resources.ai_gateway.ai_gateway import AIGatewayResource, AsyncAIGatewayResource
    from .resources.hyperdrive.hyperdrive import HyperdriveResource, AsyncHyperdriveResource
    from .resources.zero_trust.zero_trust import ZeroTrustResource, AsyncZeroTrustResource
    from .resources.origin_ca_certificates import OriginCACertificatesResource, AsyncOriginCACertificatesResource
    from .resources.api_gateway.api_gateway import APIGatewayResource, AsyncAPIGatewayResource
    from .resources.botnet_feed.botnet_feed import BotnetFeedResource, AsyncBotnetFeedResource
    from .resources.diagnostics.diagnostics import DiagnosticsResource, AsyncDiagnosticsResource
    from .resources.page_shield.page_shield import PageShieldResource, AsyncPageShieldResource
    from .resources.url_scanner.url_scanner import URLScannerResource, AsyncURLScannerResource
    from .resources.dns_firewall.dns_firewall import DNSFirewallResource, AsyncDNSFirewallResource
    from .resources.healthchecks.healthchecks import HealthchecksResource, AsyncHealthchecksResource
    from .resources.email_routing.email_routing import EmailRoutingResource, AsyncEmailRoutingResource
    from .resources.magic_transit.magic_transit import MagicTransitResource, AsyncMagicTransitResource
    from .resources.waiting_rooms.waiting_rooms import WaitingRoomsResource, AsyncWaitingRoomsResource
    from .resources.cloudforce_one.cloudforce_one import CloudforceOneResource, AsyncCloudforceOneResource
    from .resources.email_security.email_security import EmailSecurityResource, AsyncEmailSecurityResource
    from .resources.load_balancers.load_balancers import LoadBalancersResource, AsyncLoadBalancersResource
    from .resources.origin_post_quantum_encryption import (
        OriginPostQuantumEncryptionResource,
        AsyncOriginPostQuantumEncryptionResource,
    )
    from .resources.cloud_connector.cloud_connector import CloudConnectorResource, AsyncCloudConnectorResource
    from .resources.durable_objects.durable_objects import DurableObjectsResource, AsyncDurableObjectsResource
    from .resources.request_tracers.request_tracers import RequestTracersResource, AsyncRequestTracersResource
    from .resources.security_center.security_center import SecurityCenterResource, AsyncSecurityCenterResource
    from .resources.content_scanning.content_scanning import ContentScanningResource, AsyncContentScanningResource
    from .resources.custom_hostnames.custom_hostnames import CustomHostnamesResource, AsyncCustomHostnamesResource
    from .resources.resource_sharing.resource_sharing import ResourceSharingResource, AsyncResourceSharingResource
    from .resources.browser_rendering.browser_rendering import BrowserRenderingResource, AsyncBrowserRenderingResource
    from .resources.mtls_certificates.mtls_certificates import MTLSCertificatesResource, AsyncMTLSCertificatesResource
    from .resources.custom_certificates.custom_certificates import (
        CustomCertificatesResource,
        AsyncCustomCertificatesResource,
    )
    from .resources.network_interconnects.network_interconnects import (
        NetworkInterconnectsResource,
        AsyncNetworkInterconnectsResource,
    )
    from .resources.workers_for_platforms.workers_for_platforms import (
        WorkersForPlatformsResource,
        AsyncWorkersForPlatformsResource,
    )
    from .resources.magic_cloud_networking.magic_cloud_networking import (
        MagicCloudNetworkingResource,
        AsyncMagicCloudNetworkingResource,
    )
    from .resources.origin_tls_client_auth.origin_tls_client_auth import (
        OriginTLSClientAuthResource,
        AsyncOriginTLSClientAuthResource,
    )
    from .resources.certificate_authorities.certificate_authorities import (
        CertificateAuthoritiesResource,
        AsyncCertificateAuthoritiesResource,
    )
    from .resources.leaked_credential_checks.leaked_credential_checks import (
        LeakedCredentialChecksResource,
        AsyncLeakedCredentialChecksResource,
    )
    from .resources.magic_network_monitoring.magic_network_monitoring import (
        MagicNetworkMonitoringResource,
        AsyncMagicNetworkMonitoringResource,
    )

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Cloudflare",
    "AsyncCloudflare",
    "Client",
    "AsyncClient",
]


class Cloudflare(SyncAPIClient):
    # client options
    api_token: str | None
    api_key: str | None
    api_email: str | None
    user_service_key: str | None

    def __init__(
        self,
        *,
        api_token: str | None = None,
        api_key: str | None = None,
        api_email: str | None = None,
        user_service_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Cloudflare client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_token` from `CLOUDFLARE_API_TOKEN`
        - `api_key` from `CLOUDFLARE_API_KEY`
        - `api_email` from `CLOUDFLARE_EMAIL`
        - `user_service_key` from `CLOUDFLARE_API_USER_SERVICE_KEY`
        """
        if api_token is None:
            api_token = os.environ.get("CLOUDFLARE_API_TOKEN")
        self.api_token = api_token

        if api_key is None:
            api_key = os.environ.get("CLOUDFLARE_API_KEY")
        self.api_key = api_key

        if api_email is None:
            api_email = os.environ.get("CLOUDFLARE_EMAIL")
        self.api_email = api_email

        if user_service_key is None:
            user_service_key = os.environ.get("CLOUDFLARE_API_USER_SERVICE_KEY")
        self.user_service_key = user_service_key

        if base_url is None:
            base_url = os.environ.get("CLOUDFLARE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.cloudflare.com/client/v4"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def accounts(self) -> AccountsResource:
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def origin_ca_certificates(self) -> OriginCACertificatesResource:
        from .resources.origin_ca_certificates import OriginCACertificatesResource

        return OriginCACertificatesResource(self)

    @cached_property
    def ips(self) -> IPsResource:
        from .resources.ips import IPsResource

        return IPsResource(self)

    @cached_property
    def memberships(self) -> MembershipsResource:
        from .resources.memberships import MembershipsResource

        return MembershipsResource(self)

    @cached_property
    def user(self) -> UserResource:
        from .resources.user import UserResource

        return UserResource(self)

    @cached_property
    def zones(self) -> ZonesResource:
        from .resources.zones import ZonesResource

        return ZonesResource(self)

    @cached_property
    def load_balancers(self) -> LoadBalancersResource:
        from .resources.load_balancers import LoadBalancersResource

        return LoadBalancersResource(self)

    @cached_property
    def cache(self) -> CacheResource:
        from .resources.cache import CacheResource

        return CacheResource(self)

    @cached_property
    def ssl(self) -> SSLResource:
        from .resources.ssl import SSLResource

        return SSLResource(self)

    @cached_property
    def acm(self) -> ACMResource:
        from .resources.acm import ACMResource

        return ACMResource(self)

    @cached_property
    def argo(self) -> ArgoResource:
        from .resources.argo import ArgoResource

        return ArgoResource(self)

    @cached_property
    def certificate_authorities(self) -> CertificateAuthoritiesResource:
        from .resources.certificate_authorities import CertificateAuthoritiesResource

        return CertificateAuthoritiesResource(self)

    @cached_property
    def client_certificates(self) -> ClientCertificatesResource:
        from .resources.client_certificates import ClientCertificatesResource

        return ClientCertificatesResource(self)

    @cached_property
    def custom_certificates(self) -> CustomCertificatesResource:
        from .resources.custom_certificates import CustomCertificatesResource

        return CustomCertificatesResource(self)

    @cached_property
    def custom_hostnames(self) -> CustomHostnamesResource:
        from .resources.custom_hostnames import CustomHostnamesResource

        return CustomHostnamesResource(self)

    @cached_property
    def custom_nameservers(self) -> CustomNameserversResource:
        from .resources.custom_nameservers import CustomNameserversResource

        return CustomNameserversResource(self)

    @cached_property
    def dns_firewall(self) -> DNSFirewallResource:
        from .resources.dns_firewall import DNSFirewallResource

        return DNSFirewallResource(self)

    @cached_property
    def dns(self) -> DNSResource:
        from .resources.dns import DNSResource

        return DNSResource(self)

    @cached_property
    def email_security(self) -> EmailSecurityResource:
        from .resources.email_security import EmailSecurityResource

        return EmailSecurityResource(self)

    @cached_property
    def email_routing(self) -> EmailRoutingResource:
        from .resources.email_routing import EmailRoutingResource

        return EmailRoutingResource(self)

    @cached_property
    def filters(self) -> FiltersResource:
        from .resources.filters import FiltersResource

        return FiltersResource(self)

    @cached_property
    def firewall(self) -> FirewallResource:
        from .resources.firewall import FirewallResource

        return FirewallResource(self)

    @cached_property
    def healthchecks(self) -> HealthchecksResource:
        from .resources.healthchecks import HealthchecksResource

        return HealthchecksResource(self)

    @cached_property
    def keyless_certificates(self) -> KeylessCertificatesResource:
        from .resources.keyless_certificates import KeylessCertificatesResource

        return KeylessCertificatesResource(self)

    @cached_property
    def logpush(self) -> LogpushResource:
        from .resources.logpush import LogpushResource

        return LogpushResource(self)

    @cached_property
    def logs(self) -> LogsResource:
        from .resources.logs import LogsResource

        return LogsResource(self)

    @cached_property
    def origin_tls_client_auth(self) -> OriginTLSClientAuthResource:
        from .resources.origin_tls_client_auth import OriginTLSClientAuthResource

        return OriginTLSClientAuthResource(self)

    @cached_property
    def page_rules(self) -> PageRulesResource:
        from .resources.page_rules import PageRulesResource

        return PageRulesResource(self)

    @cached_property
    def rate_limits(self) -> RateLimitsResource:
        from .resources.rate_limits import RateLimitsResource

        return RateLimitsResource(self)

    @cached_property
    def waiting_rooms(self) -> WaitingRoomsResource:
        from .resources.waiting_rooms import WaitingRoomsResource

        return WaitingRoomsResource(self)

    @cached_property
    def web3(self) -> Web3Resource:
        from .resources.web3 import Web3Resource

        return Web3Resource(self)

    @cached_property
    def workers(self) -> WorkersResource:
        from .resources.workers import WorkersResource

        return WorkersResource(self)

    @cached_property
    def kv(self) -> KVResource:
        from .resources.kv import KVResource

        return KVResource(self)

    @cached_property
    def durable_objects(self) -> DurableObjectsResource:
        from .resources.durable_objects import DurableObjectsResource

        return DurableObjectsResource(self)

    @cached_property
    def queues(self) -> QueuesResource:
        from .resources.queues import QueuesResource

        return QueuesResource(self)

    @cached_property
    def api_gateway(self) -> APIGatewayResource:
        from .resources.api_gateway import APIGatewayResource

        return APIGatewayResource(self)

    @cached_property
    def managed_transforms(self) -> ManagedTransformsResource:
        from .resources.managed_transforms import ManagedTransformsResource

        return ManagedTransformsResource(self)

    @cached_property
    def page_shield(self) -> PageShieldResource:
        from .resources.page_shield import PageShieldResource

        return PageShieldResource(self)

    @cached_property
    def rulesets(self) -> RulesetsResource:
        from .resources.rulesets import RulesetsResource

        return RulesetsResource(self)

    @cached_property
    def url_normalization(self) -> URLNormalizationResource:
        from .resources.url_normalization import URLNormalizationResource

        return URLNormalizationResource(self)

    @cached_property
    def spectrum(self) -> SpectrumResource:
        from .resources.spectrum import SpectrumResource

        return SpectrumResource(self)

    @cached_property
    def addressing(self) -> AddressingResource:
        from .resources.addressing import AddressingResource

        return AddressingResource(self)

    @cached_property
    def audit_logs(self) -> AuditLogsResource:
        from .resources.audit_logs import AuditLogsResource

        return AuditLogsResource(self)

    @cached_property
    def billing(self) -> BillingResource:
        from .resources.billing import BillingResource

        return BillingResource(self)

    @cached_property
    def brand_protection(self) -> BrandProtectionResource:
        from .resources.brand_protection import BrandProtectionResource

        return BrandProtectionResource(self)

    @cached_property
    def diagnostics(self) -> DiagnosticsResource:
        from .resources.diagnostics import DiagnosticsResource

        return DiagnosticsResource(self)

    @cached_property
    def images(self) -> ImagesResource:
        from .resources.images import ImagesResource

        return ImagesResource(self)

    @cached_property
    def intel(self) -> IntelResource:
        from .resources.intel import IntelResource

        return IntelResource(self)

    @cached_property
    def magic_transit(self) -> MagicTransitResource:
        from .resources.magic_transit import MagicTransitResource

        return MagicTransitResource(self)

    @cached_property
    def magic_network_monitoring(self) -> MagicNetworkMonitoringResource:
        from .resources.magic_network_monitoring import MagicNetworkMonitoringResource

        return MagicNetworkMonitoringResource(self)

    @cached_property
    def magic_cloud_networking(self) -> MagicCloudNetworkingResource:
        from .resources.magic_cloud_networking import MagicCloudNetworkingResource

        return MagicCloudNetworkingResource(self)

    @cached_property
    def network_interconnects(self) -> NetworkInterconnectsResource:
        from .resources.network_interconnects import NetworkInterconnectsResource

        return NetworkInterconnectsResource(self)

    @cached_property
    def mtls_certificates(self) -> MTLSCertificatesResource:
        from .resources.mtls_certificates import MTLSCertificatesResource

        return MTLSCertificatesResource(self)

    @cached_property
    def pages(self) -> PagesResource:
        from .resources.pages import PagesResource

        return PagesResource(self)

    @cached_property
    def registrar(self) -> RegistrarResource:
        from .resources.registrar import RegistrarResource

        return RegistrarResource(self)

    @cached_property
    def request_tracers(self) -> RequestTracersResource:
        from .resources.request_tracers import RequestTracersResource

        return RequestTracersResource(self)

    @cached_property
    def rules(self) -> RulesResource:
        from .resources.rules import RulesResource

        return RulesResource(self)

    @cached_property
    def stream(self) -> StreamResource:
        from .resources.stream import StreamResource

        return StreamResource(self)

    @cached_property
    def alerting(self) -> AlertingResource:
        from .resources.alerting import AlertingResource

        return AlertingResource(self)

    @cached_property
    def d1(self) -> D1Resource:
        from .resources.d1 import D1Resource

        return D1Resource(self)

    @cached_property
    def r2(self) -> R2Resource:
        from .resources.r2 import R2Resource

        return R2Resource(self)

    @cached_property
    def workers_for_platforms(self) -> WorkersForPlatformsResource:
        from .resources.workers_for_platforms import WorkersForPlatformsResource

        return WorkersForPlatformsResource(self)

    @cached_property
    def zero_trust(self) -> ZeroTrustResource:
        from .resources.zero_trust import ZeroTrustResource

        return ZeroTrustResource(self)

    @cached_property
    def turnstile(self) -> TurnstileResource:
        from .resources.turnstile import TurnstileResource

        return TurnstileResource(self)

    @cached_property
    def hyperdrive(self) -> HyperdriveResource:
        from .resources.hyperdrive import HyperdriveResource

        return HyperdriveResource(self)

    @cached_property
    def rum(self) -> RUMResource:
        from .resources.rum import RUMResource

        return RUMResource(self)

    @cached_property
    def vectorize(self) -> VectorizeResource:
        from .resources.vectorize import VectorizeResource

        return VectorizeResource(self)

    @cached_property
    def url_scanner(self) -> URLScannerResource:
        from .resources.url_scanner import URLScannerResource

        return URLScannerResource(self)

    @cached_property
    def radar(self) -> RadarResource:
        from .resources.radar import RadarResource

        return RadarResource(self)

    @cached_property
    def bot_management(self) -> BotManagementResource:
        from .resources.bot_management import BotManagementResource

        return BotManagementResource(self)

    @cached_property
    def origin_post_quantum_encryption(self) -> OriginPostQuantumEncryptionResource:
        from .resources.origin_post_quantum_encryption import OriginPostQuantumEncryptionResource

        return OriginPostQuantumEncryptionResource(self)

    @cached_property
    def zaraz(self) -> ZarazResource:
        from .resources.zaraz import ZarazResource

        return ZarazResource(self)

    @cached_property
    def speed(self) -> SpeedResource:
        from .resources.speed import SpeedResource

        return SpeedResource(self)

    @cached_property
    def dcv_delegation(self) -> DCVDelegationResource:
        from .resources.dcv_delegation import DCVDelegationResource

        return DCVDelegationResource(self)

    @cached_property
    def hostnames(self) -> HostnamesResource:
        from .resources.hostnames import HostnamesResource

        return HostnamesResource(self)

    @cached_property
    def snippets(self) -> SnippetsResource:
        from .resources.snippets import SnippetsResource

        return SnippetsResource(self)

    @cached_property
    def calls(self) -> CallsResource:
        from .resources.calls import CallsResource

        return CallsResource(self)

    @cached_property
    def cloudforce_one(self) -> CloudforceOneResource:
        from .resources.cloudforce_one import CloudforceOneResource

        return CloudforceOneResource(self)

    @cached_property
    def ai_gateway(self) -> AIGatewayResource:
        from .resources.ai_gateway import AIGatewayResource

        return AIGatewayResource(self)

    @cached_property
    def iam(self) -> IAMResource:
        from .resources.iam import IAMResource

        return IAMResource(self)

    @cached_property
    def cloud_connector(self) -> CloudConnectorResource:
        from .resources.cloud_connector import CloudConnectorResource

        return CloudConnectorResource(self)

    @cached_property
    def botnet_feed(self) -> BotnetFeedResource:
        from .resources.botnet_feed import BotnetFeedResource

        return BotnetFeedResource(self)

    @cached_property
    def security_txt(self) -> SecurityTXTResource:
        from .resources.security_txt import SecurityTXTResource

        return SecurityTXTResource(self)

    @cached_property
    def workflows(self) -> WorkflowsResource:
        from .resources.workflows import WorkflowsResource

        return WorkflowsResource(self)

    @cached_property
    def resource_sharing(self) -> ResourceSharingResource:
        from .resources.resource_sharing import ResourceSharingResource

        return ResourceSharingResource(self)

    @cached_property
    def leaked_credential_checks(self) -> LeakedCredentialChecksResource:
        from .resources.leaked_credential_checks import LeakedCredentialChecksResource

        return LeakedCredentialChecksResource(self)

    @cached_property
    def content_scanning(self) -> ContentScanningResource:
        from .resources.content_scanning import ContentScanningResource

        return ContentScanningResource(self)

    @cached_property
    def abuse_reports(self) -> AbuseReportsResource:
        from .resources.abuse_reports import AbuseReportsResource

        return AbuseReportsResource(self)

    @cached_property
    def ai(self) -> AIResource:
        from .resources.ai import AIResource

        return AIResource(self)

    @cached_property
    def security_center(self) -> SecurityCenterResource:
        from .resources.security_center import SecurityCenterResource

        return SecurityCenterResource(self)

    @cached_property
    def browser_rendering(self) -> BrowserRenderingResource:
        from .resources.browser_rendering import BrowserRenderingResource

        return BrowserRenderingResource(self)

    @cached_property
    def custom_pages(self) -> CustomPagesResource:
        from .resources.custom_pages import CustomPagesResource

        return CustomPagesResource(self)

    @cached_property
    def with_raw_response(self) -> CloudflareWithRawResponse:
        return CloudflareWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudflareWithStreamedResponse:
        return CloudflareWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self._api_email:
            return self._api_email
        if self._api_key:
            return self._api_key
        if self._api_token:
            return self._api_token
        if self._user_service_key:
            return self._user_service_key
        return {}

    @property
    def _api_email(self) -> dict[str, str]:
        api_email = self.api_email
        if api_email is None:
            return {}
        return {"X-Auth-Email": api_email}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-Auth-Key": api_key}

    @property
    def _api_token(self) -> dict[str, str]:
        api_token = self.api_token
        if api_token is None:
            return {}
        return {"Authorization": f"Bearer {api_token}"}

    @property
    def _user_service_key(self) -> dict[str, str]:
        user_service_key = self.user_service_key
        if user_service_key is None:
            return {}
        return {"X-Auth-User-Service-Key": user_service_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "X-Auth-Key": self.api_key if self.api_key is not None else Omit(),
            "X-Auth-Email": self.api_email if self.api_email is not None else Omit(),
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_email and headers.get("X-Auth-Email"):
            return
        if isinstance(custom_headers.get("X-Auth-Email"), Omit):
            return

        if self.api_key and headers.get("X-Auth-Key"):
            return
        if isinstance(custom_headers.get("X-Auth-Key"), Omit):
            return

        if self.api_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.user_service_key and headers.get("X-Auth-User-Service-Key"):
            return
        if isinstance(custom_headers.get("X-Auth-User-Service-Key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected one of api_email, api_key, api_token or user_service_key to be set. Or for one of the `X-Auth-Email`, `X-Auth-Key`, `Authorization` or `X-Auth-User-Service-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_token: str | None = None,
        api_key: str | None = None,
        api_email: str | None = None,
        user_service_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_token=api_token or self.api_token,
            api_key=api_key or self.api_key,
            api_email=api_email or self.api_email,
            user_service_key=user_service_key or self.user_service_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCloudflare(AsyncAPIClient):
    # client options
    api_token: str | None
    api_key: str | None
    api_email: str | None
    user_service_key: str | None

    def __init__(
        self,
        *,
        api_token: str | None = None,
        api_key: str | None = None,
        api_email: str | None = None,
        user_service_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCloudflare client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_token` from `CLOUDFLARE_API_TOKEN`
        - `api_key` from `CLOUDFLARE_API_KEY`
        - `api_email` from `CLOUDFLARE_EMAIL`
        - `user_service_key` from `CLOUDFLARE_API_USER_SERVICE_KEY`
        """
        if api_token is None:
            api_token = os.environ.get("CLOUDFLARE_API_TOKEN")
        self.api_token = api_token

        if api_key is None:
            api_key = os.environ.get("CLOUDFLARE_API_KEY")
        self.api_key = api_key

        if api_email is None:
            api_email = os.environ.get("CLOUDFLARE_EMAIL")
        self.api_email = api_email

        if user_service_key is None:
            user_service_key = os.environ.get("CLOUDFLARE_API_USER_SERVICE_KEY")
        self.user_service_key = user_service_key

        if base_url is None:
            base_url = os.environ.get("CLOUDFLARE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.cloudflare.com/client/v4"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def origin_ca_certificates(self) -> AsyncOriginCACertificatesResource:
        from .resources.origin_ca_certificates import AsyncOriginCACertificatesResource

        return AsyncOriginCACertificatesResource(self)

    @cached_property
    def ips(self) -> AsyncIPsResource:
        from .resources.ips import AsyncIPsResource

        return AsyncIPsResource(self)

    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        from .resources.memberships import AsyncMembershipsResource

        return AsyncMembershipsResource(self)

    @cached_property
    def user(self) -> AsyncUserResource:
        from .resources.user import AsyncUserResource

        return AsyncUserResource(self)

    @cached_property
    def zones(self) -> AsyncZonesResource:
        from .resources.zones import AsyncZonesResource

        return AsyncZonesResource(self)

    @cached_property
    def load_balancers(self) -> AsyncLoadBalancersResource:
        from .resources.load_balancers import AsyncLoadBalancersResource

        return AsyncLoadBalancersResource(self)

    @cached_property
    def cache(self) -> AsyncCacheResource:
        from .resources.cache import AsyncCacheResource

        return AsyncCacheResource(self)

    @cached_property
    def ssl(self) -> AsyncSSLResource:
        from .resources.ssl import AsyncSSLResource

        return AsyncSSLResource(self)

    @cached_property
    def acm(self) -> AsyncACMResource:
        from .resources.acm import AsyncACMResource

        return AsyncACMResource(self)

    @cached_property
    def argo(self) -> AsyncArgoResource:
        from .resources.argo import AsyncArgoResource

        return AsyncArgoResource(self)

    @cached_property
    def certificate_authorities(self) -> AsyncCertificateAuthoritiesResource:
        from .resources.certificate_authorities import AsyncCertificateAuthoritiesResource

        return AsyncCertificateAuthoritiesResource(self)

    @cached_property
    def client_certificates(self) -> AsyncClientCertificatesResource:
        from .resources.client_certificates import AsyncClientCertificatesResource

        return AsyncClientCertificatesResource(self)

    @cached_property
    def custom_certificates(self) -> AsyncCustomCertificatesResource:
        from .resources.custom_certificates import AsyncCustomCertificatesResource

        return AsyncCustomCertificatesResource(self)

    @cached_property
    def custom_hostnames(self) -> AsyncCustomHostnamesResource:
        from .resources.custom_hostnames import AsyncCustomHostnamesResource

        return AsyncCustomHostnamesResource(self)

    @cached_property
    def custom_nameservers(self) -> AsyncCustomNameserversResource:
        from .resources.custom_nameservers import AsyncCustomNameserversResource

        return AsyncCustomNameserversResource(self)

    @cached_property
    def dns_firewall(self) -> AsyncDNSFirewallResource:
        from .resources.dns_firewall import AsyncDNSFirewallResource

        return AsyncDNSFirewallResource(self)

    @cached_property
    def dns(self) -> AsyncDNSResource:
        from .resources.dns import AsyncDNSResource

        return AsyncDNSResource(self)

    @cached_property
    def email_security(self) -> AsyncEmailSecurityResource:
        from .resources.email_security import AsyncEmailSecurityResource

        return AsyncEmailSecurityResource(self)

    @cached_property
    def email_routing(self) -> AsyncEmailRoutingResource:
        from .resources.email_routing import AsyncEmailRoutingResource

        return AsyncEmailRoutingResource(self)

    @cached_property
    def filters(self) -> AsyncFiltersResource:
        from .resources.filters import AsyncFiltersResource

        return AsyncFiltersResource(self)

    @cached_property
    def firewall(self) -> AsyncFirewallResource:
        from .resources.firewall import AsyncFirewallResource

        return AsyncFirewallResource(self)

    @cached_property
    def healthchecks(self) -> AsyncHealthchecksResource:
        from .resources.healthchecks import AsyncHealthchecksResource

        return AsyncHealthchecksResource(self)

    @cached_property
    def keyless_certificates(self) -> AsyncKeylessCertificatesResource:
        from .resources.keyless_certificates import AsyncKeylessCertificatesResource

        return AsyncKeylessCertificatesResource(self)

    @cached_property
    def logpush(self) -> AsyncLogpushResource:
        from .resources.logpush import AsyncLogpushResource

        return AsyncLogpushResource(self)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        from .resources.logs import AsyncLogsResource

        return AsyncLogsResource(self)

    @cached_property
    def origin_tls_client_auth(self) -> AsyncOriginTLSClientAuthResource:
        from .resources.origin_tls_client_auth import AsyncOriginTLSClientAuthResource

        return AsyncOriginTLSClientAuthResource(self)

    @cached_property
    def page_rules(self) -> AsyncPageRulesResource:
        from .resources.page_rules import AsyncPageRulesResource

        return AsyncPageRulesResource(self)

    @cached_property
    def rate_limits(self) -> AsyncRateLimitsResource:
        from .resources.rate_limits import AsyncRateLimitsResource

        return AsyncRateLimitsResource(self)

    @cached_property
    def waiting_rooms(self) -> AsyncWaitingRoomsResource:
        from .resources.waiting_rooms import AsyncWaitingRoomsResource

        return AsyncWaitingRoomsResource(self)

    @cached_property
    def web3(self) -> AsyncWeb3Resource:
        from .resources.web3 import AsyncWeb3Resource

        return AsyncWeb3Resource(self)

    @cached_property
    def workers(self) -> AsyncWorkersResource:
        from .resources.workers import AsyncWorkersResource

        return AsyncWorkersResource(self)

    @cached_property
    def kv(self) -> AsyncKVResource:
        from .resources.kv import AsyncKVResource

        return AsyncKVResource(self)

    @cached_property
    def durable_objects(self) -> AsyncDurableObjectsResource:
        from .resources.durable_objects import AsyncDurableObjectsResource

        return AsyncDurableObjectsResource(self)

    @cached_property
    def queues(self) -> AsyncQueuesResource:
        from .resources.queues import AsyncQueuesResource

        return AsyncQueuesResource(self)

    @cached_property
    def api_gateway(self) -> AsyncAPIGatewayResource:
        from .resources.api_gateway import AsyncAPIGatewayResource

        return AsyncAPIGatewayResource(self)

    @cached_property
    def managed_transforms(self) -> AsyncManagedTransformsResource:
        from .resources.managed_transforms import AsyncManagedTransformsResource

        return AsyncManagedTransformsResource(self)

    @cached_property
    def page_shield(self) -> AsyncPageShieldResource:
        from .resources.page_shield import AsyncPageShieldResource

        return AsyncPageShieldResource(self)

    @cached_property
    def rulesets(self) -> AsyncRulesetsResource:
        from .resources.rulesets import AsyncRulesetsResource

        return AsyncRulesetsResource(self)

    @cached_property
    def url_normalization(self) -> AsyncURLNormalizationResource:
        from .resources.url_normalization import AsyncURLNormalizationResource

        return AsyncURLNormalizationResource(self)

    @cached_property
    def spectrum(self) -> AsyncSpectrumResource:
        from .resources.spectrum import AsyncSpectrumResource

        return AsyncSpectrumResource(self)

    @cached_property
    def addressing(self) -> AsyncAddressingResource:
        from .resources.addressing import AsyncAddressingResource

        return AsyncAddressingResource(self)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResource:
        from .resources.audit_logs import AsyncAuditLogsResource

        return AsyncAuditLogsResource(self)

    @cached_property
    def billing(self) -> AsyncBillingResource:
        from .resources.billing import AsyncBillingResource

        return AsyncBillingResource(self)

    @cached_property
    def brand_protection(self) -> AsyncBrandProtectionResource:
        from .resources.brand_protection import AsyncBrandProtectionResource

        return AsyncBrandProtectionResource(self)

    @cached_property
    def diagnostics(self) -> AsyncDiagnosticsResource:
        from .resources.diagnostics import AsyncDiagnosticsResource

        return AsyncDiagnosticsResource(self)

    @cached_property
    def images(self) -> AsyncImagesResource:
        from .resources.images import AsyncImagesResource

        return AsyncImagesResource(self)

    @cached_property
    def intel(self) -> AsyncIntelResource:
        from .resources.intel import AsyncIntelResource

        return AsyncIntelResource(self)

    @cached_property
    def magic_transit(self) -> AsyncMagicTransitResource:
        from .resources.magic_transit import AsyncMagicTransitResource

        return AsyncMagicTransitResource(self)

    @cached_property
    def magic_network_monitoring(self) -> AsyncMagicNetworkMonitoringResource:
        from .resources.magic_network_monitoring import AsyncMagicNetworkMonitoringResource

        return AsyncMagicNetworkMonitoringResource(self)

    @cached_property
    def magic_cloud_networking(self) -> AsyncMagicCloudNetworkingResource:
        from .resources.magic_cloud_networking import AsyncMagicCloudNetworkingResource

        return AsyncMagicCloudNetworkingResource(self)

    @cached_property
    def network_interconnects(self) -> AsyncNetworkInterconnectsResource:
        from .resources.network_interconnects import AsyncNetworkInterconnectsResource

        return AsyncNetworkInterconnectsResource(self)

    @cached_property
    def mtls_certificates(self) -> AsyncMTLSCertificatesResource:
        from .resources.mtls_certificates import AsyncMTLSCertificatesResource

        return AsyncMTLSCertificatesResource(self)

    @cached_property
    def pages(self) -> AsyncPagesResource:
        from .resources.pages import AsyncPagesResource

        return AsyncPagesResource(self)

    @cached_property
    def registrar(self) -> AsyncRegistrarResource:
        from .resources.registrar import AsyncRegistrarResource

        return AsyncRegistrarResource(self)

    @cached_property
    def request_tracers(self) -> AsyncRequestTracersResource:
        from .resources.request_tracers import AsyncRequestTracersResource

        return AsyncRequestTracersResource(self)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        from .resources.rules import AsyncRulesResource

        return AsyncRulesResource(self)

    @cached_property
    def stream(self) -> AsyncStreamResource:
        from .resources.stream import AsyncStreamResource

        return AsyncStreamResource(self)

    @cached_property
    def alerting(self) -> AsyncAlertingResource:
        from .resources.alerting import AsyncAlertingResource

        return AsyncAlertingResource(self)

    @cached_property
    def d1(self) -> AsyncD1Resource:
        from .resources.d1 import AsyncD1Resource

        return AsyncD1Resource(self)

    @cached_property
    def r2(self) -> AsyncR2Resource:
        from .resources.r2 import AsyncR2Resource

        return AsyncR2Resource(self)

    @cached_property
    def workers_for_platforms(self) -> AsyncWorkersForPlatformsResource:
        from .resources.workers_for_platforms import AsyncWorkersForPlatformsResource

        return AsyncWorkersForPlatformsResource(self)

    @cached_property
    def zero_trust(self) -> AsyncZeroTrustResource:
        from .resources.zero_trust import AsyncZeroTrustResource

        return AsyncZeroTrustResource(self)

    @cached_property
    def turnstile(self) -> AsyncTurnstileResource:
        from .resources.turnstile import AsyncTurnstileResource

        return AsyncTurnstileResource(self)

    @cached_property
    def hyperdrive(self) -> AsyncHyperdriveResource:
        from .resources.hyperdrive import AsyncHyperdriveResource

        return AsyncHyperdriveResource(self)

    @cached_property
    def rum(self) -> AsyncRUMResource:
        from .resources.rum import AsyncRUMResource

        return AsyncRUMResource(self)

    @cached_property
    def vectorize(self) -> AsyncVectorizeResource:
        from .resources.vectorize import AsyncVectorizeResource

        return AsyncVectorizeResource(self)

    @cached_property
    def url_scanner(self) -> AsyncURLScannerResource:
        from .resources.url_scanner import AsyncURLScannerResource

        return AsyncURLScannerResource(self)

    @cached_property
    def radar(self) -> AsyncRadarResource:
        from .resources.radar import AsyncRadarResource

        return AsyncRadarResource(self)

    @cached_property
    def bot_management(self) -> AsyncBotManagementResource:
        from .resources.bot_management import AsyncBotManagementResource

        return AsyncBotManagementResource(self)

    @cached_property
    def origin_post_quantum_encryption(self) -> AsyncOriginPostQuantumEncryptionResource:
        from .resources.origin_post_quantum_encryption import AsyncOriginPostQuantumEncryptionResource

        return AsyncOriginPostQuantumEncryptionResource(self)

    @cached_property
    def zaraz(self) -> AsyncZarazResource:
        from .resources.zaraz import AsyncZarazResource

        return AsyncZarazResource(self)

    @cached_property
    def speed(self) -> AsyncSpeedResource:
        from .resources.speed import AsyncSpeedResource

        return AsyncSpeedResource(self)

    @cached_property
    def dcv_delegation(self) -> AsyncDCVDelegationResource:
        from .resources.dcv_delegation import AsyncDCVDelegationResource

        return AsyncDCVDelegationResource(self)

    @cached_property
    def hostnames(self) -> AsyncHostnamesResource:
        from .resources.hostnames import AsyncHostnamesResource

        return AsyncHostnamesResource(self)

    @cached_property
    def snippets(self) -> AsyncSnippetsResource:
        from .resources.snippets import AsyncSnippetsResource

        return AsyncSnippetsResource(self)

    @cached_property
    def calls(self) -> AsyncCallsResource:
        from .resources.calls import AsyncCallsResource

        return AsyncCallsResource(self)

    @cached_property
    def cloudforce_one(self) -> AsyncCloudforceOneResource:
        from .resources.cloudforce_one import AsyncCloudforceOneResource

        return AsyncCloudforceOneResource(self)

    @cached_property
    def ai_gateway(self) -> AsyncAIGatewayResource:
        from .resources.ai_gateway import AsyncAIGatewayResource

        return AsyncAIGatewayResource(self)

    @cached_property
    def iam(self) -> AsyncIAMResource:
        from .resources.iam import AsyncIAMResource

        return AsyncIAMResource(self)

    @cached_property
    def cloud_connector(self) -> AsyncCloudConnectorResource:
        from .resources.cloud_connector import AsyncCloudConnectorResource

        return AsyncCloudConnectorResource(self)

    @cached_property
    def botnet_feed(self) -> AsyncBotnetFeedResource:
        from .resources.botnet_feed import AsyncBotnetFeedResource

        return AsyncBotnetFeedResource(self)

    @cached_property
    def security_txt(self) -> AsyncSecurityTXTResource:
        from .resources.security_txt import AsyncSecurityTXTResource

        return AsyncSecurityTXTResource(self)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResource:
        from .resources.workflows import AsyncWorkflowsResource

        return AsyncWorkflowsResource(self)

    @cached_property
    def resource_sharing(self) -> AsyncResourceSharingResource:
        from .resources.resource_sharing import AsyncResourceSharingResource

        return AsyncResourceSharingResource(self)

    @cached_property
    def leaked_credential_checks(self) -> AsyncLeakedCredentialChecksResource:
        from .resources.leaked_credential_checks import AsyncLeakedCredentialChecksResource

        return AsyncLeakedCredentialChecksResource(self)

    @cached_property
    def content_scanning(self) -> AsyncContentScanningResource:
        from .resources.content_scanning import AsyncContentScanningResource

        return AsyncContentScanningResource(self)

    @cached_property
    def abuse_reports(self) -> AsyncAbuseReportsResource:
        from .resources.abuse_reports import AsyncAbuseReportsResource

        return AsyncAbuseReportsResource(self)

    @cached_property
    def ai(self) -> AsyncAIResource:
        from .resources.ai import AsyncAIResource

        return AsyncAIResource(self)

    @cached_property
    def security_center(self) -> AsyncSecurityCenterResource:
        from .resources.security_center import AsyncSecurityCenterResource

        return AsyncSecurityCenterResource(self)

    @cached_property
    def browser_rendering(self) -> AsyncBrowserRenderingResource:
        from .resources.browser_rendering import AsyncBrowserRenderingResource

        return AsyncBrowserRenderingResource(self)

    @cached_property
    def custom_pages(self) -> AsyncCustomPagesResource:
        from .resources.custom_pages import AsyncCustomPagesResource

        return AsyncCustomPagesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncCloudflareWithRawResponse:
        return AsyncCloudflareWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudflareWithStreamedResponse:
        return AsyncCloudflareWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self._api_email:
            return self._api_email
        if self._api_key:
            return self._api_key
        if self._api_token:
            return self._api_token
        if self._user_service_key:
            return self._user_service_key
        return {}

    @property
    def _api_email(self) -> dict[str, str]:
        api_email = self.api_email
        if api_email is None:
            return {}
        return {"X-Auth-Email": api_email}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-Auth-Key": api_key}

    @property
    def _api_token(self) -> dict[str, str]:
        api_token = self.api_token
        if api_token is None:
            return {}
        return {"Authorization": f"Bearer {api_token}"}

    @property
    def _user_service_key(self) -> dict[str, str]:
        user_service_key = self.user_service_key
        if user_service_key is None:
            return {}
        return {"X-Auth-User-Service-Key": user_service_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "X-Auth-Key": self.api_key if self.api_key is not None else Omit(),
            "X-Auth-Email": self.api_email if self.api_email is not None else Omit(),
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_email and headers.get("X-Auth-Email"):
            return
        if isinstance(custom_headers.get("X-Auth-Email"), Omit):
            return

        if self.api_key and headers.get("X-Auth-Key"):
            return
        if isinstance(custom_headers.get("X-Auth-Key"), Omit):
            return

        if self.api_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.user_service_key and headers.get("X-Auth-User-Service-Key"):
            return
        if isinstance(custom_headers.get("X-Auth-User-Service-Key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected one of api_email, api_key, api_token or user_service_key to be set. Or for one of the `X-Auth-Email`, `X-Auth-Key`, `Authorization` or `X-Auth-User-Service-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_token: str | None = None,
        api_key: str | None = None,
        api_email: str | None = None,
        user_service_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_token=api_token or self.api_token,
            api_key=api_key or self.api_key,
            api_email=api_email or self.api_email,
            user_service_key=user_service_key or self.user_service_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CloudflareWithRawResponse:
    _client: Cloudflare

    def __init__(self, client: Cloudflare) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def origin_ca_certificates(self) -> origin_ca_certificates.OriginCACertificatesResourceWithRawResponse:
        from .resources.origin_ca_certificates import OriginCACertificatesResourceWithRawResponse

        return OriginCACertificatesResourceWithRawResponse(self._client.origin_ca_certificates)

    @cached_property
    def ips(self) -> ips.IPsResourceWithRawResponse:
        from .resources.ips import IPsResourceWithRawResponse

        return IPsResourceWithRawResponse(self._client.ips)

    @cached_property
    def memberships(self) -> memberships.MembershipsResourceWithRawResponse:
        from .resources.memberships import MembershipsResourceWithRawResponse

        return MembershipsResourceWithRawResponse(self._client.memberships)

    @cached_property
    def user(self) -> user.UserResourceWithRawResponse:
        from .resources.user import UserResourceWithRawResponse

        return UserResourceWithRawResponse(self._client.user)

    @cached_property
    def zones(self) -> zones.ZonesResourceWithRawResponse:
        from .resources.zones import ZonesResourceWithRawResponse

        return ZonesResourceWithRawResponse(self._client.zones)

    @cached_property
    def load_balancers(self) -> load_balancers.LoadBalancersResourceWithRawResponse:
        from .resources.load_balancers import LoadBalancersResourceWithRawResponse

        return LoadBalancersResourceWithRawResponse(self._client.load_balancers)

    @cached_property
    def cache(self) -> cache.CacheResourceWithRawResponse:
        from .resources.cache import CacheResourceWithRawResponse

        return CacheResourceWithRawResponse(self._client.cache)

    @cached_property
    def ssl(self) -> ssl.SSLResourceWithRawResponse:
        from .resources.ssl import SSLResourceWithRawResponse

        return SSLResourceWithRawResponse(self._client.ssl)

    @cached_property
    def acm(self) -> acm.ACMResourceWithRawResponse:
        from .resources.acm import ACMResourceWithRawResponse

        return ACMResourceWithRawResponse(self._client.acm)

    @cached_property
    def argo(self) -> argo.ArgoResourceWithRawResponse:
        from .resources.argo import ArgoResourceWithRawResponse

        return ArgoResourceWithRawResponse(self._client.argo)

    @cached_property
    def certificate_authorities(self) -> certificate_authorities.CertificateAuthoritiesResourceWithRawResponse:
        from .resources.certificate_authorities import CertificateAuthoritiesResourceWithRawResponse

        return CertificateAuthoritiesResourceWithRawResponse(self._client.certificate_authorities)

    @cached_property
    def client_certificates(self) -> client_certificates.ClientCertificatesResourceWithRawResponse:
        from .resources.client_certificates import ClientCertificatesResourceWithRawResponse

        return ClientCertificatesResourceWithRawResponse(self._client.client_certificates)

    @cached_property
    def custom_certificates(self) -> custom_certificates.CustomCertificatesResourceWithRawResponse:
        from .resources.custom_certificates import CustomCertificatesResourceWithRawResponse

        return CustomCertificatesResourceWithRawResponse(self._client.custom_certificates)

    @cached_property
    def custom_hostnames(self) -> custom_hostnames.CustomHostnamesResourceWithRawResponse:
        from .resources.custom_hostnames import CustomHostnamesResourceWithRawResponse

        return CustomHostnamesResourceWithRawResponse(self._client.custom_hostnames)

    @cached_property
    def custom_nameservers(self) -> custom_nameservers.CustomNameserversResourceWithRawResponse:
        from .resources.custom_nameservers import CustomNameserversResourceWithRawResponse

        return CustomNameserversResourceWithRawResponse(self._client.custom_nameservers)

    @cached_property
    def dns_firewall(self) -> dns_firewall.DNSFirewallResourceWithRawResponse:
        from .resources.dns_firewall import DNSFirewallResourceWithRawResponse

        return DNSFirewallResourceWithRawResponse(self._client.dns_firewall)

    @cached_property
    def dns(self) -> dns.DNSResourceWithRawResponse:
        from .resources.dns import DNSResourceWithRawResponse

        return DNSResourceWithRawResponse(self._client.dns)

    @cached_property
    def email_security(self) -> email_security.EmailSecurityResourceWithRawResponse:
        from .resources.email_security import EmailSecurityResourceWithRawResponse

        return EmailSecurityResourceWithRawResponse(self._client.email_security)

    @cached_property
    def email_routing(self) -> email_routing.EmailRoutingResourceWithRawResponse:
        from .resources.email_routing import EmailRoutingResourceWithRawResponse

        return EmailRoutingResourceWithRawResponse(self._client.email_routing)

    @cached_property
    def filters(self) -> filters.FiltersResourceWithRawResponse:
        from .resources.filters import FiltersResourceWithRawResponse

        return FiltersResourceWithRawResponse(self._client.filters)

    @cached_property
    def firewall(self) -> firewall.FirewallResourceWithRawResponse:
        from .resources.firewall import FirewallResourceWithRawResponse

        return FirewallResourceWithRawResponse(self._client.firewall)

    @cached_property
    def healthchecks(self) -> healthchecks.HealthchecksResourceWithRawResponse:
        from .resources.healthchecks import HealthchecksResourceWithRawResponse

        return HealthchecksResourceWithRawResponse(self._client.healthchecks)

    @cached_property
    def keyless_certificates(self) -> keyless_certificates.KeylessCertificatesResourceWithRawResponse:
        from .resources.keyless_certificates import KeylessCertificatesResourceWithRawResponse

        return KeylessCertificatesResourceWithRawResponse(self._client.keyless_certificates)

    @cached_property
    def logpush(self) -> logpush.LogpushResourceWithRawResponse:
        from .resources.logpush import LogpushResourceWithRawResponse

        return LogpushResourceWithRawResponse(self._client.logpush)

    @cached_property
    def logs(self) -> logs.LogsResourceWithRawResponse:
        from .resources.logs import LogsResourceWithRawResponse

        return LogsResourceWithRawResponse(self._client.logs)

    @cached_property
    def origin_tls_client_auth(self) -> origin_tls_client_auth.OriginTLSClientAuthResourceWithRawResponse:
        from .resources.origin_tls_client_auth import OriginTLSClientAuthResourceWithRawResponse

        return OriginTLSClientAuthResourceWithRawResponse(self._client.origin_tls_client_auth)

    @cached_property
    def page_rules(self) -> page_rules.PageRulesResourceWithRawResponse:
        from .resources.page_rules import PageRulesResourceWithRawResponse

        return PageRulesResourceWithRawResponse(self._client.page_rules)

    @cached_property
    def rate_limits(self) -> rate_limits.RateLimitsResourceWithRawResponse:
        from .resources.rate_limits import RateLimitsResourceWithRawResponse

        return RateLimitsResourceWithRawResponse(self._client.rate_limits)

    @cached_property
    def waiting_rooms(self) -> waiting_rooms.WaitingRoomsResourceWithRawResponse:
        from .resources.waiting_rooms import WaitingRoomsResourceWithRawResponse

        return WaitingRoomsResourceWithRawResponse(self._client.waiting_rooms)

    @cached_property
    def web3(self) -> web3.Web3ResourceWithRawResponse:
        from .resources.web3 import Web3ResourceWithRawResponse

        return Web3ResourceWithRawResponse(self._client.web3)

    @cached_property
    def workers(self) -> workers.WorkersResourceWithRawResponse:
        from .resources.workers import WorkersResourceWithRawResponse

        return WorkersResourceWithRawResponse(self._client.workers)

    @cached_property
    def kv(self) -> kv.KVResourceWithRawResponse:
        from .resources.kv import KVResourceWithRawResponse

        return KVResourceWithRawResponse(self._client.kv)

    @cached_property
    def durable_objects(self) -> durable_objects.DurableObjectsResourceWithRawResponse:
        from .resources.durable_objects import DurableObjectsResourceWithRawResponse

        return DurableObjectsResourceWithRawResponse(self._client.durable_objects)

    @cached_property
    def queues(self) -> queues.QueuesResourceWithRawResponse:
        from .resources.queues import QueuesResourceWithRawResponse

        return QueuesResourceWithRawResponse(self._client.queues)

    @cached_property
    def api_gateway(self) -> api_gateway.APIGatewayResourceWithRawResponse:
        from .resources.api_gateway import APIGatewayResourceWithRawResponse

        return APIGatewayResourceWithRawResponse(self._client.api_gateway)

    @cached_property
    def managed_transforms(self) -> managed_transforms.ManagedTransformsResourceWithRawResponse:
        from .resources.managed_transforms import ManagedTransformsResourceWithRawResponse

        return ManagedTransformsResourceWithRawResponse(self._client.managed_transforms)

    @cached_property
    def page_shield(self) -> page_shield.PageShieldResourceWithRawResponse:
        from .resources.page_shield import PageShieldResourceWithRawResponse

        return PageShieldResourceWithRawResponse(self._client.page_shield)

    @cached_property
    def rulesets(self) -> rulesets.RulesetsResourceWithRawResponse:
        from .resources.rulesets import RulesetsResourceWithRawResponse

        return RulesetsResourceWithRawResponse(self._client.rulesets)

    @cached_property
    def url_normalization(self) -> url_normalization.URLNormalizationResourceWithRawResponse:
        from .resources.url_normalization import URLNormalizationResourceWithRawResponse

        return URLNormalizationResourceWithRawResponse(self._client.url_normalization)

    @cached_property
    def spectrum(self) -> spectrum.SpectrumResourceWithRawResponse:
        from .resources.spectrum import SpectrumResourceWithRawResponse

        return SpectrumResourceWithRawResponse(self._client.spectrum)

    @cached_property
    def addressing(self) -> addressing.AddressingResourceWithRawResponse:
        from .resources.addressing import AddressingResourceWithRawResponse

        return AddressingResourceWithRawResponse(self._client.addressing)

    @cached_property
    def audit_logs(self) -> audit_logs.AuditLogsResourceWithRawResponse:
        from .resources.audit_logs import AuditLogsResourceWithRawResponse

        return AuditLogsResourceWithRawResponse(self._client.audit_logs)

    @cached_property
    def billing(self) -> billing.BillingResourceWithRawResponse:
        from .resources.billing import BillingResourceWithRawResponse

        return BillingResourceWithRawResponse(self._client.billing)

    @cached_property
    def brand_protection(self) -> brand_protection.BrandProtectionResourceWithRawResponse:
        from .resources.brand_protection import BrandProtectionResourceWithRawResponse

        return BrandProtectionResourceWithRawResponse(self._client.brand_protection)

    @cached_property
    def diagnostics(self) -> diagnostics.DiagnosticsResourceWithRawResponse:
        from .resources.diagnostics import DiagnosticsResourceWithRawResponse

        return DiagnosticsResourceWithRawResponse(self._client.diagnostics)

    @cached_property
    def images(self) -> images.ImagesResourceWithRawResponse:
        from .resources.images import ImagesResourceWithRawResponse

        return ImagesResourceWithRawResponse(self._client.images)

    @cached_property
    def intel(self) -> intel.IntelResourceWithRawResponse:
        from .resources.intel import IntelResourceWithRawResponse

        return IntelResourceWithRawResponse(self._client.intel)

    @cached_property
    def magic_transit(self) -> magic_transit.MagicTransitResourceWithRawResponse:
        from .resources.magic_transit import MagicTransitResourceWithRawResponse

        return MagicTransitResourceWithRawResponse(self._client.magic_transit)

    @cached_property
    def magic_network_monitoring(self) -> magic_network_monitoring.MagicNetworkMonitoringResourceWithRawResponse:
        from .resources.magic_network_monitoring import MagicNetworkMonitoringResourceWithRawResponse

        return MagicNetworkMonitoringResourceWithRawResponse(self._client.magic_network_monitoring)

    @cached_property
    def magic_cloud_networking(self) -> magic_cloud_networking.MagicCloudNetworkingResourceWithRawResponse:
        from .resources.magic_cloud_networking import MagicCloudNetworkingResourceWithRawResponse

        return MagicCloudNetworkingResourceWithRawResponse(self._client.magic_cloud_networking)

    @cached_property
    def network_interconnects(self) -> network_interconnects.NetworkInterconnectsResourceWithRawResponse:
        from .resources.network_interconnects import NetworkInterconnectsResourceWithRawResponse

        return NetworkInterconnectsResourceWithRawResponse(self._client.network_interconnects)

    @cached_property
    def mtls_certificates(self) -> mtls_certificates.MTLSCertificatesResourceWithRawResponse:
        from .resources.mtls_certificates import MTLSCertificatesResourceWithRawResponse

        return MTLSCertificatesResourceWithRawResponse(self._client.mtls_certificates)

    @cached_property
    def pages(self) -> pages.PagesResourceWithRawResponse:
        from .resources.pages import PagesResourceWithRawResponse

        return PagesResourceWithRawResponse(self._client.pages)

    @cached_property
    def registrar(self) -> registrar.RegistrarResourceWithRawResponse:
        from .resources.registrar import RegistrarResourceWithRawResponse

        return RegistrarResourceWithRawResponse(self._client.registrar)

    @cached_property
    def request_tracers(self) -> request_tracers.RequestTracersResourceWithRawResponse:
        from .resources.request_tracers import RequestTracersResourceWithRawResponse

        return RequestTracersResourceWithRawResponse(self._client.request_tracers)

    @cached_property
    def rules(self) -> rules.RulesResourceWithRawResponse:
        from .resources.rules import RulesResourceWithRawResponse

        return RulesResourceWithRawResponse(self._client.rules)

    @cached_property
    def stream(self) -> stream.StreamResourceWithRawResponse:
        from .resources.stream import StreamResourceWithRawResponse

        return StreamResourceWithRawResponse(self._client.stream)

    @cached_property
    def alerting(self) -> alerting.AlertingResourceWithRawResponse:
        from .resources.alerting import AlertingResourceWithRawResponse

        return AlertingResourceWithRawResponse(self._client.alerting)

    @cached_property
    def d1(self) -> d1.D1ResourceWithRawResponse:
        from .resources.d1 import D1ResourceWithRawResponse

        return D1ResourceWithRawResponse(self._client.d1)

    @cached_property
    def r2(self) -> r2.R2ResourceWithRawResponse:
        from .resources.r2 import R2ResourceWithRawResponse

        return R2ResourceWithRawResponse(self._client.r2)

    @cached_property
    def workers_for_platforms(self) -> workers_for_platforms.WorkersForPlatformsResourceWithRawResponse:
        from .resources.workers_for_platforms import WorkersForPlatformsResourceWithRawResponse

        return WorkersForPlatformsResourceWithRawResponse(self._client.workers_for_platforms)

    @cached_property
    def zero_trust(self) -> zero_trust.ZeroTrustResourceWithRawResponse:
        from .resources.zero_trust import ZeroTrustResourceWithRawResponse

        return ZeroTrustResourceWithRawResponse(self._client.zero_trust)

    @cached_property
    def turnstile(self) -> turnstile.TurnstileResourceWithRawResponse:
        from .resources.turnstile import TurnstileResourceWithRawResponse

        return TurnstileResourceWithRawResponse(self._client.turnstile)

    @cached_property
    def hyperdrive(self) -> hyperdrive.HyperdriveResourceWithRawResponse:
        from .resources.hyperdrive import HyperdriveResourceWithRawResponse

        return HyperdriveResourceWithRawResponse(self._client.hyperdrive)

    @cached_property
    def rum(self) -> rum.RUMResourceWithRawResponse:
        from .resources.rum import RUMResourceWithRawResponse

        return RUMResourceWithRawResponse(self._client.rum)

    @cached_property
    def vectorize(self) -> vectorize.VectorizeResourceWithRawResponse:
        from .resources.vectorize import VectorizeResourceWithRawResponse

        return VectorizeResourceWithRawResponse(self._client.vectorize)

    @cached_property
    def url_scanner(self) -> url_scanner.URLScannerResourceWithRawResponse:
        from .resources.url_scanner import URLScannerResourceWithRawResponse

        return URLScannerResourceWithRawResponse(self._client.url_scanner)

    @cached_property
    def radar(self) -> radar.RadarResourceWithRawResponse:
        from .resources.radar import RadarResourceWithRawResponse

        return RadarResourceWithRawResponse(self._client.radar)

    @cached_property
    def bot_management(self) -> bot_management.BotManagementResourceWithRawResponse:
        from .resources.bot_management import BotManagementResourceWithRawResponse

        return BotManagementResourceWithRawResponse(self._client.bot_management)

    @cached_property
    def origin_post_quantum_encryption(
        self,
    ) -> origin_post_quantum_encryption.OriginPostQuantumEncryptionResourceWithRawResponse:
        from .resources.origin_post_quantum_encryption import OriginPostQuantumEncryptionResourceWithRawResponse

        return OriginPostQuantumEncryptionResourceWithRawResponse(self._client.origin_post_quantum_encryption)

    @cached_property
    def zaraz(self) -> zaraz.ZarazResourceWithRawResponse:
        from .resources.zaraz import ZarazResourceWithRawResponse

        return ZarazResourceWithRawResponse(self._client.zaraz)

    @cached_property
    def speed(self) -> speed.SpeedResourceWithRawResponse:
        from .resources.speed import SpeedResourceWithRawResponse

        return SpeedResourceWithRawResponse(self._client.speed)

    @cached_property
    def dcv_delegation(self) -> dcv_delegation.DCVDelegationResourceWithRawResponse:
        from .resources.dcv_delegation import DCVDelegationResourceWithRawResponse

        return DCVDelegationResourceWithRawResponse(self._client.dcv_delegation)

    @cached_property
    def hostnames(self) -> hostnames.HostnamesResourceWithRawResponse:
        from .resources.hostnames import HostnamesResourceWithRawResponse

        return HostnamesResourceWithRawResponse(self._client.hostnames)

    @cached_property
    def snippets(self) -> snippets.SnippetsResourceWithRawResponse:
        from .resources.snippets import SnippetsResourceWithRawResponse

        return SnippetsResourceWithRawResponse(self._client.snippets)

    @cached_property
    def calls(self) -> calls.CallsResourceWithRawResponse:
        from .resources.calls import CallsResourceWithRawResponse

        return CallsResourceWithRawResponse(self._client.calls)

    @cached_property
    def cloudforce_one(self) -> cloudforce_one.CloudforceOneResourceWithRawResponse:
        from .resources.cloudforce_one import CloudforceOneResourceWithRawResponse

        return CloudforceOneResourceWithRawResponse(self._client.cloudforce_one)

    @cached_property
    def ai_gateway(self) -> ai_gateway.AIGatewayResourceWithRawResponse:
        from .resources.ai_gateway import AIGatewayResourceWithRawResponse

        return AIGatewayResourceWithRawResponse(self._client.ai_gateway)

    @cached_property
    def iam(self) -> iam.IAMResourceWithRawResponse:
        from .resources.iam import IAMResourceWithRawResponse

        return IAMResourceWithRawResponse(self._client.iam)

    @cached_property
    def cloud_connector(self) -> cloud_connector.CloudConnectorResourceWithRawResponse:
        from .resources.cloud_connector import CloudConnectorResourceWithRawResponse

        return CloudConnectorResourceWithRawResponse(self._client.cloud_connector)

    @cached_property
    def botnet_feed(self) -> botnet_feed.BotnetFeedResourceWithRawResponse:
        from .resources.botnet_feed import BotnetFeedResourceWithRawResponse

        return BotnetFeedResourceWithRawResponse(self._client.botnet_feed)

    @cached_property
    def security_txt(self) -> security_txt.SecurityTXTResourceWithRawResponse:
        from .resources.security_txt import SecurityTXTResourceWithRawResponse

        return SecurityTXTResourceWithRawResponse(self._client.security_txt)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithRawResponse:
        from .resources.workflows import WorkflowsResourceWithRawResponse

        return WorkflowsResourceWithRawResponse(self._client.workflows)

    @cached_property
    def resource_sharing(self) -> resource_sharing.ResourceSharingResourceWithRawResponse:
        from .resources.resource_sharing import ResourceSharingResourceWithRawResponse

        return ResourceSharingResourceWithRawResponse(self._client.resource_sharing)

    @cached_property
    def leaked_credential_checks(self) -> leaked_credential_checks.LeakedCredentialChecksResourceWithRawResponse:
        from .resources.leaked_credential_checks import LeakedCredentialChecksResourceWithRawResponse

        return LeakedCredentialChecksResourceWithRawResponse(self._client.leaked_credential_checks)

    @cached_property
    def content_scanning(self) -> content_scanning.ContentScanningResourceWithRawResponse:
        from .resources.content_scanning import ContentScanningResourceWithRawResponse

        return ContentScanningResourceWithRawResponse(self._client.content_scanning)

    @cached_property
    def abuse_reports(self) -> abuse_reports.AbuseReportsResourceWithRawResponse:
        from .resources.abuse_reports import AbuseReportsResourceWithRawResponse

        return AbuseReportsResourceWithRawResponse(self._client.abuse_reports)

    @cached_property
    def ai(self) -> ai.AIResourceWithRawResponse:
        from .resources.ai import AIResourceWithRawResponse

        return AIResourceWithRawResponse(self._client.ai)

    @cached_property
    def security_center(self) -> security_center.SecurityCenterResourceWithRawResponse:
        from .resources.security_center import SecurityCenterResourceWithRawResponse

        return SecurityCenterResourceWithRawResponse(self._client.security_center)

    @cached_property
    def browser_rendering(self) -> browser_rendering.BrowserRenderingResourceWithRawResponse:
        from .resources.browser_rendering import BrowserRenderingResourceWithRawResponse

        return BrowserRenderingResourceWithRawResponse(self._client.browser_rendering)

    @cached_property
    def custom_pages(self) -> custom_pages.CustomPagesResourceWithRawResponse:
        from .resources.custom_pages import CustomPagesResourceWithRawResponse

        return CustomPagesResourceWithRawResponse(self._client.custom_pages)


class AsyncCloudflareWithRawResponse:
    _client: AsyncCloudflare

    def __init__(self, client: AsyncCloudflare) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def origin_ca_certificates(self) -> origin_ca_certificates.AsyncOriginCACertificatesResourceWithRawResponse:
        from .resources.origin_ca_certificates import AsyncOriginCACertificatesResourceWithRawResponse

        return AsyncOriginCACertificatesResourceWithRawResponse(self._client.origin_ca_certificates)

    @cached_property
    def ips(self) -> ips.AsyncIPsResourceWithRawResponse:
        from .resources.ips import AsyncIPsResourceWithRawResponse

        return AsyncIPsResourceWithRawResponse(self._client.ips)

    @cached_property
    def memberships(self) -> memberships.AsyncMembershipsResourceWithRawResponse:
        from .resources.memberships import AsyncMembershipsResourceWithRawResponse

        return AsyncMembershipsResourceWithRawResponse(self._client.memberships)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithRawResponse:
        from .resources.user import AsyncUserResourceWithRawResponse

        return AsyncUserResourceWithRawResponse(self._client.user)

    @cached_property
    def zones(self) -> zones.AsyncZonesResourceWithRawResponse:
        from .resources.zones import AsyncZonesResourceWithRawResponse

        return AsyncZonesResourceWithRawResponse(self._client.zones)

    @cached_property
    def load_balancers(self) -> load_balancers.AsyncLoadBalancersResourceWithRawResponse:
        from .resources.load_balancers import AsyncLoadBalancersResourceWithRawResponse

        return AsyncLoadBalancersResourceWithRawResponse(self._client.load_balancers)

    @cached_property
    def cache(self) -> cache.AsyncCacheResourceWithRawResponse:
        from .resources.cache import AsyncCacheResourceWithRawResponse

        return AsyncCacheResourceWithRawResponse(self._client.cache)

    @cached_property
    def ssl(self) -> ssl.AsyncSSLResourceWithRawResponse:
        from .resources.ssl import AsyncSSLResourceWithRawResponse

        return AsyncSSLResourceWithRawResponse(self._client.ssl)

    @cached_property
    def acm(self) -> acm.AsyncACMResourceWithRawResponse:
        from .resources.acm import AsyncACMResourceWithRawResponse

        return AsyncACMResourceWithRawResponse(self._client.acm)

    @cached_property
    def argo(self) -> argo.AsyncArgoResourceWithRawResponse:
        from .resources.argo import AsyncArgoResourceWithRawResponse

        return AsyncArgoResourceWithRawResponse(self._client.argo)

    @cached_property
    def certificate_authorities(self) -> certificate_authorities.AsyncCertificateAuthoritiesResourceWithRawResponse:
        from .resources.certificate_authorities import AsyncCertificateAuthoritiesResourceWithRawResponse

        return AsyncCertificateAuthoritiesResourceWithRawResponse(self._client.certificate_authorities)

    @cached_property
    def client_certificates(self) -> client_certificates.AsyncClientCertificatesResourceWithRawResponse:
        from .resources.client_certificates import AsyncClientCertificatesResourceWithRawResponse

        return AsyncClientCertificatesResourceWithRawResponse(self._client.client_certificates)

    @cached_property
    def custom_certificates(self) -> custom_certificates.AsyncCustomCertificatesResourceWithRawResponse:
        from .resources.custom_certificates import AsyncCustomCertificatesResourceWithRawResponse

        return AsyncCustomCertificatesResourceWithRawResponse(self._client.custom_certificates)

    @cached_property
    def custom_hostnames(self) -> custom_hostnames.AsyncCustomHostnamesResourceWithRawResponse:
        from .resources.custom_hostnames import AsyncCustomHostnamesResourceWithRawResponse

        return AsyncCustomHostnamesResourceWithRawResponse(self._client.custom_hostnames)

    @cached_property
    def custom_nameservers(self) -> custom_nameservers.AsyncCustomNameserversResourceWithRawResponse:
        from .resources.custom_nameservers import AsyncCustomNameserversResourceWithRawResponse

        return AsyncCustomNameserversResourceWithRawResponse(self._client.custom_nameservers)

    @cached_property
    def dns_firewall(self) -> dns_firewall.AsyncDNSFirewallResourceWithRawResponse:
        from .resources.dns_firewall import AsyncDNSFirewallResourceWithRawResponse

        return AsyncDNSFirewallResourceWithRawResponse(self._client.dns_firewall)

    @cached_property
    def dns(self) -> dns.AsyncDNSResourceWithRawResponse:
        from .resources.dns import AsyncDNSResourceWithRawResponse

        return AsyncDNSResourceWithRawResponse(self._client.dns)

    @cached_property
    def email_security(self) -> email_security.AsyncEmailSecurityResourceWithRawResponse:
        from .resources.email_security import AsyncEmailSecurityResourceWithRawResponse

        return AsyncEmailSecurityResourceWithRawResponse(self._client.email_security)

    @cached_property
    def email_routing(self) -> email_routing.AsyncEmailRoutingResourceWithRawResponse:
        from .resources.email_routing import AsyncEmailRoutingResourceWithRawResponse

        return AsyncEmailRoutingResourceWithRawResponse(self._client.email_routing)

    @cached_property
    def filters(self) -> filters.AsyncFiltersResourceWithRawResponse:
        from .resources.filters import AsyncFiltersResourceWithRawResponse

        return AsyncFiltersResourceWithRawResponse(self._client.filters)

    @cached_property
    def firewall(self) -> firewall.AsyncFirewallResourceWithRawResponse:
        from .resources.firewall import AsyncFirewallResourceWithRawResponse

        return AsyncFirewallResourceWithRawResponse(self._client.firewall)

    @cached_property
    def healthchecks(self) -> healthchecks.AsyncHealthchecksResourceWithRawResponse:
        from .resources.healthchecks import AsyncHealthchecksResourceWithRawResponse

        return AsyncHealthchecksResourceWithRawResponse(self._client.healthchecks)

    @cached_property
    def keyless_certificates(self) -> keyless_certificates.AsyncKeylessCertificatesResourceWithRawResponse:
        from .resources.keyless_certificates import AsyncKeylessCertificatesResourceWithRawResponse

        return AsyncKeylessCertificatesResourceWithRawResponse(self._client.keyless_certificates)

    @cached_property
    def logpush(self) -> logpush.AsyncLogpushResourceWithRawResponse:
        from .resources.logpush import AsyncLogpushResourceWithRawResponse

        return AsyncLogpushResourceWithRawResponse(self._client.logpush)

    @cached_property
    def logs(self) -> logs.AsyncLogsResourceWithRawResponse:
        from .resources.logs import AsyncLogsResourceWithRawResponse

        return AsyncLogsResourceWithRawResponse(self._client.logs)

    @cached_property
    def origin_tls_client_auth(self) -> origin_tls_client_auth.AsyncOriginTLSClientAuthResourceWithRawResponse:
        from .resources.origin_tls_client_auth import AsyncOriginTLSClientAuthResourceWithRawResponse

        return AsyncOriginTLSClientAuthResourceWithRawResponse(self._client.origin_tls_client_auth)

    @cached_property
    def page_rules(self) -> page_rules.AsyncPageRulesResourceWithRawResponse:
        from .resources.page_rules import AsyncPageRulesResourceWithRawResponse

        return AsyncPageRulesResourceWithRawResponse(self._client.page_rules)

    @cached_property
    def rate_limits(self) -> rate_limits.AsyncRateLimitsResourceWithRawResponse:
        from .resources.rate_limits import AsyncRateLimitsResourceWithRawResponse

        return AsyncRateLimitsResourceWithRawResponse(self._client.rate_limits)

    @cached_property
    def waiting_rooms(self) -> waiting_rooms.AsyncWaitingRoomsResourceWithRawResponse:
        from .resources.waiting_rooms import AsyncWaitingRoomsResourceWithRawResponse

        return AsyncWaitingRoomsResourceWithRawResponse(self._client.waiting_rooms)

    @cached_property
    def web3(self) -> web3.AsyncWeb3ResourceWithRawResponse:
        from .resources.web3 import AsyncWeb3ResourceWithRawResponse

        return AsyncWeb3ResourceWithRawResponse(self._client.web3)

    @cached_property
    def workers(self) -> workers.AsyncWorkersResourceWithRawResponse:
        from .resources.workers import AsyncWorkersResourceWithRawResponse

        return AsyncWorkersResourceWithRawResponse(self._client.workers)

    @cached_property
    def kv(self) -> kv.AsyncKVResourceWithRawResponse:
        from .resources.kv import AsyncKVResourceWithRawResponse

        return AsyncKVResourceWithRawResponse(self._client.kv)

    @cached_property
    def durable_objects(self) -> durable_objects.AsyncDurableObjectsResourceWithRawResponse:
        from .resources.durable_objects import AsyncDurableObjectsResourceWithRawResponse

        return AsyncDurableObjectsResourceWithRawResponse(self._client.durable_objects)

    @cached_property
    def queues(self) -> queues.AsyncQueuesResourceWithRawResponse:
        from .resources.queues import AsyncQueuesResourceWithRawResponse

        return AsyncQueuesResourceWithRawResponse(self._client.queues)

    @cached_property
    def api_gateway(self) -> api_gateway.AsyncAPIGatewayResourceWithRawResponse:
        from .resources.api_gateway import AsyncAPIGatewayResourceWithRawResponse

        return AsyncAPIGatewayResourceWithRawResponse(self._client.api_gateway)

    @cached_property
    def managed_transforms(self) -> managed_transforms.AsyncManagedTransformsResourceWithRawResponse:
        from .resources.managed_transforms import AsyncManagedTransformsResourceWithRawResponse

        return AsyncManagedTransformsResourceWithRawResponse(self._client.managed_transforms)

    @cached_property
    def page_shield(self) -> page_shield.AsyncPageShieldResourceWithRawResponse:
        from .resources.page_shield import AsyncPageShieldResourceWithRawResponse

        return AsyncPageShieldResourceWithRawResponse(self._client.page_shield)

    @cached_property
    def rulesets(self) -> rulesets.AsyncRulesetsResourceWithRawResponse:
        from .resources.rulesets import AsyncRulesetsResourceWithRawResponse

        return AsyncRulesetsResourceWithRawResponse(self._client.rulesets)

    @cached_property
    def url_normalization(self) -> url_normalization.AsyncURLNormalizationResourceWithRawResponse:
        from .resources.url_normalization import AsyncURLNormalizationResourceWithRawResponse

        return AsyncURLNormalizationResourceWithRawResponse(self._client.url_normalization)

    @cached_property
    def spectrum(self) -> spectrum.AsyncSpectrumResourceWithRawResponse:
        from .resources.spectrum import AsyncSpectrumResourceWithRawResponse

        return AsyncSpectrumResourceWithRawResponse(self._client.spectrum)

    @cached_property
    def addressing(self) -> addressing.AsyncAddressingResourceWithRawResponse:
        from .resources.addressing import AsyncAddressingResourceWithRawResponse

        return AsyncAddressingResourceWithRawResponse(self._client.addressing)

    @cached_property
    def audit_logs(self) -> audit_logs.AsyncAuditLogsResourceWithRawResponse:
        from .resources.audit_logs import AsyncAuditLogsResourceWithRawResponse

        return AsyncAuditLogsResourceWithRawResponse(self._client.audit_logs)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithRawResponse:
        from .resources.billing import AsyncBillingResourceWithRawResponse

        return AsyncBillingResourceWithRawResponse(self._client.billing)

    @cached_property
    def brand_protection(self) -> brand_protection.AsyncBrandProtectionResourceWithRawResponse:
        from .resources.brand_protection import AsyncBrandProtectionResourceWithRawResponse

        return AsyncBrandProtectionResourceWithRawResponse(self._client.brand_protection)

    @cached_property
    def diagnostics(self) -> diagnostics.AsyncDiagnosticsResourceWithRawResponse:
        from .resources.diagnostics import AsyncDiagnosticsResourceWithRawResponse

        return AsyncDiagnosticsResourceWithRawResponse(self._client.diagnostics)

    @cached_property
    def images(self) -> images.AsyncImagesResourceWithRawResponse:
        from .resources.images import AsyncImagesResourceWithRawResponse

        return AsyncImagesResourceWithRawResponse(self._client.images)

    @cached_property
    def intel(self) -> intel.AsyncIntelResourceWithRawResponse:
        from .resources.intel import AsyncIntelResourceWithRawResponse

        return AsyncIntelResourceWithRawResponse(self._client.intel)

    @cached_property
    def magic_transit(self) -> magic_transit.AsyncMagicTransitResourceWithRawResponse:
        from .resources.magic_transit import AsyncMagicTransitResourceWithRawResponse

        return AsyncMagicTransitResourceWithRawResponse(self._client.magic_transit)

    @cached_property
    def magic_network_monitoring(self) -> magic_network_monitoring.AsyncMagicNetworkMonitoringResourceWithRawResponse:
        from .resources.magic_network_monitoring import AsyncMagicNetworkMonitoringResourceWithRawResponse

        return AsyncMagicNetworkMonitoringResourceWithRawResponse(self._client.magic_network_monitoring)

    @cached_property
    def magic_cloud_networking(self) -> magic_cloud_networking.AsyncMagicCloudNetworkingResourceWithRawResponse:
        from .resources.magic_cloud_networking import AsyncMagicCloudNetworkingResourceWithRawResponse

        return AsyncMagicCloudNetworkingResourceWithRawResponse(self._client.magic_cloud_networking)

    @cached_property
    def network_interconnects(self) -> network_interconnects.AsyncNetworkInterconnectsResourceWithRawResponse:
        from .resources.network_interconnects import AsyncNetworkInterconnectsResourceWithRawResponse

        return AsyncNetworkInterconnectsResourceWithRawResponse(self._client.network_interconnects)

    @cached_property
    def mtls_certificates(self) -> mtls_certificates.AsyncMTLSCertificatesResourceWithRawResponse:
        from .resources.mtls_certificates import AsyncMTLSCertificatesResourceWithRawResponse

        return AsyncMTLSCertificatesResourceWithRawResponse(self._client.mtls_certificates)

    @cached_property
    def pages(self) -> pages.AsyncPagesResourceWithRawResponse:
        from .resources.pages import AsyncPagesResourceWithRawResponse

        return AsyncPagesResourceWithRawResponse(self._client.pages)

    @cached_property
    def registrar(self) -> registrar.AsyncRegistrarResourceWithRawResponse:
        from .resources.registrar import AsyncRegistrarResourceWithRawResponse

        return AsyncRegistrarResourceWithRawResponse(self._client.registrar)

    @cached_property
    def request_tracers(self) -> request_tracers.AsyncRequestTracersResourceWithRawResponse:
        from .resources.request_tracers import AsyncRequestTracersResourceWithRawResponse

        return AsyncRequestTracersResourceWithRawResponse(self._client.request_tracers)

    @cached_property
    def rules(self) -> rules.AsyncRulesResourceWithRawResponse:
        from .resources.rules import AsyncRulesResourceWithRawResponse

        return AsyncRulesResourceWithRawResponse(self._client.rules)

    @cached_property
    def stream(self) -> stream.AsyncStreamResourceWithRawResponse:
        from .resources.stream import AsyncStreamResourceWithRawResponse

        return AsyncStreamResourceWithRawResponse(self._client.stream)

    @cached_property
    def alerting(self) -> alerting.AsyncAlertingResourceWithRawResponse:
        from .resources.alerting import AsyncAlertingResourceWithRawResponse

        return AsyncAlertingResourceWithRawResponse(self._client.alerting)

    @cached_property
    def d1(self) -> d1.AsyncD1ResourceWithRawResponse:
        from .resources.d1 import AsyncD1ResourceWithRawResponse

        return AsyncD1ResourceWithRawResponse(self._client.d1)

    @cached_property
    def r2(self) -> r2.AsyncR2ResourceWithRawResponse:
        from .resources.r2 import AsyncR2ResourceWithRawResponse

        return AsyncR2ResourceWithRawResponse(self._client.r2)

    @cached_property
    def workers_for_platforms(self) -> workers_for_platforms.AsyncWorkersForPlatformsResourceWithRawResponse:
        from .resources.workers_for_platforms import AsyncWorkersForPlatformsResourceWithRawResponse

        return AsyncWorkersForPlatformsResourceWithRawResponse(self._client.workers_for_platforms)

    @cached_property
    def zero_trust(self) -> zero_trust.AsyncZeroTrustResourceWithRawResponse:
        from .resources.zero_trust import AsyncZeroTrustResourceWithRawResponse

        return AsyncZeroTrustResourceWithRawResponse(self._client.zero_trust)

    @cached_property
    def turnstile(self) -> turnstile.AsyncTurnstileResourceWithRawResponse:
        from .resources.turnstile import AsyncTurnstileResourceWithRawResponse

        return AsyncTurnstileResourceWithRawResponse(self._client.turnstile)

    @cached_property
    def hyperdrive(self) -> hyperdrive.AsyncHyperdriveResourceWithRawResponse:
        from .resources.hyperdrive import AsyncHyperdriveResourceWithRawResponse

        return AsyncHyperdriveResourceWithRawResponse(self._client.hyperdrive)

    @cached_property
    def rum(self) -> rum.AsyncRUMResourceWithRawResponse:
        from .resources.rum import AsyncRUMResourceWithRawResponse

        return AsyncRUMResourceWithRawResponse(self._client.rum)

    @cached_property
    def vectorize(self) -> vectorize.AsyncVectorizeResourceWithRawResponse:
        from .resources.vectorize import AsyncVectorizeResourceWithRawResponse

        return AsyncVectorizeResourceWithRawResponse(self._client.vectorize)

    @cached_property
    def url_scanner(self) -> url_scanner.AsyncURLScannerResourceWithRawResponse:
        from .resources.url_scanner import AsyncURLScannerResourceWithRawResponse

        return AsyncURLScannerResourceWithRawResponse(self._client.url_scanner)

    @cached_property
    def radar(self) -> radar.AsyncRadarResourceWithRawResponse:
        from .resources.radar import AsyncRadarResourceWithRawResponse

        return AsyncRadarResourceWithRawResponse(self._client.radar)

    @cached_property
    def bot_management(self) -> bot_management.AsyncBotManagementResourceWithRawResponse:
        from .resources.bot_management import AsyncBotManagementResourceWithRawResponse

        return AsyncBotManagementResourceWithRawResponse(self._client.bot_management)

    @cached_property
    def origin_post_quantum_encryption(
        self,
    ) -> origin_post_quantum_encryption.AsyncOriginPostQuantumEncryptionResourceWithRawResponse:
        from .resources.origin_post_quantum_encryption import AsyncOriginPostQuantumEncryptionResourceWithRawResponse

        return AsyncOriginPostQuantumEncryptionResourceWithRawResponse(self._client.origin_post_quantum_encryption)

    @cached_property
    def zaraz(self) -> zaraz.AsyncZarazResourceWithRawResponse:
        from .resources.zaraz import AsyncZarazResourceWithRawResponse

        return AsyncZarazResourceWithRawResponse(self._client.zaraz)

    @cached_property
    def speed(self) -> speed.AsyncSpeedResourceWithRawResponse:
        from .resources.speed import AsyncSpeedResourceWithRawResponse

        return AsyncSpeedResourceWithRawResponse(self._client.speed)

    @cached_property
    def dcv_delegation(self) -> dcv_delegation.AsyncDCVDelegationResourceWithRawResponse:
        from .resources.dcv_delegation import AsyncDCVDelegationResourceWithRawResponse

        return AsyncDCVDelegationResourceWithRawResponse(self._client.dcv_delegation)

    @cached_property
    def hostnames(self) -> hostnames.AsyncHostnamesResourceWithRawResponse:
        from .resources.hostnames import AsyncHostnamesResourceWithRawResponse

        return AsyncHostnamesResourceWithRawResponse(self._client.hostnames)

    @cached_property
    def snippets(self) -> snippets.AsyncSnippetsResourceWithRawResponse:
        from .resources.snippets import AsyncSnippetsResourceWithRawResponse

        return AsyncSnippetsResourceWithRawResponse(self._client.snippets)

    @cached_property
    def calls(self) -> calls.AsyncCallsResourceWithRawResponse:
        from .resources.calls import AsyncCallsResourceWithRawResponse

        return AsyncCallsResourceWithRawResponse(self._client.calls)

    @cached_property
    def cloudforce_one(self) -> cloudforce_one.AsyncCloudforceOneResourceWithRawResponse:
        from .resources.cloudforce_one import AsyncCloudforceOneResourceWithRawResponse

        return AsyncCloudforceOneResourceWithRawResponse(self._client.cloudforce_one)

    @cached_property
    def ai_gateway(self) -> ai_gateway.AsyncAIGatewayResourceWithRawResponse:
        from .resources.ai_gateway import AsyncAIGatewayResourceWithRawResponse

        return AsyncAIGatewayResourceWithRawResponse(self._client.ai_gateway)

    @cached_property
    def iam(self) -> iam.AsyncIAMResourceWithRawResponse:
        from .resources.iam import AsyncIAMResourceWithRawResponse

        return AsyncIAMResourceWithRawResponse(self._client.iam)

    @cached_property
    def cloud_connector(self) -> cloud_connector.AsyncCloudConnectorResourceWithRawResponse:
        from .resources.cloud_connector import AsyncCloudConnectorResourceWithRawResponse

        return AsyncCloudConnectorResourceWithRawResponse(self._client.cloud_connector)

    @cached_property
    def botnet_feed(self) -> botnet_feed.AsyncBotnetFeedResourceWithRawResponse:
        from .resources.botnet_feed import AsyncBotnetFeedResourceWithRawResponse

        return AsyncBotnetFeedResourceWithRawResponse(self._client.botnet_feed)

    @cached_property
    def security_txt(self) -> security_txt.AsyncSecurityTXTResourceWithRawResponse:
        from .resources.security_txt import AsyncSecurityTXTResourceWithRawResponse

        return AsyncSecurityTXTResourceWithRawResponse(self._client.security_txt)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithRawResponse:
        from .resources.workflows import AsyncWorkflowsResourceWithRawResponse

        return AsyncWorkflowsResourceWithRawResponse(self._client.workflows)

    @cached_property
    def resource_sharing(self) -> resource_sharing.AsyncResourceSharingResourceWithRawResponse:
        from .resources.resource_sharing import AsyncResourceSharingResourceWithRawResponse

        return AsyncResourceSharingResourceWithRawResponse(self._client.resource_sharing)

    @cached_property
    def leaked_credential_checks(self) -> leaked_credential_checks.AsyncLeakedCredentialChecksResourceWithRawResponse:
        from .resources.leaked_credential_checks import AsyncLeakedCredentialChecksResourceWithRawResponse

        return AsyncLeakedCredentialChecksResourceWithRawResponse(self._client.leaked_credential_checks)

    @cached_property
    def content_scanning(self) -> content_scanning.AsyncContentScanningResourceWithRawResponse:
        from .resources.content_scanning import AsyncContentScanningResourceWithRawResponse

        return AsyncContentScanningResourceWithRawResponse(self._client.content_scanning)

    @cached_property
    def abuse_reports(self) -> abuse_reports.AsyncAbuseReportsResourceWithRawResponse:
        from .resources.abuse_reports import AsyncAbuseReportsResourceWithRawResponse

        return AsyncAbuseReportsResourceWithRawResponse(self._client.abuse_reports)

    @cached_property
    def ai(self) -> ai.AsyncAIResourceWithRawResponse:
        from .resources.ai import AsyncAIResourceWithRawResponse

        return AsyncAIResourceWithRawResponse(self._client.ai)

    @cached_property
    def security_center(self) -> security_center.AsyncSecurityCenterResourceWithRawResponse:
        from .resources.security_center import AsyncSecurityCenterResourceWithRawResponse

        return AsyncSecurityCenterResourceWithRawResponse(self._client.security_center)

    @cached_property
    def browser_rendering(self) -> browser_rendering.AsyncBrowserRenderingResourceWithRawResponse:
        from .resources.browser_rendering import AsyncBrowserRenderingResourceWithRawResponse

        return AsyncBrowserRenderingResourceWithRawResponse(self._client.browser_rendering)

    @cached_property
    def custom_pages(self) -> custom_pages.AsyncCustomPagesResourceWithRawResponse:
        from .resources.custom_pages import AsyncCustomPagesResourceWithRawResponse

        return AsyncCustomPagesResourceWithRawResponse(self._client.custom_pages)


class CloudflareWithStreamedResponse:
    _client: Cloudflare

    def __init__(self, client: Cloudflare) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def origin_ca_certificates(self) -> origin_ca_certificates.OriginCACertificatesResourceWithStreamingResponse:
        from .resources.origin_ca_certificates import OriginCACertificatesResourceWithStreamingResponse

        return OriginCACertificatesResourceWithStreamingResponse(self._client.origin_ca_certificates)

    @cached_property
    def ips(self) -> ips.IPsResourceWithStreamingResponse:
        from .resources.ips import IPsResourceWithStreamingResponse

        return IPsResourceWithStreamingResponse(self._client.ips)

    @cached_property
    def memberships(self) -> memberships.MembershipsResourceWithStreamingResponse:
        from .resources.memberships import MembershipsResourceWithStreamingResponse

        return MembershipsResourceWithStreamingResponse(self._client.memberships)

    @cached_property
    def user(self) -> user.UserResourceWithStreamingResponse:
        from .resources.user import UserResourceWithStreamingResponse

        return UserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def zones(self) -> zones.ZonesResourceWithStreamingResponse:
        from .resources.zones import ZonesResourceWithStreamingResponse

        return ZonesResourceWithStreamingResponse(self._client.zones)

    @cached_property
    def load_balancers(self) -> load_balancers.LoadBalancersResourceWithStreamingResponse:
        from .resources.load_balancers import LoadBalancersResourceWithStreamingResponse

        return LoadBalancersResourceWithStreamingResponse(self._client.load_balancers)

    @cached_property
    def cache(self) -> cache.CacheResourceWithStreamingResponse:
        from .resources.cache import CacheResourceWithStreamingResponse

        return CacheResourceWithStreamingResponse(self._client.cache)

    @cached_property
    def ssl(self) -> ssl.SSLResourceWithStreamingResponse:
        from .resources.ssl import SSLResourceWithStreamingResponse

        return SSLResourceWithStreamingResponse(self._client.ssl)

    @cached_property
    def acm(self) -> acm.ACMResourceWithStreamingResponse:
        from .resources.acm import ACMResourceWithStreamingResponse

        return ACMResourceWithStreamingResponse(self._client.acm)

    @cached_property
    def argo(self) -> argo.ArgoResourceWithStreamingResponse:
        from .resources.argo import ArgoResourceWithStreamingResponse

        return ArgoResourceWithStreamingResponse(self._client.argo)

    @cached_property
    def certificate_authorities(self) -> certificate_authorities.CertificateAuthoritiesResourceWithStreamingResponse:
        from .resources.certificate_authorities import CertificateAuthoritiesResourceWithStreamingResponse

        return CertificateAuthoritiesResourceWithStreamingResponse(self._client.certificate_authorities)

    @cached_property
    def client_certificates(self) -> client_certificates.ClientCertificatesResourceWithStreamingResponse:
        from .resources.client_certificates import ClientCertificatesResourceWithStreamingResponse

        return ClientCertificatesResourceWithStreamingResponse(self._client.client_certificates)

    @cached_property
    def custom_certificates(self) -> custom_certificates.CustomCertificatesResourceWithStreamingResponse:
        from .resources.custom_certificates import CustomCertificatesResourceWithStreamingResponse

        return CustomCertificatesResourceWithStreamingResponse(self._client.custom_certificates)

    @cached_property
    def custom_hostnames(self) -> custom_hostnames.CustomHostnamesResourceWithStreamingResponse:
        from .resources.custom_hostnames import CustomHostnamesResourceWithStreamingResponse

        return CustomHostnamesResourceWithStreamingResponse(self._client.custom_hostnames)

    @cached_property
    def custom_nameservers(self) -> custom_nameservers.CustomNameserversResourceWithStreamingResponse:
        from .resources.custom_nameservers import CustomNameserversResourceWithStreamingResponse

        return CustomNameserversResourceWithStreamingResponse(self._client.custom_nameservers)

    @cached_property
    def dns_firewall(self) -> dns_firewall.DNSFirewallResourceWithStreamingResponse:
        from .resources.dns_firewall import DNSFirewallResourceWithStreamingResponse

        return DNSFirewallResourceWithStreamingResponse(self._client.dns_firewall)

    @cached_property
    def dns(self) -> dns.DNSResourceWithStreamingResponse:
        from .resources.dns import DNSResourceWithStreamingResponse

        return DNSResourceWithStreamingResponse(self._client.dns)

    @cached_property
    def email_security(self) -> email_security.EmailSecurityResourceWithStreamingResponse:
        from .resources.email_security import EmailSecurityResourceWithStreamingResponse

        return EmailSecurityResourceWithStreamingResponse(self._client.email_security)

    @cached_property
    def email_routing(self) -> email_routing.EmailRoutingResourceWithStreamingResponse:
        from .resources.email_routing import EmailRoutingResourceWithStreamingResponse

        return EmailRoutingResourceWithStreamingResponse(self._client.email_routing)

    @cached_property
    def filters(self) -> filters.FiltersResourceWithStreamingResponse:
        from .resources.filters import FiltersResourceWithStreamingResponse

        return FiltersResourceWithStreamingResponse(self._client.filters)

    @cached_property
    def firewall(self) -> firewall.FirewallResourceWithStreamingResponse:
        from .resources.firewall import FirewallResourceWithStreamingResponse

        return FirewallResourceWithStreamingResponse(self._client.firewall)

    @cached_property
    def healthchecks(self) -> healthchecks.HealthchecksResourceWithStreamingResponse:
        from .resources.healthchecks import HealthchecksResourceWithStreamingResponse

        return HealthchecksResourceWithStreamingResponse(self._client.healthchecks)

    @cached_property
    def keyless_certificates(self) -> keyless_certificates.KeylessCertificatesResourceWithStreamingResponse:
        from .resources.keyless_certificates import KeylessCertificatesResourceWithStreamingResponse

        return KeylessCertificatesResourceWithStreamingResponse(self._client.keyless_certificates)

    @cached_property
    def logpush(self) -> logpush.LogpushResourceWithStreamingResponse:
        from .resources.logpush import LogpushResourceWithStreamingResponse

        return LogpushResourceWithStreamingResponse(self._client.logpush)

    @cached_property
    def logs(self) -> logs.LogsResourceWithStreamingResponse:
        from .resources.logs import LogsResourceWithStreamingResponse

        return LogsResourceWithStreamingResponse(self._client.logs)

    @cached_property
    def origin_tls_client_auth(self) -> origin_tls_client_auth.OriginTLSClientAuthResourceWithStreamingResponse:
        from .resources.origin_tls_client_auth import OriginTLSClientAuthResourceWithStreamingResponse

        return OriginTLSClientAuthResourceWithStreamingResponse(self._client.origin_tls_client_auth)

    @cached_property
    def page_rules(self) -> page_rules.PageRulesResourceWithStreamingResponse:
        from .resources.page_rules import PageRulesResourceWithStreamingResponse

        return PageRulesResourceWithStreamingResponse(self._client.page_rules)

    @cached_property
    def rate_limits(self) -> rate_limits.RateLimitsResourceWithStreamingResponse:
        from .resources.rate_limits import RateLimitsResourceWithStreamingResponse

        return RateLimitsResourceWithStreamingResponse(self._client.rate_limits)

    @cached_property
    def waiting_rooms(self) -> waiting_rooms.WaitingRoomsResourceWithStreamingResponse:
        from .resources.waiting_rooms import WaitingRoomsResourceWithStreamingResponse

        return WaitingRoomsResourceWithStreamingResponse(self._client.waiting_rooms)

    @cached_property
    def web3(self) -> web3.Web3ResourceWithStreamingResponse:
        from .resources.web3 import Web3ResourceWithStreamingResponse

        return Web3ResourceWithStreamingResponse(self._client.web3)

    @cached_property
    def workers(self) -> workers.WorkersResourceWithStreamingResponse:
        from .resources.workers import WorkersResourceWithStreamingResponse

        return WorkersResourceWithStreamingResponse(self._client.workers)

    @cached_property
    def kv(self) -> kv.KVResourceWithStreamingResponse:
        from .resources.kv import KVResourceWithStreamingResponse

        return KVResourceWithStreamingResponse(self._client.kv)

    @cached_property
    def durable_objects(self) -> durable_objects.DurableObjectsResourceWithStreamingResponse:
        from .resources.durable_objects import DurableObjectsResourceWithStreamingResponse

        return DurableObjectsResourceWithStreamingResponse(self._client.durable_objects)

    @cached_property
    def queues(self) -> queues.QueuesResourceWithStreamingResponse:
        from .resources.queues import QueuesResourceWithStreamingResponse

        return QueuesResourceWithStreamingResponse(self._client.queues)

    @cached_property
    def api_gateway(self) -> api_gateway.APIGatewayResourceWithStreamingResponse:
        from .resources.api_gateway import APIGatewayResourceWithStreamingResponse

        return APIGatewayResourceWithStreamingResponse(self._client.api_gateway)

    @cached_property
    def managed_transforms(self) -> managed_transforms.ManagedTransformsResourceWithStreamingResponse:
        from .resources.managed_transforms import ManagedTransformsResourceWithStreamingResponse

        return ManagedTransformsResourceWithStreamingResponse(self._client.managed_transforms)

    @cached_property
    def page_shield(self) -> page_shield.PageShieldResourceWithStreamingResponse:
        from .resources.page_shield import PageShieldResourceWithStreamingResponse

        return PageShieldResourceWithStreamingResponse(self._client.page_shield)

    @cached_property
    def rulesets(self) -> rulesets.RulesetsResourceWithStreamingResponse:
        from .resources.rulesets import RulesetsResourceWithStreamingResponse

        return RulesetsResourceWithStreamingResponse(self._client.rulesets)

    @cached_property
    def url_normalization(self) -> url_normalization.URLNormalizationResourceWithStreamingResponse:
        from .resources.url_normalization import URLNormalizationResourceWithStreamingResponse

        return URLNormalizationResourceWithStreamingResponse(self._client.url_normalization)

    @cached_property
    def spectrum(self) -> spectrum.SpectrumResourceWithStreamingResponse:
        from .resources.spectrum import SpectrumResourceWithStreamingResponse

        return SpectrumResourceWithStreamingResponse(self._client.spectrum)

    @cached_property
    def addressing(self) -> addressing.AddressingResourceWithStreamingResponse:
        from .resources.addressing import AddressingResourceWithStreamingResponse

        return AddressingResourceWithStreamingResponse(self._client.addressing)

    @cached_property
    def audit_logs(self) -> audit_logs.AuditLogsResourceWithStreamingResponse:
        from .resources.audit_logs import AuditLogsResourceWithStreamingResponse

        return AuditLogsResourceWithStreamingResponse(self._client.audit_logs)

    @cached_property
    def billing(self) -> billing.BillingResourceWithStreamingResponse:
        from .resources.billing import BillingResourceWithStreamingResponse

        return BillingResourceWithStreamingResponse(self._client.billing)

    @cached_property
    def brand_protection(self) -> brand_protection.BrandProtectionResourceWithStreamingResponse:
        from .resources.brand_protection import BrandProtectionResourceWithStreamingResponse

        return BrandProtectionResourceWithStreamingResponse(self._client.brand_protection)

    @cached_property
    def diagnostics(self) -> diagnostics.DiagnosticsResourceWithStreamingResponse:
        from .resources.diagnostics import DiagnosticsResourceWithStreamingResponse

        return DiagnosticsResourceWithStreamingResponse(self._client.diagnostics)

    @cached_property
    def images(self) -> images.ImagesResourceWithStreamingResponse:
        from .resources.images import ImagesResourceWithStreamingResponse

        return ImagesResourceWithStreamingResponse(self._client.images)

    @cached_property
    def intel(self) -> intel.IntelResourceWithStreamingResponse:
        from .resources.intel import IntelResourceWithStreamingResponse

        return IntelResourceWithStreamingResponse(self._client.intel)

    @cached_property
    def magic_transit(self) -> magic_transit.MagicTransitResourceWithStreamingResponse:
        from .resources.magic_transit import MagicTransitResourceWithStreamingResponse

        return MagicTransitResourceWithStreamingResponse(self._client.magic_transit)

    @cached_property
    def magic_network_monitoring(self) -> magic_network_monitoring.MagicNetworkMonitoringResourceWithStreamingResponse:
        from .resources.magic_network_monitoring import MagicNetworkMonitoringResourceWithStreamingResponse

        return MagicNetworkMonitoringResourceWithStreamingResponse(self._client.magic_network_monitoring)

    @cached_property
    def magic_cloud_networking(self) -> magic_cloud_networking.MagicCloudNetworkingResourceWithStreamingResponse:
        from .resources.magic_cloud_networking import MagicCloudNetworkingResourceWithStreamingResponse

        return MagicCloudNetworkingResourceWithStreamingResponse(self._client.magic_cloud_networking)

    @cached_property
    def network_interconnects(self) -> network_interconnects.NetworkInterconnectsResourceWithStreamingResponse:
        from .resources.network_interconnects import NetworkInterconnectsResourceWithStreamingResponse

        return NetworkInterconnectsResourceWithStreamingResponse(self._client.network_interconnects)

    @cached_property
    def mtls_certificates(self) -> mtls_certificates.MTLSCertificatesResourceWithStreamingResponse:
        from .resources.mtls_certificates import MTLSCertificatesResourceWithStreamingResponse

        return MTLSCertificatesResourceWithStreamingResponse(self._client.mtls_certificates)

    @cached_property
    def pages(self) -> pages.PagesResourceWithStreamingResponse:
        from .resources.pages import PagesResourceWithStreamingResponse

        return PagesResourceWithStreamingResponse(self._client.pages)

    @cached_property
    def registrar(self) -> registrar.RegistrarResourceWithStreamingResponse:
        from .resources.registrar import RegistrarResourceWithStreamingResponse

        return RegistrarResourceWithStreamingResponse(self._client.registrar)

    @cached_property
    def request_tracers(self) -> request_tracers.RequestTracersResourceWithStreamingResponse:
        from .resources.request_tracers import RequestTracersResourceWithStreamingResponse

        return RequestTracersResourceWithStreamingResponse(self._client.request_tracers)

    @cached_property
    def rules(self) -> rules.RulesResourceWithStreamingResponse:
        from .resources.rules import RulesResourceWithStreamingResponse

        return RulesResourceWithStreamingResponse(self._client.rules)

    @cached_property
    def stream(self) -> stream.StreamResourceWithStreamingResponse:
        from .resources.stream import StreamResourceWithStreamingResponse

        return StreamResourceWithStreamingResponse(self._client.stream)

    @cached_property
    def alerting(self) -> alerting.AlertingResourceWithStreamingResponse:
        from .resources.alerting import AlertingResourceWithStreamingResponse

        return AlertingResourceWithStreamingResponse(self._client.alerting)

    @cached_property
    def d1(self) -> d1.D1ResourceWithStreamingResponse:
        from .resources.d1 import D1ResourceWithStreamingResponse

        return D1ResourceWithStreamingResponse(self._client.d1)

    @cached_property
    def r2(self) -> r2.R2ResourceWithStreamingResponse:
        from .resources.r2 import R2ResourceWithStreamingResponse

        return R2ResourceWithStreamingResponse(self._client.r2)

    @cached_property
    def workers_for_platforms(self) -> workers_for_platforms.WorkersForPlatformsResourceWithStreamingResponse:
        from .resources.workers_for_platforms import WorkersForPlatformsResourceWithStreamingResponse

        return WorkersForPlatformsResourceWithStreamingResponse(self._client.workers_for_platforms)

    @cached_property
    def zero_trust(self) -> zero_trust.ZeroTrustResourceWithStreamingResponse:
        from .resources.zero_trust import ZeroTrustResourceWithStreamingResponse

        return ZeroTrustResourceWithStreamingResponse(self._client.zero_trust)

    @cached_property
    def turnstile(self) -> turnstile.TurnstileResourceWithStreamingResponse:
        from .resources.turnstile import TurnstileResourceWithStreamingResponse

        return TurnstileResourceWithStreamingResponse(self._client.turnstile)

    @cached_property
    def hyperdrive(self) -> hyperdrive.HyperdriveResourceWithStreamingResponse:
        from .resources.hyperdrive import HyperdriveResourceWithStreamingResponse

        return HyperdriveResourceWithStreamingResponse(self._client.hyperdrive)

    @cached_property
    def rum(self) -> rum.RUMResourceWithStreamingResponse:
        from .resources.rum import RUMResourceWithStreamingResponse

        return RUMResourceWithStreamingResponse(self._client.rum)

    @cached_property
    def vectorize(self) -> vectorize.VectorizeResourceWithStreamingResponse:
        from .resources.vectorize import VectorizeResourceWithStreamingResponse

        return VectorizeResourceWithStreamingResponse(self._client.vectorize)

    @cached_property
    def url_scanner(self) -> url_scanner.URLScannerResourceWithStreamingResponse:
        from .resources.url_scanner import URLScannerResourceWithStreamingResponse

        return URLScannerResourceWithStreamingResponse(self._client.url_scanner)

    @cached_property
    def radar(self) -> radar.RadarResourceWithStreamingResponse:
        from .resources.radar import RadarResourceWithStreamingResponse

        return RadarResourceWithStreamingResponse(self._client.radar)

    @cached_property
    def bot_management(self) -> bot_management.BotManagementResourceWithStreamingResponse:
        from .resources.bot_management import BotManagementResourceWithStreamingResponse

        return BotManagementResourceWithStreamingResponse(self._client.bot_management)

    @cached_property
    def origin_post_quantum_encryption(
        self,
    ) -> origin_post_quantum_encryption.OriginPostQuantumEncryptionResourceWithStreamingResponse:
        from .resources.origin_post_quantum_encryption import OriginPostQuantumEncryptionResourceWithStreamingResponse

        return OriginPostQuantumEncryptionResourceWithStreamingResponse(self._client.origin_post_quantum_encryption)

    @cached_property
    def zaraz(self) -> zaraz.ZarazResourceWithStreamingResponse:
        from .resources.zaraz import ZarazResourceWithStreamingResponse

        return ZarazResourceWithStreamingResponse(self._client.zaraz)

    @cached_property
    def speed(self) -> speed.SpeedResourceWithStreamingResponse:
        from .resources.speed import SpeedResourceWithStreamingResponse

        return SpeedResourceWithStreamingResponse(self._client.speed)

    @cached_property
    def dcv_delegation(self) -> dcv_delegation.DCVDelegationResourceWithStreamingResponse:
        from .resources.dcv_delegation import DCVDelegationResourceWithStreamingResponse

        return DCVDelegationResourceWithStreamingResponse(self._client.dcv_delegation)

    @cached_property
    def hostnames(self) -> hostnames.HostnamesResourceWithStreamingResponse:
        from .resources.hostnames import HostnamesResourceWithStreamingResponse

        return HostnamesResourceWithStreamingResponse(self._client.hostnames)

    @cached_property
    def snippets(self) -> snippets.SnippetsResourceWithStreamingResponse:
        from .resources.snippets import SnippetsResourceWithStreamingResponse

        return SnippetsResourceWithStreamingResponse(self._client.snippets)

    @cached_property
    def calls(self) -> calls.CallsResourceWithStreamingResponse:
        from .resources.calls import CallsResourceWithStreamingResponse

        return CallsResourceWithStreamingResponse(self._client.calls)

    @cached_property
    def cloudforce_one(self) -> cloudforce_one.CloudforceOneResourceWithStreamingResponse:
        from .resources.cloudforce_one import CloudforceOneResourceWithStreamingResponse

        return CloudforceOneResourceWithStreamingResponse(self._client.cloudforce_one)

    @cached_property
    def ai_gateway(self) -> ai_gateway.AIGatewayResourceWithStreamingResponse:
        from .resources.ai_gateway import AIGatewayResourceWithStreamingResponse

        return AIGatewayResourceWithStreamingResponse(self._client.ai_gateway)

    @cached_property
    def iam(self) -> iam.IAMResourceWithStreamingResponse:
        from .resources.iam import IAMResourceWithStreamingResponse

        return IAMResourceWithStreamingResponse(self._client.iam)

    @cached_property
    def cloud_connector(self) -> cloud_connector.CloudConnectorResourceWithStreamingResponse:
        from .resources.cloud_connector import CloudConnectorResourceWithStreamingResponse

        return CloudConnectorResourceWithStreamingResponse(self._client.cloud_connector)

    @cached_property
    def botnet_feed(self) -> botnet_feed.BotnetFeedResourceWithStreamingResponse:
        from .resources.botnet_feed import BotnetFeedResourceWithStreamingResponse

        return BotnetFeedResourceWithStreamingResponse(self._client.botnet_feed)

    @cached_property
    def security_txt(self) -> security_txt.SecurityTXTResourceWithStreamingResponse:
        from .resources.security_txt import SecurityTXTResourceWithStreamingResponse

        return SecurityTXTResourceWithStreamingResponse(self._client.security_txt)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithStreamingResponse:
        from .resources.workflows import WorkflowsResourceWithStreamingResponse

        return WorkflowsResourceWithStreamingResponse(self._client.workflows)

    @cached_property
    def resource_sharing(self) -> resource_sharing.ResourceSharingResourceWithStreamingResponse:
        from .resources.resource_sharing import ResourceSharingResourceWithStreamingResponse

        return ResourceSharingResourceWithStreamingResponse(self._client.resource_sharing)

    @cached_property
    def leaked_credential_checks(self) -> leaked_credential_checks.LeakedCredentialChecksResourceWithStreamingResponse:
        from .resources.leaked_credential_checks import LeakedCredentialChecksResourceWithStreamingResponse

        return LeakedCredentialChecksResourceWithStreamingResponse(self._client.leaked_credential_checks)

    @cached_property
    def content_scanning(self) -> content_scanning.ContentScanningResourceWithStreamingResponse:
        from .resources.content_scanning import ContentScanningResourceWithStreamingResponse

        return ContentScanningResourceWithStreamingResponse(self._client.content_scanning)

    @cached_property
    def abuse_reports(self) -> abuse_reports.AbuseReportsResourceWithStreamingResponse:
        from .resources.abuse_reports import AbuseReportsResourceWithStreamingResponse

        return AbuseReportsResourceWithStreamingResponse(self._client.abuse_reports)

    @cached_property
    def ai(self) -> ai.AIResourceWithStreamingResponse:
        from .resources.ai import AIResourceWithStreamingResponse

        return AIResourceWithStreamingResponse(self._client.ai)

    @cached_property
    def security_center(self) -> security_center.SecurityCenterResourceWithStreamingResponse:
        from .resources.security_center import SecurityCenterResourceWithStreamingResponse

        return SecurityCenterResourceWithStreamingResponse(self._client.security_center)

    @cached_property
    def browser_rendering(self) -> browser_rendering.BrowserRenderingResourceWithStreamingResponse:
        from .resources.browser_rendering import BrowserRenderingResourceWithStreamingResponse

        return BrowserRenderingResourceWithStreamingResponse(self._client.browser_rendering)

    @cached_property
    def custom_pages(self) -> custom_pages.CustomPagesResourceWithStreamingResponse:
        from .resources.custom_pages import CustomPagesResourceWithStreamingResponse

        return CustomPagesResourceWithStreamingResponse(self._client.custom_pages)


class AsyncCloudflareWithStreamedResponse:
    _client: AsyncCloudflare

    def __init__(self, client: AsyncCloudflare) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def origin_ca_certificates(self) -> origin_ca_certificates.AsyncOriginCACertificatesResourceWithStreamingResponse:
        from .resources.origin_ca_certificates import AsyncOriginCACertificatesResourceWithStreamingResponse

        return AsyncOriginCACertificatesResourceWithStreamingResponse(self._client.origin_ca_certificates)

    @cached_property
    def ips(self) -> ips.AsyncIPsResourceWithStreamingResponse:
        from .resources.ips import AsyncIPsResourceWithStreamingResponse

        return AsyncIPsResourceWithStreamingResponse(self._client.ips)

    @cached_property
    def memberships(self) -> memberships.AsyncMembershipsResourceWithStreamingResponse:
        from .resources.memberships import AsyncMembershipsResourceWithStreamingResponse

        return AsyncMembershipsResourceWithStreamingResponse(self._client.memberships)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithStreamingResponse:
        from .resources.user import AsyncUserResourceWithStreamingResponse

        return AsyncUserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def zones(self) -> zones.AsyncZonesResourceWithStreamingResponse:
        from .resources.zones import AsyncZonesResourceWithStreamingResponse

        return AsyncZonesResourceWithStreamingResponse(self._client.zones)

    @cached_property
    def load_balancers(self) -> load_balancers.AsyncLoadBalancersResourceWithStreamingResponse:
        from .resources.load_balancers import AsyncLoadBalancersResourceWithStreamingResponse

        return AsyncLoadBalancersResourceWithStreamingResponse(self._client.load_balancers)

    @cached_property
    def cache(self) -> cache.AsyncCacheResourceWithStreamingResponse:
        from .resources.cache import AsyncCacheResourceWithStreamingResponse

        return AsyncCacheResourceWithStreamingResponse(self._client.cache)

    @cached_property
    def ssl(self) -> ssl.AsyncSSLResourceWithStreamingResponse:
        from .resources.ssl import AsyncSSLResourceWithStreamingResponse

        return AsyncSSLResourceWithStreamingResponse(self._client.ssl)

    @cached_property
    def acm(self) -> acm.AsyncACMResourceWithStreamingResponse:
        from .resources.acm import AsyncACMResourceWithStreamingResponse

        return AsyncACMResourceWithStreamingResponse(self._client.acm)

    @cached_property
    def argo(self) -> argo.AsyncArgoResourceWithStreamingResponse:
        from .resources.argo import AsyncArgoResourceWithStreamingResponse

        return AsyncArgoResourceWithStreamingResponse(self._client.argo)

    @cached_property
    def certificate_authorities(
        self,
    ) -> certificate_authorities.AsyncCertificateAuthoritiesResourceWithStreamingResponse:
        from .resources.certificate_authorities import AsyncCertificateAuthoritiesResourceWithStreamingResponse

        return AsyncCertificateAuthoritiesResourceWithStreamingResponse(self._client.certificate_authorities)

    @cached_property
    def client_certificates(self) -> client_certificates.AsyncClientCertificatesResourceWithStreamingResponse:
        from .resources.client_certificates import AsyncClientCertificatesResourceWithStreamingResponse

        return AsyncClientCertificatesResourceWithStreamingResponse(self._client.client_certificates)

    @cached_property
    def custom_certificates(self) -> custom_certificates.AsyncCustomCertificatesResourceWithStreamingResponse:
        from .resources.custom_certificates import AsyncCustomCertificatesResourceWithStreamingResponse

        return AsyncCustomCertificatesResourceWithStreamingResponse(self._client.custom_certificates)

    @cached_property
    def custom_hostnames(self) -> custom_hostnames.AsyncCustomHostnamesResourceWithStreamingResponse:
        from .resources.custom_hostnames import AsyncCustomHostnamesResourceWithStreamingResponse

        return AsyncCustomHostnamesResourceWithStreamingResponse(self._client.custom_hostnames)

    @cached_property
    def custom_nameservers(self) -> custom_nameservers.AsyncCustomNameserversResourceWithStreamingResponse:
        from .resources.custom_nameservers import AsyncCustomNameserversResourceWithStreamingResponse

        return AsyncCustomNameserversResourceWithStreamingResponse(self._client.custom_nameservers)

    @cached_property
    def dns_firewall(self) -> dns_firewall.AsyncDNSFirewallResourceWithStreamingResponse:
        from .resources.dns_firewall import AsyncDNSFirewallResourceWithStreamingResponse

        return AsyncDNSFirewallResourceWithStreamingResponse(self._client.dns_firewall)

    @cached_property
    def dns(self) -> dns.AsyncDNSResourceWithStreamingResponse:
        from .resources.dns import AsyncDNSResourceWithStreamingResponse

        return AsyncDNSResourceWithStreamingResponse(self._client.dns)

    @cached_property
    def email_security(self) -> email_security.AsyncEmailSecurityResourceWithStreamingResponse:
        from .resources.email_security import AsyncEmailSecurityResourceWithStreamingResponse

        return AsyncEmailSecurityResourceWithStreamingResponse(self._client.email_security)

    @cached_property
    def email_routing(self) -> email_routing.AsyncEmailRoutingResourceWithStreamingResponse:
        from .resources.email_routing import AsyncEmailRoutingResourceWithStreamingResponse

        return AsyncEmailRoutingResourceWithStreamingResponse(self._client.email_routing)

    @cached_property
    def filters(self) -> filters.AsyncFiltersResourceWithStreamingResponse:
        from .resources.filters import AsyncFiltersResourceWithStreamingResponse

        return AsyncFiltersResourceWithStreamingResponse(self._client.filters)

    @cached_property
    def firewall(self) -> firewall.AsyncFirewallResourceWithStreamingResponse:
        from .resources.firewall import AsyncFirewallResourceWithStreamingResponse

        return AsyncFirewallResourceWithStreamingResponse(self._client.firewall)

    @cached_property
    def healthchecks(self) -> healthchecks.AsyncHealthchecksResourceWithStreamingResponse:
        from .resources.healthchecks import AsyncHealthchecksResourceWithStreamingResponse

        return AsyncHealthchecksResourceWithStreamingResponse(self._client.healthchecks)

    @cached_property
    def keyless_certificates(self) -> keyless_certificates.AsyncKeylessCertificatesResourceWithStreamingResponse:
        from .resources.keyless_certificates import AsyncKeylessCertificatesResourceWithStreamingResponse

        return AsyncKeylessCertificatesResourceWithStreamingResponse(self._client.keyless_certificates)

    @cached_property
    def logpush(self) -> logpush.AsyncLogpushResourceWithStreamingResponse:
        from .resources.logpush import AsyncLogpushResourceWithStreamingResponse

        return AsyncLogpushResourceWithStreamingResponse(self._client.logpush)

    @cached_property
    def logs(self) -> logs.AsyncLogsResourceWithStreamingResponse:
        from .resources.logs import AsyncLogsResourceWithStreamingResponse

        return AsyncLogsResourceWithStreamingResponse(self._client.logs)

    @cached_property
    def origin_tls_client_auth(self) -> origin_tls_client_auth.AsyncOriginTLSClientAuthResourceWithStreamingResponse:
        from .resources.origin_tls_client_auth import AsyncOriginTLSClientAuthResourceWithStreamingResponse

        return AsyncOriginTLSClientAuthResourceWithStreamingResponse(self._client.origin_tls_client_auth)

    @cached_property
    def page_rules(self) -> page_rules.AsyncPageRulesResourceWithStreamingResponse:
        from .resources.page_rules import AsyncPageRulesResourceWithStreamingResponse

        return AsyncPageRulesResourceWithStreamingResponse(self._client.page_rules)

    @cached_property
    def rate_limits(self) -> rate_limits.AsyncRateLimitsResourceWithStreamingResponse:
        from .resources.rate_limits import AsyncRateLimitsResourceWithStreamingResponse

        return AsyncRateLimitsResourceWithStreamingResponse(self._client.rate_limits)

    @cached_property
    def waiting_rooms(self) -> waiting_rooms.AsyncWaitingRoomsResourceWithStreamingResponse:
        from .resources.waiting_rooms import AsyncWaitingRoomsResourceWithStreamingResponse

        return AsyncWaitingRoomsResourceWithStreamingResponse(self._client.waiting_rooms)

    @cached_property
    def web3(self) -> web3.AsyncWeb3ResourceWithStreamingResponse:
        from .resources.web3 import AsyncWeb3ResourceWithStreamingResponse

        return AsyncWeb3ResourceWithStreamingResponse(self._client.web3)

    @cached_property
    def workers(self) -> workers.AsyncWorkersResourceWithStreamingResponse:
        from .resources.workers import AsyncWorkersResourceWithStreamingResponse

        return AsyncWorkersResourceWithStreamingResponse(self._client.workers)

    @cached_property
    def kv(self) -> kv.AsyncKVResourceWithStreamingResponse:
        from .resources.kv import AsyncKVResourceWithStreamingResponse

        return AsyncKVResourceWithStreamingResponse(self._client.kv)

    @cached_property
    def durable_objects(self) -> durable_objects.AsyncDurableObjectsResourceWithStreamingResponse:
        from .resources.durable_objects import AsyncDurableObjectsResourceWithStreamingResponse

        return AsyncDurableObjectsResourceWithStreamingResponse(self._client.durable_objects)

    @cached_property
    def queues(self) -> queues.AsyncQueuesResourceWithStreamingResponse:
        from .resources.queues import AsyncQueuesResourceWithStreamingResponse

        return AsyncQueuesResourceWithStreamingResponse(self._client.queues)

    @cached_property
    def api_gateway(self) -> api_gateway.AsyncAPIGatewayResourceWithStreamingResponse:
        from .resources.api_gateway import AsyncAPIGatewayResourceWithStreamingResponse

        return AsyncAPIGatewayResourceWithStreamingResponse(self._client.api_gateway)

    @cached_property
    def managed_transforms(self) -> managed_transforms.AsyncManagedTransformsResourceWithStreamingResponse:
        from .resources.managed_transforms import AsyncManagedTransformsResourceWithStreamingResponse

        return AsyncManagedTransformsResourceWithStreamingResponse(self._client.managed_transforms)

    @cached_property
    def page_shield(self) -> page_shield.AsyncPageShieldResourceWithStreamingResponse:
        from .resources.page_shield import AsyncPageShieldResourceWithStreamingResponse

        return AsyncPageShieldResourceWithStreamingResponse(self._client.page_shield)

    @cached_property
    def rulesets(self) -> rulesets.AsyncRulesetsResourceWithStreamingResponse:
        from .resources.rulesets import AsyncRulesetsResourceWithStreamingResponse

        return AsyncRulesetsResourceWithStreamingResponse(self._client.rulesets)

    @cached_property
    def url_normalization(self) -> url_normalization.AsyncURLNormalizationResourceWithStreamingResponse:
        from .resources.url_normalization import AsyncURLNormalizationResourceWithStreamingResponse

        return AsyncURLNormalizationResourceWithStreamingResponse(self._client.url_normalization)

    @cached_property
    def spectrum(self) -> spectrum.AsyncSpectrumResourceWithStreamingResponse:
        from .resources.spectrum import AsyncSpectrumResourceWithStreamingResponse

        return AsyncSpectrumResourceWithStreamingResponse(self._client.spectrum)

    @cached_property
    def addressing(self) -> addressing.AsyncAddressingResourceWithStreamingResponse:
        from .resources.addressing import AsyncAddressingResourceWithStreamingResponse

        return AsyncAddressingResourceWithStreamingResponse(self._client.addressing)

    @cached_property
    def audit_logs(self) -> audit_logs.AsyncAuditLogsResourceWithStreamingResponse:
        from .resources.audit_logs import AsyncAuditLogsResourceWithStreamingResponse

        return AsyncAuditLogsResourceWithStreamingResponse(self._client.audit_logs)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithStreamingResponse:
        from .resources.billing import AsyncBillingResourceWithStreamingResponse

        return AsyncBillingResourceWithStreamingResponse(self._client.billing)

    @cached_property
    def brand_protection(self) -> brand_protection.AsyncBrandProtectionResourceWithStreamingResponse:
        from .resources.brand_protection import AsyncBrandProtectionResourceWithStreamingResponse

        return AsyncBrandProtectionResourceWithStreamingResponse(self._client.brand_protection)

    @cached_property
    def diagnostics(self) -> diagnostics.AsyncDiagnosticsResourceWithStreamingResponse:
        from .resources.diagnostics import AsyncDiagnosticsResourceWithStreamingResponse

        return AsyncDiagnosticsResourceWithStreamingResponse(self._client.diagnostics)

    @cached_property
    def images(self) -> images.AsyncImagesResourceWithStreamingResponse:
        from .resources.images import AsyncImagesResourceWithStreamingResponse

        return AsyncImagesResourceWithStreamingResponse(self._client.images)

    @cached_property
    def intel(self) -> intel.AsyncIntelResourceWithStreamingResponse:
        from .resources.intel import AsyncIntelResourceWithStreamingResponse

        return AsyncIntelResourceWithStreamingResponse(self._client.intel)

    @cached_property
    def magic_transit(self) -> magic_transit.AsyncMagicTransitResourceWithStreamingResponse:
        from .resources.magic_transit import AsyncMagicTransitResourceWithStreamingResponse

        return AsyncMagicTransitResourceWithStreamingResponse(self._client.magic_transit)

    @cached_property
    def magic_network_monitoring(
        self,
    ) -> magic_network_monitoring.AsyncMagicNetworkMonitoringResourceWithStreamingResponse:
        from .resources.magic_network_monitoring import AsyncMagicNetworkMonitoringResourceWithStreamingResponse

        return AsyncMagicNetworkMonitoringResourceWithStreamingResponse(self._client.magic_network_monitoring)

    @cached_property
    def magic_cloud_networking(self) -> magic_cloud_networking.AsyncMagicCloudNetworkingResourceWithStreamingResponse:
        from .resources.magic_cloud_networking import AsyncMagicCloudNetworkingResourceWithStreamingResponse

        return AsyncMagicCloudNetworkingResourceWithStreamingResponse(self._client.magic_cloud_networking)

    @cached_property
    def network_interconnects(self) -> network_interconnects.AsyncNetworkInterconnectsResourceWithStreamingResponse:
        from .resources.network_interconnects import AsyncNetworkInterconnectsResourceWithStreamingResponse

        return AsyncNetworkInterconnectsResourceWithStreamingResponse(self._client.network_interconnects)

    @cached_property
    def mtls_certificates(self) -> mtls_certificates.AsyncMTLSCertificatesResourceWithStreamingResponse:
        from .resources.mtls_certificates import AsyncMTLSCertificatesResourceWithStreamingResponse

        return AsyncMTLSCertificatesResourceWithStreamingResponse(self._client.mtls_certificates)

    @cached_property
    def pages(self) -> pages.AsyncPagesResourceWithStreamingResponse:
        from .resources.pages import AsyncPagesResourceWithStreamingResponse

        return AsyncPagesResourceWithStreamingResponse(self._client.pages)

    @cached_property
    def registrar(self) -> registrar.AsyncRegistrarResourceWithStreamingResponse:
        from .resources.registrar import AsyncRegistrarResourceWithStreamingResponse

        return AsyncRegistrarResourceWithStreamingResponse(self._client.registrar)

    @cached_property
    def request_tracers(self) -> request_tracers.AsyncRequestTracersResourceWithStreamingResponse:
        from .resources.request_tracers import AsyncRequestTracersResourceWithStreamingResponse

        return AsyncRequestTracersResourceWithStreamingResponse(self._client.request_tracers)

    @cached_property
    def rules(self) -> rules.AsyncRulesResourceWithStreamingResponse:
        from .resources.rules import AsyncRulesResourceWithStreamingResponse

        return AsyncRulesResourceWithStreamingResponse(self._client.rules)

    @cached_property
    def stream(self) -> stream.AsyncStreamResourceWithStreamingResponse:
        from .resources.stream import AsyncStreamResourceWithStreamingResponse

        return AsyncStreamResourceWithStreamingResponse(self._client.stream)

    @cached_property
    def alerting(self) -> alerting.AsyncAlertingResourceWithStreamingResponse:
        from .resources.alerting import AsyncAlertingResourceWithStreamingResponse

        return AsyncAlertingResourceWithStreamingResponse(self._client.alerting)

    @cached_property
    def d1(self) -> d1.AsyncD1ResourceWithStreamingResponse:
        from .resources.d1 import AsyncD1ResourceWithStreamingResponse

        return AsyncD1ResourceWithStreamingResponse(self._client.d1)

    @cached_property
    def r2(self) -> r2.AsyncR2ResourceWithStreamingResponse:
        from .resources.r2 import AsyncR2ResourceWithStreamingResponse

        return AsyncR2ResourceWithStreamingResponse(self._client.r2)

    @cached_property
    def workers_for_platforms(self) -> workers_for_platforms.AsyncWorkersForPlatformsResourceWithStreamingResponse:
        from .resources.workers_for_platforms import AsyncWorkersForPlatformsResourceWithStreamingResponse

        return AsyncWorkersForPlatformsResourceWithStreamingResponse(self._client.workers_for_platforms)

    @cached_property
    def zero_trust(self) -> zero_trust.AsyncZeroTrustResourceWithStreamingResponse:
        from .resources.zero_trust import AsyncZeroTrustResourceWithStreamingResponse

        return AsyncZeroTrustResourceWithStreamingResponse(self._client.zero_trust)

    @cached_property
    def turnstile(self) -> turnstile.AsyncTurnstileResourceWithStreamingResponse:
        from .resources.turnstile import AsyncTurnstileResourceWithStreamingResponse

        return AsyncTurnstileResourceWithStreamingResponse(self._client.turnstile)

    @cached_property
    def hyperdrive(self) -> hyperdrive.AsyncHyperdriveResourceWithStreamingResponse:
        from .resources.hyperdrive import AsyncHyperdriveResourceWithStreamingResponse

        return AsyncHyperdriveResourceWithStreamingResponse(self._client.hyperdrive)

    @cached_property
    def rum(self) -> rum.AsyncRUMResourceWithStreamingResponse:
        from .resources.rum import AsyncRUMResourceWithStreamingResponse

        return AsyncRUMResourceWithStreamingResponse(self._client.rum)

    @cached_property
    def vectorize(self) -> vectorize.AsyncVectorizeResourceWithStreamingResponse:
        from .resources.vectorize import AsyncVectorizeResourceWithStreamingResponse

        return AsyncVectorizeResourceWithStreamingResponse(self._client.vectorize)

    @cached_property
    def url_scanner(self) -> url_scanner.AsyncURLScannerResourceWithStreamingResponse:
        from .resources.url_scanner import AsyncURLScannerResourceWithStreamingResponse

        return AsyncURLScannerResourceWithStreamingResponse(self._client.url_scanner)

    @cached_property
    def radar(self) -> radar.AsyncRadarResourceWithStreamingResponse:
        from .resources.radar import AsyncRadarResourceWithStreamingResponse

        return AsyncRadarResourceWithStreamingResponse(self._client.radar)

    @cached_property
    def bot_management(self) -> bot_management.AsyncBotManagementResourceWithStreamingResponse:
        from .resources.bot_management import AsyncBotManagementResourceWithStreamingResponse

        return AsyncBotManagementResourceWithStreamingResponse(self._client.bot_management)

    @cached_property
    def origin_post_quantum_encryption(
        self,
    ) -> origin_post_quantum_encryption.AsyncOriginPostQuantumEncryptionResourceWithStreamingResponse:
        from .resources.origin_post_quantum_encryption import (
            AsyncOriginPostQuantumEncryptionResourceWithStreamingResponse,
        )

        return AsyncOriginPostQuantumEncryptionResourceWithStreamingResponse(
            self._client.origin_post_quantum_encryption
        )

    @cached_property
    def zaraz(self) -> zaraz.AsyncZarazResourceWithStreamingResponse:
        from .resources.zaraz import AsyncZarazResourceWithStreamingResponse

        return AsyncZarazResourceWithStreamingResponse(self._client.zaraz)

    @cached_property
    def speed(self) -> speed.AsyncSpeedResourceWithStreamingResponse:
        from .resources.speed import AsyncSpeedResourceWithStreamingResponse

        return AsyncSpeedResourceWithStreamingResponse(self._client.speed)

    @cached_property
    def dcv_delegation(self) -> dcv_delegation.AsyncDCVDelegationResourceWithStreamingResponse:
        from .resources.dcv_delegation import AsyncDCVDelegationResourceWithStreamingResponse

        return AsyncDCVDelegationResourceWithStreamingResponse(self._client.dcv_delegation)

    @cached_property
    def hostnames(self) -> hostnames.AsyncHostnamesResourceWithStreamingResponse:
        from .resources.hostnames import AsyncHostnamesResourceWithStreamingResponse

        return AsyncHostnamesResourceWithStreamingResponse(self._client.hostnames)

    @cached_property
    def snippets(self) -> snippets.AsyncSnippetsResourceWithStreamingResponse:
        from .resources.snippets import AsyncSnippetsResourceWithStreamingResponse

        return AsyncSnippetsResourceWithStreamingResponse(self._client.snippets)

    @cached_property
    def calls(self) -> calls.AsyncCallsResourceWithStreamingResponse:
        from .resources.calls import AsyncCallsResourceWithStreamingResponse

        return AsyncCallsResourceWithStreamingResponse(self._client.calls)

    @cached_property
    def cloudforce_one(self) -> cloudforce_one.AsyncCloudforceOneResourceWithStreamingResponse:
        from .resources.cloudforce_one import AsyncCloudforceOneResourceWithStreamingResponse

        return AsyncCloudforceOneResourceWithStreamingResponse(self._client.cloudforce_one)

    @cached_property
    def ai_gateway(self) -> ai_gateway.AsyncAIGatewayResourceWithStreamingResponse:
        from .resources.ai_gateway import AsyncAIGatewayResourceWithStreamingResponse

        return AsyncAIGatewayResourceWithStreamingResponse(self._client.ai_gateway)

    @cached_property
    def iam(self) -> iam.AsyncIAMResourceWithStreamingResponse:
        from .resources.iam import AsyncIAMResourceWithStreamingResponse

        return AsyncIAMResourceWithStreamingResponse(self._client.iam)

    @cached_property
    def cloud_connector(self) -> cloud_connector.AsyncCloudConnectorResourceWithStreamingResponse:
        from .resources.cloud_connector import AsyncCloudConnectorResourceWithStreamingResponse

        return AsyncCloudConnectorResourceWithStreamingResponse(self._client.cloud_connector)

    @cached_property
    def botnet_feed(self) -> botnet_feed.AsyncBotnetFeedResourceWithStreamingResponse:
        from .resources.botnet_feed import AsyncBotnetFeedResourceWithStreamingResponse

        return AsyncBotnetFeedResourceWithStreamingResponse(self._client.botnet_feed)

    @cached_property
    def security_txt(self) -> security_txt.AsyncSecurityTXTResourceWithStreamingResponse:
        from .resources.security_txt import AsyncSecurityTXTResourceWithStreamingResponse

        return AsyncSecurityTXTResourceWithStreamingResponse(self._client.security_txt)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithStreamingResponse:
        from .resources.workflows import AsyncWorkflowsResourceWithStreamingResponse

        return AsyncWorkflowsResourceWithStreamingResponse(self._client.workflows)

    @cached_property
    def resource_sharing(self) -> resource_sharing.AsyncResourceSharingResourceWithStreamingResponse:
        from .resources.resource_sharing import AsyncResourceSharingResourceWithStreamingResponse

        return AsyncResourceSharingResourceWithStreamingResponse(self._client.resource_sharing)

    @cached_property
    def leaked_credential_checks(
        self,
    ) -> leaked_credential_checks.AsyncLeakedCredentialChecksResourceWithStreamingResponse:
        from .resources.leaked_credential_checks import AsyncLeakedCredentialChecksResourceWithStreamingResponse

        return AsyncLeakedCredentialChecksResourceWithStreamingResponse(self._client.leaked_credential_checks)

    @cached_property
    def content_scanning(self) -> content_scanning.AsyncContentScanningResourceWithStreamingResponse:
        from .resources.content_scanning import AsyncContentScanningResourceWithStreamingResponse

        return AsyncContentScanningResourceWithStreamingResponse(self._client.content_scanning)

    @cached_property
    def abuse_reports(self) -> abuse_reports.AsyncAbuseReportsResourceWithStreamingResponse:
        from .resources.abuse_reports import AsyncAbuseReportsResourceWithStreamingResponse

        return AsyncAbuseReportsResourceWithStreamingResponse(self._client.abuse_reports)

    @cached_property
    def ai(self) -> ai.AsyncAIResourceWithStreamingResponse:
        from .resources.ai import AsyncAIResourceWithStreamingResponse

        return AsyncAIResourceWithStreamingResponse(self._client.ai)

    @cached_property
    def security_center(self) -> security_center.AsyncSecurityCenterResourceWithStreamingResponse:
        from .resources.security_center import AsyncSecurityCenterResourceWithStreamingResponse

        return AsyncSecurityCenterResourceWithStreamingResponse(self._client.security_center)

    @cached_property
    def browser_rendering(self) -> browser_rendering.AsyncBrowserRenderingResourceWithStreamingResponse:
        from .resources.browser_rendering import AsyncBrowserRenderingResourceWithStreamingResponse

        return AsyncBrowserRenderingResourceWithStreamingResponse(self._client.browser_rendering)

    @cached_property
    def custom_pages(self) -> custom_pages.AsyncCustomPagesResourceWithStreamingResponse:
        from .resources.custom_pages import AsyncCustomPagesResourceWithStreamingResponse

        return AsyncCustomPagesResourceWithStreamingResponse(self._client.custom_pages)


Client = Cloudflare

AsyncClient = AsyncCloudflare
