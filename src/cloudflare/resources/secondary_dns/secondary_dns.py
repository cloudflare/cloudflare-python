# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .acls import (
    ACLsResource,
    AsyncACLsResource,
    ACLsResourceWithRawResponse,
    AsyncACLsResourceWithRawResponse,
    ACLsResourceWithStreamingResponse,
    AsyncACLsResourceWithStreamingResponse,
)
from .peers import (
    PeersResource,
    AsyncPeersResource,
    PeersResourceWithRawResponse,
    AsyncPeersResourceWithRawResponse,
    PeersResourceWithStreamingResponse,
    AsyncPeersResourceWithStreamingResponse,
)
from .tsigs import (
    TSIGsResource,
    AsyncTSIGsResource,
    TSIGsResourceWithRawResponse,
    AsyncTSIGsResourceWithRawResponse,
    TSIGsResourceWithStreamingResponse,
    AsyncTSIGsResourceWithStreamingResponse,
)
from .incoming import (
    IncomingResource,
    AsyncIncomingResource,
    IncomingResourceWithRawResponse,
    AsyncIncomingResourceWithRawResponse,
    IncomingResourceWithStreamingResponse,
    AsyncIncomingResourceWithStreamingResponse,
)
from .outgoing import (
    OutgoingResource,
    AsyncOutgoingResource,
    OutgoingResourceWithRawResponse,
    AsyncOutgoingResourceWithRawResponse,
    OutgoingResourceWithStreamingResponse,
    AsyncOutgoingResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .force_axfr import (
    ForceAXFRResource,
    AsyncForceAXFRResource,
    ForceAXFRResourceWithRawResponse,
    AsyncForceAXFRResourceWithRawResponse,
    ForceAXFRResourceWithStreamingResponse,
    AsyncForceAXFRResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .outgoing.outgoing import OutgoingResource, AsyncOutgoingResource

__all__ = ["SecondaryDNSResource", "AsyncSecondaryDNSResource"]


class SecondaryDNSResource(SyncAPIResource):
    @cached_property
    def force_axfr(self) -> ForceAXFRResource:
        return ForceAXFRResource(self._client)

    @cached_property
    def incoming(self) -> IncomingResource:
        return IncomingResource(self._client)

    @cached_property
    def outgoing(self) -> OutgoingResource:
        return OutgoingResource(self._client)

    @cached_property
    def acls(self) -> ACLsResource:
        return ACLsResource(self._client)

    @cached_property
    def peers(self) -> PeersResource:
        return PeersResource(self._client)

    @cached_property
    def tsigs(self) -> TSIGsResource:
        return TSIGsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecondaryDNSResourceWithRawResponse:
        return SecondaryDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecondaryDNSResourceWithStreamingResponse:
        return SecondaryDNSResourceWithStreamingResponse(self)


class AsyncSecondaryDNSResource(AsyncAPIResource):
    @cached_property
    def force_axfr(self) -> AsyncForceAXFRResource:
        return AsyncForceAXFRResource(self._client)

    @cached_property
    def incoming(self) -> AsyncIncomingResource:
        return AsyncIncomingResource(self._client)

    @cached_property
    def outgoing(self) -> AsyncOutgoingResource:
        return AsyncOutgoingResource(self._client)

    @cached_property
    def acls(self) -> AsyncACLsResource:
        return AsyncACLsResource(self._client)

    @cached_property
    def peers(self) -> AsyncPeersResource:
        return AsyncPeersResource(self._client)

    @cached_property
    def tsigs(self) -> AsyncTSIGsResource:
        return AsyncTSIGsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecondaryDNSResourceWithRawResponse:
        return AsyncSecondaryDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecondaryDNSResourceWithStreamingResponse:
        return AsyncSecondaryDNSResourceWithStreamingResponse(self)


class SecondaryDNSResourceWithRawResponse:
    def __init__(self, secondary_dns: SecondaryDNSResource) -> None:
        self._secondary_dns = secondary_dns

    @cached_property
    def force_axfr(self) -> ForceAXFRResourceWithRawResponse:
        return ForceAXFRResourceWithRawResponse(self._secondary_dns.force_axfr)

    @cached_property
    def incoming(self) -> IncomingResourceWithRawResponse:
        return IncomingResourceWithRawResponse(self._secondary_dns.incoming)

    @cached_property
    def outgoing(self) -> OutgoingResourceWithRawResponse:
        return OutgoingResourceWithRawResponse(self._secondary_dns.outgoing)

    @cached_property
    def acls(self) -> ACLsResourceWithRawResponse:
        return ACLsResourceWithRawResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> PeersResourceWithRawResponse:
        return PeersResourceWithRawResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> TSIGsResourceWithRawResponse:
        return TSIGsResourceWithRawResponse(self._secondary_dns.tsigs)


class AsyncSecondaryDNSResourceWithRawResponse:
    def __init__(self, secondary_dns: AsyncSecondaryDNSResource) -> None:
        self._secondary_dns = secondary_dns

    @cached_property
    def force_axfr(self) -> AsyncForceAXFRResourceWithRawResponse:
        return AsyncForceAXFRResourceWithRawResponse(self._secondary_dns.force_axfr)

    @cached_property
    def incoming(self) -> AsyncIncomingResourceWithRawResponse:
        return AsyncIncomingResourceWithRawResponse(self._secondary_dns.incoming)

    @cached_property
    def outgoing(self) -> AsyncOutgoingResourceWithRawResponse:
        return AsyncOutgoingResourceWithRawResponse(self._secondary_dns.outgoing)

    @cached_property
    def acls(self) -> AsyncACLsResourceWithRawResponse:
        return AsyncACLsResourceWithRawResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> AsyncPeersResourceWithRawResponse:
        return AsyncPeersResourceWithRawResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> AsyncTSIGsResourceWithRawResponse:
        return AsyncTSIGsResourceWithRawResponse(self._secondary_dns.tsigs)


class SecondaryDNSResourceWithStreamingResponse:
    def __init__(self, secondary_dns: SecondaryDNSResource) -> None:
        self._secondary_dns = secondary_dns

    @cached_property
    def force_axfr(self) -> ForceAXFRResourceWithStreamingResponse:
        return ForceAXFRResourceWithStreamingResponse(self._secondary_dns.force_axfr)

    @cached_property
    def incoming(self) -> IncomingResourceWithStreamingResponse:
        return IncomingResourceWithStreamingResponse(self._secondary_dns.incoming)

    @cached_property
    def outgoing(self) -> OutgoingResourceWithStreamingResponse:
        return OutgoingResourceWithStreamingResponse(self._secondary_dns.outgoing)

    @cached_property
    def acls(self) -> ACLsResourceWithStreamingResponse:
        return ACLsResourceWithStreamingResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> PeersResourceWithStreamingResponse:
        return PeersResourceWithStreamingResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> TSIGsResourceWithStreamingResponse:
        return TSIGsResourceWithStreamingResponse(self._secondary_dns.tsigs)


class AsyncSecondaryDNSResourceWithStreamingResponse:
    def __init__(self, secondary_dns: AsyncSecondaryDNSResource) -> None:
        self._secondary_dns = secondary_dns

    @cached_property
    def force_axfr(self) -> AsyncForceAXFRResourceWithStreamingResponse:
        return AsyncForceAXFRResourceWithStreamingResponse(self._secondary_dns.force_axfr)

    @cached_property
    def incoming(self) -> AsyncIncomingResourceWithStreamingResponse:
        return AsyncIncomingResourceWithStreamingResponse(self._secondary_dns.incoming)

    @cached_property
    def outgoing(self) -> AsyncOutgoingResourceWithStreamingResponse:
        return AsyncOutgoingResourceWithStreamingResponse(self._secondary_dns.outgoing)

    @cached_property
    def acls(self) -> AsyncACLsResourceWithStreamingResponse:
        return AsyncACLsResourceWithStreamingResponse(self._secondary_dns.acls)

    @cached_property
    def peers(self) -> AsyncPeersResourceWithStreamingResponse:
        return AsyncPeersResourceWithStreamingResponse(self._secondary_dns.peers)

    @cached_property
    def tsigs(self) -> AsyncTSIGsResourceWithStreamingResponse:
        return AsyncTSIGsResourceWithStreamingResponse(self._secondary_dns.tsigs)
