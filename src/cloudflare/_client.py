# File generated from our OpenAPI spec by Stainless.

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
from ._exceptions import APIStatusError, CloudflareError
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
    accounts: resources.Accounts
    certificates: resources.Certificates
    ips: resources.IPs
    memberships: resources.Memberships
    users: resources.Users
    zones: resources.Zones
    load_balancers: resources.LoadBalancers
    access: resources.Access
    dns_analytics: resources.DNSAnalytics
    purge_caches: resources.PurgeCaches
    ssls: resources.SSLs
    subscriptions: resources.Subscriptions
    acms: resources.Acms
    analytics: resources.Analytics
    argo: resources.Argo
    available_plans: resources.AvailablePlans
    available_rate_plans: resources.AvailableRatePlans
    caches: resources.Caches
    certificate_authorities: resources.CertificateAuthorities
    client_certificates: resources.ClientCertificates
    custom_certificates: resources.CustomCertificates
    custom_hostnames: resources.CustomHostnames
    custom_ns: resources.CustomNs
    dns_records: resources.DNSRecords
    dnssecs: resources.DNSSECs
    emails: resources.Emails
    filters: resources.Filters
    firewalls: resources.Firewalls
    healthchecks: resources.Healthchecks
    keyless_certificates: resources.KeylessCertificates
    logpush: resources.Logpush
    logs: resources.Logs
    origin_tls_client_auth: resources.OriginTLSClientAuth
    pagerules: resources.Pagerules
    rate_limits: resources.RateLimits
    secondary_dns: resources.SecondaryDNS
    settings: resources.Settings
    waiting_rooms: resources.WaitingRooms
    web3s: resources.Web3s
    workers: resources.Workers
    activation_checks: resources.ActivationChecks
    api_gateways: resources.APIGateways
    managed_headers: resources.ManagedHeaders
    page_shields: resources.PageShields
    rulesets: resources.Rulesets
    url_normalizations: resources.URLNormalizations
    spectrums: resources.Spectrums
    addresses: resources.Addresses
    audit_logs: resources.AuditLogs
    billings: resources.Billings
    brand_protections: resources.BrandProtections
    cfd_tunnels: resources.CfdTunnels
    diagnostics: resources.Diagnostics
    dlps: resources.DLPs
    dns_firewalls: resources.DNSFirewalls
    images: resources.Images
    intels: resources.Intels
    magics: resources.Magics
    account_members: resources.AccountMembers
    mnms: resources.Mnms
    mtls_certificates: resources.MtlsCertificates
    pages: resources.Pages
    pcaps: resources.Pcaps
    registrar: resources.Registrar
    request_tracers: resources.RequestTracers
    roles: resources.Roles
    rules: resources.Rules
    storage: resources.Storage
    stream: resources.Stream
    teamnets: resources.Teamnets
    tunnels: resources.Tunnels
    gateways: resources.Gateways
    alerting: resources.Alerting
    devices: resources.Devices
    d1: resources.D1
    dex: resources.DEX
    r2: resources.R2
    teamnet: resources.Teamnet
    warp_connector: resources.WarpConnector
    dispatchers: resources.Dispatchers
    workers_for_platforms: resources.WorkersForPlatforms
    worker_domains: resources.WorkerDomains
    worker_scripts: resources.WorkerScripts
    zerotrust: resources.Zerotrust
    addressing: resources.Addressing
    challenges: resources.Challenges
    hyperdrive: resources.Hyperdrive
    intel: resources.Intel
    rum: resources.Rum
    vectorize: resources.Vectorize
    url_scanner: resources.URLScanner
    radar: resources.Radar
    bot_managements: resources.BotManagements
    cache_reserves: resources.CacheReserves
    origin_post_quantum_encryptions: resources.OriginPostQuantumEncryptions
    cache: resources.Cache
    firewall: resources.Firewall
    zaraz: resources.Zaraz
    speed_api: resources.SpeedAPI
    dcv_delegation: resources.DcvDelegation
    hostnames: resources.Hostnames
    page_shield: resources.PageShield
    font_settings: resources.FontSettings
    snippets: resources.Snippets
    dlp: resources.DLP
    gateway: resources.Gateway
    access_tags: resources.AccessTags
    with_raw_response: CloudflareWithRawResponse
    with_streaming_response: CloudflareWithStreamedResponse

    # client options
    api_key: str
    api_email: str
    api_token: str
    user_service_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_email: str | None = None,
        api_token: str | None = None,
        user_service_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
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
        - `api_key` from `CLOUDFLARE_API_KEY`
        - `api_email` from `CLOUDFLARE_EMAIL`
        - `api_token` from `CLOUDFLARE_API_TOKEN`
        - `user_service_key` from `CLOUDFLARE_API_USER_SERVICE_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("CLOUDFLARE_API_KEY")
        if api_key is None:
            raise CloudflareError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CLOUDFLARE_API_KEY environment variable"
            )
        self.api_key = api_key

        if api_email is None:
            api_email = os.environ.get("CLOUDFLARE_EMAIL")
        if api_email is None:
            raise CloudflareError(
                "The api_email client option must be set either by passing api_email to the client or by setting the CLOUDFLARE_EMAIL environment variable"
            )
        self.api_email = api_email

        if api_token is None:
            api_token = os.environ.get("CLOUDFLARE_API_TOKEN")
        if api_token is None:
            raise CloudflareError(
                "The api_token client option must be set either by passing api_token to the client or by setting the CLOUDFLARE_API_TOKEN environment variable"
            )
        self.api_token = api_token

        if user_service_key is None:
            user_service_key = os.environ.get("CLOUDFLARE_API_USER_SERVICE_KEY")
        if user_service_key is None:
            raise CloudflareError(
                "The user_service_key client option must be set either by passing user_service_key to the client or by setting the CLOUDFLARE_API_USER_SERVICE_KEY environment variable"
            )
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

        self.accounts = resources.Accounts(self)
        self.certificates = resources.Certificates(self)
        self.ips = resources.IPs(self)
        self.memberships = resources.Memberships(self)
        self.users = resources.Users(self)
        self.zones = resources.Zones(self)
        self.load_balancers = resources.LoadBalancers(self)
        self.access = resources.Access(self)
        self.dns_analytics = resources.DNSAnalytics(self)
        self.purge_caches = resources.PurgeCaches(self)
        self.ssls = resources.SSLs(self)
        self.subscriptions = resources.Subscriptions(self)
        self.acms = resources.Acms(self)
        self.analytics = resources.Analytics(self)
        self.argo = resources.Argo(self)
        self.available_plans = resources.AvailablePlans(self)
        self.available_rate_plans = resources.AvailableRatePlans(self)
        self.caches = resources.Caches(self)
        self.certificate_authorities = resources.CertificateAuthorities(self)
        self.client_certificates = resources.ClientCertificates(self)
        self.custom_certificates = resources.CustomCertificates(self)
        self.custom_hostnames = resources.CustomHostnames(self)
        self.custom_ns = resources.CustomNs(self)
        self.dns_records = resources.DNSRecords(self)
        self.dnssecs = resources.DNSSECs(self)
        self.emails = resources.Emails(self)
        self.filters = resources.Filters(self)
        self.firewalls = resources.Firewalls(self)
        self.healthchecks = resources.Healthchecks(self)
        self.keyless_certificates = resources.KeylessCertificates(self)
        self.logpush = resources.Logpush(self)
        self.logs = resources.Logs(self)
        self.origin_tls_client_auth = resources.OriginTLSClientAuth(self)
        self.pagerules = resources.Pagerules(self)
        self.rate_limits = resources.RateLimits(self)
        self.secondary_dns = resources.SecondaryDNS(self)
        self.settings = resources.Settings(self)
        self.waiting_rooms = resources.WaitingRooms(self)
        self.web3s = resources.Web3s(self)
        self.workers = resources.Workers(self)
        self.activation_checks = resources.ActivationChecks(self)
        self.api_gateways = resources.APIGateways(self)
        self.managed_headers = resources.ManagedHeaders(self)
        self.page_shields = resources.PageShields(self)
        self.rulesets = resources.Rulesets(self)
        self.url_normalizations = resources.URLNormalizations(self)
        self.spectrums = resources.Spectrums(self)
        self.addresses = resources.Addresses(self)
        self.audit_logs = resources.AuditLogs(self)
        self.billings = resources.Billings(self)
        self.brand_protections = resources.BrandProtections(self)
        self.cfd_tunnels = resources.CfdTunnels(self)
        self.diagnostics = resources.Diagnostics(self)
        self.dlps = resources.DLPs(self)
        self.dns_firewalls = resources.DNSFirewalls(self)
        self.images = resources.Images(self)
        self.intels = resources.Intels(self)
        self.magics = resources.Magics(self)
        self.account_members = resources.AccountMembers(self)
        self.mnms = resources.Mnms(self)
        self.mtls_certificates = resources.MtlsCertificates(self)
        self.pages = resources.Pages(self)
        self.pcaps = resources.Pcaps(self)
        self.registrar = resources.Registrar(self)
        self.request_tracers = resources.RequestTracers(self)
        self.roles = resources.Roles(self)
        self.rules = resources.Rules(self)
        self.storage = resources.Storage(self)
        self.stream = resources.Stream(self)
        self.teamnets = resources.Teamnets(self)
        self.tunnels = resources.Tunnels(self)
        self.gateways = resources.Gateways(self)
        self.alerting = resources.Alerting(self)
        self.devices = resources.Devices(self)
        self.d1 = resources.D1(self)
        self.dex = resources.DEX(self)
        self.r2 = resources.R2(self)
        self.teamnet = resources.Teamnet(self)
        self.warp_connector = resources.WarpConnector(self)
        self.dispatchers = resources.Dispatchers(self)
        self.workers_for_platforms = resources.WorkersForPlatforms(self)
        self.worker_domains = resources.WorkerDomains(self)
        self.worker_scripts = resources.WorkerScripts(self)
        self.zerotrust = resources.Zerotrust(self)
        self.addressing = resources.Addressing(self)
        self.challenges = resources.Challenges(self)
        self.hyperdrive = resources.Hyperdrive(self)
        self.intel = resources.Intel(self)
        self.rum = resources.Rum(self)
        self.vectorize = resources.Vectorize(self)
        self.url_scanner = resources.URLScanner(self)
        self.radar = resources.Radar(self)
        self.bot_managements = resources.BotManagements(self)
        self.cache_reserves = resources.CacheReserves(self)
        self.origin_post_quantum_encryptions = resources.OriginPostQuantumEncryptions(self)
        self.cache = resources.Cache(self)
        self.firewall = resources.Firewall(self)
        self.zaraz = resources.Zaraz(self)
        self.speed_api = resources.SpeedAPI(self)
        self.dcv_delegation = resources.DcvDelegation(self)
        self.hostnames = resources.Hostnames(self)
        self.page_shield = resources.PageShield(self)
        self.font_settings = resources.FontSettings(self)
        self.snippets = resources.Snippets(self)
        self.dlp = resources.DLP(self)
        self.gateway = resources.Gateway(self)
        self.access_tags = resources.AccessTags(self)
        self.with_raw_response = CloudflareWithRawResponse(self)
        self.with_streaming_response = CloudflareWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

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
        return {"X-Auth-Email": api_email}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-Auth-Key": api_key}

    @property
    def _api_token(self) -> dict[str, str]:
        api_token = self.api_token
        return {"Authorization": f"Bearer {api_token}"}

    @property
    def _user_service_key(self) -> dict[str, str]:
        user_service_key = self.user_service_key
        return {"X-Auth-User-Service-Key": user_service_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "x-auth-email": self.api_email,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        api_email: str | None = None,
        api_token: str | None = None,
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
            api_key=api_key or self.api_key,
            api_email=api_email or self.api_email,
            api_token=api_token or self.api_token,
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
    accounts: resources.AsyncAccounts
    certificates: resources.AsyncCertificates
    ips: resources.AsyncIPs
    memberships: resources.AsyncMemberships
    users: resources.AsyncUsers
    zones: resources.AsyncZones
    load_balancers: resources.AsyncLoadBalancers
    access: resources.AsyncAccess
    dns_analytics: resources.AsyncDNSAnalytics
    purge_caches: resources.AsyncPurgeCaches
    ssls: resources.AsyncSSLs
    subscriptions: resources.AsyncSubscriptions
    acms: resources.AsyncAcms
    analytics: resources.AsyncAnalytics
    argo: resources.AsyncArgo
    available_plans: resources.AsyncAvailablePlans
    available_rate_plans: resources.AsyncAvailableRatePlans
    caches: resources.AsyncCaches
    certificate_authorities: resources.AsyncCertificateAuthorities
    client_certificates: resources.AsyncClientCertificates
    custom_certificates: resources.AsyncCustomCertificates
    custom_hostnames: resources.AsyncCustomHostnames
    custom_ns: resources.AsyncCustomNs
    dns_records: resources.AsyncDNSRecords
    dnssecs: resources.AsyncDNSSECs
    emails: resources.AsyncEmails
    filters: resources.AsyncFilters
    firewalls: resources.AsyncFirewalls
    healthchecks: resources.AsyncHealthchecks
    keyless_certificates: resources.AsyncKeylessCertificates
    logpush: resources.AsyncLogpush
    logs: resources.AsyncLogs
    origin_tls_client_auth: resources.AsyncOriginTLSClientAuth
    pagerules: resources.AsyncPagerules
    rate_limits: resources.AsyncRateLimits
    secondary_dns: resources.AsyncSecondaryDNS
    settings: resources.AsyncSettings
    waiting_rooms: resources.AsyncWaitingRooms
    web3s: resources.AsyncWeb3s
    workers: resources.AsyncWorkers
    activation_checks: resources.AsyncActivationChecks
    api_gateways: resources.AsyncAPIGateways
    managed_headers: resources.AsyncManagedHeaders
    page_shields: resources.AsyncPageShields
    rulesets: resources.AsyncRulesets
    url_normalizations: resources.AsyncURLNormalizations
    spectrums: resources.AsyncSpectrums
    addresses: resources.AsyncAddresses
    audit_logs: resources.AsyncAuditLogs
    billings: resources.AsyncBillings
    brand_protections: resources.AsyncBrandProtections
    cfd_tunnels: resources.AsyncCfdTunnels
    diagnostics: resources.AsyncDiagnostics
    dlps: resources.AsyncDLPs
    dns_firewalls: resources.AsyncDNSFirewalls
    images: resources.AsyncImages
    intels: resources.AsyncIntels
    magics: resources.AsyncMagics
    account_members: resources.AsyncAccountMembers
    mnms: resources.AsyncMnms
    mtls_certificates: resources.AsyncMtlsCertificates
    pages: resources.AsyncPages
    pcaps: resources.AsyncPcaps
    registrar: resources.AsyncRegistrar
    request_tracers: resources.AsyncRequestTracers
    roles: resources.AsyncRoles
    rules: resources.AsyncRules
    storage: resources.AsyncStorage
    stream: resources.AsyncStream
    teamnets: resources.AsyncTeamnets
    tunnels: resources.AsyncTunnels
    gateways: resources.AsyncGateways
    alerting: resources.AsyncAlerting
    devices: resources.AsyncDevices
    d1: resources.AsyncD1
    dex: resources.AsyncDEX
    r2: resources.AsyncR2
    teamnet: resources.AsyncTeamnet
    warp_connector: resources.AsyncWarpConnector
    dispatchers: resources.AsyncDispatchers
    workers_for_platforms: resources.AsyncWorkersForPlatforms
    worker_domains: resources.AsyncWorkerDomains
    worker_scripts: resources.AsyncWorkerScripts
    zerotrust: resources.AsyncZerotrust
    addressing: resources.AsyncAddressing
    challenges: resources.AsyncChallenges
    hyperdrive: resources.AsyncHyperdrive
    intel: resources.AsyncIntel
    rum: resources.AsyncRum
    vectorize: resources.AsyncVectorize
    url_scanner: resources.AsyncURLScanner
    radar: resources.AsyncRadar
    bot_managements: resources.AsyncBotManagements
    cache_reserves: resources.AsyncCacheReserves
    origin_post_quantum_encryptions: resources.AsyncOriginPostQuantumEncryptions
    cache: resources.AsyncCache
    firewall: resources.AsyncFirewall
    zaraz: resources.AsyncZaraz
    speed_api: resources.AsyncSpeedAPI
    dcv_delegation: resources.AsyncDcvDelegation
    hostnames: resources.AsyncHostnames
    page_shield: resources.AsyncPageShield
    font_settings: resources.AsyncFontSettings
    snippets: resources.AsyncSnippets
    dlp: resources.AsyncDLP
    gateway: resources.AsyncGateway
    access_tags: resources.AsyncAccessTags
    with_raw_response: AsyncCloudflareWithRawResponse
    with_streaming_response: AsyncCloudflareWithStreamedResponse

    # client options
    api_key: str
    api_email: str
    api_token: str
    user_service_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_email: str | None = None,
        api_token: str | None = None,
        user_service_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
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
        - `api_key` from `CLOUDFLARE_API_KEY`
        - `api_email` from `CLOUDFLARE_EMAIL`
        - `api_token` from `CLOUDFLARE_API_TOKEN`
        - `user_service_key` from `CLOUDFLARE_API_USER_SERVICE_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("CLOUDFLARE_API_KEY")
        if api_key is None:
            raise CloudflareError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CLOUDFLARE_API_KEY environment variable"
            )
        self.api_key = api_key

        if api_email is None:
            api_email = os.environ.get("CLOUDFLARE_EMAIL")
        if api_email is None:
            raise CloudflareError(
                "The api_email client option must be set either by passing api_email to the client or by setting the CLOUDFLARE_EMAIL environment variable"
            )
        self.api_email = api_email

        if api_token is None:
            api_token = os.environ.get("CLOUDFLARE_API_TOKEN")
        if api_token is None:
            raise CloudflareError(
                "The api_token client option must be set either by passing api_token to the client or by setting the CLOUDFLARE_API_TOKEN environment variable"
            )
        self.api_token = api_token

        if user_service_key is None:
            user_service_key = os.environ.get("CLOUDFLARE_API_USER_SERVICE_KEY")
        if user_service_key is None:
            raise CloudflareError(
                "The user_service_key client option must be set either by passing user_service_key to the client or by setting the CLOUDFLARE_API_USER_SERVICE_KEY environment variable"
            )
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

        self.accounts = resources.AsyncAccounts(self)
        self.certificates = resources.AsyncCertificates(self)
        self.ips = resources.AsyncIPs(self)
        self.memberships = resources.AsyncMemberships(self)
        self.users = resources.AsyncUsers(self)
        self.zones = resources.AsyncZones(self)
        self.load_balancers = resources.AsyncLoadBalancers(self)
        self.access = resources.AsyncAccess(self)
        self.dns_analytics = resources.AsyncDNSAnalytics(self)
        self.purge_caches = resources.AsyncPurgeCaches(self)
        self.ssls = resources.AsyncSSLs(self)
        self.subscriptions = resources.AsyncSubscriptions(self)
        self.acms = resources.AsyncAcms(self)
        self.analytics = resources.AsyncAnalytics(self)
        self.argo = resources.AsyncArgo(self)
        self.available_plans = resources.AsyncAvailablePlans(self)
        self.available_rate_plans = resources.AsyncAvailableRatePlans(self)
        self.caches = resources.AsyncCaches(self)
        self.certificate_authorities = resources.AsyncCertificateAuthorities(self)
        self.client_certificates = resources.AsyncClientCertificates(self)
        self.custom_certificates = resources.AsyncCustomCertificates(self)
        self.custom_hostnames = resources.AsyncCustomHostnames(self)
        self.custom_ns = resources.AsyncCustomNs(self)
        self.dns_records = resources.AsyncDNSRecords(self)
        self.dnssecs = resources.AsyncDNSSECs(self)
        self.emails = resources.AsyncEmails(self)
        self.filters = resources.AsyncFilters(self)
        self.firewalls = resources.AsyncFirewalls(self)
        self.healthchecks = resources.AsyncHealthchecks(self)
        self.keyless_certificates = resources.AsyncKeylessCertificates(self)
        self.logpush = resources.AsyncLogpush(self)
        self.logs = resources.AsyncLogs(self)
        self.origin_tls_client_auth = resources.AsyncOriginTLSClientAuth(self)
        self.pagerules = resources.AsyncPagerules(self)
        self.rate_limits = resources.AsyncRateLimits(self)
        self.secondary_dns = resources.AsyncSecondaryDNS(self)
        self.settings = resources.AsyncSettings(self)
        self.waiting_rooms = resources.AsyncWaitingRooms(self)
        self.web3s = resources.AsyncWeb3s(self)
        self.workers = resources.AsyncWorkers(self)
        self.activation_checks = resources.AsyncActivationChecks(self)
        self.api_gateways = resources.AsyncAPIGateways(self)
        self.managed_headers = resources.AsyncManagedHeaders(self)
        self.page_shields = resources.AsyncPageShields(self)
        self.rulesets = resources.AsyncRulesets(self)
        self.url_normalizations = resources.AsyncURLNormalizations(self)
        self.spectrums = resources.AsyncSpectrums(self)
        self.addresses = resources.AsyncAddresses(self)
        self.audit_logs = resources.AsyncAuditLogs(self)
        self.billings = resources.AsyncBillings(self)
        self.brand_protections = resources.AsyncBrandProtections(self)
        self.cfd_tunnels = resources.AsyncCfdTunnels(self)
        self.diagnostics = resources.AsyncDiagnostics(self)
        self.dlps = resources.AsyncDLPs(self)
        self.dns_firewalls = resources.AsyncDNSFirewalls(self)
        self.images = resources.AsyncImages(self)
        self.intels = resources.AsyncIntels(self)
        self.magics = resources.AsyncMagics(self)
        self.account_members = resources.AsyncAccountMembers(self)
        self.mnms = resources.AsyncMnms(self)
        self.mtls_certificates = resources.AsyncMtlsCertificates(self)
        self.pages = resources.AsyncPages(self)
        self.pcaps = resources.AsyncPcaps(self)
        self.registrar = resources.AsyncRegistrar(self)
        self.request_tracers = resources.AsyncRequestTracers(self)
        self.roles = resources.AsyncRoles(self)
        self.rules = resources.AsyncRules(self)
        self.storage = resources.AsyncStorage(self)
        self.stream = resources.AsyncStream(self)
        self.teamnets = resources.AsyncTeamnets(self)
        self.tunnels = resources.AsyncTunnels(self)
        self.gateways = resources.AsyncGateways(self)
        self.alerting = resources.AsyncAlerting(self)
        self.devices = resources.AsyncDevices(self)
        self.d1 = resources.AsyncD1(self)
        self.dex = resources.AsyncDEX(self)
        self.r2 = resources.AsyncR2(self)
        self.teamnet = resources.AsyncTeamnet(self)
        self.warp_connector = resources.AsyncWarpConnector(self)
        self.dispatchers = resources.AsyncDispatchers(self)
        self.workers_for_platforms = resources.AsyncWorkersForPlatforms(self)
        self.worker_domains = resources.AsyncWorkerDomains(self)
        self.worker_scripts = resources.AsyncWorkerScripts(self)
        self.zerotrust = resources.AsyncZerotrust(self)
        self.addressing = resources.AsyncAddressing(self)
        self.challenges = resources.AsyncChallenges(self)
        self.hyperdrive = resources.AsyncHyperdrive(self)
        self.intel = resources.AsyncIntel(self)
        self.rum = resources.AsyncRum(self)
        self.vectorize = resources.AsyncVectorize(self)
        self.url_scanner = resources.AsyncURLScanner(self)
        self.radar = resources.AsyncRadar(self)
        self.bot_managements = resources.AsyncBotManagements(self)
        self.cache_reserves = resources.AsyncCacheReserves(self)
        self.origin_post_quantum_encryptions = resources.AsyncOriginPostQuantumEncryptions(self)
        self.cache = resources.AsyncCache(self)
        self.firewall = resources.AsyncFirewall(self)
        self.zaraz = resources.AsyncZaraz(self)
        self.speed_api = resources.AsyncSpeedAPI(self)
        self.dcv_delegation = resources.AsyncDcvDelegation(self)
        self.hostnames = resources.AsyncHostnames(self)
        self.page_shield = resources.AsyncPageShield(self)
        self.font_settings = resources.AsyncFontSettings(self)
        self.snippets = resources.AsyncSnippets(self)
        self.dlp = resources.AsyncDLP(self)
        self.gateway = resources.AsyncGateway(self)
        self.access_tags = resources.AsyncAccessTags(self)
        self.with_raw_response = AsyncCloudflareWithRawResponse(self)
        self.with_streaming_response = AsyncCloudflareWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

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
        return {"X-Auth-Email": api_email}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-Auth-Key": api_key}

    @property
    def _api_token(self) -> dict[str, str]:
        api_token = self.api_token
        return {"Authorization": f"Bearer {api_token}"}

    @property
    def _user_service_key(self) -> dict[str, str]:
        user_service_key = self.user_service_key
        return {"X-Auth-User-Service-Key": user_service_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "x-auth-email": self.api_email,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        api_email: str | None = None,
        api_token: str | None = None,
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
            api_key=api_key or self.api_key,
            api_email=api_email or self.api_email,
            api_token=api_token or self.api_token,
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
        self.accounts = resources.AccountsWithRawResponse(client.accounts)
        self.certificates = resources.CertificatesWithRawResponse(client.certificates)
        self.ips = resources.IPsWithRawResponse(client.ips)
        self.memberships = resources.MembershipsWithRawResponse(client.memberships)
        self.users = resources.UsersWithRawResponse(client.users)
        self.zones = resources.ZonesWithRawResponse(client.zones)
        self.load_balancers = resources.LoadBalancersWithRawResponse(client.load_balancers)
        self.access = resources.AccessWithRawResponse(client.access)
        self.dns_analytics = resources.DNSAnalyticsWithRawResponse(client.dns_analytics)
        self.purge_caches = resources.PurgeCachesWithRawResponse(client.purge_caches)
        self.ssls = resources.SSLsWithRawResponse(client.ssls)
        self.subscriptions = resources.SubscriptionsWithRawResponse(client.subscriptions)
        self.acms = resources.AcmsWithRawResponse(client.acms)
        self.analytics = resources.AnalyticsWithRawResponse(client.analytics)
        self.argo = resources.ArgoWithRawResponse(client.argo)
        self.available_plans = resources.AvailablePlansWithRawResponse(client.available_plans)
        self.available_rate_plans = resources.AvailableRatePlansWithRawResponse(client.available_rate_plans)
        self.caches = resources.CachesWithRawResponse(client.caches)
        self.certificate_authorities = resources.CertificateAuthoritiesWithRawResponse(client.certificate_authorities)
        self.client_certificates = resources.ClientCertificatesWithRawResponse(client.client_certificates)
        self.custom_certificates = resources.CustomCertificatesWithRawResponse(client.custom_certificates)
        self.custom_hostnames = resources.CustomHostnamesWithRawResponse(client.custom_hostnames)
        self.custom_ns = resources.CustomNsWithRawResponse(client.custom_ns)
        self.dns_records = resources.DNSRecordsWithRawResponse(client.dns_records)
        self.dnssecs = resources.DNSSECsWithRawResponse(client.dnssecs)
        self.emails = resources.EmailsWithRawResponse(client.emails)
        self.filters = resources.FiltersWithRawResponse(client.filters)
        self.firewalls = resources.FirewallsWithRawResponse(client.firewalls)
        self.healthchecks = resources.HealthchecksWithRawResponse(client.healthchecks)
        self.keyless_certificates = resources.KeylessCertificatesWithRawResponse(client.keyless_certificates)
        self.logpush = resources.LogpushWithRawResponse(client.logpush)
        self.logs = resources.LogsWithRawResponse(client.logs)
        self.origin_tls_client_auth = resources.OriginTLSClientAuthWithRawResponse(client.origin_tls_client_auth)
        self.pagerules = resources.PagerulesWithRawResponse(client.pagerules)
        self.rate_limits = resources.RateLimitsWithRawResponse(client.rate_limits)
        self.secondary_dns = resources.SecondaryDNSWithRawResponse(client.secondary_dns)
        self.settings = resources.SettingsWithRawResponse(client.settings)
        self.waiting_rooms = resources.WaitingRoomsWithRawResponse(client.waiting_rooms)
        self.web3s = resources.Web3sWithRawResponse(client.web3s)
        self.workers = resources.WorkersWithRawResponse(client.workers)
        self.activation_checks = resources.ActivationChecksWithRawResponse(client.activation_checks)
        self.api_gateways = resources.APIGatewaysWithRawResponse(client.api_gateways)
        self.managed_headers = resources.ManagedHeadersWithRawResponse(client.managed_headers)
        self.page_shields = resources.PageShieldsWithRawResponse(client.page_shields)
        self.rulesets = resources.RulesetsWithRawResponse(client.rulesets)
        self.url_normalizations = resources.URLNormalizationsWithRawResponse(client.url_normalizations)
        self.spectrums = resources.SpectrumsWithRawResponse(client.spectrums)
        self.addresses = resources.AddressesWithRawResponse(client.addresses)
        self.audit_logs = resources.AuditLogsWithRawResponse(client.audit_logs)
        self.billings = resources.BillingsWithRawResponse(client.billings)
        self.brand_protections = resources.BrandProtectionsWithRawResponse(client.brand_protections)
        self.cfd_tunnels = resources.CfdTunnelsWithRawResponse(client.cfd_tunnels)
        self.diagnostics = resources.DiagnosticsWithRawResponse(client.diagnostics)
        self.dlps = resources.DLPsWithRawResponse(client.dlps)
        self.dns_firewalls = resources.DNSFirewallsWithRawResponse(client.dns_firewalls)
        self.images = resources.ImagesWithRawResponse(client.images)
        self.intels = resources.IntelsWithRawResponse(client.intels)
        self.magics = resources.MagicsWithRawResponse(client.magics)
        self.account_members = resources.AccountMembersWithRawResponse(client.account_members)
        self.mnms = resources.MnmsWithRawResponse(client.mnms)
        self.mtls_certificates = resources.MtlsCertificatesWithRawResponse(client.mtls_certificates)
        self.pages = resources.PagesWithRawResponse(client.pages)
        self.pcaps = resources.PcapsWithRawResponse(client.pcaps)
        self.registrar = resources.RegistrarWithRawResponse(client.registrar)
        self.request_tracers = resources.RequestTracersWithRawResponse(client.request_tracers)
        self.roles = resources.RolesWithRawResponse(client.roles)
        self.rules = resources.RulesWithRawResponse(client.rules)
        self.storage = resources.StorageWithRawResponse(client.storage)
        self.stream = resources.StreamWithRawResponse(client.stream)
        self.teamnets = resources.TeamnetsWithRawResponse(client.teamnets)
        self.tunnels = resources.TunnelsWithRawResponse(client.tunnels)
        self.gateways = resources.GatewaysWithRawResponse(client.gateways)
        self.alerting = resources.AlertingWithRawResponse(client.alerting)
        self.devices = resources.DevicesWithRawResponse(client.devices)
        self.d1 = resources.D1WithRawResponse(client.d1)
        self.dex = resources.DEXWithRawResponse(client.dex)
        self.r2 = resources.R2WithRawResponse(client.r2)
        self.teamnet = resources.TeamnetWithRawResponse(client.teamnet)
        self.warp_connector = resources.WarpConnectorWithRawResponse(client.warp_connector)
        self.dispatchers = resources.DispatchersWithRawResponse(client.dispatchers)
        self.workers_for_platforms = resources.WorkersForPlatformsWithRawResponse(client.workers_for_platforms)
        self.worker_domains = resources.WorkerDomainsWithRawResponse(client.worker_domains)
        self.worker_scripts = resources.WorkerScriptsWithRawResponse(client.worker_scripts)
        self.zerotrust = resources.ZerotrustWithRawResponse(client.zerotrust)
        self.addressing = resources.AddressingWithRawResponse(client.addressing)
        self.challenges = resources.ChallengesWithRawResponse(client.challenges)
        self.hyperdrive = resources.HyperdriveWithRawResponse(client.hyperdrive)
        self.intel = resources.IntelWithRawResponse(client.intel)
        self.rum = resources.RumWithRawResponse(client.rum)
        self.vectorize = resources.VectorizeWithRawResponse(client.vectorize)
        self.url_scanner = resources.URLScannerWithRawResponse(client.url_scanner)
        self.radar = resources.RadarWithRawResponse(client.radar)
        self.bot_managements = resources.BotManagementsWithRawResponse(client.bot_managements)
        self.cache_reserves = resources.CacheReservesWithRawResponse(client.cache_reserves)
        self.origin_post_quantum_encryptions = resources.OriginPostQuantumEncryptionsWithRawResponse(
            client.origin_post_quantum_encryptions
        )
        self.cache = resources.CacheWithRawResponse(client.cache)
        self.firewall = resources.FirewallWithRawResponse(client.firewall)
        self.zaraz = resources.ZarazWithRawResponse(client.zaraz)
        self.speed_api = resources.SpeedAPIWithRawResponse(client.speed_api)
        self.dcv_delegation = resources.DcvDelegationWithRawResponse(client.dcv_delegation)
        self.hostnames = resources.HostnamesWithRawResponse(client.hostnames)
        self.page_shield = resources.PageShieldWithRawResponse(client.page_shield)
        self.font_settings = resources.FontSettingsWithRawResponse(client.font_settings)
        self.snippets = resources.SnippetsWithRawResponse(client.snippets)
        self.dlp = resources.DLPWithRawResponse(client.dlp)
        self.gateway = resources.GatewayWithRawResponse(client.gateway)
        self.access_tags = resources.AccessTagsWithRawResponse(client.access_tags)


class AsyncCloudflareWithRawResponse:
    def __init__(self, client: AsyncCloudflare) -> None:
        self.accounts = resources.AsyncAccountsWithRawResponse(client.accounts)
        self.certificates = resources.AsyncCertificatesWithRawResponse(client.certificates)
        self.ips = resources.AsyncIPsWithRawResponse(client.ips)
        self.memberships = resources.AsyncMembershipsWithRawResponse(client.memberships)
        self.users = resources.AsyncUsersWithRawResponse(client.users)
        self.zones = resources.AsyncZonesWithRawResponse(client.zones)
        self.load_balancers = resources.AsyncLoadBalancersWithRawResponse(client.load_balancers)
        self.access = resources.AsyncAccessWithRawResponse(client.access)
        self.dns_analytics = resources.AsyncDNSAnalyticsWithRawResponse(client.dns_analytics)
        self.purge_caches = resources.AsyncPurgeCachesWithRawResponse(client.purge_caches)
        self.ssls = resources.AsyncSSLsWithRawResponse(client.ssls)
        self.subscriptions = resources.AsyncSubscriptionsWithRawResponse(client.subscriptions)
        self.acms = resources.AsyncAcmsWithRawResponse(client.acms)
        self.analytics = resources.AsyncAnalyticsWithRawResponse(client.analytics)
        self.argo = resources.AsyncArgoWithRawResponse(client.argo)
        self.available_plans = resources.AsyncAvailablePlansWithRawResponse(client.available_plans)
        self.available_rate_plans = resources.AsyncAvailableRatePlansWithRawResponse(client.available_rate_plans)
        self.caches = resources.AsyncCachesWithRawResponse(client.caches)
        self.certificate_authorities = resources.AsyncCertificateAuthoritiesWithRawResponse(
            client.certificate_authorities
        )
        self.client_certificates = resources.AsyncClientCertificatesWithRawResponse(client.client_certificates)
        self.custom_certificates = resources.AsyncCustomCertificatesWithRawResponse(client.custom_certificates)
        self.custom_hostnames = resources.AsyncCustomHostnamesWithRawResponse(client.custom_hostnames)
        self.custom_ns = resources.AsyncCustomNsWithRawResponse(client.custom_ns)
        self.dns_records = resources.AsyncDNSRecordsWithRawResponse(client.dns_records)
        self.dnssecs = resources.AsyncDNSSECsWithRawResponse(client.dnssecs)
        self.emails = resources.AsyncEmailsWithRawResponse(client.emails)
        self.filters = resources.AsyncFiltersWithRawResponse(client.filters)
        self.firewalls = resources.AsyncFirewallsWithRawResponse(client.firewalls)
        self.healthchecks = resources.AsyncHealthchecksWithRawResponse(client.healthchecks)
        self.keyless_certificates = resources.AsyncKeylessCertificatesWithRawResponse(client.keyless_certificates)
        self.logpush = resources.AsyncLogpushWithRawResponse(client.logpush)
        self.logs = resources.AsyncLogsWithRawResponse(client.logs)
        self.origin_tls_client_auth = resources.AsyncOriginTLSClientAuthWithRawResponse(client.origin_tls_client_auth)
        self.pagerules = resources.AsyncPagerulesWithRawResponse(client.pagerules)
        self.rate_limits = resources.AsyncRateLimitsWithRawResponse(client.rate_limits)
        self.secondary_dns = resources.AsyncSecondaryDNSWithRawResponse(client.secondary_dns)
        self.settings = resources.AsyncSettingsWithRawResponse(client.settings)
        self.waiting_rooms = resources.AsyncWaitingRoomsWithRawResponse(client.waiting_rooms)
        self.web3s = resources.AsyncWeb3sWithRawResponse(client.web3s)
        self.workers = resources.AsyncWorkersWithRawResponse(client.workers)
        self.activation_checks = resources.AsyncActivationChecksWithRawResponse(client.activation_checks)
        self.api_gateways = resources.AsyncAPIGatewaysWithRawResponse(client.api_gateways)
        self.managed_headers = resources.AsyncManagedHeadersWithRawResponse(client.managed_headers)
        self.page_shields = resources.AsyncPageShieldsWithRawResponse(client.page_shields)
        self.rulesets = resources.AsyncRulesetsWithRawResponse(client.rulesets)
        self.url_normalizations = resources.AsyncURLNormalizationsWithRawResponse(client.url_normalizations)
        self.spectrums = resources.AsyncSpectrumsWithRawResponse(client.spectrums)
        self.addresses = resources.AsyncAddressesWithRawResponse(client.addresses)
        self.audit_logs = resources.AsyncAuditLogsWithRawResponse(client.audit_logs)
        self.billings = resources.AsyncBillingsWithRawResponse(client.billings)
        self.brand_protections = resources.AsyncBrandProtectionsWithRawResponse(client.brand_protections)
        self.cfd_tunnels = resources.AsyncCfdTunnelsWithRawResponse(client.cfd_tunnels)
        self.diagnostics = resources.AsyncDiagnosticsWithRawResponse(client.diagnostics)
        self.dlps = resources.AsyncDLPsWithRawResponse(client.dlps)
        self.dns_firewalls = resources.AsyncDNSFirewallsWithRawResponse(client.dns_firewalls)
        self.images = resources.AsyncImagesWithRawResponse(client.images)
        self.intels = resources.AsyncIntelsWithRawResponse(client.intels)
        self.magics = resources.AsyncMagicsWithRawResponse(client.magics)
        self.account_members = resources.AsyncAccountMembersWithRawResponse(client.account_members)
        self.mnms = resources.AsyncMnmsWithRawResponse(client.mnms)
        self.mtls_certificates = resources.AsyncMtlsCertificatesWithRawResponse(client.mtls_certificates)
        self.pages = resources.AsyncPagesWithRawResponse(client.pages)
        self.pcaps = resources.AsyncPcapsWithRawResponse(client.pcaps)
        self.registrar = resources.AsyncRegistrarWithRawResponse(client.registrar)
        self.request_tracers = resources.AsyncRequestTracersWithRawResponse(client.request_tracers)
        self.roles = resources.AsyncRolesWithRawResponse(client.roles)
        self.rules = resources.AsyncRulesWithRawResponse(client.rules)
        self.storage = resources.AsyncStorageWithRawResponse(client.storage)
        self.stream = resources.AsyncStreamWithRawResponse(client.stream)
        self.teamnets = resources.AsyncTeamnetsWithRawResponse(client.teamnets)
        self.tunnels = resources.AsyncTunnelsWithRawResponse(client.tunnels)
        self.gateways = resources.AsyncGatewaysWithRawResponse(client.gateways)
        self.alerting = resources.AsyncAlertingWithRawResponse(client.alerting)
        self.devices = resources.AsyncDevicesWithRawResponse(client.devices)
        self.d1 = resources.AsyncD1WithRawResponse(client.d1)
        self.dex = resources.AsyncDEXWithRawResponse(client.dex)
        self.r2 = resources.AsyncR2WithRawResponse(client.r2)
        self.teamnet = resources.AsyncTeamnetWithRawResponse(client.teamnet)
        self.warp_connector = resources.AsyncWarpConnectorWithRawResponse(client.warp_connector)
        self.dispatchers = resources.AsyncDispatchersWithRawResponse(client.dispatchers)
        self.workers_for_platforms = resources.AsyncWorkersForPlatformsWithRawResponse(client.workers_for_platforms)
        self.worker_domains = resources.AsyncWorkerDomainsWithRawResponse(client.worker_domains)
        self.worker_scripts = resources.AsyncWorkerScriptsWithRawResponse(client.worker_scripts)
        self.zerotrust = resources.AsyncZerotrustWithRawResponse(client.zerotrust)
        self.addressing = resources.AsyncAddressingWithRawResponse(client.addressing)
        self.challenges = resources.AsyncChallengesWithRawResponse(client.challenges)
        self.hyperdrive = resources.AsyncHyperdriveWithRawResponse(client.hyperdrive)
        self.intel = resources.AsyncIntelWithRawResponse(client.intel)
        self.rum = resources.AsyncRumWithRawResponse(client.rum)
        self.vectorize = resources.AsyncVectorizeWithRawResponse(client.vectorize)
        self.url_scanner = resources.AsyncURLScannerWithRawResponse(client.url_scanner)
        self.radar = resources.AsyncRadarWithRawResponse(client.radar)
        self.bot_managements = resources.AsyncBotManagementsWithRawResponse(client.bot_managements)
        self.cache_reserves = resources.AsyncCacheReservesWithRawResponse(client.cache_reserves)
        self.origin_post_quantum_encryptions = resources.AsyncOriginPostQuantumEncryptionsWithRawResponse(
            client.origin_post_quantum_encryptions
        )
        self.cache = resources.AsyncCacheWithRawResponse(client.cache)
        self.firewall = resources.AsyncFirewallWithRawResponse(client.firewall)
        self.zaraz = resources.AsyncZarazWithRawResponse(client.zaraz)
        self.speed_api = resources.AsyncSpeedAPIWithRawResponse(client.speed_api)
        self.dcv_delegation = resources.AsyncDcvDelegationWithRawResponse(client.dcv_delegation)
        self.hostnames = resources.AsyncHostnamesWithRawResponse(client.hostnames)
        self.page_shield = resources.AsyncPageShieldWithRawResponse(client.page_shield)
        self.font_settings = resources.AsyncFontSettingsWithRawResponse(client.font_settings)
        self.snippets = resources.AsyncSnippetsWithRawResponse(client.snippets)
        self.dlp = resources.AsyncDLPWithRawResponse(client.dlp)
        self.gateway = resources.AsyncGatewayWithRawResponse(client.gateway)
        self.access_tags = resources.AsyncAccessTagsWithRawResponse(client.access_tags)


class CloudflareWithStreamedResponse:
    def __init__(self, client: Cloudflare) -> None:
        self.accounts = resources.AccountsWithStreamingResponse(client.accounts)
        self.certificates = resources.CertificatesWithStreamingResponse(client.certificates)
        self.ips = resources.IPsWithStreamingResponse(client.ips)
        self.memberships = resources.MembershipsWithStreamingResponse(client.memberships)
        self.users = resources.UsersWithStreamingResponse(client.users)
        self.zones = resources.ZonesWithStreamingResponse(client.zones)
        self.load_balancers = resources.LoadBalancersWithStreamingResponse(client.load_balancers)
        self.access = resources.AccessWithStreamingResponse(client.access)
        self.dns_analytics = resources.DNSAnalyticsWithStreamingResponse(client.dns_analytics)
        self.purge_caches = resources.PurgeCachesWithStreamingResponse(client.purge_caches)
        self.ssls = resources.SSLsWithStreamingResponse(client.ssls)
        self.subscriptions = resources.SubscriptionsWithStreamingResponse(client.subscriptions)
        self.acms = resources.AcmsWithStreamingResponse(client.acms)
        self.analytics = resources.AnalyticsWithStreamingResponse(client.analytics)
        self.argo = resources.ArgoWithStreamingResponse(client.argo)
        self.available_plans = resources.AvailablePlansWithStreamingResponse(client.available_plans)
        self.available_rate_plans = resources.AvailableRatePlansWithStreamingResponse(client.available_rate_plans)
        self.caches = resources.CachesWithStreamingResponse(client.caches)
        self.certificate_authorities = resources.CertificateAuthoritiesWithStreamingResponse(
            client.certificate_authorities
        )
        self.client_certificates = resources.ClientCertificatesWithStreamingResponse(client.client_certificates)
        self.custom_certificates = resources.CustomCertificatesWithStreamingResponse(client.custom_certificates)
        self.custom_hostnames = resources.CustomHostnamesWithStreamingResponse(client.custom_hostnames)
        self.custom_ns = resources.CustomNsWithStreamingResponse(client.custom_ns)
        self.dns_records = resources.DNSRecordsWithStreamingResponse(client.dns_records)
        self.dnssecs = resources.DNSSECsWithStreamingResponse(client.dnssecs)
        self.emails = resources.EmailsWithStreamingResponse(client.emails)
        self.filters = resources.FiltersWithStreamingResponse(client.filters)
        self.firewalls = resources.FirewallsWithStreamingResponse(client.firewalls)
        self.healthchecks = resources.HealthchecksWithStreamingResponse(client.healthchecks)
        self.keyless_certificates = resources.KeylessCertificatesWithStreamingResponse(client.keyless_certificates)
        self.logpush = resources.LogpushWithStreamingResponse(client.logpush)
        self.logs = resources.LogsWithStreamingResponse(client.logs)
        self.origin_tls_client_auth = resources.OriginTLSClientAuthWithStreamingResponse(client.origin_tls_client_auth)
        self.pagerules = resources.PagerulesWithStreamingResponse(client.pagerules)
        self.rate_limits = resources.RateLimitsWithStreamingResponse(client.rate_limits)
        self.secondary_dns = resources.SecondaryDNSWithStreamingResponse(client.secondary_dns)
        self.settings = resources.SettingsWithStreamingResponse(client.settings)
        self.waiting_rooms = resources.WaitingRoomsWithStreamingResponse(client.waiting_rooms)
        self.web3s = resources.Web3sWithStreamingResponse(client.web3s)
        self.workers = resources.WorkersWithStreamingResponse(client.workers)
        self.activation_checks = resources.ActivationChecksWithStreamingResponse(client.activation_checks)
        self.api_gateways = resources.APIGatewaysWithStreamingResponse(client.api_gateways)
        self.managed_headers = resources.ManagedHeadersWithStreamingResponse(client.managed_headers)
        self.page_shields = resources.PageShieldsWithStreamingResponse(client.page_shields)
        self.rulesets = resources.RulesetsWithStreamingResponse(client.rulesets)
        self.url_normalizations = resources.URLNormalizationsWithStreamingResponse(client.url_normalizations)
        self.spectrums = resources.SpectrumsWithStreamingResponse(client.spectrums)
        self.addresses = resources.AddressesWithStreamingResponse(client.addresses)
        self.audit_logs = resources.AuditLogsWithStreamingResponse(client.audit_logs)
        self.billings = resources.BillingsWithStreamingResponse(client.billings)
        self.brand_protections = resources.BrandProtectionsWithStreamingResponse(client.brand_protections)
        self.cfd_tunnels = resources.CfdTunnelsWithStreamingResponse(client.cfd_tunnels)
        self.diagnostics = resources.DiagnosticsWithStreamingResponse(client.diagnostics)
        self.dlps = resources.DLPsWithStreamingResponse(client.dlps)
        self.dns_firewalls = resources.DNSFirewallsWithStreamingResponse(client.dns_firewalls)
        self.images = resources.ImagesWithStreamingResponse(client.images)
        self.intels = resources.IntelsWithStreamingResponse(client.intels)
        self.magics = resources.MagicsWithStreamingResponse(client.magics)
        self.account_members = resources.AccountMembersWithStreamingResponse(client.account_members)
        self.mnms = resources.MnmsWithStreamingResponse(client.mnms)
        self.mtls_certificates = resources.MtlsCertificatesWithStreamingResponse(client.mtls_certificates)
        self.pages = resources.PagesWithStreamingResponse(client.pages)
        self.pcaps = resources.PcapsWithStreamingResponse(client.pcaps)
        self.registrar = resources.RegistrarWithStreamingResponse(client.registrar)
        self.request_tracers = resources.RequestTracersWithStreamingResponse(client.request_tracers)
        self.roles = resources.RolesWithStreamingResponse(client.roles)
        self.rules = resources.RulesWithStreamingResponse(client.rules)
        self.storage = resources.StorageWithStreamingResponse(client.storage)
        self.stream = resources.StreamWithStreamingResponse(client.stream)
        self.teamnets = resources.TeamnetsWithStreamingResponse(client.teamnets)
        self.tunnels = resources.TunnelsWithStreamingResponse(client.tunnels)
        self.gateways = resources.GatewaysWithStreamingResponse(client.gateways)
        self.alerting = resources.AlertingWithStreamingResponse(client.alerting)
        self.devices = resources.DevicesWithStreamingResponse(client.devices)
        self.d1 = resources.D1WithStreamingResponse(client.d1)
        self.dex = resources.DEXWithStreamingResponse(client.dex)
        self.r2 = resources.R2WithStreamingResponse(client.r2)
        self.teamnet = resources.TeamnetWithStreamingResponse(client.teamnet)
        self.warp_connector = resources.WarpConnectorWithStreamingResponse(client.warp_connector)
        self.dispatchers = resources.DispatchersWithStreamingResponse(client.dispatchers)
        self.workers_for_platforms = resources.WorkersForPlatformsWithStreamingResponse(client.workers_for_platforms)
        self.worker_domains = resources.WorkerDomainsWithStreamingResponse(client.worker_domains)
        self.worker_scripts = resources.WorkerScriptsWithStreamingResponse(client.worker_scripts)
        self.zerotrust = resources.ZerotrustWithStreamingResponse(client.zerotrust)
        self.addressing = resources.AddressingWithStreamingResponse(client.addressing)
        self.challenges = resources.ChallengesWithStreamingResponse(client.challenges)
        self.hyperdrive = resources.HyperdriveWithStreamingResponse(client.hyperdrive)
        self.intel = resources.IntelWithStreamingResponse(client.intel)
        self.rum = resources.RumWithStreamingResponse(client.rum)
        self.vectorize = resources.VectorizeWithStreamingResponse(client.vectorize)
        self.url_scanner = resources.URLScannerWithStreamingResponse(client.url_scanner)
        self.radar = resources.RadarWithStreamingResponse(client.radar)
        self.bot_managements = resources.BotManagementsWithStreamingResponse(client.bot_managements)
        self.cache_reserves = resources.CacheReservesWithStreamingResponse(client.cache_reserves)
        self.origin_post_quantum_encryptions = resources.OriginPostQuantumEncryptionsWithStreamingResponse(
            client.origin_post_quantum_encryptions
        )
        self.cache = resources.CacheWithStreamingResponse(client.cache)
        self.firewall = resources.FirewallWithStreamingResponse(client.firewall)
        self.zaraz = resources.ZarazWithStreamingResponse(client.zaraz)
        self.speed_api = resources.SpeedAPIWithStreamingResponse(client.speed_api)
        self.dcv_delegation = resources.DcvDelegationWithStreamingResponse(client.dcv_delegation)
        self.hostnames = resources.HostnamesWithStreamingResponse(client.hostnames)
        self.page_shield = resources.PageShieldWithStreamingResponse(client.page_shield)
        self.font_settings = resources.FontSettingsWithStreamingResponse(client.font_settings)
        self.snippets = resources.SnippetsWithStreamingResponse(client.snippets)
        self.dlp = resources.DLPWithStreamingResponse(client.dlp)
        self.gateway = resources.GatewayWithStreamingResponse(client.gateway)
        self.access_tags = resources.AccessTagsWithStreamingResponse(client.access_tags)


class AsyncCloudflareWithStreamedResponse:
    def __init__(self, client: AsyncCloudflare) -> None:
        self.accounts = resources.AsyncAccountsWithStreamingResponse(client.accounts)
        self.certificates = resources.AsyncCertificatesWithStreamingResponse(client.certificates)
        self.ips = resources.AsyncIPsWithStreamingResponse(client.ips)
        self.memberships = resources.AsyncMembershipsWithStreamingResponse(client.memberships)
        self.users = resources.AsyncUsersWithStreamingResponse(client.users)
        self.zones = resources.AsyncZonesWithStreamingResponse(client.zones)
        self.load_balancers = resources.AsyncLoadBalancersWithStreamingResponse(client.load_balancers)
        self.access = resources.AsyncAccessWithStreamingResponse(client.access)
        self.dns_analytics = resources.AsyncDNSAnalyticsWithStreamingResponse(client.dns_analytics)
        self.purge_caches = resources.AsyncPurgeCachesWithStreamingResponse(client.purge_caches)
        self.ssls = resources.AsyncSSLsWithStreamingResponse(client.ssls)
        self.subscriptions = resources.AsyncSubscriptionsWithStreamingResponse(client.subscriptions)
        self.acms = resources.AsyncAcmsWithStreamingResponse(client.acms)
        self.analytics = resources.AsyncAnalyticsWithStreamingResponse(client.analytics)
        self.argo = resources.AsyncArgoWithStreamingResponse(client.argo)
        self.available_plans = resources.AsyncAvailablePlansWithStreamingResponse(client.available_plans)
        self.available_rate_plans = resources.AsyncAvailableRatePlansWithStreamingResponse(client.available_rate_plans)
        self.caches = resources.AsyncCachesWithStreamingResponse(client.caches)
        self.certificate_authorities = resources.AsyncCertificateAuthoritiesWithStreamingResponse(
            client.certificate_authorities
        )
        self.client_certificates = resources.AsyncClientCertificatesWithStreamingResponse(client.client_certificates)
        self.custom_certificates = resources.AsyncCustomCertificatesWithStreamingResponse(client.custom_certificates)
        self.custom_hostnames = resources.AsyncCustomHostnamesWithStreamingResponse(client.custom_hostnames)
        self.custom_ns = resources.AsyncCustomNsWithStreamingResponse(client.custom_ns)
        self.dns_records = resources.AsyncDNSRecordsWithStreamingResponse(client.dns_records)
        self.dnssecs = resources.AsyncDNSSECsWithStreamingResponse(client.dnssecs)
        self.emails = resources.AsyncEmailsWithStreamingResponse(client.emails)
        self.filters = resources.AsyncFiltersWithStreamingResponse(client.filters)
        self.firewalls = resources.AsyncFirewallsWithStreamingResponse(client.firewalls)
        self.healthchecks = resources.AsyncHealthchecksWithStreamingResponse(client.healthchecks)
        self.keyless_certificates = resources.AsyncKeylessCertificatesWithStreamingResponse(client.keyless_certificates)
        self.logpush = resources.AsyncLogpushWithStreamingResponse(client.logpush)
        self.logs = resources.AsyncLogsWithStreamingResponse(client.logs)
        self.origin_tls_client_auth = resources.AsyncOriginTLSClientAuthWithStreamingResponse(
            client.origin_tls_client_auth
        )
        self.pagerules = resources.AsyncPagerulesWithStreamingResponse(client.pagerules)
        self.rate_limits = resources.AsyncRateLimitsWithStreamingResponse(client.rate_limits)
        self.secondary_dns = resources.AsyncSecondaryDNSWithStreamingResponse(client.secondary_dns)
        self.settings = resources.AsyncSettingsWithStreamingResponse(client.settings)
        self.waiting_rooms = resources.AsyncWaitingRoomsWithStreamingResponse(client.waiting_rooms)
        self.web3s = resources.AsyncWeb3sWithStreamingResponse(client.web3s)
        self.workers = resources.AsyncWorkersWithStreamingResponse(client.workers)
        self.activation_checks = resources.AsyncActivationChecksWithStreamingResponse(client.activation_checks)
        self.api_gateways = resources.AsyncAPIGatewaysWithStreamingResponse(client.api_gateways)
        self.managed_headers = resources.AsyncManagedHeadersWithStreamingResponse(client.managed_headers)
        self.page_shields = resources.AsyncPageShieldsWithStreamingResponse(client.page_shields)
        self.rulesets = resources.AsyncRulesetsWithStreamingResponse(client.rulesets)
        self.url_normalizations = resources.AsyncURLNormalizationsWithStreamingResponse(client.url_normalizations)
        self.spectrums = resources.AsyncSpectrumsWithStreamingResponse(client.spectrums)
        self.addresses = resources.AsyncAddressesWithStreamingResponse(client.addresses)
        self.audit_logs = resources.AsyncAuditLogsWithStreamingResponse(client.audit_logs)
        self.billings = resources.AsyncBillingsWithStreamingResponse(client.billings)
        self.brand_protections = resources.AsyncBrandProtectionsWithStreamingResponse(client.brand_protections)
        self.cfd_tunnels = resources.AsyncCfdTunnelsWithStreamingResponse(client.cfd_tunnels)
        self.diagnostics = resources.AsyncDiagnosticsWithStreamingResponse(client.diagnostics)
        self.dlps = resources.AsyncDLPsWithStreamingResponse(client.dlps)
        self.dns_firewalls = resources.AsyncDNSFirewallsWithStreamingResponse(client.dns_firewalls)
        self.images = resources.AsyncImagesWithStreamingResponse(client.images)
        self.intels = resources.AsyncIntelsWithStreamingResponse(client.intels)
        self.magics = resources.AsyncMagicsWithStreamingResponse(client.magics)
        self.account_members = resources.AsyncAccountMembersWithStreamingResponse(client.account_members)
        self.mnms = resources.AsyncMnmsWithStreamingResponse(client.mnms)
        self.mtls_certificates = resources.AsyncMtlsCertificatesWithStreamingResponse(client.mtls_certificates)
        self.pages = resources.AsyncPagesWithStreamingResponse(client.pages)
        self.pcaps = resources.AsyncPcapsWithStreamingResponse(client.pcaps)
        self.registrar = resources.AsyncRegistrarWithStreamingResponse(client.registrar)
        self.request_tracers = resources.AsyncRequestTracersWithStreamingResponse(client.request_tracers)
        self.roles = resources.AsyncRolesWithStreamingResponse(client.roles)
        self.rules = resources.AsyncRulesWithStreamingResponse(client.rules)
        self.storage = resources.AsyncStorageWithStreamingResponse(client.storage)
        self.stream = resources.AsyncStreamWithStreamingResponse(client.stream)
        self.teamnets = resources.AsyncTeamnetsWithStreamingResponse(client.teamnets)
        self.tunnels = resources.AsyncTunnelsWithStreamingResponse(client.tunnels)
        self.gateways = resources.AsyncGatewaysWithStreamingResponse(client.gateways)
        self.alerting = resources.AsyncAlertingWithStreamingResponse(client.alerting)
        self.devices = resources.AsyncDevicesWithStreamingResponse(client.devices)
        self.d1 = resources.AsyncD1WithStreamingResponse(client.d1)
        self.dex = resources.AsyncDEXWithStreamingResponse(client.dex)
        self.r2 = resources.AsyncR2WithStreamingResponse(client.r2)
        self.teamnet = resources.AsyncTeamnetWithStreamingResponse(client.teamnet)
        self.warp_connector = resources.AsyncWarpConnectorWithStreamingResponse(client.warp_connector)
        self.dispatchers = resources.AsyncDispatchersWithStreamingResponse(client.dispatchers)
        self.workers_for_platforms = resources.AsyncWorkersForPlatformsWithStreamingResponse(
            client.workers_for_platforms
        )
        self.worker_domains = resources.AsyncWorkerDomainsWithStreamingResponse(client.worker_domains)
        self.worker_scripts = resources.AsyncWorkerScriptsWithStreamingResponse(client.worker_scripts)
        self.zerotrust = resources.AsyncZerotrustWithStreamingResponse(client.zerotrust)
        self.addressing = resources.AsyncAddressingWithStreamingResponse(client.addressing)
        self.challenges = resources.AsyncChallengesWithStreamingResponse(client.challenges)
        self.hyperdrive = resources.AsyncHyperdriveWithStreamingResponse(client.hyperdrive)
        self.intel = resources.AsyncIntelWithStreamingResponse(client.intel)
        self.rum = resources.AsyncRumWithStreamingResponse(client.rum)
        self.vectorize = resources.AsyncVectorizeWithStreamingResponse(client.vectorize)
        self.url_scanner = resources.AsyncURLScannerWithStreamingResponse(client.url_scanner)
        self.radar = resources.AsyncRadarWithStreamingResponse(client.radar)
        self.bot_managements = resources.AsyncBotManagementsWithStreamingResponse(client.bot_managements)
        self.cache_reserves = resources.AsyncCacheReservesWithStreamingResponse(client.cache_reserves)
        self.origin_post_quantum_encryptions = resources.AsyncOriginPostQuantumEncryptionsWithStreamingResponse(
            client.origin_post_quantum_encryptions
        )
        self.cache = resources.AsyncCacheWithStreamingResponse(client.cache)
        self.firewall = resources.AsyncFirewallWithStreamingResponse(client.firewall)
        self.zaraz = resources.AsyncZarazWithStreamingResponse(client.zaraz)
        self.speed_api = resources.AsyncSpeedAPIWithStreamingResponse(client.speed_api)
        self.dcv_delegation = resources.AsyncDcvDelegationWithStreamingResponse(client.dcv_delegation)
        self.hostnames = resources.AsyncHostnamesWithStreamingResponse(client.hostnames)
        self.page_shield = resources.AsyncPageShieldWithStreamingResponse(client.page_shield)
        self.font_settings = resources.AsyncFontSettingsWithStreamingResponse(client.font_settings)
        self.snippets = resources.AsyncSnippetsWithStreamingResponse(client.snippets)
        self.dlp = resources.AsyncDLPWithStreamingResponse(client.dlp)
        self.gateway = resources.AsyncGatewayWithStreamingResponse(client.gateway)
        self.access_tags = resources.AsyncAccessTagsWithStreamingResponse(client.access_tags)


Client = Cloudflare

AsyncClient = AsyncCloudflare
