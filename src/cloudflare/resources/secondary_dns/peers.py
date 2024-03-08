# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.secondary_dns import (
    PeerListResponse,
    SecondaryDNSPeer,
    PeerDeleteResponse,
    peer_create_params,
    peer_update_params,
)

__all__ = ["Peers", "AsyncPeers"]


class Peers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PeersWithRawResponse:
        return PeersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PeersWithStreamingResponse:
        return PeersWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: object,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecondaryDNSPeer:
        """
        Create Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_id}/secondary_dns/peers",
            body=maybe_transform(body, peer_create_params.PeerCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSPeer], ResultWrapper[SecondaryDNSPeer]),
        )

    def update(
        self,
        peer_id: object,
        *,
        account_id: object,
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
    ) -> SecondaryDNSPeer:
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
            f"/accounts/{account_id}/secondary_dns/peers/{peer_id}",
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
            cast_to=cast(Type[SecondaryDNSPeer], ResultWrapper[SecondaryDNSPeer]),
        )

    def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PeerListResponse]:
        """
        List Peers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/secondary_dns/peers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PeerListResponse]], ResultWrapper[PeerListResponse]),
        )

    def delete(
        self,
        peer_id: object,
        *,
        account_id: object,
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
            f"/accounts/{account_id}/secondary_dns/peers/{peer_id}",
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
        peer_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecondaryDNSPeer:
        """
        Get Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/secondary_dns/peers/{peer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSPeer], ResultWrapper[SecondaryDNSPeer]),
        )


class AsyncPeers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPeersWithRawResponse:
        return AsyncPeersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPeersWithStreamingResponse:
        return AsyncPeersWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: object,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecondaryDNSPeer:
        """
        Create Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_id}/secondary_dns/peers",
            body=await async_maybe_transform(body, peer_create_params.PeerCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSPeer], ResultWrapper[SecondaryDNSPeer]),
        )

    async def update(
        self,
        peer_id: object,
        *,
        account_id: object,
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
    ) -> SecondaryDNSPeer:
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
            f"/accounts/{account_id}/secondary_dns/peers/{peer_id}",
            body=await async_maybe_transform(
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
            cast_to=cast(Type[SecondaryDNSPeer], ResultWrapper[SecondaryDNSPeer]),
        )

    async def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PeerListResponse]:
        """
        List Peers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/secondary_dns/peers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PeerListResponse]], ResultWrapper[PeerListResponse]),
        )

    async def delete(
        self,
        peer_id: object,
        *,
        account_id: object,
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
            f"/accounts/{account_id}/secondary_dns/peers/{peer_id}",
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
        peer_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecondaryDNSPeer:
        """
        Get Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/secondary_dns/peers/{peer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSPeer], ResultWrapper[SecondaryDNSPeer]),
        )


class PeersWithRawResponse:
    def __init__(self, peers: Peers) -> None:
        self._peers = peers

        self.create = to_raw_response_wrapper(
            peers.create,
        )
        self.update = to_raw_response_wrapper(
            peers.update,
        )
        self.list = to_raw_response_wrapper(
            peers.list,
        )
        self.delete = to_raw_response_wrapper(
            peers.delete,
        )
        self.get = to_raw_response_wrapper(
            peers.get,
        )


class AsyncPeersWithRawResponse:
    def __init__(self, peers: AsyncPeers) -> None:
        self._peers = peers

        self.create = async_to_raw_response_wrapper(
            peers.create,
        )
        self.update = async_to_raw_response_wrapper(
            peers.update,
        )
        self.list = async_to_raw_response_wrapper(
            peers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            peers.delete,
        )
        self.get = async_to_raw_response_wrapper(
            peers.get,
        )


class PeersWithStreamingResponse:
    def __init__(self, peers: Peers) -> None:
        self._peers = peers

        self.create = to_streamed_response_wrapper(
            peers.create,
        )
        self.update = to_streamed_response_wrapper(
            peers.update,
        )
        self.list = to_streamed_response_wrapper(
            peers.list,
        )
        self.delete = to_streamed_response_wrapper(
            peers.delete,
        )
        self.get = to_streamed_response_wrapper(
            peers.get,
        )


class AsyncPeersWithStreamingResponse:
    def __init__(self, peers: AsyncPeers) -> None:
        self._peers = peers

        self.create = async_to_streamed_response_wrapper(
            peers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            peers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            peers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            peers.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            peers.get,
        )
