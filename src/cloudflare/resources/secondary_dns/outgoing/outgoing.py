# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from .status import (
    Status,
    AsyncStatus,
    StatusWithRawResponse,
    AsyncStatusWithRawResponse,
    StatusWithStreamingResponse,
    AsyncStatusWithStreamingResponse,
)
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
from ...._base_client import (
    make_request_options,
)
from ....types.secondary_dns import (
    OutgoingGetResponse,
    OutgoingCreateResponse,
    OutgoingDeleteResponse,
    OutgoingUpdateResponse,
    outgoing_create_params,
    outgoing_update_params,
)

__all__ = ["Outgoing", "AsyncOutgoing"]


class Outgoing(SyncAPIResource):
    @cached_property
    def status(self) -> Status:
        return Status(self._client)

    @cached_property
    def with_raw_response(self) -> OutgoingWithRawResponse:
        return OutgoingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutgoingWithStreamingResponse:
        return OutgoingWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingCreateResponse:
        """
        Create primary zone configuration for outgoing zone transfers.

        Args:
          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            body=maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_create_params.OutgoingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutgoingCreateResponse], ResultWrapper[OutgoingCreateResponse]),
        )

    def update(
        self,
        *,
        zone_id: str,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingUpdateResponse:
        """
        Update primary zone configuration for outgoing zone transfers.

        Args:
          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            body=maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_update_params.OutgoingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutgoingUpdateResponse], ResultWrapper[OutgoingUpdateResponse]),
        )

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingDeleteResponse:
        """
        Delete primary zone configuration for outgoing zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutgoingDeleteResponse], ResultWrapper[OutgoingDeleteResponse]),
        )

    def disable(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Disable outgoing zone transfers for primary zone and clears IXFR backlog of
        primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def enable(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Enable outgoing zone transfers for primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def force_notify(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Notifies the secondary nameserver(s) and clears IXFR backlog of primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/force_notify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingGetResponse:
        """
        Get primary zone configuration for outgoing zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutgoingGetResponse], ResultWrapper[OutgoingGetResponse]),
        )


class AsyncOutgoing(AsyncAPIResource):
    @cached_property
    def status(self) -> AsyncStatus:
        return AsyncStatus(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOutgoingWithRawResponse:
        return AsyncOutgoingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutgoingWithStreamingResponse:
        return AsyncOutgoingWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingCreateResponse:
        """
        Create primary zone configuration for outgoing zone transfers.

        Args:
          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_create_params.OutgoingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutgoingCreateResponse], ResultWrapper[OutgoingCreateResponse]),
        )

    async def update(
        self,
        *,
        zone_id: str,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingUpdateResponse:
        """
        Update primary zone configuration for outgoing zone transfers.

        Args:
          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_update_params.OutgoingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutgoingUpdateResponse], ResultWrapper[OutgoingUpdateResponse]),
        )

    async def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingDeleteResponse:
        """
        Delete primary zone configuration for outgoing zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutgoingDeleteResponse], ResultWrapper[OutgoingDeleteResponse]),
        )

    async def disable(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Disable outgoing zone transfers for primary zone and clears IXFR backlog of
        primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def enable(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Enable outgoing zone transfers for primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def force_notify(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Notifies the secondary nameserver(s) and clears IXFR backlog of primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/force_notify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingGetResponse:
        """
        Get primary zone configuration for outgoing zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutgoingGetResponse], ResultWrapper[OutgoingGetResponse]),
        )


class OutgoingWithRawResponse:
    def __init__(self, outgoing: Outgoing) -> None:
        self._outgoing = outgoing

        self.create = to_raw_response_wrapper(
            outgoing.create,
        )
        self.update = to_raw_response_wrapper(
            outgoing.update,
        )
        self.delete = to_raw_response_wrapper(
            outgoing.delete,
        )
        self.disable = to_raw_response_wrapper(
            outgoing.disable,
        )
        self.enable = to_raw_response_wrapper(
            outgoing.enable,
        )
        self.force_notify = to_raw_response_wrapper(
            outgoing.force_notify,
        )
        self.get = to_raw_response_wrapper(
            outgoing.get,
        )

    @cached_property
    def status(self) -> StatusWithRawResponse:
        return StatusWithRawResponse(self._outgoing.status)


class AsyncOutgoingWithRawResponse:
    def __init__(self, outgoing: AsyncOutgoing) -> None:
        self._outgoing = outgoing

        self.create = async_to_raw_response_wrapper(
            outgoing.create,
        )
        self.update = async_to_raw_response_wrapper(
            outgoing.update,
        )
        self.delete = async_to_raw_response_wrapper(
            outgoing.delete,
        )
        self.disable = async_to_raw_response_wrapper(
            outgoing.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            outgoing.enable,
        )
        self.force_notify = async_to_raw_response_wrapper(
            outgoing.force_notify,
        )
        self.get = async_to_raw_response_wrapper(
            outgoing.get,
        )

    @cached_property
    def status(self) -> AsyncStatusWithRawResponse:
        return AsyncStatusWithRawResponse(self._outgoing.status)


class OutgoingWithStreamingResponse:
    def __init__(self, outgoing: Outgoing) -> None:
        self._outgoing = outgoing

        self.create = to_streamed_response_wrapper(
            outgoing.create,
        )
        self.update = to_streamed_response_wrapper(
            outgoing.update,
        )
        self.delete = to_streamed_response_wrapper(
            outgoing.delete,
        )
        self.disable = to_streamed_response_wrapper(
            outgoing.disable,
        )
        self.enable = to_streamed_response_wrapper(
            outgoing.enable,
        )
        self.force_notify = to_streamed_response_wrapper(
            outgoing.force_notify,
        )
        self.get = to_streamed_response_wrapper(
            outgoing.get,
        )

    @cached_property
    def status(self) -> StatusWithStreamingResponse:
        return StatusWithStreamingResponse(self._outgoing.status)


class AsyncOutgoingWithStreamingResponse:
    def __init__(self, outgoing: AsyncOutgoing) -> None:
        self._outgoing = outgoing

        self.create = async_to_streamed_response_wrapper(
            outgoing.create,
        )
        self.update = async_to_streamed_response_wrapper(
            outgoing.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            outgoing.delete,
        )
        self.disable = async_to_streamed_response_wrapper(
            outgoing.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            outgoing.enable,
        )
        self.force_notify = async_to_streamed_response_wrapper(
            outgoing.force_notify,
        )
        self.get = async_to_streamed_response_wrapper(
            outgoing.get,
        )

    @cached_property
    def status(self) -> AsyncStatusWithStreamingResponse:
        return AsyncStatusWithStreamingResponse(self._outgoing.status)
