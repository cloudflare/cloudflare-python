# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .dnssec import (
    DNSSECResource,
    AsyncDNSSECResource,
    DNSSECResourceWithRawResponse,
    AsyncDNSSECResourceWithRawResponse,
    DNSSECResourceWithStreamingResponse,
    AsyncDNSSECResourceWithStreamingResponse,
)
from .records import (
    RecordsResource,
    AsyncRecordsResource,
    RecordsResourceWithRawResponse,
    AsyncRecordsResourceWithRawResponse,
    RecordsResourceWithStreamingResponse,
    AsyncRecordsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .settings.settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .analytics.analytics import (
    AnalyticsResource,
    AsyncAnalyticsResource,
    AnalyticsResourceWithRawResponse,
    AsyncAnalyticsResourceWithRawResponse,
    AnalyticsResourceWithStreamingResponse,
    AsyncAnalyticsResourceWithStreamingResponse,
)
from .zone_transfers.zone_transfers import (
    ZoneTransfersResource,
    AsyncZoneTransfersResource,
    ZoneTransfersResourceWithRawResponse,
    AsyncZoneTransfersResourceWithRawResponse,
    ZoneTransfersResourceWithStreamingResponse,
    AsyncZoneTransfersResourceWithStreamingResponse,
)

__all__ = ["DNSResource", "AsyncDNSResource"]


class DNSResource(SyncAPIResource):
    @cached_property
    def dnssec(self) -> DNSSECResource:
        return DNSSECResource(self._client)

    @cached_property
    def records(self) -> RecordsResource:
        return RecordsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def analytics(self) -> AnalyticsResource:
        return AnalyticsResource(self._client)

    @cached_property
    def zone_transfers(self) -> ZoneTransfersResource:
        return ZoneTransfersResource(self._client)

    @cached_property
    def with_raw_response(self) -> DNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DNSResourceWithStreamingResponse(self)


class AsyncDNSResource(AsyncAPIResource):
    @cached_property
    def dnssec(self) -> AsyncDNSSECResource:
        return AsyncDNSSECResource(self._client)

    @cached_property
    def records(self) -> AsyncRecordsResource:
        return AsyncRecordsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def zone_transfers(self) -> AsyncZoneTransfersResource:
        return AsyncZoneTransfersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDNSResourceWithStreamingResponse(self)


class DNSResourceWithRawResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

    @cached_property
    def dnssec(self) -> DNSSECResourceWithRawResponse:
        return DNSSECResourceWithRawResponse(self._dns.dnssec)

    @cached_property
    def records(self) -> RecordsResourceWithRawResponse:
        return RecordsResourceWithRawResponse(self._dns.records)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._dns.settings)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self._dns.analytics)

    @cached_property
    def zone_transfers(self) -> ZoneTransfersResourceWithRawResponse:
        return ZoneTransfersResourceWithRawResponse(self._dns.zone_transfers)


class AsyncDNSResourceWithRawResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

    @cached_property
    def dnssec(self) -> AsyncDNSSECResourceWithRawResponse:
        return AsyncDNSSECResourceWithRawResponse(self._dns.dnssec)

    @cached_property
    def records(self) -> AsyncRecordsResourceWithRawResponse:
        return AsyncRecordsResourceWithRawResponse(self._dns.records)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._dns.settings)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self._dns.analytics)

    @cached_property
    def zone_transfers(self) -> AsyncZoneTransfersResourceWithRawResponse:
        return AsyncZoneTransfersResourceWithRawResponse(self._dns.zone_transfers)


class DNSResourceWithStreamingResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

    @cached_property
    def dnssec(self) -> DNSSECResourceWithStreamingResponse:
        return DNSSECResourceWithStreamingResponse(self._dns.dnssec)

    @cached_property
    def records(self) -> RecordsResourceWithStreamingResponse:
        return RecordsResourceWithStreamingResponse(self._dns.records)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._dns.settings)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self._dns.analytics)

    @cached_property
    def zone_transfers(self) -> ZoneTransfersResourceWithStreamingResponse:
        return ZoneTransfersResourceWithStreamingResponse(self._dns.zone_transfers)


class AsyncDNSResourceWithStreamingResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

    @cached_property
    def dnssec(self) -> AsyncDNSSECResourceWithStreamingResponse:
        return AsyncDNSSECResourceWithStreamingResponse(self._dns.dnssec)

    @cached_property
    def records(self) -> AsyncRecordsResourceWithStreamingResponse:
        return AsyncRecordsResourceWithStreamingResponse(self._dns.records)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._dns.settings)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._dns.analytics)

    @cached_property
    def zone_transfers(self) -> AsyncZoneTransfersResourceWithStreamingResponse:
        return AsyncZoneTransfersResourceWithStreamingResponse(self._dns.zone_transfers)
