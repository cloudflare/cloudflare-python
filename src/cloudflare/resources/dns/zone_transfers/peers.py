# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.dns.zone_transfers import peer_create_params, peer_update_params
from ....types.dns.zone_transfers.peer import Peer
from ....types.dns.zone_transfers.peer_delete_response import PeerDeleteResponse

__all__ = ["PeersResource", "AsyncPeersResource"]


class PeersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PeersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PeersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PeersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PeersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Peer]:
        """
        Create Peer.

        Args:
          name: The name of the peer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/secondary_dns/peers",
            body=maybe_transform({"name": name}, peer_create_params.PeerCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Peer]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Peer]], ResultWrapper[Peer]),
        )

    def update(
        self,
        peer_id: str,
        *,
        account_id: str,
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
    ) -> Optional[Peer]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
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
                post_parser=ResultWrapper[Optional[Peer]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Peer]], ResultWrapper[Peer]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Peer]:
        """
        List Peers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/secondary_dns/peers",
            page=SyncSinglePage[Peer],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Peer,
        )

    def delete(
        self,
        peer_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PeerDeleteResponse]:
        """
        Delete Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return self._delete(
            f"/accounts/{account_id}/secondary_dns/peers/{peer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PeerDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PeerDeleteResponse]], ResultWrapper[PeerDeleteResponse]),
        )

    def get(
        self,
        peer_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Peer]:
        """
        Get Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return self._get(
            f"/accounts/{account_id}/secondary_dns/peers/{peer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Peer]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Peer]], ResultWrapper[Peer]),
        )


class AsyncPeersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPeersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPeersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPeersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPeersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Peer]:
        """
        Create Peer.

        Args:
          name: The name of the peer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/secondary_dns/peers",
            body=await async_maybe_transform({"name": name}, peer_create_params.PeerCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Peer]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Peer]], ResultWrapper[Peer]),
        )

    async def update(
        self,
        peer_id: str,
        *,
        account_id: str,
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
    ) -> Optional[Peer]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
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
                post_parser=ResultWrapper[Optional[Peer]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Peer]], ResultWrapper[Peer]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Peer, AsyncSinglePage[Peer]]:
        """
        List Peers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/secondary_dns/peers",
            page=AsyncSinglePage[Peer],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Peer,
        )

    async def delete(
        self,
        peer_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PeerDeleteResponse]:
        """
        Delete Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/secondary_dns/peers/{peer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PeerDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PeerDeleteResponse]], ResultWrapper[PeerDeleteResponse]),
        )

    async def get(
        self,
        peer_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Peer]:
        """
        Get Peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return await self._get(
            f"/accounts/{account_id}/secondary_dns/peers/{peer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Peer]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Peer]], ResultWrapper[Peer]),
        )


class PeersResourceWithRawResponse:
    def __init__(self, peers: PeersResource) -> None:
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


class AsyncPeersResourceWithRawResponse:
    def __init__(self, peers: AsyncPeersResource) -> None:
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


class PeersResourceWithStreamingResponse:
    def __init__(self, peers: PeersResource) -> None:
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


class AsyncPeersResourceWithStreamingResponse:
    def __init__(self, peers: AsyncPeersResource) -> None:
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
