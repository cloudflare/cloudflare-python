# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.secondary_dns import (
    PeerUpdateResponse,
    PeerDeleteResponse,
    PeerGetResponse,
    PeerSecondaryDNSPeerCreatePeerResponse,
    PeerSecondaryDNSPeerListPeersResponse,
)

from typing import Type, Optional

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

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
from ...types.secondary_dns import peer_update_params
from ...types.secondary_dns import peer_secondary_dns_peer_create_peer_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Peers", "AsyncPeers"]


class Peers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PeersWithRawResponse:
        return PeersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PeersWithStreamingResponse:
        return PeersWithStreamingResponse(self)

    def update(
        self,
        identifier: object,
        *,
        account_identifier: object,
        name: str,
        ip: str | NotGiven = NOT_GIVEN,
        ixfr_enable: bool | NotGiven = NOT_GIVEN,
        port: float | NotGiven = NOT_GIVEN,
        tsig_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PeerUpdateResponse:
        """
        Modify Peer.

        Args:
          name: The name of the peer.

          ip: IPv4/IPv6 address of primary or secondary nameserver, depending on what zone
              this peer is linked to. For primary zones this IP defines the IP of the
              secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary
              zones this IP defines the IP of the primary nameserver Cloudflare will send
              AXFR/IXFR requests to.

          ixfr_enable: Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary
              zones.

          port: DNS port of primary or secondary nameserver, depending on what zone this peer is
              linked to.

          tsig_id: TSIG authentication will be used for zone transfer if configured.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_identifier}/secondary_dns/peers/{identifier}",
            body=maybe_transform(
                {
                    "name": name,
                    "ip": ip,
                    "ixfr_enable": ixfr_enable,
                    "port": port,
                    "tsig_id": tsig_id,
                },
                peer_update_params.PeerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PeerUpdateResponse], ResultWrapper[PeerUpdateResponse]),
        )

    def delete(
        self,
        identifier: object,
        *,
        account_identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PeerDeleteResponse:
        """
        Delete Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/accounts/{account_identifier}/secondary_dns/peers/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PeerDeleteResponse], ResultWrapper[PeerDeleteResponse]),
        )

    def get(
        self,
        identifier: object,
        *,
        account_identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PeerGetResponse:
        """
        Get Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_identifier}/secondary_dns/peers/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PeerGetResponse], ResultWrapper[PeerGetResponse]),
        )

    def secondary_dns_peer_create_peer(
        self,
        account_identifier: object,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PeerSecondaryDNSPeerCreatePeerResponse:
        """
        Create Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_identifier}/secondary_dns/peers",
            body=maybe_transform(body, peer_secondary_dns_peer_create_peer_params.PeerSecondaryDNSPeerCreatePeerParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PeerSecondaryDNSPeerCreatePeerResponse], ResultWrapper[PeerSecondaryDNSPeerCreatePeerResponse]
            ),
        )

    def secondary_dns_peer_list_peers(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PeerSecondaryDNSPeerListPeersResponse]:
        """
        List Peers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_identifier}/secondary_dns/peers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PeerSecondaryDNSPeerListPeersResponse]],
                ResultWrapper[PeerSecondaryDNSPeerListPeersResponse],
            ),
        )


class AsyncPeers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPeersWithRawResponse:
        return AsyncPeersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPeersWithStreamingResponse:
        return AsyncPeersWithStreamingResponse(self)

    async def update(
        self,
        identifier: object,
        *,
        account_identifier: object,
        name: str,
        ip: str | NotGiven = NOT_GIVEN,
        ixfr_enable: bool | NotGiven = NOT_GIVEN,
        port: float | NotGiven = NOT_GIVEN,
        tsig_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PeerUpdateResponse:
        """
        Modify Peer.

        Args:
          name: The name of the peer.

          ip: IPv4/IPv6 address of primary or secondary nameserver, depending on what zone
              this peer is linked to. For primary zones this IP defines the IP of the
              secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary
              zones this IP defines the IP of the primary nameserver Cloudflare will send
              AXFR/IXFR requests to.

          ixfr_enable: Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary
              zones.

          port: DNS port of primary or secondary nameserver, depending on what zone this peer is
              linked to.

          tsig_id: TSIG authentication will be used for zone transfer if configured.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_identifier}/secondary_dns/peers/{identifier}",
            body=maybe_transform(
                {
                    "name": name,
                    "ip": ip,
                    "ixfr_enable": ixfr_enable,
                    "port": port,
                    "tsig_id": tsig_id,
                },
                peer_update_params.PeerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PeerUpdateResponse], ResultWrapper[PeerUpdateResponse]),
        )

    async def delete(
        self,
        identifier: object,
        *,
        account_identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PeerDeleteResponse:
        """
        Delete Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/accounts/{account_identifier}/secondary_dns/peers/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PeerDeleteResponse], ResultWrapper[PeerDeleteResponse]),
        )

    async def get(
        self,
        identifier: object,
        *,
        account_identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PeerGetResponse:
        """
        Get Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_identifier}/secondary_dns/peers/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PeerGetResponse], ResultWrapper[PeerGetResponse]),
        )

    async def secondary_dns_peer_create_peer(
        self,
        account_identifier: object,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PeerSecondaryDNSPeerCreatePeerResponse:
        """
        Create Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_identifier}/secondary_dns/peers",
            body=maybe_transform(body, peer_secondary_dns_peer_create_peer_params.PeerSecondaryDNSPeerCreatePeerParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PeerSecondaryDNSPeerCreatePeerResponse], ResultWrapper[PeerSecondaryDNSPeerCreatePeerResponse]
            ),
        )

    async def secondary_dns_peer_list_peers(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PeerSecondaryDNSPeerListPeersResponse]:
        """
        List Peers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_identifier}/secondary_dns/peers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PeerSecondaryDNSPeerListPeersResponse]],
                ResultWrapper[PeerSecondaryDNSPeerListPeersResponse],
            ),
        )


class PeersWithRawResponse:
    def __init__(self, peers: Peers) -> None:
        self._peers = peers

        self.update = to_raw_response_wrapper(
            peers.update,
        )
        self.delete = to_raw_response_wrapper(
            peers.delete,
        )
        self.get = to_raw_response_wrapper(
            peers.get,
        )
        self.secondary_dns_peer_create_peer = to_raw_response_wrapper(
            peers.secondary_dns_peer_create_peer,
        )
        self.secondary_dns_peer_list_peers = to_raw_response_wrapper(
            peers.secondary_dns_peer_list_peers,
        )


class AsyncPeersWithRawResponse:
    def __init__(self, peers: AsyncPeers) -> None:
        self._peers = peers

        self.update = async_to_raw_response_wrapper(
            peers.update,
        )
        self.delete = async_to_raw_response_wrapper(
            peers.delete,
        )
        self.get = async_to_raw_response_wrapper(
            peers.get,
        )
        self.secondary_dns_peer_create_peer = async_to_raw_response_wrapper(
            peers.secondary_dns_peer_create_peer,
        )
        self.secondary_dns_peer_list_peers = async_to_raw_response_wrapper(
            peers.secondary_dns_peer_list_peers,
        )


class PeersWithStreamingResponse:
    def __init__(self, peers: Peers) -> None:
        self._peers = peers

        self.update = to_streamed_response_wrapper(
            peers.update,
        )
        self.delete = to_streamed_response_wrapper(
            peers.delete,
        )
        self.get = to_streamed_response_wrapper(
            peers.get,
        )
        self.secondary_dns_peer_create_peer = to_streamed_response_wrapper(
            peers.secondary_dns_peer_create_peer,
        )
        self.secondary_dns_peer_list_peers = to_streamed_response_wrapper(
            peers.secondary_dns_peer_list_peers,
        )


class AsyncPeersWithStreamingResponse:
    def __init__(self, peers: AsyncPeers) -> None:
        self._peers = peers

        self.update = async_to_streamed_response_wrapper(
            peers.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            peers.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            peers.get,
        )
        self.secondary_dns_peer_create_peer = async_to_streamed_response_wrapper(
            peers.secondary_dns_peer_create_peer,
        )
        self.secondary_dns_peer_list_peers = async_to_streamed_response_wrapper(
            peers.secondary_dns_peer_list_peers,
        )
