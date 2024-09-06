# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .records import RecordsResource, AsyncRecordsResource

from ..._compat import cached_property

from .settings import SettingsResource, AsyncSettingsResource

from .analytics.analytics import AnalyticsResource, AsyncAnalyticsResource

from .firewall.firewall import FirewallResource, AsyncFirewallResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .records import (
    RecordsResource,
    AsyncRecordsResource,
    RecordsResourceWithRawResponse,
    AsyncRecordsResourceWithRawResponse,
    RecordsResourceWithStreamingResponse,
    AsyncRecordsResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .analytics import (
    AnalyticsResource,
    AsyncAnalyticsResource,
    AnalyticsResourceWithRawResponse,
    AsyncAnalyticsResourceWithRawResponse,
    AnalyticsResourceWithStreamingResponse,
    AsyncAnalyticsResourceWithStreamingResponse,
)
from .firewall import (
    FirewallResource,
    AsyncFirewallResource,
    FirewallResourceWithRawResponse,
    AsyncFirewallResourceWithRawResponse,
    FirewallResourceWithStreamingResponse,
    AsyncFirewallResourceWithStreamingResponse,
)

__all__ = ["DNSResource", "AsyncDNSResource"]


class DNSResource(SyncAPIResource):
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
    def firewall(self) -> FirewallResource:
        return FirewallResource(self._client)

    @cached_property
    def with_raw_response(self) -> DNSResourceWithRawResponse:
        return DNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSResourceWithStreamingResponse:
        return DNSResourceWithStreamingResponse(self)


class AsyncDNSResource(AsyncAPIResource):
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
    def firewall(self) -> AsyncFirewallResource:
        return AsyncFirewallResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSResourceWithRawResponse:
        return AsyncDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSResourceWithStreamingResponse:
        return AsyncDNSResourceWithStreamingResponse(self)


class DNSResourceWithRawResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

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
    def firewall(self) -> FirewallResourceWithRawResponse:
        return FirewallResourceWithRawResponse(self._dns.firewall)


class AsyncDNSResourceWithRawResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

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
    def firewall(self) -> AsyncFirewallResourceWithRawResponse:
        return AsyncFirewallResourceWithRawResponse(self._dns.firewall)


class DNSResourceWithStreamingResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

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
    def firewall(self) -> FirewallResourceWithStreamingResponse:
        return FirewallResourceWithStreamingResponse(self._dns.firewall)


class AsyncDNSResourceWithStreamingResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

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
    def firewall(self) -> AsyncFirewallResourceWithStreamingResponse:
        return AsyncFirewallResourceWithStreamingResponse(self._dns.firewall)
