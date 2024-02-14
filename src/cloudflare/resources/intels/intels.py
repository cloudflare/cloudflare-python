# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .asn.asn import Asn, AsyncAsn

from ..._compat import cached_property

from .dns import DNS, AsyncDNS

from .domains.domains import Domains, AsyncDomains

from .domain_histories import DomainHistories, AsyncDomainHistories

from .ips import IPs, AsyncIPs

from .ip_lists import IPLists, AsyncIPLists

from .miscategorizations import Miscategorizations, AsyncMiscategorizations

from .whois import Whois, AsyncWhois

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .asn import (
    Asn,
    AsyncAsn,
    AsnWithRawResponse,
    AsyncAsnWithRawResponse,
    AsnWithStreamingResponse,
    AsyncAsnWithStreamingResponse,
)
from .dns import (
    DNS,
    AsyncDNS,
    DNSWithRawResponse,
    AsyncDNSWithRawResponse,
    DNSWithStreamingResponse,
    AsyncDNSWithStreamingResponse,
)
from .domains import (
    Domains,
    AsyncDomains,
    DomainsWithRawResponse,
    AsyncDomainsWithRawResponse,
    DomainsWithStreamingResponse,
    AsyncDomainsWithStreamingResponse,
)
from .domain_histories import (
    DomainHistories,
    AsyncDomainHistories,
    DomainHistoriesWithRawResponse,
    AsyncDomainHistoriesWithRawResponse,
    DomainHistoriesWithStreamingResponse,
    AsyncDomainHistoriesWithStreamingResponse,
)
from .ips import (
    IPs,
    AsyncIPs,
    IPsWithRawResponse,
    AsyncIPsWithRawResponse,
    IPsWithStreamingResponse,
    AsyncIPsWithStreamingResponse,
)
from .ip_lists import (
    IPLists,
    AsyncIPLists,
    IPListsWithRawResponse,
    AsyncIPListsWithRawResponse,
    IPListsWithStreamingResponse,
    AsyncIPListsWithStreamingResponse,
)
from .miscategorizations import (
    Miscategorizations,
    AsyncMiscategorizations,
    MiscategorizationsWithRawResponse,
    AsyncMiscategorizationsWithRawResponse,
    MiscategorizationsWithStreamingResponse,
    AsyncMiscategorizationsWithStreamingResponse,
)
from .whois import (
    Whois,
    AsyncWhois,
    WhoisWithRawResponse,
    AsyncWhoisWithRawResponse,
    WhoisWithStreamingResponse,
    AsyncWhoisWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Intels", "AsyncIntels"]


class Intels(SyncAPIResource):
    @cached_property
    def asn(self) -> Asn:
        return Asn(self._client)

    @cached_property
    def dns(self) -> DNS:
        return DNS(self._client)

    @cached_property
    def domains(self) -> Domains:
        return Domains(self._client)

    @cached_property
    def domain_histories(self) -> DomainHistories:
        return DomainHistories(self._client)

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
    def with_raw_response(self) -> IntelsWithRawResponse:
        return IntelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntelsWithStreamingResponse:
        return IntelsWithStreamingResponse(self)


class AsyncIntels(AsyncAPIResource):
    @cached_property
    def asn(self) -> AsyncAsn:
        return AsyncAsn(self._client)

    @cached_property
    def dns(self) -> AsyncDNS:
        return AsyncDNS(self._client)

    @cached_property
    def domains(self) -> AsyncDomains:
        return AsyncDomains(self._client)

    @cached_property
    def domain_histories(self) -> AsyncDomainHistories:
        return AsyncDomainHistories(self._client)

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
    def with_raw_response(self) -> AsyncIntelsWithRawResponse:
        return AsyncIntelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntelsWithStreamingResponse:
        return AsyncIntelsWithStreamingResponse(self)


class IntelsWithRawResponse:
    def __init__(self, intels: Intels) -> None:
        self._intels = intels

    @cached_property
    def asn(self) -> AsnWithRawResponse:
        return AsnWithRawResponse(self._intels.asn)

    @cached_property
    def dns(self) -> DNSWithRawResponse:
        return DNSWithRawResponse(self._intels.dns)

    @cached_property
    def domains(self) -> DomainsWithRawResponse:
        return DomainsWithRawResponse(self._intels.domains)

    @cached_property
    def domain_histories(self) -> DomainHistoriesWithRawResponse:
        return DomainHistoriesWithRawResponse(self._intels.domain_histories)

    @cached_property
    def ips(self) -> IPsWithRawResponse:
        return IPsWithRawResponse(self._intels.ips)

    @cached_property
    def ip_lists(self) -> IPListsWithRawResponse:
        return IPListsWithRawResponse(self._intels.ip_lists)

    @cached_property
    def miscategorizations(self) -> MiscategorizationsWithRawResponse:
        return MiscategorizationsWithRawResponse(self._intels.miscategorizations)

    @cached_property
    def whois(self) -> WhoisWithRawResponse:
        return WhoisWithRawResponse(self._intels.whois)


class AsyncIntelsWithRawResponse:
    def __init__(self, intels: AsyncIntels) -> None:
        self._intels = intels

    @cached_property
    def asn(self) -> AsyncAsnWithRawResponse:
        return AsyncAsnWithRawResponse(self._intels.asn)

    @cached_property
    def dns(self) -> AsyncDNSWithRawResponse:
        return AsyncDNSWithRawResponse(self._intels.dns)

    @cached_property
    def domains(self) -> AsyncDomainsWithRawResponse:
        return AsyncDomainsWithRawResponse(self._intels.domains)

    @cached_property
    def domain_histories(self) -> AsyncDomainHistoriesWithRawResponse:
        return AsyncDomainHistoriesWithRawResponse(self._intels.domain_histories)

    @cached_property
    def ips(self) -> AsyncIPsWithRawResponse:
        return AsyncIPsWithRawResponse(self._intels.ips)

    @cached_property
    def ip_lists(self) -> AsyncIPListsWithRawResponse:
        return AsyncIPListsWithRawResponse(self._intels.ip_lists)

    @cached_property
    def miscategorizations(self) -> AsyncMiscategorizationsWithRawResponse:
        return AsyncMiscategorizationsWithRawResponse(self._intels.miscategorizations)

    @cached_property
    def whois(self) -> AsyncWhoisWithRawResponse:
        return AsyncWhoisWithRawResponse(self._intels.whois)


class IntelsWithStreamingResponse:
    def __init__(self, intels: Intels) -> None:
        self._intels = intels

    @cached_property
    def asn(self) -> AsnWithStreamingResponse:
        return AsnWithStreamingResponse(self._intels.asn)

    @cached_property
    def dns(self) -> DNSWithStreamingResponse:
        return DNSWithStreamingResponse(self._intels.dns)

    @cached_property
    def domains(self) -> DomainsWithStreamingResponse:
        return DomainsWithStreamingResponse(self._intels.domains)

    @cached_property
    def domain_histories(self) -> DomainHistoriesWithStreamingResponse:
        return DomainHistoriesWithStreamingResponse(self._intels.domain_histories)

    @cached_property
    def ips(self) -> IPsWithStreamingResponse:
        return IPsWithStreamingResponse(self._intels.ips)

    @cached_property
    def ip_lists(self) -> IPListsWithStreamingResponse:
        return IPListsWithStreamingResponse(self._intels.ip_lists)

    @cached_property
    def miscategorizations(self) -> MiscategorizationsWithStreamingResponse:
        return MiscategorizationsWithStreamingResponse(self._intels.miscategorizations)

    @cached_property
    def whois(self) -> WhoisWithStreamingResponse:
        return WhoisWithStreamingResponse(self._intels.whois)


class AsyncIntelsWithStreamingResponse:
    def __init__(self, intels: AsyncIntels) -> None:
        self._intels = intels

    @cached_property
    def asn(self) -> AsyncAsnWithStreamingResponse:
        return AsyncAsnWithStreamingResponse(self._intels.asn)

    @cached_property
    def dns(self) -> AsyncDNSWithStreamingResponse:
        return AsyncDNSWithStreamingResponse(self._intels.dns)

    @cached_property
    def domains(self) -> AsyncDomainsWithStreamingResponse:
        return AsyncDomainsWithStreamingResponse(self._intels.domains)

    @cached_property
    def domain_histories(self) -> AsyncDomainHistoriesWithStreamingResponse:
        return AsyncDomainHistoriesWithStreamingResponse(self._intels.domain_histories)

    @cached_property
    def ips(self) -> AsyncIPsWithStreamingResponse:
        return AsyncIPsWithStreamingResponse(self._intels.ips)

    @cached_property
    def ip_lists(self) -> AsyncIPListsWithStreamingResponse:
        return AsyncIPListsWithStreamingResponse(self._intels.ip_lists)

    @cached_property
    def miscategorizations(self) -> AsyncMiscategorizationsWithStreamingResponse:
        return AsyncMiscategorizationsWithStreamingResponse(self._intels.miscategorizations)

    @cached_property
    def whois(self) -> AsyncWhoisWithStreamingResponse:
        return AsyncWhoisWithStreamingResponse(self._intels.whois)
