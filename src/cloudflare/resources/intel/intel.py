# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .dns import (
    DNSResource,
    AsyncDNSResource,
    DNSResourceWithRawResponse,
    AsyncDNSResourceWithRawResponse,
    DNSResourceWithStreamingResponse,
    AsyncDNSResourceWithStreamingResponse,
)
from .ips import (
    IPsResource,
    AsyncIPsResource,
    IPsResourceWithRawResponse,
    AsyncIPsResourceWithRawResponse,
    IPsResourceWithStreamingResponse,
    AsyncIPsResourceWithStreamingResponse,
)
from .whois import (
    WhoisResource,
    AsyncWhoisResource,
    WhoisResourceWithRawResponse,
    AsyncWhoisResourceWithRawResponse,
    WhoisResourceWithStreamingResponse,
    AsyncWhoisResourceWithStreamingResponse,
)
from .asn.asn import (
    ASNResource,
    AsyncASNResource,
    ASNResourceWithRawResponse,
    AsyncASNResourceWithRawResponse,
    ASNResourceWithStreamingResponse,
    AsyncASNResourceWithStreamingResponse,
)
from .ip_lists import (
    IPListsResource,
    AsyncIPListsResource,
    IPListsResourceWithRawResponse,
    AsyncIPListsResourceWithRawResponse,
    IPListsResourceWithStreamingResponse,
    AsyncIPListsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .sinkholes import (
    SinkholesResource,
    AsyncSinkholesResource,
    SinkholesResourceWithRawResponse,
    AsyncSinkholesResourceWithRawResponse,
    SinkholesResourceWithStreamingResponse,
    AsyncSinkholesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .domain_history import (
    DomainHistoryResource,
    AsyncDomainHistoryResource,
    DomainHistoryResourceWithRawResponse,
    AsyncDomainHistoryResourceWithRawResponse,
    DomainHistoryResourceWithStreamingResponse,
    AsyncDomainHistoryResourceWithStreamingResponse,
)
from .domains.domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from .miscategorizations import (
    MiscategorizationsResource,
    AsyncMiscategorizationsResource,
    MiscategorizationsResourceWithRawResponse,
    AsyncMiscategorizationsResourceWithRawResponse,
    MiscategorizationsResourceWithStreamingResponse,
    AsyncMiscategorizationsResourceWithStreamingResponse,
)
from .indicator_feeds.indicator_feeds import (
    IndicatorFeedsResource,
    AsyncIndicatorFeedsResource,
    IndicatorFeedsResourceWithRawResponse,
    AsyncIndicatorFeedsResourceWithRawResponse,
    IndicatorFeedsResourceWithStreamingResponse,
    AsyncIndicatorFeedsResourceWithStreamingResponse,
)
from .attack_surface_report.attack_surface_report import (
    AttackSurfaceReportResource,
    AsyncAttackSurfaceReportResource,
    AttackSurfaceReportResourceWithRawResponse,
    AsyncAttackSurfaceReportResourceWithRawResponse,
    AttackSurfaceReportResourceWithStreamingResponse,
    AsyncAttackSurfaceReportResourceWithStreamingResponse,
)

__all__ = ["IntelResource", "AsyncIntelResource"]


class IntelResource(SyncAPIResource):
    @cached_property
    def asn(self) -> ASNResource:
        return ASNResource(self._client)

    @cached_property
    def dns(self) -> DNSResource:
        return DNSResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def domain_history(self) -> DomainHistoryResource:
        return DomainHistoryResource(self._client)

    @cached_property
    def ips(self) -> IPsResource:
        return IPsResource(self._client)

    @cached_property
    def ip_lists(self) -> IPListsResource:
        return IPListsResource(self._client)

    @cached_property
    def miscategorizations(self) -> MiscategorizationsResource:
        return MiscategorizationsResource(self._client)

    @cached_property
    def whois(self) -> WhoisResource:
        return WhoisResource(self._client)

    @cached_property
    def indicator_feeds(self) -> IndicatorFeedsResource:
        return IndicatorFeedsResource(self._client)

    @cached_property
    def sinkholes(self) -> SinkholesResource:
        return SinkholesResource(self._client)

    @cached_property
    def attack_surface_report(self) -> AttackSurfaceReportResource:
        return AttackSurfaceReportResource(self._client)

    @cached_property
    def with_raw_response(self) -> IntelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IntelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IntelResourceWithStreamingResponse(self)


class AsyncIntelResource(AsyncAPIResource):
    @cached_property
    def asn(self) -> AsyncASNResource:
        return AsyncASNResource(self._client)

    @cached_property
    def dns(self) -> AsyncDNSResource:
        return AsyncDNSResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def domain_history(self) -> AsyncDomainHistoryResource:
        return AsyncDomainHistoryResource(self._client)

    @cached_property
    def ips(self) -> AsyncIPsResource:
        return AsyncIPsResource(self._client)

    @cached_property
    def ip_lists(self) -> AsyncIPListsResource:
        return AsyncIPListsResource(self._client)

    @cached_property
    def miscategorizations(self) -> AsyncMiscategorizationsResource:
        return AsyncMiscategorizationsResource(self._client)

    @cached_property
    def whois(self) -> AsyncWhoisResource:
        return AsyncWhoisResource(self._client)

    @cached_property
    def indicator_feeds(self) -> AsyncIndicatorFeedsResource:
        return AsyncIndicatorFeedsResource(self._client)

    @cached_property
    def sinkholes(self) -> AsyncSinkholesResource:
        return AsyncSinkholesResource(self._client)

    @cached_property
    def attack_surface_report(self) -> AsyncAttackSurfaceReportResource:
        return AsyncAttackSurfaceReportResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIntelResourceWithStreamingResponse(self)


class IntelResourceWithRawResponse:
    def __init__(self, intel: IntelResource) -> None:
        self._intel = intel

    @cached_property
    def asn(self) -> ASNResourceWithRawResponse:
        return ASNResourceWithRawResponse(self._intel.asn)

    @cached_property
    def dns(self) -> DNSResourceWithRawResponse:
        return DNSResourceWithRawResponse(self._intel.dns)

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._intel.domains)

    @cached_property
    def domain_history(self) -> DomainHistoryResourceWithRawResponse:
        return DomainHistoryResourceWithRawResponse(self._intel.domain_history)

    @cached_property
    def ips(self) -> IPsResourceWithRawResponse:
        return IPsResourceWithRawResponse(self._intel.ips)

    @cached_property
    def ip_lists(self) -> IPListsResourceWithRawResponse:
        return IPListsResourceWithRawResponse(self._intel.ip_lists)

    @cached_property
    def miscategorizations(self) -> MiscategorizationsResourceWithRawResponse:
        return MiscategorizationsResourceWithRawResponse(self._intel.miscategorizations)

    @cached_property
    def whois(self) -> WhoisResourceWithRawResponse:
        return WhoisResourceWithRawResponse(self._intel.whois)

    @cached_property
    def indicator_feeds(self) -> IndicatorFeedsResourceWithRawResponse:
        return IndicatorFeedsResourceWithRawResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> SinkholesResourceWithRawResponse:
        return SinkholesResourceWithRawResponse(self._intel.sinkholes)

    @cached_property
    def attack_surface_report(self) -> AttackSurfaceReportResourceWithRawResponse:
        return AttackSurfaceReportResourceWithRawResponse(self._intel.attack_surface_report)


class AsyncIntelResourceWithRawResponse:
    def __init__(self, intel: AsyncIntelResource) -> None:
        self._intel = intel

    @cached_property
    def asn(self) -> AsyncASNResourceWithRawResponse:
        return AsyncASNResourceWithRawResponse(self._intel.asn)

    @cached_property
    def dns(self) -> AsyncDNSResourceWithRawResponse:
        return AsyncDNSResourceWithRawResponse(self._intel.dns)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._intel.domains)

    @cached_property
    def domain_history(self) -> AsyncDomainHistoryResourceWithRawResponse:
        return AsyncDomainHistoryResourceWithRawResponse(self._intel.domain_history)

    @cached_property
    def ips(self) -> AsyncIPsResourceWithRawResponse:
        return AsyncIPsResourceWithRawResponse(self._intel.ips)

    @cached_property
    def ip_lists(self) -> AsyncIPListsResourceWithRawResponse:
        return AsyncIPListsResourceWithRawResponse(self._intel.ip_lists)

    @cached_property
    def miscategorizations(self) -> AsyncMiscategorizationsResourceWithRawResponse:
        return AsyncMiscategorizationsResourceWithRawResponse(self._intel.miscategorizations)

    @cached_property
    def whois(self) -> AsyncWhoisResourceWithRawResponse:
        return AsyncWhoisResourceWithRawResponse(self._intel.whois)

    @cached_property
    def indicator_feeds(self) -> AsyncIndicatorFeedsResourceWithRawResponse:
        return AsyncIndicatorFeedsResourceWithRawResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> AsyncSinkholesResourceWithRawResponse:
        return AsyncSinkholesResourceWithRawResponse(self._intel.sinkholes)

    @cached_property
    def attack_surface_report(self) -> AsyncAttackSurfaceReportResourceWithRawResponse:
        return AsyncAttackSurfaceReportResourceWithRawResponse(self._intel.attack_surface_report)


class IntelResourceWithStreamingResponse:
    def __init__(self, intel: IntelResource) -> None:
        self._intel = intel

    @cached_property
    def asn(self) -> ASNResourceWithStreamingResponse:
        return ASNResourceWithStreamingResponse(self._intel.asn)

    @cached_property
    def dns(self) -> DNSResourceWithStreamingResponse:
        return DNSResourceWithStreamingResponse(self._intel.dns)

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._intel.domains)

    @cached_property
    def domain_history(self) -> DomainHistoryResourceWithStreamingResponse:
        return DomainHistoryResourceWithStreamingResponse(self._intel.domain_history)

    @cached_property
    def ips(self) -> IPsResourceWithStreamingResponse:
        return IPsResourceWithStreamingResponse(self._intel.ips)

    @cached_property
    def ip_lists(self) -> IPListsResourceWithStreamingResponse:
        return IPListsResourceWithStreamingResponse(self._intel.ip_lists)

    @cached_property
    def miscategorizations(self) -> MiscategorizationsResourceWithStreamingResponse:
        return MiscategorizationsResourceWithStreamingResponse(self._intel.miscategorizations)

    @cached_property
    def whois(self) -> WhoisResourceWithStreamingResponse:
        return WhoisResourceWithStreamingResponse(self._intel.whois)

    @cached_property
    def indicator_feeds(self) -> IndicatorFeedsResourceWithStreamingResponse:
        return IndicatorFeedsResourceWithStreamingResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> SinkholesResourceWithStreamingResponse:
        return SinkholesResourceWithStreamingResponse(self._intel.sinkholes)

    @cached_property
    def attack_surface_report(self) -> AttackSurfaceReportResourceWithStreamingResponse:
        return AttackSurfaceReportResourceWithStreamingResponse(self._intel.attack_surface_report)


class AsyncIntelResourceWithStreamingResponse:
    def __init__(self, intel: AsyncIntelResource) -> None:
        self._intel = intel

    @cached_property
    def asn(self) -> AsyncASNResourceWithStreamingResponse:
        return AsyncASNResourceWithStreamingResponse(self._intel.asn)

    @cached_property
    def dns(self) -> AsyncDNSResourceWithStreamingResponse:
        return AsyncDNSResourceWithStreamingResponse(self._intel.dns)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._intel.domains)

    @cached_property
    def domain_history(self) -> AsyncDomainHistoryResourceWithStreamingResponse:
        return AsyncDomainHistoryResourceWithStreamingResponse(self._intel.domain_history)

    @cached_property
    def ips(self) -> AsyncIPsResourceWithStreamingResponse:
        return AsyncIPsResourceWithStreamingResponse(self._intel.ips)

    @cached_property
    def ip_lists(self) -> AsyncIPListsResourceWithStreamingResponse:
        return AsyncIPListsResourceWithStreamingResponse(self._intel.ip_lists)

    @cached_property
    def miscategorizations(self) -> AsyncMiscategorizationsResourceWithStreamingResponse:
        return AsyncMiscategorizationsResourceWithStreamingResponse(self._intel.miscategorizations)

    @cached_property
    def whois(self) -> AsyncWhoisResourceWithStreamingResponse:
        return AsyncWhoisResourceWithStreamingResponse(self._intel.whois)

    @cached_property
    def indicator_feeds(self) -> AsyncIndicatorFeedsResourceWithStreamingResponse:
        return AsyncIndicatorFeedsResourceWithStreamingResponse(self._intel.indicator_feeds)

    @cached_property
    def sinkholes(self) -> AsyncSinkholesResourceWithStreamingResponse:
        return AsyncSinkholesResourceWithStreamingResponse(self._intel.sinkholes)

    @cached_property
    def attack_surface_report(self) -> AsyncAttackSurfaceReportResourceWithStreamingResponse:
        return AsyncAttackSurfaceReportResourceWithStreamingResponse(self._intel.attack_surface_report)
