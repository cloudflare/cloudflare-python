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
from ...._compat import cached_property
from .force_axfr import (
    ForceAXFRResource,
    AsyncForceAXFRResource,
    ForceAXFRResourceWithRawResponse,
    AsyncForceAXFRResourceWithRawResponse,
    ForceAXFRResourceWithStreamingResponse,
    AsyncForceAXFRResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .outgoing.outgoing import (
    OutgoingResource,
    AsyncOutgoingResource,
    OutgoingResourceWithRawResponse,
    AsyncOutgoingResourceWithRawResponse,
    OutgoingResourceWithStreamingResponse,
    AsyncOutgoingResourceWithStreamingResponse,
)

__all__ = ["ZoneTransfersResource", "AsyncZoneTransfersResource"]


class ZoneTransfersResource(SyncAPIResource):
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
    def with_raw_response(self) -> ZoneTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ZoneTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZoneTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ZoneTransfersResourceWithStreamingResponse(self)


class AsyncZoneTransfersResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncZoneTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZoneTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZoneTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncZoneTransfersResourceWithStreamingResponse(self)


class ZoneTransfersResourceWithRawResponse:
    def __init__(self, zone_transfers: ZoneTransfersResource) -> None:
        self._zone_transfers = zone_transfers

    @cached_property
    def force_axfr(self) -> ForceAXFRResourceWithRawResponse:
        return ForceAXFRResourceWithRawResponse(self._zone_transfers.force_axfr)

    @cached_property
    def incoming(self) -> IncomingResourceWithRawResponse:
        return IncomingResourceWithRawResponse(self._zone_transfers.incoming)

    @cached_property
    def outgoing(self) -> OutgoingResourceWithRawResponse:
        return OutgoingResourceWithRawResponse(self._zone_transfers.outgoing)

    @cached_property
    def acls(self) -> ACLsResourceWithRawResponse:
        return ACLsResourceWithRawResponse(self._zone_transfers.acls)

    @cached_property
    def peers(self) -> PeersResourceWithRawResponse:
        return PeersResourceWithRawResponse(self._zone_transfers.peers)

    @cached_property
    def tsigs(self) -> TSIGsResourceWithRawResponse:
        return TSIGsResourceWithRawResponse(self._zone_transfers.tsigs)


class AsyncZoneTransfersResourceWithRawResponse:
    def __init__(self, zone_transfers: AsyncZoneTransfersResource) -> None:
        self._zone_transfers = zone_transfers

    @cached_property
    def force_axfr(self) -> AsyncForceAXFRResourceWithRawResponse:
        return AsyncForceAXFRResourceWithRawResponse(self._zone_transfers.force_axfr)

    @cached_property
    def incoming(self) -> AsyncIncomingResourceWithRawResponse:
        return AsyncIncomingResourceWithRawResponse(self._zone_transfers.incoming)

    @cached_property
    def outgoing(self) -> AsyncOutgoingResourceWithRawResponse:
        return AsyncOutgoingResourceWithRawResponse(self._zone_transfers.outgoing)

    @cached_property
    def acls(self) -> AsyncACLsResourceWithRawResponse:
        return AsyncACLsResourceWithRawResponse(self._zone_transfers.acls)

    @cached_property
    def peers(self) -> AsyncPeersResourceWithRawResponse:
        return AsyncPeersResourceWithRawResponse(self._zone_transfers.peers)

    @cached_property
    def tsigs(self) -> AsyncTSIGsResourceWithRawResponse:
        return AsyncTSIGsResourceWithRawResponse(self._zone_transfers.tsigs)


class ZoneTransfersResourceWithStreamingResponse:
    def __init__(self, zone_transfers: ZoneTransfersResource) -> None:
        self._zone_transfers = zone_transfers

    @cached_property
    def force_axfr(self) -> ForceAXFRResourceWithStreamingResponse:
        return ForceAXFRResourceWithStreamingResponse(self._zone_transfers.force_axfr)

    @cached_property
    def incoming(self) -> IncomingResourceWithStreamingResponse:
        return IncomingResourceWithStreamingResponse(self._zone_transfers.incoming)

    @cached_property
    def outgoing(self) -> OutgoingResourceWithStreamingResponse:
        return OutgoingResourceWithStreamingResponse(self._zone_transfers.outgoing)

    @cached_property
    def acls(self) -> ACLsResourceWithStreamingResponse:
        return ACLsResourceWithStreamingResponse(self._zone_transfers.acls)

    @cached_property
    def peers(self) -> PeersResourceWithStreamingResponse:
        return PeersResourceWithStreamingResponse(self._zone_transfers.peers)

    @cached_property
    def tsigs(self) -> TSIGsResourceWithStreamingResponse:
        return TSIGsResourceWithStreamingResponse(self._zone_transfers.tsigs)


class AsyncZoneTransfersResourceWithStreamingResponse:
    def __init__(self, zone_transfers: AsyncZoneTransfersResource) -> None:
        self._zone_transfers = zone_transfers

    @cached_property
    def force_axfr(self) -> AsyncForceAXFRResourceWithStreamingResponse:
        return AsyncForceAXFRResourceWithStreamingResponse(self._zone_transfers.force_axfr)

    @cached_property
    def incoming(self) -> AsyncIncomingResourceWithStreamingResponse:
        return AsyncIncomingResourceWithStreamingResponse(self._zone_transfers.incoming)

    @cached_property
    def outgoing(self) -> AsyncOutgoingResourceWithStreamingResponse:
        return AsyncOutgoingResourceWithStreamingResponse(self._zone_transfers.outgoing)

    @cached_property
    def acls(self) -> AsyncACLsResourceWithStreamingResponse:
        return AsyncACLsResourceWithStreamingResponse(self._zone_transfers.acls)

    @cached_property
    def peers(self) -> AsyncPeersResourceWithStreamingResponse:
        return AsyncPeersResourceWithStreamingResponse(self._zone_transfers.peers)

    @cached_property
    def tsigs(self) -> AsyncTSIGsResourceWithStreamingResponse:
        return AsyncTSIGsResourceWithStreamingResponse(self._zone_transfers.tsigs)
