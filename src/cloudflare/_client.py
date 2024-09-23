# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
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
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Cloudflare",
    "AsyncCloudflare",
    "Client",
    "AsyncClient",
]


class Cloudflare(SyncAPIClient):
    accounts: resources.AccountsResource
    origin_ca_certificates: resources.OriginCACertificatesResource
    ips: resources.IPsResource
    memberships: resources.MembershipsResource
    user: resources.UserResource
    zones: resources.ZonesResource
    load_balancers: resources.LoadBalancersResource
    cache: resources.CacheResource
    ssl: resources.SSLResource
    acm: resources.ACMResource
    argo: resources.ArgoResource
    certificate_authorities: resources.CertificateAuthoritiesResource
    client_certificates: resources.ClientCertificatesResource
    custom_certificates: resources.CustomCertificatesResource
    custom_hostnames: resources.CustomHostnamesResource
    custom_nameservers: resources.CustomNameserversResource
    dns: resources.DNSResource
    dnssec: resources.DNSSECResource
    email_security: resources.EmailSecurityResource
    email_routing: resources.EmailRoutingResource
    filters: resources.FiltersResource
    firewall: resources.FirewallResource
    healthchecks: resources.HealthchecksResource
    keyless_certificates: resources.KeylessCertificatesResource
    logpush: resources.LogpushResource
    logs: resources.LogsResource
    origin_tls_client_auth: resources.OriginTLSClientAuthResource
    pagerules: resources.PagerulesResource
    rate_limits: resources.RateLimitsResource
    secondary_dns: resources.SecondaryDNSResource
    waiting_rooms: resources.WaitingRoomsResource
    web3: resources.Web3Resource
    workers: resources.WorkersResource
    kv: resources.KVResource
    durable_objects: resources.DurableObjectsResource
    queues: resources.QueuesResource
    api_gateway: resources.APIGatewayResource
    managed_transforms: resources.ManagedTransformsResource
    page_shield: resources.PageShieldResource
    rulesets: resources.RulesetsResource
    url_normalization: resources.URLNormalizationResource
    spectrum: resources.SpectrumResource
    addressing: resources.AddressingResource
    audit_logs: resources.AuditLogsResource
    billing: resources.BillingResource
    brand_protection: resources.BrandProtectionResource
    diagnostics: resources.DiagnosticsResource
    images: resources.ImagesResource
    intel: resources.IntelResource
    magic_transit: resources.MagicTransitResource
    magic_network_monitoring: resources.MagicNetworkMonitoringResource
    mtls_certificates: resources.MTLSCertificatesResource
    pages: resources.PagesResource
    registrar: resources.RegistrarResource
    request_tracers: resources.RequestTracersResource
    rules: resources.RulesResource
    storage: resources.StorageResource
    stream: resources.StreamResource
    alerting: resources.AlertingResource
    d1: resources.D1Resource
    r2: resources.R2Resource
    warp_connector: resources.WARPConnectorResource
    workers_for_platforms: resources.WorkersForPlatformsResource
    zero_trust: resources.ZeroTrustResource
    turnstile: resources.TurnstileResource
    hyperdrive: resources.HyperdriveResource
    rum: resources.RUMResource
    vectorize: resources.VectorizeResource
    url_scanner: resources.URLScannerResource
    radar: resources.RadarResource
    bot_management: resources.BotManagementResource
    origin_post_quantum_encryption: resources.OriginPostQuantumEncryptionResource
    speed: resources.SpeedResource
    dcv_delegation: resources.DCVDelegationResource
    hostnames: resources.HostnamesResource
    snippets: resources.SnippetsResource
    calls: resources.CallsResource
    cloudforce_one: resources.CloudforceOneResource
    ai_gateway: resources.AIGatewayResource
    iam: resources.IAMResource
    cloud_connector: resources.CloudConnectorResource
    botnet_feed: resources.BotnetFeedResource
    with_raw_response: CloudflareWithRawResponse
    with_streaming_response: CloudflareWithStreamedResponse

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
        """Construct a new synchronous cloudflare client instance.

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

        self.accounts = resources.AccountsResource(self)
        self.origin_ca_certificates = resources.OriginCACertificatesResource(self)
        self.ips = resources.IPsResource(self)
        self.memberships = resources.MembershipsResource(self)
        self.user = resources.UserResource(self)
        self.zones = resources.ZonesResource(self)
        self.load_balancers = resources.LoadBalancersResource(self)
        self.cache = resources.CacheResource(self)
        self.ssl = resources.SSLResource(self)
        self.acm = resources.ACMResource(self)
        self.argo = resources.ArgoResource(self)
        self.certificate_authorities = resources.CertificateAuthoritiesResource(self)
        self.client_certificates = resources.ClientCertificatesResource(self)
        self.custom_certificates = resources.CustomCertificatesResource(self)
        self.custom_hostnames = resources.CustomHostnamesResource(self)
        self.custom_nameservers = resources.CustomNameserversResource(self)
        self.dns = resources.DNSResource(self)
        self.dnssec = resources.DNSSECResource(self)
        self.email_security = resources.EmailSecurityResource(self)
        self.email_routing = resources.EmailRoutingResource(self)
        self.filters = resources.FiltersResource(self)
        self.firewall = resources.FirewallResource(self)
        self.healthchecks = resources.HealthchecksResource(self)
        self.keyless_certificates = resources.KeylessCertificatesResource(self)
        self.logpush = resources.LogpushResource(self)
        self.logs = resources.LogsResource(self)
        self.origin_tls_client_auth = resources.OriginTLSClientAuthResource(self)
        self.pagerules = resources.PagerulesResource(self)
        self.rate_limits = resources.RateLimitsResource(self)
        self.secondary_dns = resources.SecondaryDNSResource(self)
        self.waiting_rooms = resources.WaitingRoomsResource(self)
        self.web3 = resources.Web3Resource(self)
        self.workers = resources.WorkersResource(self)
        self.kv = resources.KVResource(self)
        self.durable_objects = resources.DurableObjectsResource(self)
        self.queues = resources.QueuesResource(self)
        self.api_gateway = resources.APIGatewayResource(self)
        self.managed_transforms = resources.ManagedTransformsResource(self)
        self.page_shield = resources.PageShieldResource(self)
        self.rulesets = resources.RulesetsResource(self)
        self.url_normalization = resources.URLNormalizationResource(self)
        self.spectrum = resources.SpectrumResource(self)
        self.addressing = resources.AddressingResource(self)
        self.audit_logs = resources.AuditLogsResource(self)
        self.billing = resources.BillingResource(self)
        self.brand_protection = resources.BrandProtectionResource(self)
        self.diagnostics = resources.DiagnosticsResource(self)
        self.images = resources.ImagesResource(self)
        self.intel = resources.IntelResource(self)
        self.magic_transit = resources.MagicTransitResource(self)
        self.magic_network_monitoring = resources.MagicNetworkMonitoringResource(self)
        self.mtls_certificates = resources.MTLSCertificatesResource(self)
        self.pages = resources.PagesResource(self)
        self.registrar = resources.RegistrarResource(self)
        self.request_tracers = resources.RequestTracersResource(self)
        self.rules = resources.RulesResource(self)
        self.storage = resources.StorageResource(self)
        self.stream = resources.StreamResource(self)
        self.alerting = resources.AlertingResource(self)
        self.d1 = resources.D1Resource(self)
        self.r2 = resources.R2Resource(self)
        self.warp_connector = resources.WARPConnectorResource(self)
        self.workers_for_platforms = resources.WorkersForPlatformsResource(self)
        self.zero_trust = resources.ZeroTrustResource(self)
        self.turnstile = resources.TurnstileResource(self)
        self.hyperdrive = resources.HyperdriveResource(self)
        self.rum = resources.RUMResource(self)
        self.vectorize = resources.VectorizeResource(self)
        self.url_scanner = resources.URLScannerResource(self)
        self.radar = resources.RadarResource(self)
        self.bot_management = resources.BotManagementResource(self)
        self.origin_post_quantum_encryption = resources.OriginPostQuantumEncryptionResource(self)
        self.speed = resources.SpeedResource(self)
        self.dcv_delegation = resources.DCVDelegationResource(self)
        self.hostnames = resources.HostnamesResource(self)
        self.snippets = resources.SnippetsResource(self)
        self.calls = resources.CallsResource(self)
        self.cloudforce_one = resources.CloudforceOneResource(self)
        self.ai_gateway = resources.AIGatewayResource(self)
        self.iam = resources.IAMResource(self)
        self.cloud_connector = resources.CloudConnectorResource(self)
        self.botnet_feed = resources.BotnetFeedResource(self)
        self.with_raw_response = CloudflareWithRawResponse(self)
        self.with_streaming_response = CloudflareWithStreamedResponse(self)

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
    accounts: resources.AsyncAccountsResource
    origin_ca_certificates: resources.AsyncOriginCACertificatesResource
    ips: resources.AsyncIPsResource
    memberships: resources.AsyncMembershipsResource
    user: resources.AsyncUserResource
    zones: resources.AsyncZonesResource
    load_balancers: resources.AsyncLoadBalancersResource
    cache: resources.AsyncCacheResource
    ssl: resources.AsyncSSLResource
    acm: resources.AsyncACMResource
    argo: resources.AsyncArgoResource
    certificate_authorities: resources.AsyncCertificateAuthoritiesResource
    client_certificates: resources.AsyncClientCertificatesResource
    custom_certificates: resources.AsyncCustomCertificatesResource
    custom_hostnames: resources.AsyncCustomHostnamesResource
    custom_nameservers: resources.AsyncCustomNameserversResource
    dns: resources.AsyncDNSResource
    dnssec: resources.AsyncDNSSECResource
    email_security: resources.AsyncEmailSecurityResource
    email_routing: resources.AsyncEmailRoutingResource
    filters: resources.AsyncFiltersResource
    firewall: resources.AsyncFirewallResource
    healthchecks: resources.AsyncHealthchecksResource
    keyless_certificates: resources.AsyncKeylessCertificatesResource
    logpush: resources.AsyncLogpushResource
    logs: resources.AsyncLogsResource
    origin_tls_client_auth: resources.AsyncOriginTLSClientAuthResource
    pagerules: resources.AsyncPagerulesResource
    rate_limits: resources.AsyncRateLimitsResource
    secondary_dns: resources.AsyncSecondaryDNSResource
    waiting_rooms: resources.AsyncWaitingRoomsResource
    web3: resources.AsyncWeb3Resource
    workers: resources.AsyncWorkersResource
    kv: resources.AsyncKVResource
    durable_objects: resources.AsyncDurableObjectsResource
    queues: resources.AsyncQueuesResource
    api_gateway: resources.AsyncAPIGatewayResource
    managed_transforms: resources.AsyncManagedTransformsResource
    page_shield: resources.AsyncPageShieldResource
    rulesets: resources.AsyncRulesetsResource
    url_normalization: resources.AsyncURLNormalizationResource
    spectrum: resources.AsyncSpectrumResource
    addressing: resources.AsyncAddressingResource
    audit_logs: resources.AsyncAuditLogsResource
    billing: resources.AsyncBillingResource
    brand_protection: resources.AsyncBrandProtectionResource
    diagnostics: resources.AsyncDiagnosticsResource
    images: resources.AsyncImagesResource
    intel: resources.AsyncIntelResource
    magic_transit: resources.AsyncMagicTransitResource
    magic_network_monitoring: resources.AsyncMagicNetworkMonitoringResource
    mtls_certificates: resources.AsyncMTLSCertificatesResource
    pages: resources.AsyncPagesResource
    registrar: resources.AsyncRegistrarResource
    request_tracers: resources.AsyncRequestTracersResource
    rules: resources.AsyncRulesResource
    storage: resources.AsyncStorageResource
    stream: resources.AsyncStreamResource
    alerting: resources.AsyncAlertingResource
    d1: resources.AsyncD1Resource
    r2: resources.AsyncR2Resource
    warp_connector: resources.AsyncWARPConnectorResource
    workers_for_platforms: resources.AsyncWorkersForPlatformsResource
    zero_trust: resources.AsyncZeroTrustResource
    turnstile: resources.AsyncTurnstileResource
    hyperdrive: resources.AsyncHyperdriveResource
    rum: resources.AsyncRUMResource
    vectorize: resources.AsyncVectorizeResource
    url_scanner: resources.AsyncURLScannerResource
    radar: resources.AsyncRadarResource
    bot_management: resources.AsyncBotManagementResource
    origin_post_quantum_encryption: resources.AsyncOriginPostQuantumEncryptionResource
    speed: resources.AsyncSpeedResource
    dcv_delegation: resources.AsyncDCVDelegationResource
    hostnames: resources.AsyncHostnamesResource
    snippets: resources.AsyncSnippetsResource
    calls: resources.AsyncCallsResource
    cloudforce_one: resources.AsyncCloudforceOneResource
    ai_gateway: resources.AsyncAIGatewayResource
    iam: resources.AsyncIAMResource
    cloud_connector: resources.AsyncCloudConnectorResource
    botnet_feed: resources.AsyncBotnetFeedResource
    with_raw_response: AsyncCloudflareWithRawResponse
    with_streaming_response: AsyncCloudflareWithStreamedResponse

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
        """Construct a new async cloudflare client instance.

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

        self.accounts = resources.AsyncAccountsResource(self)
        self.origin_ca_certificates = resources.AsyncOriginCACertificatesResource(self)
        self.ips = resources.AsyncIPsResource(self)
        self.memberships = resources.AsyncMembershipsResource(self)
        self.user = resources.AsyncUserResource(self)
        self.zones = resources.AsyncZonesResource(self)
        self.load_balancers = resources.AsyncLoadBalancersResource(self)
        self.cache = resources.AsyncCacheResource(self)
        self.ssl = resources.AsyncSSLResource(self)
        self.acm = resources.AsyncACMResource(self)
        self.argo = resources.AsyncArgoResource(self)
        self.certificate_authorities = resources.AsyncCertificateAuthoritiesResource(self)
        self.client_certificates = resources.AsyncClientCertificatesResource(self)
        self.custom_certificates = resources.AsyncCustomCertificatesResource(self)
        self.custom_hostnames = resources.AsyncCustomHostnamesResource(self)
        self.custom_nameservers = resources.AsyncCustomNameserversResource(self)
        self.dns = resources.AsyncDNSResource(self)
        self.dnssec = resources.AsyncDNSSECResource(self)
        self.email_security = resources.AsyncEmailSecurityResource(self)
        self.email_routing = resources.AsyncEmailRoutingResource(self)
        self.filters = resources.AsyncFiltersResource(self)
        self.firewall = resources.AsyncFirewallResource(self)
        self.healthchecks = resources.AsyncHealthchecksResource(self)
        self.keyless_certificates = resources.AsyncKeylessCertificatesResource(self)
        self.logpush = resources.AsyncLogpushResource(self)
        self.logs = resources.AsyncLogsResource(self)
        self.origin_tls_client_auth = resources.AsyncOriginTLSClientAuthResource(self)
        self.pagerules = resources.AsyncPagerulesResource(self)
        self.rate_limits = resources.AsyncRateLimitsResource(self)
        self.secondary_dns = resources.AsyncSecondaryDNSResource(self)
        self.waiting_rooms = resources.AsyncWaitingRoomsResource(self)
        self.web3 = resources.AsyncWeb3Resource(self)
        self.workers = resources.AsyncWorkersResource(self)
        self.kv = resources.AsyncKVResource(self)
        self.durable_objects = resources.AsyncDurableObjectsResource(self)
        self.queues = resources.AsyncQueuesResource(self)
        self.api_gateway = resources.AsyncAPIGatewayResource(self)
        self.managed_transforms = resources.AsyncManagedTransformsResource(self)
        self.page_shield = resources.AsyncPageShieldResource(self)
        self.rulesets = resources.AsyncRulesetsResource(self)
        self.url_normalization = resources.AsyncURLNormalizationResource(self)
        self.spectrum = resources.AsyncSpectrumResource(self)
        self.addressing = resources.AsyncAddressingResource(self)
        self.audit_logs = resources.AsyncAuditLogsResource(self)
        self.billing = resources.AsyncBillingResource(self)
        self.brand_protection = resources.AsyncBrandProtectionResource(self)
        self.diagnostics = resources.AsyncDiagnosticsResource(self)
        self.images = resources.AsyncImagesResource(self)
        self.intel = resources.AsyncIntelResource(self)
        self.magic_transit = resources.AsyncMagicTransitResource(self)
        self.magic_network_monitoring = resources.AsyncMagicNetworkMonitoringResource(self)
        self.mtls_certificates = resources.AsyncMTLSCertificatesResource(self)
        self.pages = resources.AsyncPagesResource(self)
        self.registrar = resources.AsyncRegistrarResource(self)
        self.request_tracers = resources.AsyncRequestTracersResource(self)
        self.rules = resources.AsyncRulesResource(self)
        self.storage = resources.AsyncStorageResource(self)
        self.stream = resources.AsyncStreamResource(self)
        self.alerting = resources.AsyncAlertingResource(self)
        self.d1 = resources.AsyncD1Resource(self)
        self.r2 = resources.AsyncR2Resource(self)
        self.warp_connector = resources.AsyncWARPConnectorResource(self)
        self.workers_for_platforms = resources.AsyncWorkersForPlatformsResource(self)
        self.zero_trust = resources.AsyncZeroTrustResource(self)
        self.turnstile = resources.AsyncTurnstileResource(self)
        self.hyperdrive = resources.AsyncHyperdriveResource(self)
        self.rum = resources.AsyncRUMResource(self)
        self.vectorize = resources.AsyncVectorizeResource(self)
        self.url_scanner = resources.AsyncURLScannerResource(self)
        self.radar = resources.AsyncRadarResource(self)
        self.bot_management = resources.AsyncBotManagementResource(self)
        self.origin_post_quantum_encryption = resources.AsyncOriginPostQuantumEncryptionResource(self)
        self.speed = resources.AsyncSpeedResource(self)
        self.dcv_delegation = resources.AsyncDCVDelegationResource(self)
        self.hostnames = resources.AsyncHostnamesResource(self)
        self.snippets = resources.AsyncSnippetsResource(self)
        self.calls = resources.AsyncCallsResource(self)
        self.cloudforce_one = resources.AsyncCloudforceOneResource(self)
        self.ai_gateway = resources.AsyncAIGatewayResource(self)
        self.iam = resources.AsyncIAMResource(self)
        self.cloud_connector = resources.AsyncCloudConnectorResource(self)
        self.botnet_feed = resources.AsyncBotnetFeedResource(self)
        self.with_raw_response = AsyncCloudflareWithRawResponse(self)
        self.with_streaming_response = AsyncCloudflareWithStreamedResponse(self)

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
    def __init__(self, client: Cloudflare) -> None:
        self.accounts = resources.AccountsResourceWithRawResponse(client.accounts)
        self.origin_ca_certificates = resources.OriginCACertificatesResourceWithRawResponse(
            client.origin_ca_certificates
        )
        self.ips = resources.IPsResourceWithRawResponse(client.ips)
        self.memberships = resources.MembershipsResourceWithRawResponse(client.memberships)
        self.user = resources.UserResourceWithRawResponse(client.user)
        self.zones = resources.ZonesResourceWithRawResponse(client.zones)
        self.load_balancers = resources.LoadBalancersResourceWithRawResponse(client.load_balancers)
        self.cache = resources.CacheResourceWithRawResponse(client.cache)
        self.ssl = resources.SSLResourceWithRawResponse(client.ssl)
        self.acm = resources.ACMResourceWithRawResponse(client.acm)
        self.argo = resources.ArgoResourceWithRawResponse(client.argo)
        self.certificate_authorities = resources.CertificateAuthoritiesResourceWithRawResponse(
            client.certificate_authorities
        )
        self.client_certificates = resources.ClientCertificatesResourceWithRawResponse(client.client_certificates)
        self.custom_certificates = resources.CustomCertificatesResourceWithRawResponse(client.custom_certificates)
        self.custom_hostnames = resources.CustomHostnamesResourceWithRawResponse(client.custom_hostnames)
        self.custom_nameservers = resources.CustomNameserversResourceWithRawResponse(client.custom_nameservers)
        self.dns = resources.DNSResourceWithRawResponse(client.dns)
        self.dnssec = resources.DNSSECResourceWithRawResponse(client.dnssec)
        self.email_security = resources.EmailSecurityResourceWithRawResponse(client.email_security)
        self.email_routing = resources.EmailRoutingResourceWithRawResponse(client.email_routing)
        self.filters = resources.FiltersResourceWithRawResponse(client.filters)
        self.firewall = resources.FirewallResourceWithRawResponse(client.firewall)
        self.healthchecks = resources.HealthchecksResourceWithRawResponse(client.healthchecks)
        self.keyless_certificates = resources.KeylessCertificatesResourceWithRawResponse(client.keyless_certificates)
        self.logpush = resources.LogpushResourceWithRawResponse(client.logpush)
        self.logs = resources.LogsResourceWithRawResponse(client.logs)
        self.origin_tls_client_auth = resources.OriginTLSClientAuthResourceWithRawResponse(
            client.origin_tls_client_auth
        )
        self.pagerules = resources.PagerulesResourceWithRawResponse(client.pagerules)
        self.rate_limits = resources.RateLimitsResourceWithRawResponse(client.rate_limits)
        self.secondary_dns = resources.SecondaryDNSResourceWithRawResponse(client.secondary_dns)
        self.waiting_rooms = resources.WaitingRoomsResourceWithRawResponse(client.waiting_rooms)
        self.web3 = resources.Web3ResourceWithRawResponse(client.web3)
        self.workers = resources.WorkersResourceWithRawResponse(client.workers)
        self.kv = resources.KVResourceWithRawResponse(client.kv)
        self.durable_objects = resources.DurableObjectsResourceWithRawResponse(client.durable_objects)
        self.queues = resources.QueuesResourceWithRawResponse(client.queues)
        self.api_gateway = resources.APIGatewayResourceWithRawResponse(client.api_gateway)
        self.managed_transforms = resources.ManagedTransformsResourceWithRawResponse(client.managed_transforms)
        self.page_shield = resources.PageShieldResourceWithRawResponse(client.page_shield)
        self.rulesets = resources.RulesetsResourceWithRawResponse(client.rulesets)
        self.url_normalization = resources.URLNormalizationResourceWithRawResponse(client.url_normalization)
        self.spectrum = resources.SpectrumResourceWithRawResponse(client.spectrum)
        self.addressing = resources.AddressingResourceWithRawResponse(client.addressing)
        self.audit_logs = resources.AuditLogsResourceWithRawResponse(client.audit_logs)
        self.billing = resources.BillingResourceWithRawResponse(client.billing)
        self.brand_protection = resources.BrandProtectionResourceWithRawResponse(client.brand_protection)
        self.diagnostics = resources.DiagnosticsResourceWithRawResponse(client.diagnostics)
        self.images = resources.ImagesResourceWithRawResponse(client.images)
        self.intel = resources.IntelResourceWithRawResponse(client.intel)
        self.magic_transit = resources.MagicTransitResourceWithRawResponse(client.magic_transit)
        self.magic_network_monitoring = resources.MagicNetworkMonitoringResourceWithRawResponse(
            client.magic_network_monitoring
        )
        self.mtls_certificates = resources.MTLSCertificatesResourceWithRawResponse(client.mtls_certificates)
        self.pages = resources.PagesResourceWithRawResponse(client.pages)
        self.registrar = resources.RegistrarResourceWithRawResponse(client.registrar)
        self.request_tracers = resources.RequestTracersResourceWithRawResponse(client.request_tracers)
        self.rules = resources.RulesResourceWithRawResponse(client.rules)
        self.storage = resources.StorageResourceWithRawResponse(client.storage)
        self.stream = resources.StreamResourceWithRawResponse(client.stream)
        self.alerting = resources.AlertingResourceWithRawResponse(client.alerting)
        self.d1 = resources.D1ResourceWithRawResponse(client.d1)
        self.r2 = resources.R2ResourceWithRawResponse(client.r2)
        self.warp_connector = resources.WARPConnectorResourceWithRawResponse(client.warp_connector)
        self.workers_for_platforms = resources.WorkersForPlatformsResourceWithRawResponse(client.workers_for_platforms)
        self.zero_trust = resources.ZeroTrustResourceWithRawResponse(client.zero_trust)
        self.turnstile = resources.TurnstileResourceWithRawResponse(client.turnstile)
        self.hyperdrive = resources.HyperdriveResourceWithRawResponse(client.hyperdrive)
        self.rum = resources.RUMResourceWithRawResponse(client.rum)
        self.vectorize = resources.VectorizeResourceWithRawResponse(client.vectorize)
        self.url_scanner = resources.URLScannerResourceWithRawResponse(client.url_scanner)
        self.radar = resources.RadarResourceWithRawResponse(client.radar)
        self.bot_management = resources.BotManagementResourceWithRawResponse(client.bot_management)
        self.origin_post_quantum_encryption = resources.OriginPostQuantumEncryptionResourceWithRawResponse(
            client.origin_post_quantum_encryption
        )
        self.speed = resources.SpeedResourceWithRawResponse(client.speed)
        self.dcv_delegation = resources.DCVDelegationResourceWithRawResponse(client.dcv_delegation)
        self.hostnames = resources.HostnamesResourceWithRawResponse(client.hostnames)
        self.snippets = resources.SnippetsResourceWithRawResponse(client.snippets)
        self.calls = resources.CallsResourceWithRawResponse(client.calls)
        self.cloudforce_one = resources.CloudforceOneResourceWithRawResponse(client.cloudforce_one)
        self.ai_gateway = resources.AIGatewayResourceWithRawResponse(client.ai_gateway)
        self.iam = resources.IAMResourceWithRawResponse(client.iam)
        self.cloud_connector = resources.CloudConnectorResourceWithRawResponse(client.cloud_connector)
        self.botnet_feed = resources.BotnetFeedResourceWithRawResponse(client.botnet_feed)


class AsyncCloudflareWithRawResponse:
    def __init__(self, client: AsyncCloudflare) -> None:
        self.accounts = resources.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.origin_ca_certificates = resources.AsyncOriginCACertificatesResourceWithRawResponse(
            client.origin_ca_certificates
        )
        self.ips = resources.AsyncIPsResourceWithRawResponse(client.ips)
        self.memberships = resources.AsyncMembershipsResourceWithRawResponse(client.memberships)
        self.user = resources.AsyncUserResourceWithRawResponse(client.user)
        self.zones = resources.AsyncZonesResourceWithRawResponse(client.zones)
        self.load_balancers = resources.AsyncLoadBalancersResourceWithRawResponse(client.load_balancers)
        self.cache = resources.AsyncCacheResourceWithRawResponse(client.cache)
        self.ssl = resources.AsyncSSLResourceWithRawResponse(client.ssl)
        self.acm = resources.AsyncACMResourceWithRawResponse(client.acm)
        self.argo = resources.AsyncArgoResourceWithRawResponse(client.argo)
        self.certificate_authorities = resources.AsyncCertificateAuthoritiesResourceWithRawResponse(
            client.certificate_authorities
        )
        self.client_certificates = resources.AsyncClientCertificatesResourceWithRawResponse(client.client_certificates)
        self.custom_certificates = resources.AsyncCustomCertificatesResourceWithRawResponse(client.custom_certificates)
        self.custom_hostnames = resources.AsyncCustomHostnamesResourceWithRawResponse(client.custom_hostnames)
        self.custom_nameservers = resources.AsyncCustomNameserversResourceWithRawResponse(client.custom_nameservers)
        self.dns = resources.AsyncDNSResourceWithRawResponse(client.dns)
        self.dnssec = resources.AsyncDNSSECResourceWithRawResponse(client.dnssec)
        self.email_security = resources.AsyncEmailSecurityResourceWithRawResponse(client.email_security)
        self.email_routing = resources.AsyncEmailRoutingResourceWithRawResponse(client.email_routing)
        self.filters = resources.AsyncFiltersResourceWithRawResponse(client.filters)
        self.firewall = resources.AsyncFirewallResourceWithRawResponse(client.firewall)
        self.healthchecks = resources.AsyncHealthchecksResourceWithRawResponse(client.healthchecks)
        self.keyless_certificates = resources.AsyncKeylessCertificatesResourceWithRawResponse(
            client.keyless_certificates
        )
        self.logpush = resources.AsyncLogpushResourceWithRawResponse(client.logpush)
        self.logs = resources.AsyncLogsResourceWithRawResponse(client.logs)
        self.origin_tls_client_auth = resources.AsyncOriginTLSClientAuthResourceWithRawResponse(
            client.origin_tls_client_auth
        )
        self.pagerules = resources.AsyncPagerulesResourceWithRawResponse(client.pagerules)
        self.rate_limits = resources.AsyncRateLimitsResourceWithRawResponse(client.rate_limits)
        self.secondary_dns = resources.AsyncSecondaryDNSResourceWithRawResponse(client.secondary_dns)
        self.waiting_rooms = resources.AsyncWaitingRoomsResourceWithRawResponse(client.waiting_rooms)
        self.web3 = resources.AsyncWeb3ResourceWithRawResponse(client.web3)
        self.workers = resources.AsyncWorkersResourceWithRawResponse(client.workers)
        self.kv = resources.AsyncKVResourceWithRawResponse(client.kv)
        self.durable_objects = resources.AsyncDurableObjectsResourceWithRawResponse(client.durable_objects)
        self.queues = resources.AsyncQueuesResourceWithRawResponse(client.queues)
        self.api_gateway = resources.AsyncAPIGatewayResourceWithRawResponse(client.api_gateway)
        self.managed_transforms = resources.AsyncManagedTransformsResourceWithRawResponse(client.managed_transforms)
        self.page_shield = resources.AsyncPageShieldResourceWithRawResponse(client.page_shield)
        self.rulesets = resources.AsyncRulesetsResourceWithRawResponse(client.rulesets)
        self.url_normalization = resources.AsyncURLNormalizationResourceWithRawResponse(client.url_normalization)
        self.spectrum = resources.AsyncSpectrumResourceWithRawResponse(client.spectrum)
        self.addressing = resources.AsyncAddressingResourceWithRawResponse(client.addressing)
        self.audit_logs = resources.AsyncAuditLogsResourceWithRawResponse(client.audit_logs)
        self.billing = resources.AsyncBillingResourceWithRawResponse(client.billing)
        self.brand_protection = resources.AsyncBrandProtectionResourceWithRawResponse(client.brand_protection)
        self.diagnostics = resources.AsyncDiagnosticsResourceWithRawResponse(client.diagnostics)
        self.images = resources.AsyncImagesResourceWithRawResponse(client.images)
        self.intel = resources.AsyncIntelResourceWithRawResponse(client.intel)
        self.magic_transit = resources.AsyncMagicTransitResourceWithRawResponse(client.magic_transit)
        self.magic_network_monitoring = resources.AsyncMagicNetworkMonitoringResourceWithRawResponse(
            client.magic_network_monitoring
        )
        self.mtls_certificates = resources.AsyncMTLSCertificatesResourceWithRawResponse(client.mtls_certificates)
        self.pages = resources.AsyncPagesResourceWithRawResponse(client.pages)
        self.registrar = resources.AsyncRegistrarResourceWithRawResponse(client.registrar)
        self.request_tracers = resources.AsyncRequestTracersResourceWithRawResponse(client.request_tracers)
        self.rules = resources.AsyncRulesResourceWithRawResponse(client.rules)
        self.storage = resources.AsyncStorageResourceWithRawResponse(client.storage)
        self.stream = resources.AsyncStreamResourceWithRawResponse(client.stream)
        self.alerting = resources.AsyncAlertingResourceWithRawResponse(client.alerting)
        self.d1 = resources.AsyncD1ResourceWithRawResponse(client.d1)
        self.r2 = resources.AsyncR2ResourceWithRawResponse(client.r2)
        self.warp_connector = resources.AsyncWARPConnectorResourceWithRawResponse(client.warp_connector)
        self.workers_for_platforms = resources.AsyncWorkersForPlatformsResourceWithRawResponse(
            client.workers_for_platforms
        )
        self.zero_trust = resources.AsyncZeroTrustResourceWithRawResponse(client.zero_trust)
        self.turnstile = resources.AsyncTurnstileResourceWithRawResponse(client.turnstile)
        self.hyperdrive = resources.AsyncHyperdriveResourceWithRawResponse(client.hyperdrive)
        self.rum = resources.AsyncRUMResourceWithRawResponse(client.rum)
        self.vectorize = resources.AsyncVectorizeResourceWithRawResponse(client.vectorize)
        self.url_scanner = resources.AsyncURLScannerResourceWithRawResponse(client.url_scanner)
        self.radar = resources.AsyncRadarResourceWithRawResponse(client.radar)
        self.bot_management = resources.AsyncBotManagementResourceWithRawResponse(client.bot_management)
        self.origin_post_quantum_encryption = resources.AsyncOriginPostQuantumEncryptionResourceWithRawResponse(
            client.origin_post_quantum_encryption
        )
        self.speed = resources.AsyncSpeedResourceWithRawResponse(client.speed)
        self.dcv_delegation = resources.AsyncDCVDelegationResourceWithRawResponse(client.dcv_delegation)
        self.hostnames = resources.AsyncHostnamesResourceWithRawResponse(client.hostnames)
        self.snippets = resources.AsyncSnippetsResourceWithRawResponse(client.snippets)
        self.calls = resources.AsyncCallsResourceWithRawResponse(client.calls)
        self.cloudforce_one = resources.AsyncCloudforceOneResourceWithRawResponse(client.cloudforce_one)
        self.ai_gateway = resources.AsyncAIGatewayResourceWithRawResponse(client.ai_gateway)
        self.iam = resources.AsyncIAMResourceWithRawResponse(client.iam)
        self.cloud_connector = resources.AsyncCloudConnectorResourceWithRawResponse(client.cloud_connector)
        self.botnet_feed = resources.AsyncBotnetFeedResourceWithRawResponse(client.botnet_feed)


class CloudflareWithStreamedResponse:
    def __init__(self, client: Cloudflare) -> None:
        self.accounts = resources.AccountsResourceWithStreamingResponse(client.accounts)
        self.origin_ca_certificates = resources.OriginCACertificatesResourceWithStreamingResponse(
            client.origin_ca_certificates
        )
        self.ips = resources.IPsResourceWithStreamingResponse(client.ips)
        self.memberships = resources.MembershipsResourceWithStreamingResponse(client.memberships)
        self.user = resources.UserResourceWithStreamingResponse(client.user)
        self.zones = resources.ZonesResourceWithStreamingResponse(client.zones)
        self.load_balancers = resources.LoadBalancersResourceWithStreamingResponse(client.load_balancers)
        self.cache = resources.CacheResourceWithStreamingResponse(client.cache)
        self.ssl = resources.SSLResourceWithStreamingResponse(client.ssl)
        self.acm = resources.ACMResourceWithStreamingResponse(client.acm)
        self.argo = resources.ArgoResourceWithStreamingResponse(client.argo)
        self.certificate_authorities = resources.CertificateAuthoritiesResourceWithStreamingResponse(
            client.certificate_authorities
        )
        self.client_certificates = resources.ClientCertificatesResourceWithStreamingResponse(client.client_certificates)
        self.custom_certificates = resources.CustomCertificatesResourceWithStreamingResponse(client.custom_certificates)
        self.custom_hostnames = resources.CustomHostnamesResourceWithStreamingResponse(client.custom_hostnames)
        self.custom_nameservers = resources.CustomNameserversResourceWithStreamingResponse(client.custom_nameservers)
        self.dns = resources.DNSResourceWithStreamingResponse(client.dns)
        self.dnssec = resources.DNSSECResourceWithStreamingResponse(client.dnssec)
        self.email_security = resources.EmailSecurityResourceWithStreamingResponse(client.email_security)
        self.email_routing = resources.EmailRoutingResourceWithStreamingResponse(client.email_routing)
        self.filters = resources.FiltersResourceWithStreamingResponse(client.filters)
        self.firewall = resources.FirewallResourceWithStreamingResponse(client.firewall)
        self.healthchecks = resources.HealthchecksResourceWithStreamingResponse(client.healthchecks)
        self.keyless_certificates = resources.KeylessCertificatesResourceWithStreamingResponse(
            client.keyless_certificates
        )
        self.logpush = resources.LogpushResourceWithStreamingResponse(client.logpush)
        self.logs = resources.LogsResourceWithStreamingResponse(client.logs)
        self.origin_tls_client_auth = resources.OriginTLSClientAuthResourceWithStreamingResponse(
            client.origin_tls_client_auth
        )
        self.pagerules = resources.PagerulesResourceWithStreamingResponse(client.pagerules)
        self.rate_limits = resources.RateLimitsResourceWithStreamingResponse(client.rate_limits)
        self.secondary_dns = resources.SecondaryDNSResourceWithStreamingResponse(client.secondary_dns)
        self.waiting_rooms = resources.WaitingRoomsResourceWithStreamingResponse(client.waiting_rooms)
        self.web3 = resources.Web3ResourceWithStreamingResponse(client.web3)
        self.workers = resources.WorkersResourceWithStreamingResponse(client.workers)
        self.kv = resources.KVResourceWithStreamingResponse(client.kv)
        self.durable_objects = resources.DurableObjectsResourceWithStreamingResponse(client.durable_objects)
        self.queues = resources.QueuesResourceWithStreamingResponse(client.queues)
        self.api_gateway = resources.APIGatewayResourceWithStreamingResponse(client.api_gateway)
        self.managed_transforms = resources.ManagedTransformsResourceWithStreamingResponse(client.managed_transforms)
        self.page_shield = resources.PageShieldResourceWithStreamingResponse(client.page_shield)
        self.rulesets = resources.RulesetsResourceWithStreamingResponse(client.rulesets)
        self.url_normalization = resources.URLNormalizationResourceWithStreamingResponse(client.url_normalization)
        self.spectrum = resources.SpectrumResourceWithStreamingResponse(client.spectrum)
        self.addressing = resources.AddressingResourceWithStreamingResponse(client.addressing)
        self.audit_logs = resources.AuditLogsResourceWithStreamingResponse(client.audit_logs)
        self.billing = resources.BillingResourceWithStreamingResponse(client.billing)
        self.brand_protection = resources.BrandProtectionResourceWithStreamingResponse(client.brand_protection)
        self.diagnostics = resources.DiagnosticsResourceWithStreamingResponse(client.diagnostics)
        self.images = resources.ImagesResourceWithStreamingResponse(client.images)
        self.intel = resources.IntelResourceWithStreamingResponse(client.intel)
        self.magic_transit = resources.MagicTransitResourceWithStreamingResponse(client.magic_transit)
        self.magic_network_monitoring = resources.MagicNetworkMonitoringResourceWithStreamingResponse(
            client.magic_network_monitoring
        )
        self.mtls_certificates = resources.MTLSCertificatesResourceWithStreamingResponse(client.mtls_certificates)
        self.pages = resources.PagesResourceWithStreamingResponse(client.pages)
        self.registrar = resources.RegistrarResourceWithStreamingResponse(client.registrar)
        self.request_tracers = resources.RequestTracersResourceWithStreamingResponse(client.request_tracers)
        self.rules = resources.RulesResourceWithStreamingResponse(client.rules)
        self.storage = resources.StorageResourceWithStreamingResponse(client.storage)
        self.stream = resources.StreamResourceWithStreamingResponse(client.stream)
        self.alerting = resources.AlertingResourceWithStreamingResponse(client.alerting)
        self.d1 = resources.D1ResourceWithStreamingResponse(client.d1)
        self.r2 = resources.R2ResourceWithStreamingResponse(client.r2)
        self.warp_connector = resources.WARPConnectorResourceWithStreamingResponse(client.warp_connector)
        self.workers_for_platforms = resources.WorkersForPlatformsResourceWithStreamingResponse(
            client.workers_for_platforms
        )
        self.zero_trust = resources.ZeroTrustResourceWithStreamingResponse(client.zero_trust)
        self.turnstile = resources.TurnstileResourceWithStreamingResponse(client.turnstile)
        self.hyperdrive = resources.HyperdriveResourceWithStreamingResponse(client.hyperdrive)
        self.rum = resources.RUMResourceWithStreamingResponse(client.rum)
        self.vectorize = resources.VectorizeResourceWithStreamingResponse(client.vectorize)
        self.url_scanner = resources.URLScannerResourceWithStreamingResponse(client.url_scanner)
        self.radar = resources.RadarResourceWithStreamingResponse(client.radar)
        self.bot_management = resources.BotManagementResourceWithStreamingResponse(client.bot_management)
        self.origin_post_quantum_encryption = resources.OriginPostQuantumEncryptionResourceWithStreamingResponse(
            client.origin_post_quantum_encryption
        )
        self.speed = resources.SpeedResourceWithStreamingResponse(client.speed)
        self.dcv_delegation = resources.DCVDelegationResourceWithStreamingResponse(client.dcv_delegation)
        self.hostnames = resources.HostnamesResourceWithStreamingResponse(client.hostnames)
        self.snippets = resources.SnippetsResourceWithStreamingResponse(client.snippets)
        self.calls = resources.CallsResourceWithStreamingResponse(client.calls)
        self.cloudforce_one = resources.CloudforceOneResourceWithStreamingResponse(client.cloudforce_one)
        self.ai_gateway = resources.AIGatewayResourceWithStreamingResponse(client.ai_gateway)
        self.iam = resources.IAMResourceWithStreamingResponse(client.iam)
        self.cloud_connector = resources.CloudConnectorResourceWithStreamingResponse(client.cloud_connector)
        self.botnet_feed = resources.BotnetFeedResourceWithStreamingResponse(client.botnet_feed)


class AsyncCloudflareWithStreamedResponse:
    def __init__(self, client: AsyncCloudflare) -> None:
        self.accounts = resources.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.origin_ca_certificates = resources.AsyncOriginCACertificatesResourceWithStreamingResponse(
            client.origin_ca_certificates
        )
        self.ips = resources.AsyncIPsResourceWithStreamingResponse(client.ips)
        self.memberships = resources.AsyncMembershipsResourceWithStreamingResponse(client.memberships)
        self.user = resources.AsyncUserResourceWithStreamingResponse(client.user)
        self.zones = resources.AsyncZonesResourceWithStreamingResponse(client.zones)
        self.load_balancers = resources.AsyncLoadBalancersResourceWithStreamingResponse(client.load_balancers)
        self.cache = resources.AsyncCacheResourceWithStreamingResponse(client.cache)
        self.ssl = resources.AsyncSSLResourceWithStreamingResponse(client.ssl)
        self.acm = resources.AsyncACMResourceWithStreamingResponse(client.acm)
        self.argo = resources.AsyncArgoResourceWithStreamingResponse(client.argo)
        self.certificate_authorities = resources.AsyncCertificateAuthoritiesResourceWithStreamingResponse(
            client.certificate_authorities
        )
        self.client_certificates = resources.AsyncClientCertificatesResourceWithStreamingResponse(
            client.client_certificates
        )
        self.custom_certificates = resources.AsyncCustomCertificatesResourceWithStreamingResponse(
            client.custom_certificates
        )
        self.custom_hostnames = resources.AsyncCustomHostnamesResourceWithStreamingResponse(client.custom_hostnames)
        self.custom_nameservers = resources.AsyncCustomNameserversResourceWithStreamingResponse(
            client.custom_nameservers
        )
        self.dns = resources.AsyncDNSResourceWithStreamingResponse(client.dns)
        self.dnssec = resources.AsyncDNSSECResourceWithStreamingResponse(client.dnssec)
        self.email_security = resources.AsyncEmailSecurityResourceWithStreamingResponse(client.email_security)
        self.email_routing = resources.AsyncEmailRoutingResourceWithStreamingResponse(client.email_routing)
        self.filters = resources.AsyncFiltersResourceWithStreamingResponse(client.filters)
        self.firewall = resources.AsyncFirewallResourceWithStreamingResponse(client.firewall)
        self.healthchecks = resources.AsyncHealthchecksResourceWithStreamingResponse(client.healthchecks)
        self.keyless_certificates = resources.AsyncKeylessCertificatesResourceWithStreamingResponse(
            client.keyless_certificates
        )
        self.logpush = resources.AsyncLogpushResourceWithStreamingResponse(client.logpush)
        self.logs = resources.AsyncLogsResourceWithStreamingResponse(client.logs)
        self.origin_tls_client_auth = resources.AsyncOriginTLSClientAuthResourceWithStreamingResponse(
            client.origin_tls_client_auth
        )
        self.pagerules = resources.AsyncPagerulesResourceWithStreamingResponse(client.pagerules)
        self.rate_limits = resources.AsyncRateLimitsResourceWithStreamingResponse(client.rate_limits)
        self.secondary_dns = resources.AsyncSecondaryDNSResourceWithStreamingResponse(client.secondary_dns)
        self.waiting_rooms = resources.AsyncWaitingRoomsResourceWithStreamingResponse(client.waiting_rooms)
        self.web3 = resources.AsyncWeb3ResourceWithStreamingResponse(client.web3)
        self.workers = resources.AsyncWorkersResourceWithStreamingResponse(client.workers)
        self.kv = resources.AsyncKVResourceWithStreamingResponse(client.kv)
        self.durable_objects = resources.AsyncDurableObjectsResourceWithStreamingResponse(client.durable_objects)
        self.queues = resources.AsyncQueuesResourceWithStreamingResponse(client.queues)
        self.api_gateway = resources.AsyncAPIGatewayResourceWithStreamingResponse(client.api_gateway)
        self.managed_transforms = resources.AsyncManagedTransformsResourceWithStreamingResponse(
            client.managed_transforms
        )
        self.page_shield = resources.AsyncPageShieldResourceWithStreamingResponse(client.page_shield)
        self.rulesets = resources.AsyncRulesetsResourceWithStreamingResponse(client.rulesets)
        self.url_normalization = resources.AsyncURLNormalizationResourceWithStreamingResponse(client.url_normalization)
        self.spectrum = resources.AsyncSpectrumResourceWithStreamingResponse(client.spectrum)
        self.addressing = resources.AsyncAddressingResourceWithStreamingResponse(client.addressing)
        self.audit_logs = resources.AsyncAuditLogsResourceWithStreamingResponse(client.audit_logs)
        self.billing = resources.AsyncBillingResourceWithStreamingResponse(client.billing)
        self.brand_protection = resources.AsyncBrandProtectionResourceWithStreamingResponse(client.brand_protection)
        self.diagnostics = resources.AsyncDiagnosticsResourceWithStreamingResponse(client.diagnostics)
        self.images = resources.AsyncImagesResourceWithStreamingResponse(client.images)
        self.intel = resources.AsyncIntelResourceWithStreamingResponse(client.intel)
        self.magic_transit = resources.AsyncMagicTransitResourceWithStreamingResponse(client.magic_transit)
        self.magic_network_monitoring = resources.AsyncMagicNetworkMonitoringResourceWithStreamingResponse(
            client.magic_network_monitoring
        )
        self.mtls_certificates = resources.AsyncMTLSCertificatesResourceWithStreamingResponse(client.mtls_certificates)
        self.pages = resources.AsyncPagesResourceWithStreamingResponse(client.pages)
        self.registrar = resources.AsyncRegistrarResourceWithStreamingResponse(client.registrar)
        self.request_tracers = resources.AsyncRequestTracersResourceWithStreamingResponse(client.request_tracers)
        self.rules = resources.AsyncRulesResourceWithStreamingResponse(client.rules)
        self.storage = resources.AsyncStorageResourceWithStreamingResponse(client.storage)
        self.stream = resources.AsyncStreamResourceWithStreamingResponse(client.stream)
        self.alerting = resources.AsyncAlertingResourceWithStreamingResponse(client.alerting)
        self.d1 = resources.AsyncD1ResourceWithStreamingResponse(client.d1)
        self.r2 = resources.AsyncR2ResourceWithStreamingResponse(client.r2)
        self.warp_connector = resources.AsyncWARPConnectorResourceWithStreamingResponse(client.warp_connector)
        self.workers_for_platforms = resources.AsyncWorkersForPlatformsResourceWithStreamingResponse(
            client.workers_for_platforms
        )
        self.zero_trust = resources.AsyncZeroTrustResourceWithStreamingResponse(client.zero_trust)
        self.turnstile = resources.AsyncTurnstileResourceWithStreamingResponse(client.turnstile)
        self.hyperdrive = resources.AsyncHyperdriveResourceWithStreamingResponse(client.hyperdrive)
        self.rum = resources.AsyncRUMResourceWithStreamingResponse(client.rum)
        self.vectorize = resources.AsyncVectorizeResourceWithStreamingResponse(client.vectorize)
        self.url_scanner = resources.AsyncURLScannerResourceWithStreamingResponse(client.url_scanner)
        self.radar = resources.AsyncRadarResourceWithStreamingResponse(client.radar)
        self.bot_management = resources.AsyncBotManagementResourceWithStreamingResponse(client.bot_management)
        self.origin_post_quantum_encryption = resources.AsyncOriginPostQuantumEncryptionResourceWithStreamingResponse(
            client.origin_post_quantum_encryption
        )
        self.speed = resources.AsyncSpeedResourceWithStreamingResponse(client.speed)
        self.dcv_delegation = resources.AsyncDCVDelegationResourceWithStreamingResponse(client.dcv_delegation)
        self.hostnames = resources.AsyncHostnamesResourceWithStreamingResponse(client.hostnames)
        self.snippets = resources.AsyncSnippetsResourceWithStreamingResponse(client.snippets)
        self.calls = resources.AsyncCallsResourceWithStreamingResponse(client.calls)
        self.cloudforce_one = resources.AsyncCloudforceOneResourceWithStreamingResponse(client.cloudforce_one)
        self.ai_gateway = resources.AsyncAIGatewayResourceWithStreamingResponse(client.ai_gateway)
        self.iam = resources.AsyncIAMResourceWithStreamingResponse(client.iam)
        self.cloud_connector = resources.AsyncCloudConnectorResourceWithStreamingResponse(client.cloud_connector)
        self.botnet_feed = resources.AsyncBotnetFeedResourceWithStreamingResponse(client.botnet_feed)


Client = Cloudflare

AsyncClient = AsyncCloudflare
