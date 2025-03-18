# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

import httpx

from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.dns.zone_transfers import (
    outgoing_create_params,
    outgoing_enable_params,
    outgoing_update_params,
    outgoing_disable_params,
    outgoing_force_notify_params,
)
from .....types.dns.zone_transfers.enable_transfer import EnableTransfer
from .....types.dns.zone_transfers.disable_transfer import DisableTransfer
from .....types.dns.zone_transfers.outgoing_get_response import OutgoingGetResponse
from .....types.dns.zone_transfers.outgoing_create_response import OutgoingCreateResponse
from .....types.dns.zone_transfers.outgoing_delete_response import OutgoingDeleteResponse
from .....types.dns.zone_transfers.outgoing_update_response import OutgoingUpdateResponse
from .....types.dns.zone_transfers.outgoing_force_notify_response import OutgoingForceNotifyResponse

__all__ = ["OutgoingResource", "AsyncOutgoingResource"]


class OutgoingResource(SyncAPIResource):
    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> OutgoingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OutgoingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutgoingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OutgoingResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingCreateResponse]:
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
                post_parser=ResultWrapper[Optional[OutgoingCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingCreateResponse]], ResultWrapper[OutgoingCreateResponse]),
        )

    def update(
        self,
        *,
        zone_id: str,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingUpdateResponse]:
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
                post_parser=ResultWrapper[Optional[OutgoingUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingUpdateResponse]], ResultWrapper[OutgoingUpdateResponse]),
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
    ) -> Optional[OutgoingDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[OutgoingDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingDeleteResponse]], ResultWrapper[OutgoingDeleteResponse]),
        )

    def disable(
        self,
        *,
        zone_id: str,
        body: object,
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
            body=maybe_transform(body, outgoing_disable_params.OutgoingDisableParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DisableTransfer]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def enable(
        self,
        *,
        zone_id: str,
        body: object,
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
            body=maybe_transform(body, outgoing_enable_params.OutgoingEnableParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EnableTransfer]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def force_notify(
        self,
        *,
        zone_id: str,
        body: object,
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
            body=maybe_transform(body, outgoing_force_notify_params.OutgoingForceNotifyParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingForceNotifyResponse]]._unwrapper,
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
    ) -> Optional[OutgoingGetResponse]:
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
                post_parser=ResultWrapper[Optional[OutgoingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingGetResponse]], ResultWrapper[OutgoingGetResponse]),
        )


class AsyncOutgoingResource(AsyncAPIResource):
    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOutgoingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOutgoingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutgoingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOutgoingResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingCreateResponse]:
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
                post_parser=ResultWrapper[Optional[OutgoingCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingCreateResponse]], ResultWrapper[OutgoingCreateResponse]),
        )

    async def update(
        self,
        *,
        zone_id: str,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingUpdateResponse]:
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
                post_parser=ResultWrapper[Optional[OutgoingUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingUpdateResponse]], ResultWrapper[OutgoingUpdateResponse]),
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
    ) -> Optional[OutgoingDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[OutgoingDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingDeleteResponse]], ResultWrapper[OutgoingDeleteResponse]),
        )

    async def disable(
        self,
        *,
        zone_id: str,
        body: object,
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
            body=await async_maybe_transform(body, outgoing_disable_params.OutgoingDisableParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DisableTransfer]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def enable(
        self,
        *,
        zone_id: str,
        body: object,
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
            body=await async_maybe_transform(body, outgoing_enable_params.OutgoingEnableParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EnableTransfer]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def force_notify(
        self,
        *,
        zone_id: str,
        body: object,
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
            body=await async_maybe_transform(body, outgoing_force_notify_params.OutgoingForceNotifyParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingForceNotifyResponse]]._unwrapper,
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
    ) -> Optional[OutgoingGetResponse]:
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
                post_parser=ResultWrapper[Optional[OutgoingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingGetResponse]], ResultWrapper[OutgoingGetResponse]),
        )


class OutgoingResourceWithRawResponse:
    def __init__(self, outgoing: OutgoingResource) -> None:
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
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._outgoing.status)


class AsyncOutgoingResourceWithRawResponse:
    def __init__(self, outgoing: AsyncOutgoingResource) -> None:
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
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._outgoing.status)


class OutgoingResourceWithStreamingResponse:
    def __init__(self, outgoing: OutgoingResource) -> None:
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
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._outgoing.status)


class AsyncOutgoingResourceWithStreamingResponse:
    def __init__(self, outgoing: AsyncOutgoingResource) -> None:
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
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._outgoing.status)
