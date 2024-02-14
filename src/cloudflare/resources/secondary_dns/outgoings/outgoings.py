# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from .enables import (
    Enables,
    AsyncEnables,
    EnablesWithRawResponse,
    AsyncEnablesWithRawResponse,
    EnablesWithStreamingResponse,
    AsyncEnablesWithStreamingResponse,
)
from .disables import (
    Disables,
    AsyncDisables,
    DisablesWithRawResponse,
    AsyncDisablesWithRawResponse,
    DisablesWithStreamingResponse,
    AsyncDisablesWithStreamingResponse,
)
from .statuses import (
    Statuses,
    AsyncStatuses,
    StatusesWithRawResponse,
    AsyncStatusesWithRawResponse,
    StatusesWithStreamingResponse,
    AsyncStatusesWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from .force_notifies import (
    ForceNotifies,
    AsyncForceNotifies,
    ForceNotifiesWithRawResponse,
    AsyncForceNotifiesWithRawResponse,
    ForceNotifiesWithStreamingResponse,
    AsyncForceNotifiesWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from ....types.secondary_dns import (
    OutgoingDeleteResponse,
    OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationResponse,
    OutgoingSecondaryDNSPrimaryZoneUpdatePrimaryZoneConfigurationResponse,
    OutgoingSecondaryDNSPrimaryZonePrimaryZoneConfigurationDetailsResponse,
    outgoing_secondary_dns_primary_zone_create_primary_zone_configuration_params,
    outgoing_secondary_dns_primary_zone_update_primary_zone_configuration_params,
)

__all__ = ["Outgoings", "AsyncOutgoings"]


class Outgoings(SyncAPIResource):
    @cached_property
    def disables(self) -> Disables:
        return Disables(self._client)

    @cached_property
    def enables(self) -> Enables:
        return Enables(self._client)

    @cached_property
    def force_notifies(self) -> ForceNotifies:
        return ForceNotifies(self._client)

    @cached_property
    def statuses(self) -> Statuses:
        return Statuses(self._client)

    @cached_property
    def with_raw_response(self) -> OutgoingsWithRawResponse:
        return OutgoingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutgoingsWithStreamingResponse:
        return OutgoingsWithStreamingResponse(self)

    def delete(
        self,
        zone_identifier: object,
        *,
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
        return self._delete(
            f"/zones/{zone_identifier}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutgoingDeleteResponse], ResultWrapper[OutgoingDeleteResponse]),
        )

    def secondary_dns_primary_zone_create_primary_zone_configuration(
        self,
        zone_identifier: object,
        *,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationResponse:
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
        return self._post(
            f"/zones/{zone_identifier}/secondary_dns/outgoing",
            body=maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_secondary_dns_primary_zone_create_primary_zone_configuration_params.OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationResponse],
                ResultWrapper[OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationResponse],
            ),
        )

    def secondary_dns_primary_zone_primary_zone_configuration_details(
        self,
        zone_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingSecondaryDNSPrimaryZonePrimaryZoneConfigurationDetailsResponse:
        """
        Get primary zone configuration for outgoing zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/zones/{zone_identifier}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OutgoingSecondaryDNSPrimaryZonePrimaryZoneConfigurationDetailsResponse],
                ResultWrapper[OutgoingSecondaryDNSPrimaryZonePrimaryZoneConfigurationDetailsResponse],
            ),
        )

    def secondary_dns_primary_zone_update_primary_zone_configuration(
        self,
        zone_identifier: object,
        *,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingSecondaryDNSPrimaryZoneUpdatePrimaryZoneConfigurationResponse:
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
        return self._put(
            f"/zones/{zone_identifier}/secondary_dns/outgoing",
            body=maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_secondary_dns_primary_zone_update_primary_zone_configuration_params.OutgoingSecondaryDNSPrimaryZoneUpdatePrimaryZoneConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OutgoingSecondaryDNSPrimaryZoneUpdatePrimaryZoneConfigurationResponse],
                ResultWrapper[OutgoingSecondaryDNSPrimaryZoneUpdatePrimaryZoneConfigurationResponse],
            ),
        )


class AsyncOutgoings(AsyncAPIResource):
    @cached_property
    def disables(self) -> AsyncDisables:
        return AsyncDisables(self._client)

    @cached_property
    def enables(self) -> AsyncEnables:
        return AsyncEnables(self._client)

    @cached_property
    def force_notifies(self) -> AsyncForceNotifies:
        return AsyncForceNotifies(self._client)

    @cached_property
    def statuses(self) -> AsyncStatuses:
        return AsyncStatuses(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOutgoingsWithRawResponse:
        return AsyncOutgoingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutgoingsWithStreamingResponse:
        return AsyncOutgoingsWithStreamingResponse(self)

    async def delete(
        self,
        zone_identifier: object,
        *,
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
        return await self._delete(
            f"/zones/{zone_identifier}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutgoingDeleteResponse], ResultWrapper[OutgoingDeleteResponse]),
        )

    async def secondary_dns_primary_zone_create_primary_zone_configuration(
        self,
        zone_identifier: object,
        *,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationResponse:
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
        return await self._post(
            f"/zones/{zone_identifier}/secondary_dns/outgoing",
            body=maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_secondary_dns_primary_zone_create_primary_zone_configuration_params.OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationResponse],
                ResultWrapper[OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationResponse],
            ),
        )

    async def secondary_dns_primary_zone_primary_zone_configuration_details(
        self,
        zone_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingSecondaryDNSPrimaryZonePrimaryZoneConfigurationDetailsResponse:
        """
        Get primary zone configuration for outgoing zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/zones/{zone_identifier}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OutgoingSecondaryDNSPrimaryZonePrimaryZoneConfigurationDetailsResponse],
                ResultWrapper[OutgoingSecondaryDNSPrimaryZonePrimaryZoneConfigurationDetailsResponse],
            ),
        )

    async def secondary_dns_primary_zone_update_primary_zone_configuration(
        self,
        zone_identifier: object,
        *,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutgoingSecondaryDNSPrimaryZoneUpdatePrimaryZoneConfigurationResponse:
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
        return await self._put(
            f"/zones/{zone_identifier}/secondary_dns/outgoing",
            body=maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_secondary_dns_primary_zone_update_primary_zone_configuration_params.OutgoingSecondaryDNSPrimaryZoneUpdatePrimaryZoneConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OutgoingSecondaryDNSPrimaryZoneUpdatePrimaryZoneConfigurationResponse],
                ResultWrapper[OutgoingSecondaryDNSPrimaryZoneUpdatePrimaryZoneConfigurationResponse],
            ),
        )


class OutgoingsWithRawResponse:
    def __init__(self, outgoings: Outgoings) -> None:
        self._outgoings = outgoings

        self.delete = to_raw_response_wrapper(
            outgoings.delete,
        )
        self.secondary_dns_primary_zone_create_primary_zone_configuration = to_raw_response_wrapper(
            outgoings.secondary_dns_primary_zone_create_primary_zone_configuration,
        )
        self.secondary_dns_primary_zone_primary_zone_configuration_details = to_raw_response_wrapper(
            outgoings.secondary_dns_primary_zone_primary_zone_configuration_details,
        )
        self.secondary_dns_primary_zone_update_primary_zone_configuration = to_raw_response_wrapper(
            outgoings.secondary_dns_primary_zone_update_primary_zone_configuration,
        )

    @cached_property
    def disables(self) -> DisablesWithRawResponse:
        return DisablesWithRawResponse(self._outgoings.disables)

    @cached_property
    def enables(self) -> EnablesWithRawResponse:
        return EnablesWithRawResponse(self._outgoings.enables)

    @cached_property
    def force_notifies(self) -> ForceNotifiesWithRawResponse:
        return ForceNotifiesWithRawResponse(self._outgoings.force_notifies)

    @cached_property
    def statuses(self) -> StatusesWithRawResponse:
        return StatusesWithRawResponse(self._outgoings.statuses)


class AsyncOutgoingsWithRawResponse:
    def __init__(self, outgoings: AsyncOutgoings) -> None:
        self._outgoings = outgoings

        self.delete = async_to_raw_response_wrapper(
            outgoings.delete,
        )
        self.secondary_dns_primary_zone_create_primary_zone_configuration = async_to_raw_response_wrapper(
            outgoings.secondary_dns_primary_zone_create_primary_zone_configuration,
        )
        self.secondary_dns_primary_zone_primary_zone_configuration_details = async_to_raw_response_wrapper(
            outgoings.secondary_dns_primary_zone_primary_zone_configuration_details,
        )
        self.secondary_dns_primary_zone_update_primary_zone_configuration = async_to_raw_response_wrapper(
            outgoings.secondary_dns_primary_zone_update_primary_zone_configuration,
        )

    @cached_property
    def disables(self) -> AsyncDisablesWithRawResponse:
        return AsyncDisablesWithRawResponse(self._outgoings.disables)

    @cached_property
    def enables(self) -> AsyncEnablesWithRawResponse:
        return AsyncEnablesWithRawResponse(self._outgoings.enables)

    @cached_property
    def force_notifies(self) -> AsyncForceNotifiesWithRawResponse:
        return AsyncForceNotifiesWithRawResponse(self._outgoings.force_notifies)

    @cached_property
    def statuses(self) -> AsyncStatusesWithRawResponse:
        return AsyncStatusesWithRawResponse(self._outgoings.statuses)


class OutgoingsWithStreamingResponse:
    def __init__(self, outgoings: Outgoings) -> None:
        self._outgoings = outgoings

        self.delete = to_streamed_response_wrapper(
            outgoings.delete,
        )
        self.secondary_dns_primary_zone_create_primary_zone_configuration = to_streamed_response_wrapper(
            outgoings.secondary_dns_primary_zone_create_primary_zone_configuration,
        )
        self.secondary_dns_primary_zone_primary_zone_configuration_details = to_streamed_response_wrapper(
            outgoings.secondary_dns_primary_zone_primary_zone_configuration_details,
        )
        self.secondary_dns_primary_zone_update_primary_zone_configuration = to_streamed_response_wrapper(
            outgoings.secondary_dns_primary_zone_update_primary_zone_configuration,
        )

    @cached_property
    def disables(self) -> DisablesWithStreamingResponse:
        return DisablesWithStreamingResponse(self._outgoings.disables)

    @cached_property
    def enables(self) -> EnablesWithStreamingResponse:
        return EnablesWithStreamingResponse(self._outgoings.enables)

    @cached_property
    def force_notifies(self) -> ForceNotifiesWithStreamingResponse:
        return ForceNotifiesWithStreamingResponse(self._outgoings.force_notifies)

    @cached_property
    def statuses(self) -> StatusesWithStreamingResponse:
        return StatusesWithStreamingResponse(self._outgoings.statuses)


class AsyncOutgoingsWithStreamingResponse:
    def __init__(self, outgoings: AsyncOutgoings) -> None:
        self._outgoings = outgoings

        self.delete = async_to_streamed_response_wrapper(
            outgoings.delete,
        )
        self.secondary_dns_primary_zone_create_primary_zone_configuration = async_to_streamed_response_wrapper(
            outgoings.secondary_dns_primary_zone_create_primary_zone_configuration,
        )
        self.secondary_dns_primary_zone_primary_zone_configuration_details = async_to_streamed_response_wrapper(
            outgoings.secondary_dns_primary_zone_primary_zone_configuration_details,
        )
        self.secondary_dns_primary_zone_update_primary_zone_configuration = async_to_streamed_response_wrapper(
            outgoings.secondary_dns_primary_zone_update_primary_zone_configuration,
        )

    @cached_property
    def disables(self) -> AsyncDisablesWithStreamingResponse:
        return AsyncDisablesWithStreamingResponse(self._outgoings.disables)

    @cached_property
    def enables(self) -> AsyncEnablesWithStreamingResponse:
        return AsyncEnablesWithStreamingResponse(self._outgoings.enables)

    @cached_property
    def force_notifies(self) -> AsyncForceNotifiesWithStreamingResponse:
        return AsyncForceNotifiesWithStreamingResponse(self._outgoings.force_notifies)

    @cached_property
    def statuses(self) -> AsyncStatusesWithStreamingResponse:
        return AsyncStatusesWithStreamingResponse(self._outgoings.statuses)
