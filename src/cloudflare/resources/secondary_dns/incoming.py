# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

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
    IncomingGetResponse,
    IncomingCreateResponse,
    IncomingDeleteResponse,
    IncomingUpdateResponse,
    incoming_create_params,
    incoming_update_params,
)

__all__ = ["Incoming", "AsyncIncoming"]


class Incoming(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IncomingWithRawResponse:
        return IncomingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncomingWithStreamingResponse:
        return IncomingWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: object,
        auto_refresh_seconds: float,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingCreateResponse:
        """
        Create secondary zone configuration for incoming zone transfers.

        Args:
          auto_refresh_seconds: How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
              applicable for primary zones.

          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/zones/{zone_id}/secondary_dns/incoming",
            body=maybe_transform(
                {
                    "auto_refresh_seconds": auto_refresh_seconds,
                    "name": name,
                    "peers": peers,
                },
                incoming_create_params.IncomingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IncomingCreateResponse], ResultWrapper[IncomingCreateResponse]),
        )

    def update(
        self,
        *,
        zone_id: object,
        auto_refresh_seconds: float,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingUpdateResponse:
        """
        Update secondary zone configuration for incoming zone transfers.

        Args:
          auto_refresh_seconds: How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
              applicable for primary zones.

          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/zones/{zone_id}/secondary_dns/incoming",
            body=maybe_transform(
                {
                    "auto_refresh_seconds": auto_refresh_seconds,
                    "name": name,
                    "peers": peers,
                },
                incoming_update_params.IncomingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IncomingUpdateResponse], ResultWrapper[IncomingUpdateResponse]),
        )

    def delete(
        self,
        *,
        zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingDeleteResponse:
        """
        Delete secondary zone configuration for incoming zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/zones/{zone_id}/secondary_dns/incoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IncomingDeleteResponse], ResultWrapper[IncomingDeleteResponse]),
        )

    def get(
        self,
        *,
        zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingGetResponse:
        """
        Get secondary zone configuration for incoming zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/zones/{zone_id}/secondary_dns/incoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IncomingGetResponse], ResultWrapper[IncomingGetResponse]),
        )


class AsyncIncoming(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIncomingWithRawResponse:
        return AsyncIncomingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncomingWithStreamingResponse:
        return AsyncIncomingWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: object,
        auto_refresh_seconds: float,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingCreateResponse:
        """
        Create secondary zone configuration for incoming zone transfers.

        Args:
          auto_refresh_seconds: How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
              applicable for primary zones.

          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/incoming",
            body=await async_maybe_transform(
                {
                    "auto_refresh_seconds": auto_refresh_seconds,
                    "name": name,
                    "peers": peers,
                },
                incoming_create_params.IncomingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IncomingCreateResponse], ResultWrapper[IncomingCreateResponse]),
        )

    async def update(
        self,
        *,
        zone_id: object,
        auto_refresh_seconds: float,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingUpdateResponse:
        """
        Update secondary zone configuration for incoming zone transfers.

        Args:
          auto_refresh_seconds: How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
              applicable for primary zones.

          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/zones/{zone_id}/secondary_dns/incoming",
            body=await async_maybe_transform(
                {
                    "auto_refresh_seconds": auto_refresh_seconds,
                    "name": name,
                    "peers": peers,
                },
                incoming_update_params.IncomingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IncomingUpdateResponse], ResultWrapper[IncomingUpdateResponse]),
        )

    async def delete(
        self,
        *,
        zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingDeleteResponse:
        """
        Delete secondary zone configuration for incoming zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/zones/{zone_id}/secondary_dns/incoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IncomingDeleteResponse], ResultWrapper[IncomingDeleteResponse]),
        )

    async def get(
        self,
        *,
        zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingGetResponse:
        """
        Get secondary zone configuration for incoming zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/zones/{zone_id}/secondary_dns/incoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IncomingGetResponse], ResultWrapper[IncomingGetResponse]),
        )


class IncomingWithRawResponse:
    def __init__(self, incoming: Incoming) -> None:
        self._incoming = incoming

        self.create = to_raw_response_wrapper(
            incoming.create,
        )
        self.update = to_raw_response_wrapper(
            incoming.update,
        )
        self.delete = to_raw_response_wrapper(
            incoming.delete,
        )
        self.get = to_raw_response_wrapper(
            incoming.get,
        )


class AsyncIncomingWithRawResponse:
    def __init__(self, incoming: AsyncIncoming) -> None:
        self._incoming = incoming

        self.create = async_to_raw_response_wrapper(
            incoming.create,
        )
        self.update = async_to_raw_response_wrapper(
            incoming.update,
        )
        self.delete = async_to_raw_response_wrapper(
            incoming.delete,
        )
        self.get = async_to_raw_response_wrapper(
            incoming.get,
        )


class IncomingWithStreamingResponse:
    def __init__(self, incoming: Incoming) -> None:
        self._incoming = incoming

        self.create = to_streamed_response_wrapper(
            incoming.create,
        )
        self.update = to_streamed_response_wrapper(
            incoming.update,
        )
        self.delete = to_streamed_response_wrapper(
            incoming.delete,
        )
        self.get = to_streamed_response_wrapper(
            incoming.get,
        )


class AsyncIncomingWithStreamingResponse:
    def __init__(self, incoming: AsyncIncoming) -> None:
        self._incoming = incoming

        self.create = async_to_streamed_response_wrapper(
            incoming.create,
        )
        self.update = async_to_streamed_response_wrapper(
            incoming.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            incoming.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            incoming.get,
        )
