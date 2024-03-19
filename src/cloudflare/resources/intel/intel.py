# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .asn import (
    ASN,
    AsyncASN,
    ASNWithRawResponse,
    AsyncASNWithRawResponse,
    ASNWithStreamingResponse,
    AsyncASNWithStreamingResponse,
)
from .dns import (
    DNS,
    AsyncDNS,
    DNSWithRawResponse,
    AsyncDNSWithRawResponse,
    DNSWithStreamingResponse,
    AsyncDNSWithStreamingResponse,
)
from .ips import (
    IPs,
    AsyncIPs,
    IPsWithRawResponse,
    AsyncIPsWithRawResponse,
    IPsWithStreamingResponse,
    AsyncIPsWithStreamingResponse,
)
from .whois import (
    Whois,
    AsyncWhois,
    WhoisWithRawResponse,
    AsyncWhoisWithRawResponse,
    WhoisWithStreamingResponse,
    AsyncWhoisWithStreamingResponse,
)
from .asn.asn import ASN, AsyncASN
from .domains import (
    Domains,
    AsyncDomains,
    DomainsWithRawResponse,
    AsyncDomainsWithRawResponse,
    DomainsWithStreamingResponse,
    AsyncDomainsWithStreamingResponse,
)
from .ip_lists import (
    IPLists,
    AsyncIPLists,
    IPListsWithRawResponse,
    AsyncIPListsWithRawResponse,
    IPListsWithStreamingResponse,
    AsyncIPListsWithStreamingResponse,
)
from ..._compat import cached_property
from .sinkholes import (
    Sinkholes,
    AsyncSinkholes,
    SinkholesWithRawResponse,
    AsyncSinkholesWithRawResponse,
    SinkholesWithStreamingResponse,
    AsyncSinkholesWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .domain_history import (
    DomainHistory,
    AsyncDomainHistory,
    DomainHistoryWithRawResponse,
    AsyncDomainHistoryWithRawResponse,
    DomainHistoryWithStreamingResponse,
    AsyncDomainHistoryWithStreamingResponse,
)
from .domains.domains import Domains, AsyncDomains
from .indicator_feeds import (
    IndicatorFeeds,
    AsyncIndicatorFeeds,
    IndicatorFeedsWithRawResponse,
    AsyncIndicatorFeedsWithRawResponse,
    IndicatorFeedsWithStreamingResponse,
    AsyncIndicatorFeedsWithStreamingResponse,
)
from .miscategorizations import (
    Miscategorizations,
    AsyncMiscategorizations,
    MiscategorizationsWithRawResponse,
    AsyncMiscategorizationsWithRawResponse,
    MiscategorizationsWithStreamingResponse,
    AsyncMiscategorizationsWithStreamingResponse,
)
from .attack_surface_report import (
    AttackSurfaceReport,
    AsyncAttackSurfaceReport,
    AttackSurfaceReportWithRawResponse,
    AsyncAttackSurfaceReportWithRawResponse,
    AttackSurfaceReportWithStreamingResponse,
    AsyncAttackSurfaceReportWithStreamingResponse,
)
from .indicator_feeds.indicator_feeds import IndicatorFeeds, AsyncIndicatorFeeds
from .attack_surface_report.attack_surface_report import AttackSurfaceReport, AsyncAttackSurfaceReport

__all__ = ["Intel", "AsyncIntel"]


class Intel(SyncAPIResource):
    @cached_property
    def asn(self) -> ASN:
        return ASN(self._client)

    @cached_property
    def dns(self) -> DNS:
        return DNS(self._client)

    @cached_property
    def domains(self) -> Domains:
        return Domains(self._client)

    @cached_property
    def domain_history(self) -> DomainHistory:
        return DomainHistory(self._client)

    @cached_property
    def ips(self) -> IPs:
        return IPs(self._client)

    @cached_property
    def ip_lists(self) -> IPLists:
        return IPLists(self._client)

    @cached_property
    def miscategorizations(self) -> Miscategorizations:
        return Miscategorizations(self._client)

    @cached_property
    def whois(self) -> Whois:
        return Whois(self._client)

    @cached_property
    def indicator_feeds(self) -> IndicatorFeeds:
        return IndicatorFeeds(self._client)

    @cached_property
    def sinkholes(self) -> Sinkholes:
        return Sinkholes(self._client)

    @cached_property
    def attack_surface_report(self) -> AttackSurfaceReport:
        return AttackSurfaceReport(self._client)

    @cached_property
    def with_raw_response(self) -> IntelWithRawResponse:
        return IntelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntelWithStreamingResponse:
        return IntelWithStreamingResponse(self)


class AsyncIntel(AsyncAPIResource):
    @cached_property
    def asn(self) -> AsyncASN:
        return AsyncASN(self._client)

    @cached_property
    def dns(self) -> AsyncDNS:
        return AsyncDNS(self._client)

    @cached_property
    def domains(self) -> AsyncDomains:
        return AsyncDomains(self._client)

    @cached_property
    def domain_history(self) -> AsyncDomainHistory:
        return AsyncDomainHistory(self._client)

    @cached_property
    def ips(self) -> AsyncIPs:
        return AsyncIPs(self._client)

    @cached_property
    def ip_lists(self) -> AsyncIPLists:
        return AsyncIPLists(self._client)

    @cached_property
    def miscategorizations(self) -> AsyncMiscategorizations:
        return AsyncMiscategorizations(self._client)

    @cached_property
    def whois(self) -> AsyncWhois:
        return AsyncWhois(self._client)

    @cached_property
    def indicator_feeds(self) -> AsyncIndicatorFeeds:
        return AsyncIndicatorFeeds(self._client)

    @cached_property
    def sinkholes(self) -> AsyncSinkholes:
        return AsyncSinkholes(self._client)

    @cached_property
    def attack_surface_report(self) -> AsyncAttackSurfaceReport:
        return AsyncAttackSurfaceReport(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntelWithRawResponse:
        return AsyncIntelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntelWithStreamingResponse:
        return AsyncIntelWithStreamingResponse(self)


class IntelWithRawResponse:
    def __init__(self, intel: Intel) -> None:
        self._intel = intel

    @cached_property
    def asn(self) -> ASNWithRawResponse:
        return ASNWithRawResponse(self._intel.asn)

    @cached_property
    def dns(self) -> DNSWithRawResponse:
        return DNSWithRawResponse(self._intel.dns)

    @cached_property
    def domains(self) -> DomainsWithRawResponse:
        return DomainsWithRawResponse(self._intel.domains)

    @cached_property
    def domain_history(self) -> DomainHistoryWithRawResponse:
        return DomainHistoryWithRawResponse(self._intel.domain_history)

    @cached_property
    def ips(self) -> IPsWithRawResponse:
        return IPsWithRawResponse(self._intel.ips)

    @cached_property
    def ip_lists(self) -> IPListsWithRawResponse:
        return IPListsWithRawResponse(self._intel.ip_lists)

    @cached_property
    def miscategorizations(self) -> MiscategorizationsWithRawResponse:
        return MiscategorizationsWithRawResponse(self._intel.miscategorizations)

    @cached_property
    def whois(self) -> WhoisWithRawResponse:
        return WhoisWithRawResponse(self._intel.whois)

    @cached_property
    def indicator_feeds(self) -> IndicatorFeedsWithRawResponse:
        return IndicatorFeedsWithRawResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> SinkholesWithRawResponse:
        return SinkholesWithRawResponse(self._intel.sinkholes)

    @cached_property
    def attack_surface_report(self) -> AttackSurfaceReportWithRawResponse:
        return AttackSurfaceReportWithRawResponse(self._intel.attack_surface_report)


class AsyncIntelWithRawResponse:
    def __init__(self, intel: AsyncIntel) -> None:
        self._intel = intel

    @cached_property
    def asn(self) -> AsyncASNWithRawResponse:
        return AsyncASNWithRawResponse(self._intel.asn)

    @cached_property
    def dns(self) -> AsyncDNSWithRawResponse:
        return AsyncDNSWithRawResponse(self._intel.dns)

    @cached_property
    def domains(self) -> AsyncDomainsWithRawResponse:
        return AsyncDomainsWithRawResponse(self._intel.domains)

    @cached_property
    def domain_history(self) -> AsyncDomainHistoryWithRawResponse:
        return AsyncDomainHistoryWithRawResponse(self._intel.domain_history)

    @cached_property
    def ips(self) -> AsyncIPsWithRawResponse:
        return AsyncIPsWithRawResponse(self._intel.ips)

    @cached_property
    def ip_lists(self) -> AsyncIPListsWithRawResponse:
        return AsyncIPListsWithRawResponse(self._intel.ip_lists)

    @cached_property
    def miscategorizations(self) -> AsyncMiscategorizationsWithRawResponse:
        return AsyncMiscategorizationsWithRawResponse(self._intel.miscategorizations)

    @cached_property
    def whois(self) -> AsyncWhoisWithRawResponse:
        return AsyncWhoisWithRawResponse(self._intel.whois)

    @cached_property
    def indicator_feeds(self) -> AsyncIndicatorFeedsWithRawResponse:
        return AsyncIndicatorFeedsWithRawResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> AsyncSinkholesWithRawResponse:
        return AsyncSinkholesWithRawResponse(self._intel.sinkholes)

    @cached_property
    def attack_surface_report(self) -> AsyncAttackSurfaceReportWithRawResponse:
        return AsyncAttackSurfaceReportWithRawResponse(self._intel.attack_surface_report)


class IntelWithStreamingResponse:
    def __init__(self, intel: Intel) -> None:
        self._intel = intel

    @cached_property
    def asn(self) -> ASNWithStreamingResponse:
        return ASNWithStreamingResponse(self._intel.asn)

    @cached_property
    def dns(self) -> DNSWithStreamingResponse:
        return DNSWithStreamingResponse(self._intel.dns)

    @cached_property
    def domains(self) -> DomainsWithStreamingResponse:
        return DomainsWithStreamingResponse(self._intel.domains)

    @cached_property
    def domain_history(self) -> DomainHistoryWithStreamingResponse:
        return DomainHistoryWithStreamingResponse(self._intel.domain_history)

    @cached_property
    def ips(self) -> IPsWithStreamingResponse:
        return IPsWithStreamingResponse(self._intel.ips)

    @cached_property
    def ip_lists(self) -> IPListsWithStreamingResponse:
        return IPListsWithStreamingResponse(self._intel.ip_lists)

    @cached_property
    def miscategorizations(self) -> MiscategorizationsWithStreamingResponse:
        return MiscategorizationsWithStreamingResponse(self._intel.miscategorizations)

    @cached_property
    def whois(self) -> WhoisWithStreamingResponse:
        return WhoisWithStreamingResponse(self._intel.whois)

    @cached_property
    def indicator_feeds(self) -> IndicatorFeedsWithStreamingResponse:
        return IndicatorFeedsWithStreamingResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> SinkholesWithStreamingResponse:
        return SinkholesWithStreamingResponse(self._intel.sinkholes)

    @cached_property
    def attack_surface_report(self) -> AttackSurfaceReportWithStreamingResponse:
        return AttackSurfaceReportWithStreamingResponse(self._intel.attack_surface_report)


class AsyncIntelWithStreamingResponse:
    def __init__(self, intel: AsyncIntel) -> None:
        self._intel = intel

    @cached_property
    def asn(self) -> AsyncASNWithStreamingResponse:
        return AsyncASNWithStreamingResponse(self._intel.asn)

    @cached_property
    def dns(self) -> AsyncDNSWithStreamingResponse:
        return AsyncDNSWithStreamingResponse(self._intel.dns)

    @cached_property
    def domains(self) -> AsyncDomainsWithStreamingResponse:
        return AsyncDomainsWithStreamingResponse(self._intel.domains)

    @cached_property
    def domain_history(self) -> AsyncDomainHistoryWithStreamingResponse:
        return AsyncDomainHistoryWithStreamingResponse(self._intel.domain_history)

    @cached_property
    def ips(self) -> AsyncIPsWithStreamingResponse:
        return AsyncIPsWithStreamingResponse(self._intel.ips)

    @cached_property
    def ip_lists(self) -> AsyncIPListsWithStreamingResponse:
        return AsyncIPListsWithStreamingResponse(self._intel.ip_lists)

    @cached_property
    def miscategorizations(self) -> AsyncMiscategorizationsWithStreamingResponse:
        return AsyncMiscategorizationsWithStreamingResponse(self._intel.miscategorizations)

    @cached_property
    def whois(self) -> AsyncWhoisWithStreamingResponse:
        return AsyncWhoisWithStreamingResponse(self._intel.whois)

    @cached_property
    def indicator_feeds(self) -> AsyncIndicatorFeedsWithStreamingResponse:
        return AsyncIndicatorFeedsWithStreamingResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> AsyncSinkholesWithStreamingResponse:
        return AsyncSinkholesWithStreamingResponse(self._intel.sinkholes)

    @cached_property
    def attack_surface_report(self) -> AsyncAttackSurfaceReportWithStreamingResponse:
        return AsyncAttackSurfaceReportWithStreamingResponse(self._intel.attack_surface_report)
