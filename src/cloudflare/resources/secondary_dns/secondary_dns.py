# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
    TSIGs,
    AsyncTSIGs,
    TSIGsWithRawResponse,
    AsyncTSIGsWithRawResponse,
    TSIGsWithStreamingResponse,
    AsyncTSIGsWithStreamingResponse,
)
from .incoming import (
    Incoming,
    AsyncIncoming,
    IncomingWithRawResponse,
    AsyncIncomingWithRawResponse,
    IncomingWithStreamingResponse,
    AsyncIncomingWithStreamingResponse,
)
from .outgoing import (
    Outgoing,
    AsyncOutgoing,
    OutgoingWithRawResponse,
    AsyncOutgoingWithRawResponse,
    OutgoingWithStreamingResponse,
    AsyncOutgoingWithStreamingResponse,
)
from ..._compat import cached_property
from .force_axfr import (
    ForceAXFR,
    AsyncForceAXFR,
    ForceAXFRWithRawResponse,
    AsyncForceAXFRWithRawResponse,
    ForceAXFRWithStreamingResponse,
    AsyncForceAXFRWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .outgoing.outgoing import Outgoing, AsyncOutgoing

__all__ = ["SecondaryDNS", "AsyncSecondaryDNS"]


class SecondaryDNS(SyncAPIResource):
    @cached_property
    def force_axfr(self) -> ForceAXFR:
        return ForceAXFR(self._client)

    @cached_property
    def incoming(self) -> Incoming:
        return Incoming(self._client)

    @cached_property
    def outgoing(self) -> Outgoing:
        return Outgoing(self._client)

    @cached_property
    def acls(self) -> ACLs:
        return ACLs(self._client)

    @cached_property
    def peers(self) -> Peers:
        return Peers(self._client)

    @cached_property
    def tsigs(self) -> TSIGs:
        return TSIGs(self._client)

    @cached_property
    def with_raw_response(self) -> SecondaryDNSWithRawResponse:
        return SecondaryDNSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecondaryDNSWithStreamingResponse:
        return SecondaryDNSWithStreamingResponse(self)


class AsyncSecondaryDNS(AsyncAPIResource):
    @cached_property
    def force_axfr(self) -> AsyncForceAXFR:
        return AsyncForceAXFR(self._client)

    @cached_property
    def incoming(self) -> AsyncIncoming:
        return AsyncIncoming(self._client)

    @cached_property
    def outgoing(self) -> AsyncOutgoing:
        return AsyncOutgoing(self._client)

    @cached_property
    def acls(self) -> AsyncACLs:
        return AsyncACLs(self._client)

    @cached_property
    def peers(self) -> AsyncPeers:
        return AsyncPeers(self._client)

    @cached_property
    def tsigs(self) -> AsyncTSIGs:
        return AsyncTSIGs(self._client)

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
    def force_axfr(self) -> ForceAXFRWithRawResponse:
        return ForceAXFRWithRawResponse(self._secondary_dns.force_axfr)

    @cached_property
    def incoming(self) -> IncomingWithRawResponse:
        return IncomingWithRawResponse(self._secondary_dns.incoming)

    @cached_property
    def outgoing(self) -> OutgoingWithRawResponse:
        return OutgoingWithRawResponse(self._secondary_dns.outgoing)

    @cached_property
    def acls(self) -> ACLsWithRawResponse:
        return ACLsWithRawResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> PeersWithRawResponse:
        return PeersWithRawResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> TSIGsWithRawResponse:
        return TSIGsWithRawResponse(self._secondary_dns.tsigs)


class AsyncSecondaryDNSWithRawResponse:
    def __init__(self, secondary_dns: AsyncSecondaryDNS) -> None:
        self._secondary_dns = secondary_dns

    @cached_property
    def force_axfr(self) -> AsyncForceAXFRWithRawResponse:
        return AsyncForceAXFRWithRawResponse(self._secondary_dns.force_axfr)

    @cached_property
    def incoming(self) -> AsyncIncomingWithRawResponse:
        return AsyncIncomingWithRawResponse(self._secondary_dns.incoming)

    @cached_property
    def outgoing(self) -> AsyncOutgoingWithRawResponse:
        return AsyncOutgoingWithRawResponse(self._secondary_dns.outgoing)

    @cached_property
    def acls(self) -> AsyncACLsWithRawResponse:
        return AsyncACLsWithRawResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> AsyncPeersWithRawResponse:
        return AsyncPeersWithRawResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> AsyncTSIGsWithRawResponse:
        return AsyncTSIGsWithRawResponse(self._secondary_dns.tsigs)


class SecondaryDNSWithStreamingResponse:
    def __init__(self, secondary_dns: SecondaryDNS) -> None:
        self._secondary_dns = secondary_dns

    @cached_property
    def force_axfr(self) -> ForceAXFRWithStreamingResponse:
        return ForceAXFRWithStreamingResponse(self._secondary_dns.force_axfr)

    @cached_property
    def incoming(self) -> IncomingWithStreamingResponse:
        return IncomingWithStreamingResponse(self._secondary_dns.incoming)

    @cached_property
    def outgoing(self) -> OutgoingWithStreamingResponse:
        return OutgoingWithStreamingResponse(self._secondary_dns.outgoing)

    @cached_property
    def acls(self) -> ACLsWithStreamingResponse:
        return ACLsWithStreamingResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> PeersWithStreamingResponse:
        return PeersWithStreamingResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> TSIGsWithStreamingResponse:
        return TSIGsWithStreamingResponse(self._secondary_dns.tsigs)


class AsyncSecondaryDNSWithStreamingResponse:
    def __init__(self, secondary_dns: AsyncSecondaryDNS) -> None:
        self._secondary_dns = secondary_dns

    @cached_property
    def force_axfr(self) -> AsyncForceAXFRWithStreamingResponse:
        return AsyncForceAXFRWithStreamingResponse(self._secondary_dns.force_axfr)

    @cached_property
    def incoming(self) -> AsyncIncomingWithStreamingResponse:
        return AsyncIncomingWithStreamingResponse(self._secondary_dns.incoming)

    @cached_property
    def outgoing(self) -> AsyncOutgoingWithStreamingResponse:
        return AsyncOutgoingWithStreamingResponse(self._secondary_dns.outgoing)

    @cached_property
    def acls(self) -> AsyncACLsWithStreamingResponse:
        return AsyncACLsWithStreamingResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> AsyncPeersWithStreamingResponse:
        return AsyncPeersWithStreamingResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> AsyncTSIGsWithStreamingResponse:
        return AsyncTSIGsWithStreamingResponse(self._secondary_dns.tsigs)
