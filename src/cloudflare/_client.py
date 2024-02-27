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
    user: resources.User
    zones: resources.Zones
    load_balancers: resources.LoadBalancers
    access: resources.Access
    cache: resources.Cache
    ssl: resources.SSL
    subscriptions: resources.Subscriptions
    acm: resources.ACM
    argo: resources.Argo
    available_plans: resources.AvailablePlans
    available_rate_plans: resources.AvailableRatePlans
    certificate_authorities: resources.CertificateAuthorities
    client_certificates: resources.ClientCertificates
    custom_certificates: resources.CustomCertificates
    custom_hostnames: resources.CustomHostnames
    custom_nameservers: resources.CustomNameservers
    dns: resources.DNS
    dnssec: resources.DNSSEC
    emails: resources.Emails
    filters: resources.Filters
    firewall: resources.Firewall
    healthchecks: resources.Healthchecks
    keyless_certificates: resources.KeylessCertificates
    logpush: resources.Logpush
    logs: resources.Logs
    origin_tls_client_auth: resources.OriginTLSClientAuth
    pagerules: resources.Pagerules
    rate_limits: resources.RateLimits
    secondary_dns: resources.SecondaryDNS
    waiting_rooms: resources.WaitingRooms
    web3: resources.Web3
    workers: resources.Workers
    kv: resources.KV
    managed_headers: resources.ManagedHeaders
    page_shield: resources.PageShield
    rulesets: resources.Rulesets
    url_normalizations: resources.URLNormalizations
    spectrum: resources.Spectrum
    addresses: resources.Addresses
    audit_logs: resources.AuditLogs
    billing: resources.Billing
    brand_protection: resources.BrandProtection
    tunnels: resources.Tunnels
    diagnostics: resources.Diagnostics
    dlp: resources.DLP
    images: resources.Images
    intel: resources.Intel
    magic_transit: resources.MagicTransit
    mnms: resources.MNMs
    mtls_certificates: resources.MTLSCertificates
    pages: resources.Pages
    pcaps: resources.PCAPs
    registrar: resources.Registrar
    request_tracers: resources.RequestTracers
    roles: resources.Roles
    rules: resources.Rules
    storage: resources.Storage
    stream: resources.Stream
    gateways: resources.Gateways
    alerting: resources.Alerting
    devices: resources.Devices
    d1: resources.D1
    dex: resources.DEX
    r2: resources.R2
    teamnet: resources.Teamnet
    warp_connector: resources.WARPConnector
    dispatchers: resources.Dispatchers
    workers_for_platforms: resources.WorkersForPlatforms
    zero_trust: resources.ZeroTrust
    challenges: resources.Challenges
    hyperdrive: resources.Hyperdrive
    rum: resources.RUM
    vectorize: resources.Vectorize
    url_scanner: resources.URLScanner
    radar: resources.Radar
    bot_management: resources.BotManagement
    origin_post_quantum_encryption: resources.OriginPostQuantumEncryption
    speed: resources.Speed
    dcv_delegation: resources.DcvDelegation
    hostnames: resources.Hostnames
    snippets: resources.Snippets
    calls: resources.Calls
    cloudforce_one: resources.CloudforceOne
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
        self.user = resources.User(self)
        self.zones = resources.Zones(self)
        self.load_balancers = resources.LoadBalancers(self)
        self.access = resources.Access(self)
        self.cache = resources.Cache(self)
        self.ssl = resources.SSL(self)
        self.subscriptions = resources.Subscriptions(self)
        self.acm = resources.ACM(self)
        self.argo = resources.Argo(self)
        self.available_plans = resources.AvailablePlans(self)
        self.available_rate_plans = resources.AvailableRatePlans(self)
        self.certificate_authorities = resources.CertificateAuthorities(self)
        self.client_certificates = resources.ClientCertificates(self)
        self.custom_certificates = resources.CustomCertificates(self)
        self.custom_hostnames = resources.CustomHostnames(self)
        self.custom_nameservers = resources.CustomNameservers(self)
        self.dns = resources.DNS(self)
        self.dnssec = resources.DNSSEC(self)
        self.emails = resources.Emails(self)
        self.filters = resources.Filters(self)
        self.firewall = resources.Firewall(self)
        self.healthchecks = resources.Healthchecks(self)
        self.keyless_certificates = resources.KeylessCertificates(self)
        self.logpush = resources.Logpush(self)
        self.logs = resources.Logs(self)
        self.origin_tls_client_auth = resources.OriginTLSClientAuth(self)
        self.pagerules = resources.Pagerules(self)
        self.rate_limits = resources.RateLimits(self)
        self.secondary_dns = resources.SecondaryDNS(self)
        self.waiting_rooms = resources.WaitingRooms(self)
        self.web3 = resources.Web3(self)
        self.workers = resources.Workers(self)
        self.kv = resources.KV(self)
        self.managed_headers = resources.ManagedHeaders(self)
        self.page_shield = resources.PageShield(self)
        self.rulesets = resources.Rulesets(self)
        self.url_normalizations = resources.URLNormalizations(self)
        self.spectrum = resources.Spectrum(self)
        self.addresses = resources.Addresses(self)
        self.audit_logs = resources.AuditLogs(self)
        self.billing = resources.Billing(self)
        self.brand_protection = resources.BrandProtection(self)
        self.tunnels = resources.Tunnels(self)
        self.diagnostics = resources.Diagnostics(self)
        self.dlp = resources.DLP(self)
        self.images = resources.Images(self)
        self.intel = resources.Intel(self)
        self.magic_transit = resources.MagicTransit(self)
        self.mnms = resources.MNMs(self)
        self.mtls_certificates = resources.MTLSCertificates(self)
        self.pages = resources.Pages(self)
        self.pcaps = resources.PCAPs(self)
        self.registrar = resources.Registrar(self)
        self.request_tracers = resources.RequestTracers(self)
        self.roles = resources.Roles(self)
        self.rules = resources.Rules(self)
        self.storage = resources.Storage(self)
        self.stream = resources.Stream(self)
        self.gateways = resources.Gateways(self)
        self.alerting = resources.Alerting(self)
        self.devices = resources.Devices(self)
        self.d1 = resources.D1(self)
        self.dex = resources.DEX(self)
        self.r2 = resources.R2(self)
        self.teamnet = resources.Teamnet(self)
        self.warp_connector = resources.WARPConnector(self)
        self.dispatchers = resources.Dispatchers(self)
        self.workers_for_platforms = resources.WorkersForPlatforms(self)
        self.zero_trust = resources.ZeroTrust(self)
        self.challenges = resources.Challenges(self)
        self.hyperdrive = resources.Hyperdrive(self)
        self.rum = resources.RUM(self)
        self.vectorize = resources.Vectorize(self)
        self.url_scanner = resources.URLScanner(self)
        self.radar = resources.Radar(self)
        self.bot_management = resources.BotManagement(self)
        self.origin_post_quantum_encryption = resources.OriginPostQuantumEncryption(self)
        self.speed = resources.Speed(self)
        self.dcv_delegation = resources.DcvDelegation(self)
        self.hostnames = resources.Hostnames(self)
        self.snippets = resources.Snippets(self)
        self.calls = resources.Calls(self)
        self.cloudforce_one = resources.CloudforceOne(self)
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
    user: resources.AsyncUser
    zones: resources.AsyncZones
    load_balancers: resources.AsyncLoadBalancers
    access: resources.AsyncAccess
    cache: resources.AsyncCache
    ssl: resources.AsyncSSL
    subscriptions: resources.AsyncSubscriptions
    acm: resources.AsyncACM
    argo: resources.AsyncArgo
    available_plans: resources.AsyncAvailablePlans
    available_rate_plans: resources.AsyncAvailableRatePlans
    certificate_authorities: resources.AsyncCertificateAuthorities
    client_certificates: resources.AsyncClientCertificates
    custom_certificates: resources.AsyncCustomCertificates
    custom_hostnames: resources.AsyncCustomHostnames
    custom_nameservers: resources.AsyncCustomNameservers
    dns: resources.AsyncDNS
    dnssec: resources.AsyncDNSSEC
    emails: resources.AsyncEmails
    filters: resources.AsyncFilters
    firewall: resources.AsyncFirewall
    healthchecks: resources.AsyncHealthchecks
    keyless_certificates: resources.AsyncKeylessCertificates
    logpush: resources.AsyncLogpush
    logs: resources.AsyncLogs
    origin_tls_client_auth: resources.AsyncOriginTLSClientAuth
    pagerules: resources.AsyncPagerules
    rate_limits: resources.AsyncRateLimits
    secondary_dns: resources.AsyncSecondaryDNS
    waiting_rooms: resources.AsyncWaitingRooms
    web3: resources.AsyncWeb3
    workers: resources.AsyncWorkers
    kv: resources.AsyncKV
    managed_headers: resources.AsyncManagedHeaders
    page_shield: resources.AsyncPageShield
    rulesets: resources.AsyncRulesets
    url_normalizations: resources.AsyncURLNormalizations
    spectrum: resources.AsyncSpectrum
    addresses: resources.AsyncAddresses
    audit_logs: resources.AsyncAuditLogs
    billing: resources.AsyncBilling
    brand_protection: resources.AsyncBrandProtection
    tunnels: resources.AsyncTunnels
    diagnostics: resources.AsyncDiagnostics
    dlp: resources.AsyncDLP
    images: resources.AsyncImages
    intel: resources.AsyncIntel
    magic_transit: resources.AsyncMagicTransit
    mnms: resources.AsyncMNMs
    mtls_certificates: resources.AsyncMTLSCertificates
    pages: resources.AsyncPages
    pcaps: resources.AsyncPCAPs
    registrar: resources.AsyncRegistrar
    request_tracers: resources.AsyncRequestTracers
    roles: resources.AsyncRoles
    rules: resources.AsyncRules
    storage: resources.AsyncStorage
    stream: resources.AsyncStream
    gateways: resources.AsyncGateways
    alerting: resources.AsyncAlerting
    devices: resources.AsyncDevices
    d1: resources.AsyncD1
    dex: resources.AsyncDEX
    r2: resources.AsyncR2
    teamnet: resources.AsyncTeamnet
    warp_connector: resources.AsyncWARPConnector
    dispatchers: resources.AsyncDispatchers
    workers_for_platforms: resources.AsyncWorkersForPlatforms
    zero_trust: resources.AsyncZeroTrust
    challenges: resources.AsyncChallenges
    hyperdrive: resources.AsyncHyperdrive
    rum: resources.AsyncRUM
    vectorize: resources.AsyncVectorize
    url_scanner: resources.AsyncURLScanner
    radar: resources.AsyncRadar
    bot_management: resources.AsyncBotManagement
    origin_post_quantum_encryption: resources.AsyncOriginPostQuantumEncryption
    speed: resources.AsyncSpeed
    dcv_delegation: resources.AsyncDcvDelegation
    hostnames: resources.AsyncHostnames
    snippets: resources.AsyncSnippets
    calls: resources.AsyncCalls
    cloudforce_one: resources.AsyncCloudforceOne
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
        self.user = resources.AsyncUser(self)
        self.zones = resources.AsyncZones(self)
        self.load_balancers = resources.AsyncLoadBalancers(self)
        self.access = resources.AsyncAccess(self)
        self.cache = resources.AsyncCache(self)
        self.ssl = resources.AsyncSSL(self)
        self.subscriptions = resources.AsyncSubscriptions(self)
        self.acm = resources.AsyncACM(self)
        self.argo = resources.AsyncArgo(self)
        self.available_plans = resources.AsyncAvailablePlans(self)
        self.available_rate_plans = resources.AsyncAvailableRatePlans(self)
        self.certificate_authorities = resources.AsyncCertificateAuthorities(self)
        self.client_certificates = resources.AsyncClientCertificates(self)
        self.custom_certificates = resources.AsyncCustomCertificates(self)
        self.custom_hostnames = resources.AsyncCustomHostnames(self)
        self.custom_nameservers = resources.AsyncCustomNameservers(self)
        self.dns = resources.AsyncDNS(self)
        self.dnssec = resources.AsyncDNSSEC(self)
        self.emails = resources.AsyncEmails(self)
        self.filters = resources.AsyncFilters(self)
        self.firewall = resources.AsyncFirewall(self)
        self.healthchecks = resources.AsyncHealthchecks(self)
        self.keyless_certificates = resources.AsyncKeylessCertificates(self)
        self.logpush = resources.AsyncLogpush(self)
        self.logs = resources.AsyncLogs(self)
        self.origin_tls_client_auth = resources.AsyncOriginTLSClientAuth(self)
        self.pagerules = resources.AsyncPagerules(self)
        self.rate_limits = resources.AsyncRateLimits(self)
        self.secondary_dns = resources.AsyncSecondaryDNS(self)
        self.waiting_rooms = resources.AsyncWaitingRooms(self)
        self.web3 = resources.AsyncWeb3(self)
        self.workers = resources.AsyncWorkers(self)
        self.kv = resources.AsyncKV(self)
        self.managed_headers = resources.AsyncManagedHeaders(self)
        self.page_shield = resources.AsyncPageShield(self)
        self.rulesets = resources.AsyncRulesets(self)
        self.url_normalizations = resources.AsyncURLNormalizations(self)
        self.spectrum = resources.AsyncSpectrum(self)
        self.addresses = resources.AsyncAddresses(self)
        self.audit_logs = resources.AsyncAuditLogs(self)
        self.billing = resources.AsyncBilling(self)
        self.brand_protection = resources.AsyncBrandProtection(self)
        self.tunnels = resources.AsyncTunnels(self)
        self.diagnostics = resources.AsyncDiagnostics(self)
        self.dlp = resources.AsyncDLP(self)
        self.images = resources.AsyncImages(self)
        self.intel = resources.AsyncIntel(self)
        self.magic_transit = resources.AsyncMagicTransit(self)
        self.mnms = resources.AsyncMNMs(self)
        self.mtls_certificates = resources.AsyncMTLSCertificates(self)
        self.pages = resources.AsyncPages(self)
        self.pcaps = resources.AsyncPCAPs(self)
        self.registrar = resources.AsyncRegistrar(self)
        self.request_tracers = resources.AsyncRequestTracers(self)
        self.roles = resources.AsyncRoles(self)
        self.rules = resources.AsyncRules(self)
        self.storage = resources.AsyncStorage(self)
        self.stream = resources.AsyncStream(self)
        self.gateways = resources.AsyncGateways(self)
        self.alerting = resources.AsyncAlerting(self)
        self.devices = resources.AsyncDevices(self)
        self.d1 = resources.AsyncD1(self)
        self.dex = resources.AsyncDEX(self)
        self.r2 = resources.AsyncR2(self)
        self.teamnet = resources.AsyncTeamnet(self)
        self.warp_connector = resources.AsyncWARPConnector(self)
        self.dispatchers = resources.AsyncDispatchers(self)
        self.workers_for_platforms = resources.AsyncWorkersForPlatforms(self)
        self.zero_trust = resources.AsyncZeroTrust(self)
        self.challenges = resources.AsyncChallenges(self)
        self.hyperdrive = resources.AsyncHyperdrive(self)
        self.rum = resources.AsyncRUM(self)
        self.vectorize = resources.AsyncVectorize(self)
        self.url_scanner = resources.AsyncURLScanner(self)
        self.radar = resources.AsyncRadar(self)
        self.bot_management = resources.AsyncBotManagement(self)
        self.origin_post_quantum_encryption = resources.AsyncOriginPostQuantumEncryption(self)
        self.speed = resources.AsyncSpeed(self)
        self.dcv_delegation = resources.AsyncDcvDelegation(self)
        self.hostnames = resources.AsyncHostnames(self)
        self.snippets = resources.AsyncSnippets(self)
        self.calls = resources.AsyncCalls(self)
        self.cloudforce_one = resources.AsyncCloudforceOne(self)
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
        self.user = resources.UserWithRawResponse(client.user)
        self.zones = resources.ZonesWithRawResponse(client.zones)
        self.load_balancers = resources.LoadBalancersWithRawResponse(client.load_balancers)
        self.access = resources.AccessWithRawResponse(client.access)
        self.cache = resources.CacheWithRawResponse(client.cache)
        self.ssl = resources.SSLWithRawResponse(client.ssl)
        self.subscriptions = resources.SubscriptionsWithRawResponse(client.subscriptions)
        self.acm = resources.ACMWithRawResponse(client.acm)
        self.argo = resources.ArgoWithRawResponse(client.argo)
        self.available_plans = resources.AvailablePlansWithRawResponse(client.available_plans)
        self.available_rate_plans = resources.AvailableRatePlansWithRawResponse(client.available_rate_plans)
        self.certificate_authorities = resources.CertificateAuthoritiesWithRawResponse(client.certificate_authorities)
        self.client_certificates = resources.ClientCertificatesWithRawResponse(client.client_certificates)
        self.custom_certificates = resources.CustomCertificatesWithRawResponse(client.custom_certificates)
        self.custom_hostnames = resources.CustomHostnamesWithRawResponse(client.custom_hostnames)
        self.custom_nameservers = resources.CustomNameserversWithRawResponse(client.custom_nameservers)
        self.dns = resources.DNSWithRawResponse(client.dns)
        self.dnssec = resources.DNSSECWithRawResponse(client.dnssec)
        self.emails = resources.EmailsWithRawResponse(client.emails)
        self.filters = resources.FiltersWithRawResponse(client.filters)
        self.firewall = resources.FirewallWithRawResponse(client.firewall)
        self.healthchecks = resources.HealthchecksWithRawResponse(client.healthchecks)
        self.keyless_certificates = resources.KeylessCertificatesWithRawResponse(client.keyless_certificates)
        self.logpush = resources.LogpushWithRawResponse(client.logpush)
        self.logs = resources.LogsWithRawResponse(client.logs)
        self.origin_tls_client_auth = resources.OriginTLSClientAuthWithRawResponse(client.origin_tls_client_auth)
        self.pagerules = resources.PagerulesWithRawResponse(client.pagerules)
        self.rate_limits = resources.RateLimitsWithRawResponse(client.rate_limits)
        self.secondary_dns = resources.SecondaryDNSWithRawResponse(client.secondary_dns)
        self.waiting_rooms = resources.WaitingRoomsWithRawResponse(client.waiting_rooms)
        self.web3 = resources.Web3WithRawResponse(client.web3)
        self.workers = resources.WorkersWithRawResponse(client.workers)
        self.kv = resources.KVWithRawResponse(client.kv)
        self.managed_headers = resources.ManagedHeadersWithRawResponse(client.managed_headers)
        self.page_shield = resources.PageShieldWithRawResponse(client.page_shield)
        self.rulesets = resources.RulesetsWithRawResponse(client.rulesets)
        self.url_normalizations = resources.URLNormalizationsWithRawResponse(client.url_normalizations)
        self.spectrum = resources.SpectrumWithRawResponse(client.spectrum)
        self.addresses = resources.AddressesWithRawResponse(client.addresses)
        self.audit_logs = resources.AuditLogsWithRawResponse(client.audit_logs)
        self.billing = resources.BillingWithRawResponse(client.billing)
        self.brand_protection = resources.BrandProtectionWithRawResponse(client.brand_protection)
        self.tunnels = resources.TunnelsWithRawResponse(client.tunnels)
        self.diagnostics = resources.DiagnosticsWithRawResponse(client.diagnostics)
        self.dlp = resources.DLPWithRawResponse(client.dlp)
        self.images = resources.ImagesWithRawResponse(client.images)
        self.intel = resources.IntelWithRawResponse(client.intel)
        self.magic_transit = resources.MagicTransitWithRawResponse(client.magic_transit)
        self.mnms = resources.MNMsWithRawResponse(client.mnms)
        self.mtls_certificates = resources.MTLSCertificatesWithRawResponse(client.mtls_certificates)
        self.pages = resources.PagesWithRawResponse(client.pages)
        self.pcaps = resources.PCAPsWithRawResponse(client.pcaps)
        self.registrar = resources.RegistrarWithRawResponse(client.registrar)
        self.request_tracers = resources.RequestTracersWithRawResponse(client.request_tracers)
        self.roles = resources.RolesWithRawResponse(client.roles)
        self.rules = resources.RulesWithRawResponse(client.rules)
        self.storage = resources.StorageWithRawResponse(client.storage)
        self.stream = resources.StreamWithRawResponse(client.stream)
        self.gateways = resources.GatewaysWithRawResponse(client.gateways)
        self.alerting = resources.AlertingWithRawResponse(client.alerting)
        self.devices = resources.DevicesWithRawResponse(client.devices)
        self.d1 = resources.D1WithRawResponse(client.d1)
        self.dex = resources.DEXWithRawResponse(client.dex)
        self.r2 = resources.R2WithRawResponse(client.r2)
        self.teamnet = resources.TeamnetWithRawResponse(client.teamnet)
        self.warp_connector = resources.WARPConnectorWithRawResponse(client.warp_connector)
        self.dispatchers = resources.DispatchersWithRawResponse(client.dispatchers)
        self.workers_for_platforms = resources.WorkersForPlatformsWithRawResponse(client.workers_for_platforms)
        self.zero_trust = resources.ZeroTrustWithRawResponse(client.zero_trust)
        self.challenges = resources.ChallengesWithRawResponse(client.challenges)
        self.hyperdrive = resources.HyperdriveWithRawResponse(client.hyperdrive)
        self.rum = resources.RUMWithRawResponse(client.rum)
        self.vectorize = resources.VectorizeWithRawResponse(client.vectorize)
        self.url_scanner = resources.URLScannerWithRawResponse(client.url_scanner)
        self.radar = resources.RadarWithRawResponse(client.radar)
        self.bot_management = resources.BotManagementWithRawResponse(client.bot_management)
        self.origin_post_quantum_encryption = resources.OriginPostQuantumEncryptionWithRawResponse(
            client.origin_post_quantum_encryption
        )
        self.speed = resources.SpeedWithRawResponse(client.speed)
        self.dcv_delegation = resources.DcvDelegationWithRawResponse(client.dcv_delegation)
        self.hostnames = resources.HostnamesWithRawResponse(client.hostnames)
        self.snippets = resources.SnippetsWithRawResponse(client.snippets)
        self.calls = resources.CallsWithRawResponse(client.calls)
        self.cloudforce_one = resources.CloudforceOneWithRawResponse(client.cloudforce_one)


class AsyncCloudflareWithRawResponse:
    def __init__(self, client: AsyncCloudflare) -> None:
        self.accounts = resources.AsyncAccountsWithRawResponse(client.accounts)
        self.certificates = resources.AsyncCertificatesWithRawResponse(client.certificates)
        self.ips = resources.AsyncIPsWithRawResponse(client.ips)
        self.memberships = resources.AsyncMembershipsWithRawResponse(client.memberships)
        self.user = resources.AsyncUserWithRawResponse(client.user)
        self.zones = resources.AsyncZonesWithRawResponse(client.zones)
        self.load_balancers = resources.AsyncLoadBalancersWithRawResponse(client.load_balancers)
        self.access = resources.AsyncAccessWithRawResponse(client.access)
        self.cache = resources.AsyncCacheWithRawResponse(client.cache)
        self.ssl = resources.AsyncSSLWithRawResponse(client.ssl)
        self.subscriptions = resources.AsyncSubscriptionsWithRawResponse(client.subscriptions)
        self.acm = resources.AsyncACMWithRawResponse(client.acm)
        self.argo = resources.AsyncArgoWithRawResponse(client.argo)
        self.available_plans = resources.AsyncAvailablePlansWithRawResponse(client.available_plans)
        self.available_rate_plans = resources.AsyncAvailableRatePlansWithRawResponse(client.available_rate_plans)
        self.certificate_authorities = resources.AsyncCertificateAuthoritiesWithRawResponse(
            client.certificate_authorities
        )
        self.client_certificates = resources.AsyncClientCertificatesWithRawResponse(client.client_certificates)
        self.custom_certificates = resources.AsyncCustomCertificatesWithRawResponse(client.custom_certificates)
        self.custom_hostnames = resources.AsyncCustomHostnamesWithRawResponse(client.custom_hostnames)
        self.custom_nameservers = resources.AsyncCustomNameserversWithRawResponse(client.custom_nameservers)
        self.dns = resources.AsyncDNSWithRawResponse(client.dns)
        self.dnssec = resources.AsyncDNSSECWithRawResponse(client.dnssec)
        self.emails = resources.AsyncEmailsWithRawResponse(client.emails)
        self.filters = resources.AsyncFiltersWithRawResponse(client.filters)
        self.firewall = resources.AsyncFirewallWithRawResponse(client.firewall)
        self.healthchecks = resources.AsyncHealthchecksWithRawResponse(client.healthchecks)
        self.keyless_certificates = resources.AsyncKeylessCertificatesWithRawResponse(client.keyless_certificates)
        self.logpush = resources.AsyncLogpushWithRawResponse(client.logpush)
        self.logs = resources.AsyncLogsWithRawResponse(client.logs)
        self.origin_tls_client_auth = resources.AsyncOriginTLSClientAuthWithRawResponse(client.origin_tls_client_auth)
        self.pagerules = resources.AsyncPagerulesWithRawResponse(client.pagerules)
        self.rate_limits = resources.AsyncRateLimitsWithRawResponse(client.rate_limits)
        self.secondary_dns = resources.AsyncSecondaryDNSWithRawResponse(client.secondary_dns)
        self.waiting_rooms = resources.AsyncWaitingRoomsWithRawResponse(client.waiting_rooms)
        self.web3 = resources.AsyncWeb3WithRawResponse(client.web3)
        self.workers = resources.AsyncWorkersWithRawResponse(client.workers)
        self.kv = resources.AsyncKVWithRawResponse(client.kv)
        self.managed_headers = resources.AsyncManagedHeadersWithRawResponse(client.managed_headers)
        self.page_shield = resources.AsyncPageShieldWithRawResponse(client.page_shield)
        self.rulesets = resources.AsyncRulesetsWithRawResponse(client.rulesets)
        self.url_normalizations = resources.AsyncURLNormalizationsWithRawResponse(client.url_normalizations)
        self.spectrum = resources.AsyncSpectrumWithRawResponse(client.spectrum)
        self.addresses = resources.AsyncAddressesWithRawResponse(client.addresses)
        self.audit_logs = resources.AsyncAuditLogsWithRawResponse(client.audit_logs)
        self.billing = resources.AsyncBillingWithRawResponse(client.billing)
        self.brand_protection = resources.AsyncBrandProtectionWithRawResponse(client.brand_protection)
        self.tunnels = resources.AsyncTunnelsWithRawResponse(client.tunnels)
        self.diagnostics = resources.AsyncDiagnosticsWithRawResponse(client.diagnostics)
        self.dlp = resources.AsyncDLPWithRawResponse(client.dlp)
        self.images = resources.AsyncImagesWithRawResponse(client.images)
        self.intel = resources.AsyncIntelWithRawResponse(client.intel)
        self.magic_transit = resources.AsyncMagicTransitWithRawResponse(client.magic_transit)
        self.mnms = resources.AsyncMNMsWithRawResponse(client.mnms)
        self.mtls_certificates = resources.AsyncMTLSCertificatesWithRawResponse(client.mtls_certificates)
        self.pages = resources.AsyncPagesWithRawResponse(client.pages)
        self.pcaps = resources.AsyncPCAPsWithRawResponse(client.pcaps)
        self.registrar = resources.AsyncRegistrarWithRawResponse(client.registrar)
        self.request_tracers = resources.AsyncRequestTracersWithRawResponse(client.request_tracers)
        self.roles = resources.AsyncRolesWithRawResponse(client.roles)
        self.rules = resources.AsyncRulesWithRawResponse(client.rules)
        self.storage = resources.AsyncStorageWithRawResponse(client.storage)
        self.stream = resources.AsyncStreamWithRawResponse(client.stream)
        self.gateways = resources.AsyncGatewaysWithRawResponse(client.gateways)
        self.alerting = resources.AsyncAlertingWithRawResponse(client.alerting)
        self.devices = resources.AsyncDevicesWithRawResponse(client.devices)
        self.d1 = resources.AsyncD1WithRawResponse(client.d1)
        self.dex = resources.AsyncDEXWithRawResponse(client.dex)
        self.r2 = resources.AsyncR2WithRawResponse(client.r2)
        self.teamnet = resources.AsyncTeamnetWithRawResponse(client.teamnet)
        self.warp_connector = resources.AsyncWARPConnectorWithRawResponse(client.warp_connector)
        self.dispatchers = resources.AsyncDispatchersWithRawResponse(client.dispatchers)
        self.workers_for_platforms = resources.AsyncWorkersForPlatformsWithRawResponse(client.workers_for_platforms)
        self.zero_trust = resources.AsyncZeroTrustWithRawResponse(client.zero_trust)
        self.challenges = resources.AsyncChallengesWithRawResponse(client.challenges)
        self.hyperdrive = resources.AsyncHyperdriveWithRawResponse(client.hyperdrive)
        self.rum = resources.AsyncRUMWithRawResponse(client.rum)
        self.vectorize = resources.AsyncVectorizeWithRawResponse(client.vectorize)
        self.url_scanner = resources.AsyncURLScannerWithRawResponse(client.url_scanner)
        self.radar = resources.AsyncRadarWithRawResponse(client.radar)
        self.bot_management = resources.AsyncBotManagementWithRawResponse(client.bot_management)
        self.origin_post_quantum_encryption = resources.AsyncOriginPostQuantumEncryptionWithRawResponse(
            client.origin_post_quantum_encryption
        )
        self.speed = resources.AsyncSpeedWithRawResponse(client.speed)
        self.dcv_delegation = resources.AsyncDcvDelegationWithRawResponse(client.dcv_delegation)
        self.hostnames = resources.AsyncHostnamesWithRawResponse(client.hostnames)
        self.snippets = resources.AsyncSnippetsWithRawResponse(client.snippets)
        self.calls = resources.AsyncCallsWithRawResponse(client.calls)
        self.cloudforce_one = resources.AsyncCloudforceOneWithRawResponse(client.cloudforce_one)


class CloudflareWithStreamedResponse:
    def __init__(self, client: Cloudflare) -> None:
        self.accounts = resources.AccountsWithStreamingResponse(client.accounts)
        self.certificates = resources.CertificatesWithStreamingResponse(client.certificates)
        self.ips = resources.IPsWithStreamingResponse(client.ips)
        self.memberships = resources.MembershipsWithStreamingResponse(client.memberships)
        self.user = resources.UserWithStreamingResponse(client.user)
        self.zones = resources.ZonesWithStreamingResponse(client.zones)
        self.load_balancers = resources.LoadBalancersWithStreamingResponse(client.load_balancers)
        self.access = resources.AccessWithStreamingResponse(client.access)
        self.cache = resources.CacheWithStreamingResponse(client.cache)
        self.ssl = resources.SSLWithStreamingResponse(client.ssl)
        self.subscriptions = resources.SubscriptionsWithStreamingResponse(client.subscriptions)
        self.acm = resources.ACMWithStreamingResponse(client.acm)
        self.argo = resources.ArgoWithStreamingResponse(client.argo)
        self.available_plans = resources.AvailablePlansWithStreamingResponse(client.available_plans)
        self.available_rate_plans = resources.AvailableRatePlansWithStreamingResponse(client.available_rate_plans)
        self.certificate_authorities = resources.CertificateAuthoritiesWithStreamingResponse(
            client.certificate_authorities
        )
        self.client_certificates = resources.ClientCertificatesWithStreamingResponse(client.client_certificates)
        self.custom_certificates = resources.CustomCertificatesWithStreamingResponse(client.custom_certificates)
        self.custom_hostnames = resources.CustomHostnamesWithStreamingResponse(client.custom_hostnames)
        self.custom_nameservers = resources.CustomNameserversWithStreamingResponse(client.custom_nameservers)
        self.dns = resources.DNSWithStreamingResponse(client.dns)
        self.dnssec = resources.DNSSECWithStreamingResponse(client.dnssec)
        self.emails = resources.EmailsWithStreamingResponse(client.emails)
        self.filters = resources.FiltersWithStreamingResponse(client.filters)
        self.firewall = resources.FirewallWithStreamingResponse(client.firewall)
        self.healthchecks = resources.HealthchecksWithStreamingResponse(client.healthchecks)
        self.keyless_certificates = resources.KeylessCertificatesWithStreamingResponse(client.keyless_certificates)
        self.logpush = resources.LogpushWithStreamingResponse(client.logpush)
        self.logs = resources.LogsWithStreamingResponse(client.logs)
        self.origin_tls_client_auth = resources.OriginTLSClientAuthWithStreamingResponse(client.origin_tls_client_auth)
        self.pagerules = resources.PagerulesWithStreamingResponse(client.pagerules)
        self.rate_limits = resources.RateLimitsWithStreamingResponse(client.rate_limits)
        self.secondary_dns = resources.SecondaryDNSWithStreamingResponse(client.secondary_dns)
        self.waiting_rooms = resources.WaitingRoomsWithStreamingResponse(client.waiting_rooms)
        self.web3 = resources.Web3WithStreamingResponse(client.web3)
        self.workers = resources.WorkersWithStreamingResponse(client.workers)
        self.kv = resources.KVWithStreamingResponse(client.kv)
        self.managed_headers = resources.ManagedHeadersWithStreamingResponse(client.managed_headers)
        self.page_shield = resources.PageShieldWithStreamingResponse(client.page_shield)
        self.rulesets = resources.RulesetsWithStreamingResponse(client.rulesets)
        self.url_normalizations = resources.URLNormalizationsWithStreamingResponse(client.url_normalizations)
        self.spectrum = resources.SpectrumWithStreamingResponse(client.spectrum)
        self.addresses = resources.AddressesWithStreamingResponse(client.addresses)
        self.audit_logs = resources.AuditLogsWithStreamingResponse(client.audit_logs)
        self.billing = resources.BillingWithStreamingResponse(client.billing)
        self.brand_protection = resources.BrandProtectionWithStreamingResponse(client.brand_protection)
        self.tunnels = resources.TunnelsWithStreamingResponse(client.tunnels)
        self.diagnostics = resources.DiagnosticsWithStreamingResponse(client.diagnostics)
        self.dlp = resources.DLPWithStreamingResponse(client.dlp)
        self.images = resources.ImagesWithStreamingResponse(client.images)
        self.intel = resources.IntelWithStreamingResponse(client.intel)
        self.magic_transit = resources.MagicTransitWithStreamingResponse(client.magic_transit)
        self.mnms = resources.MNMsWithStreamingResponse(client.mnms)
        self.mtls_certificates = resources.MTLSCertificatesWithStreamingResponse(client.mtls_certificates)
        self.pages = resources.PagesWithStreamingResponse(client.pages)
        self.pcaps = resources.PCAPsWithStreamingResponse(client.pcaps)
        self.registrar = resources.RegistrarWithStreamingResponse(client.registrar)
        self.request_tracers = resources.RequestTracersWithStreamingResponse(client.request_tracers)
        self.roles = resources.RolesWithStreamingResponse(client.roles)
        self.rules = resources.RulesWithStreamingResponse(client.rules)
        self.storage = resources.StorageWithStreamingResponse(client.storage)
        self.stream = resources.StreamWithStreamingResponse(client.stream)
        self.gateways = resources.GatewaysWithStreamingResponse(client.gateways)
        self.alerting = resources.AlertingWithStreamingResponse(client.alerting)
        self.devices = resources.DevicesWithStreamingResponse(client.devices)
        self.d1 = resources.D1WithStreamingResponse(client.d1)
        self.dex = resources.DEXWithStreamingResponse(client.dex)
        self.r2 = resources.R2WithStreamingResponse(client.r2)
        self.teamnet = resources.TeamnetWithStreamingResponse(client.teamnet)
        self.warp_connector = resources.WARPConnectorWithStreamingResponse(client.warp_connector)
        self.dispatchers = resources.DispatchersWithStreamingResponse(client.dispatchers)
        self.workers_for_platforms = resources.WorkersForPlatformsWithStreamingResponse(client.workers_for_platforms)
        self.zero_trust = resources.ZeroTrustWithStreamingResponse(client.zero_trust)
        self.challenges = resources.ChallengesWithStreamingResponse(client.challenges)
        self.hyperdrive = resources.HyperdriveWithStreamingResponse(client.hyperdrive)
        self.rum = resources.RUMWithStreamingResponse(client.rum)
        self.vectorize = resources.VectorizeWithStreamingResponse(client.vectorize)
        self.url_scanner = resources.URLScannerWithStreamingResponse(client.url_scanner)
        self.radar = resources.RadarWithStreamingResponse(client.radar)
        self.bot_management = resources.BotManagementWithStreamingResponse(client.bot_management)
        self.origin_post_quantum_encryption = resources.OriginPostQuantumEncryptionWithStreamingResponse(
            client.origin_post_quantum_encryption
        )
        self.speed = resources.SpeedWithStreamingResponse(client.speed)
        self.dcv_delegation = resources.DcvDelegationWithStreamingResponse(client.dcv_delegation)
        self.hostnames = resources.HostnamesWithStreamingResponse(client.hostnames)
        self.snippets = resources.SnippetsWithStreamingResponse(client.snippets)
        self.calls = resources.CallsWithStreamingResponse(client.calls)
        self.cloudforce_one = resources.CloudforceOneWithStreamingResponse(client.cloudforce_one)


class AsyncCloudflareWithStreamedResponse:
    def __init__(self, client: AsyncCloudflare) -> None:
        self.accounts = resources.AsyncAccountsWithStreamingResponse(client.accounts)
        self.certificates = resources.AsyncCertificatesWithStreamingResponse(client.certificates)
        self.ips = resources.AsyncIPsWithStreamingResponse(client.ips)
        self.memberships = resources.AsyncMembershipsWithStreamingResponse(client.memberships)
        self.user = resources.AsyncUserWithStreamingResponse(client.user)
        self.zones = resources.AsyncZonesWithStreamingResponse(client.zones)
        self.load_balancers = resources.AsyncLoadBalancersWithStreamingResponse(client.load_balancers)
        self.access = resources.AsyncAccessWithStreamingResponse(client.access)
        self.cache = resources.AsyncCacheWithStreamingResponse(client.cache)
        self.ssl = resources.AsyncSSLWithStreamingResponse(client.ssl)
        self.subscriptions = resources.AsyncSubscriptionsWithStreamingResponse(client.subscriptions)
        self.acm = resources.AsyncACMWithStreamingResponse(client.acm)
        self.argo = resources.AsyncArgoWithStreamingResponse(client.argo)
        self.available_plans = resources.AsyncAvailablePlansWithStreamingResponse(client.available_plans)
        self.available_rate_plans = resources.AsyncAvailableRatePlansWithStreamingResponse(client.available_rate_plans)
        self.certificate_authorities = resources.AsyncCertificateAuthoritiesWithStreamingResponse(
            client.certificate_authorities
        )
        self.client_certificates = resources.AsyncClientCertificatesWithStreamingResponse(client.client_certificates)
        self.custom_certificates = resources.AsyncCustomCertificatesWithStreamingResponse(client.custom_certificates)
        self.custom_hostnames = resources.AsyncCustomHostnamesWithStreamingResponse(client.custom_hostnames)
        self.custom_nameservers = resources.AsyncCustomNameserversWithStreamingResponse(client.custom_nameservers)
        self.dns = resources.AsyncDNSWithStreamingResponse(client.dns)
        self.dnssec = resources.AsyncDNSSECWithStreamingResponse(client.dnssec)
        self.emails = resources.AsyncEmailsWithStreamingResponse(client.emails)
        self.filters = resources.AsyncFiltersWithStreamingResponse(client.filters)
        self.firewall = resources.AsyncFirewallWithStreamingResponse(client.firewall)
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
        self.waiting_rooms = resources.AsyncWaitingRoomsWithStreamingResponse(client.waiting_rooms)
        self.web3 = resources.AsyncWeb3WithStreamingResponse(client.web3)
        self.workers = resources.AsyncWorkersWithStreamingResponse(client.workers)
        self.kv = resources.AsyncKVWithStreamingResponse(client.kv)
        self.managed_headers = resources.AsyncManagedHeadersWithStreamingResponse(client.managed_headers)
        self.page_shield = resources.AsyncPageShieldWithStreamingResponse(client.page_shield)
        self.rulesets = resources.AsyncRulesetsWithStreamingResponse(client.rulesets)
        self.url_normalizations = resources.AsyncURLNormalizationsWithStreamingResponse(client.url_normalizations)
        self.spectrum = resources.AsyncSpectrumWithStreamingResponse(client.spectrum)
        self.addresses = resources.AsyncAddressesWithStreamingResponse(client.addresses)
        self.audit_logs = resources.AsyncAuditLogsWithStreamingResponse(client.audit_logs)
        self.billing = resources.AsyncBillingWithStreamingResponse(client.billing)
        self.brand_protection = resources.AsyncBrandProtectionWithStreamingResponse(client.brand_protection)
        self.tunnels = resources.AsyncTunnelsWithStreamingResponse(client.tunnels)
        self.diagnostics = resources.AsyncDiagnosticsWithStreamingResponse(client.diagnostics)
        self.dlp = resources.AsyncDLPWithStreamingResponse(client.dlp)
        self.images = resources.AsyncImagesWithStreamingResponse(client.images)
        self.intel = resources.AsyncIntelWithStreamingResponse(client.intel)
        self.magic_transit = resources.AsyncMagicTransitWithStreamingResponse(client.magic_transit)
        self.mnms = resources.AsyncMNMsWithStreamingResponse(client.mnms)
        self.mtls_certificates = resources.AsyncMTLSCertificatesWithStreamingResponse(client.mtls_certificates)
        self.pages = resources.AsyncPagesWithStreamingResponse(client.pages)
        self.pcaps = resources.AsyncPCAPsWithStreamingResponse(client.pcaps)
        self.registrar = resources.AsyncRegistrarWithStreamingResponse(client.registrar)
        self.request_tracers = resources.AsyncRequestTracersWithStreamingResponse(client.request_tracers)
        self.roles = resources.AsyncRolesWithStreamingResponse(client.roles)
        self.rules = resources.AsyncRulesWithStreamingResponse(client.rules)
        self.storage = resources.AsyncStorageWithStreamingResponse(client.storage)
        self.stream = resources.AsyncStreamWithStreamingResponse(client.stream)
        self.gateways = resources.AsyncGatewaysWithStreamingResponse(client.gateways)
        self.alerting = resources.AsyncAlertingWithStreamingResponse(client.alerting)
        self.devices = resources.AsyncDevicesWithStreamingResponse(client.devices)
        self.d1 = resources.AsyncD1WithStreamingResponse(client.d1)
        self.dex = resources.AsyncDEXWithStreamingResponse(client.dex)
        self.r2 = resources.AsyncR2WithStreamingResponse(client.r2)
        self.teamnet = resources.AsyncTeamnetWithStreamingResponse(client.teamnet)
        self.warp_connector = resources.AsyncWARPConnectorWithStreamingResponse(client.warp_connector)
        self.dispatchers = resources.AsyncDispatchersWithStreamingResponse(client.dispatchers)
        self.workers_for_platforms = resources.AsyncWorkersForPlatformsWithStreamingResponse(
            client.workers_for_platforms
        )
        self.zero_trust = resources.AsyncZeroTrustWithStreamingResponse(client.zero_trust)
        self.challenges = resources.AsyncChallengesWithStreamingResponse(client.challenges)
        self.hyperdrive = resources.AsyncHyperdriveWithStreamingResponse(client.hyperdrive)
        self.rum = resources.AsyncRUMWithStreamingResponse(client.rum)
        self.vectorize = resources.AsyncVectorizeWithStreamingResponse(client.vectorize)
        self.url_scanner = resources.AsyncURLScannerWithStreamingResponse(client.url_scanner)
        self.radar = resources.AsyncRadarWithStreamingResponse(client.radar)
        self.bot_management = resources.AsyncBotManagementWithStreamingResponse(client.bot_management)
        self.origin_post_quantum_encryption = resources.AsyncOriginPostQuantumEncryptionWithStreamingResponse(
            client.origin_post_quantum_encryption
        )
        self.speed = resources.AsyncSpeedWithStreamingResponse(client.speed)
        self.dcv_delegation = resources.AsyncDcvDelegationWithStreamingResponse(client.dcv_delegation)
        self.hostnames = resources.AsyncHostnamesWithStreamingResponse(client.hostnames)
        self.snippets = resources.AsyncSnippetsWithStreamingResponse(client.snippets)
        self.calls = resources.AsyncCallsWithStreamingResponse(client.calls)
        self.cloudforce_one = resources.AsyncCloudforceOneWithStreamingResponse(client.cloudforce_one)


Client = Cloudflare

AsyncClient = AsyncCloudflare
