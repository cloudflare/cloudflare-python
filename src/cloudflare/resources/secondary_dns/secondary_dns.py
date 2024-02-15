# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .force_axfrs import ForceAxfrs, AsyncForceAxfrs

from ..._compat import cached_property

from .incomings import Incomings, AsyncIncomings

from .outgoings.outgoings import Outgoings, AsyncOutgoings

from .acls import ACLs, AsyncACLs

from .peers import Peers, AsyncPeers

from .tsigs import Tsigs, AsyncTsigs

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
from .force_axfrs import (
    ForceAxfrs,
    AsyncForceAxfrs,
    ForceAxfrsWithRawResponse,
    AsyncForceAxfrsWithRawResponse,
    ForceAxfrsWithStreamingResponse,
    AsyncForceAxfrsWithStreamingResponse,
)
from .incomings import (
    Incomings,
    AsyncIncomings,
    IncomingsWithRawResponse,
    AsyncIncomingsWithRawResponse,
    IncomingsWithStreamingResponse,
    AsyncIncomingsWithStreamingResponse,
)
from .outgoings import (
    Outgoings,
    AsyncOutgoings,
    OutgoingsWithRawResponse,
    AsyncOutgoingsWithRawResponse,
    OutgoingsWithStreamingResponse,
    AsyncOutgoingsWithStreamingResponse,
)
from .acls import (
    ACLs,
    AsyncACLs,
    ACLsWithRawResponse,
    AsyncACLsWithRawResponse,
    ACLsWithStreamingResponse,
    AsyncACLsWithStreamingResponse,
)
from .peers import (
    Peers,
    AsyncPeers,
    PeersWithRawResponse,
    AsyncPeersWithRawResponse,
    PeersWithStreamingResponse,
    AsyncPeersWithStreamingResponse,
)
from .tsigs import (
    Tsigs,
    AsyncTsigs,
    TsigsWithRawResponse,
    AsyncTsigsWithRawResponse,
    TsigsWithStreamingResponse,
    AsyncTsigsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["SecondaryDNS", "AsyncSecondaryDNS"]


class SecondaryDNS(SyncAPIResource):
    @cached_property
    def force_axfrs(self) -> ForceAxfrs:
        return ForceAxfrs(self._client)

    @cached_property
    def incomings(self) -> Incomings:
        return Incomings(self._client)

    @cached_property
    def outgoings(self) -> Outgoings:
        return Outgoings(self._client)

    @cached_property
    def acls(self) -> ACLs:
        return ACLs(self._client)

    @cached_property
    def peers(self) -> Peers:
        return Peers(self._client)

    @cached_property
    def tsigs(self) -> Tsigs:
        return Tsigs(self._client)

    @cached_property
    def with_raw_response(self) -> SecondaryDNSWithRawResponse:
        return SecondaryDNSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecondaryDNSWithStreamingResponse:
        return SecondaryDNSWithStreamingResponse(self)


class AsyncSecondaryDNS(AsyncAPIResource):
    @cached_property
    def force_axfrs(self) -> AsyncForceAxfrs:
        return AsyncForceAxfrs(self._client)

    @cached_property
    def incomings(self) -> AsyncIncomings:
        return AsyncIncomings(self._client)

    @cached_property
    def outgoings(self) -> AsyncOutgoings:
        return AsyncOutgoings(self._client)

    @cached_property
    def acls(self) -> AsyncACLs:
        return AsyncACLs(self._client)

    @cached_property
    def peers(self) -> AsyncPeers:
        return AsyncPeers(self._client)

    @cached_property
    def tsigs(self) -> AsyncTsigs:
        return AsyncTsigs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecondaryDNSWithRawResponse:
        return AsyncSecondaryDNSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecondaryDNSWithStreamingResponse:
        return AsyncSecondaryDNSWithStreamingResponse(self)


class SecondaryDNSWithRawResponse:
    def __init__(self, secondary_dns: SecondaryDNS) -> None:
        self._secondary_dns = secondary_dns

    @cached_property
    def force_axfrs(self) -> ForceAxfrsWithRawResponse:
        return ForceAxfrsWithRawResponse(self._secondary_dns.force_axfrs)

    @cached_property
    def incomings(self) -> IncomingsWithRawResponse:
        return IncomingsWithRawResponse(self._secondary_dns.incomings)

    @cached_property
    def outgoings(self) -> OutgoingsWithRawResponse:
        return OutgoingsWithRawResponse(self._secondary_dns.outgoings)

    @cached_property
    def acls(self) -> ACLsWithRawResponse:
        return ACLsWithRawResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> PeersWithRawResponse:
        return PeersWithRawResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> TsigsWithRawResponse:
        return TsigsWithRawResponse(self._secondary_dns.tsigs)


class AsyncSecondaryDNSWithRawResponse:
    def __init__(self, secondary_dns: AsyncSecondaryDNS) -> None:
        self._secondary_dns = secondary_dns

    @cached_property
    def force_axfrs(self) -> AsyncForceAxfrsWithRawResponse:
        return AsyncForceAxfrsWithRawResponse(self._secondary_dns.force_axfrs)

    @cached_property
    def incomings(self) -> AsyncIncomingsWithRawResponse:
        return AsyncIncomingsWithRawResponse(self._secondary_dns.incomings)

    @cached_property
    def outgoings(self) -> AsyncOutgoingsWithRawResponse:
        return AsyncOutgoingsWithRawResponse(self._secondary_dns.outgoings)

    @cached_property
    def acls(self) -> AsyncACLsWithRawResponse:
        return AsyncACLsWithRawResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> AsyncPeersWithRawResponse:
        return AsyncPeersWithRawResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> AsyncTsigsWithRawResponse:
        return AsyncTsigsWithRawResponse(self._secondary_dns.tsigs)


class SecondaryDNSWithStreamingResponse:
    def __init__(self, secondary_dns: SecondaryDNS) -> None:
        self._secondary_dns = secondary_dns

    @cached_property
    def force_axfrs(self) -> ForceAxfrsWithStreamingResponse:
        return ForceAxfrsWithStreamingResponse(self._secondary_dns.force_axfrs)

    @cached_property
    def incomings(self) -> IncomingsWithStreamingResponse:
        return IncomingsWithStreamingResponse(self._secondary_dns.incomings)

    @cached_property
    def outgoings(self) -> OutgoingsWithStreamingResponse:
        return OutgoingsWithStreamingResponse(self._secondary_dns.outgoings)

    @cached_property
    def acls(self) -> ACLsWithStreamingResponse:
        return ACLsWithStreamingResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> PeersWithStreamingResponse:
        return PeersWithStreamingResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> TsigsWithStreamingResponse:
        return TsigsWithStreamingResponse(self._secondary_dns.tsigs)


class AsyncSecondaryDNSWithStreamingResponse:
    def __init__(self, secondary_dns: AsyncSecondaryDNS) -> None:
        self._secondary_dns = secondary_dns

    @cached_property
    def force_axfrs(self) -> AsyncForceAxfrsWithStreamingResponse:
        return AsyncForceAxfrsWithStreamingResponse(self._secondary_dns.force_axfrs)

    @cached_property
    def incomings(self) -> AsyncIncomingsWithStreamingResponse:
        return AsyncIncomingsWithStreamingResponse(self._secondary_dns.incomings)

    @cached_property
    def outgoings(self) -> AsyncOutgoingsWithStreamingResponse:
        return AsyncOutgoingsWithStreamingResponse(self._secondary_dns.outgoings)

    @cached_property
    def acls(self) -> AsyncACLsWithStreamingResponse:
        return AsyncACLsWithStreamingResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> AsyncPeersWithStreamingResponse:
        return AsyncPeersWithStreamingResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> AsyncTsigsWithStreamingResponse:
        return AsyncTsigsWithStreamingResponse(self._secondary_dns.tsigs)
