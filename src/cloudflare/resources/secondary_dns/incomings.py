# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
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
    IncomingDeleteResponse,
    IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse,
    IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse,
    IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse,
    incoming_secondary_dns_secondary_zone_create_secondary_zone_configuration_params,
    incoming_secondary_dns_secondary_zone_update_secondary_zone_configuration_params,
)

__all__ = ["Incomings", "AsyncIncomings"]


class Incomings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IncomingsWithRawResponse:
        return IncomingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncomingsWithStreamingResponse:
        return IncomingsWithStreamingResponse(self)

    def delete(
        self,
        zone_id: object,
        *,
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

    def secondary_dns_secondary_zone_create_secondary_zone_configuration(
        self,
        zone_id: object,
        *,
        auto_refresh_seconds: float,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse:
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
                incoming_secondary_dns_secondary_zone_create_secondary_zone_configuration_params.IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse],
                ResultWrapper[IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse],
            ),
        )

    def secondary_dns_secondary_zone_secondary_zone_configuration_details(
        self,
        zone_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse:
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
            cast_to=cast(
                Type[IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse],
                ResultWrapper[IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse],
            ),
        )

    def secondary_dns_secondary_zone_update_secondary_zone_configuration(
        self,
        zone_id: object,
        *,
        auto_refresh_seconds: float,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse:
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
                incoming_secondary_dns_secondary_zone_update_secondary_zone_configuration_params.IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse],
                ResultWrapper[IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse],
            ),
        )


class AsyncIncomings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIncomingsWithRawResponse:
        return AsyncIncomingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncomingsWithStreamingResponse:
        return AsyncIncomingsWithStreamingResponse(self)

    async def delete(
        self,
        zone_id: object,
        *,
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

    async def secondary_dns_secondary_zone_create_secondary_zone_configuration(
        self,
        zone_id: object,
        *,
        auto_refresh_seconds: float,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse:
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
            body=maybe_transform(
                {
                    "auto_refresh_seconds": auto_refresh_seconds,
                    "name": name,
                    "peers": peers,
                },
                incoming_secondary_dns_secondary_zone_create_secondary_zone_configuration_params.IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse],
                ResultWrapper[IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse],
            ),
        )

    async def secondary_dns_secondary_zone_secondary_zone_configuration_details(
        self,
        zone_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse:
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
            cast_to=cast(
                Type[IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse],
                ResultWrapper[IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse],
            ),
        )

    async def secondary_dns_secondary_zone_update_secondary_zone_configuration(
        self,
        zone_id: object,
        *,
        auto_refresh_seconds: float,
        name: str,
        peers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse:
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
            body=maybe_transform(
                {
                    "auto_refresh_seconds": auto_refresh_seconds,
                    "name": name,
                    "peers": peers,
                },
                incoming_secondary_dns_secondary_zone_update_secondary_zone_configuration_params.IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse],
                ResultWrapper[IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse],
            ),
        )


class IncomingsWithRawResponse:
    def __init__(self, incomings: Incomings) -> None:
        self._incomings = incomings

        self.delete = to_raw_response_wrapper(
            incomings.delete,
        )
        self.secondary_dns_secondary_zone_create_secondary_zone_configuration = to_raw_response_wrapper(
            incomings.secondary_dns_secondary_zone_create_secondary_zone_configuration,
        )
        self.secondary_dns_secondary_zone_secondary_zone_configuration_details = to_raw_response_wrapper(
            incomings.secondary_dns_secondary_zone_secondary_zone_configuration_details,
        )
        self.secondary_dns_secondary_zone_update_secondary_zone_configuration = to_raw_response_wrapper(
            incomings.secondary_dns_secondary_zone_update_secondary_zone_configuration,
        )


class AsyncIncomingsWithRawResponse:
    def __init__(self, incomings: AsyncIncomings) -> None:
        self._incomings = incomings

        self.delete = async_to_raw_response_wrapper(
            incomings.delete,
        )
        self.secondary_dns_secondary_zone_create_secondary_zone_configuration = async_to_raw_response_wrapper(
            incomings.secondary_dns_secondary_zone_create_secondary_zone_configuration,
        )
        self.secondary_dns_secondary_zone_secondary_zone_configuration_details = async_to_raw_response_wrapper(
            incomings.secondary_dns_secondary_zone_secondary_zone_configuration_details,
        )
        self.secondary_dns_secondary_zone_update_secondary_zone_configuration = async_to_raw_response_wrapper(
            incomings.secondary_dns_secondary_zone_update_secondary_zone_configuration,
        )


class IncomingsWithStreamingResponse:
    def __init__(self, incomings: Incomings) -> None:
        self._incomings = incomings

        self.delete = to_streamed_response_wrapper(
            incomings.delete,
        )
        self.secondary_dns_secondary_zone_create_secondary_zone_configuration = to_streamed_response_wrapper(
            incomings.secondary_dns_secondary_zone_create_secondary_zone_configuration,
        )
        self.secondary_dns_secondary_zone_secondary_zone_configuration_details = to_streamed_response_wrapper(
            incomings.secondary_dns_secondary_zone_secondary_zone_configuration_details,
        )
        self.secondary_dns_secondary_zone_update_secondary_zone_configuration = to_streamed_response_wrapper(
            incomings.secondary_dns_secondary_zone_update_secondary_zone_configuration,
        )


class AsyncIncomingsWithStreamingResponse:
    def __init__(self, incomings: AsyncIncomings) -> None:
        self._incomings = incomings

        self.delete = async_to_streamed_response_wrapper(
            incomings.delete,
        )
        self.secondary_dns_secondary_zone_create_secondary_zone_configuration = async_to_streamed_response_wrapper(
            incomings.secondary_dns_secondary_zone_create_secondary_zone_configuration,
        )
        self.secondary_dns_secondary_zone_secondary_zone_configuration_details = async_to_streamed_response_wrapper(
            incomings.secondary_dns_secondary_zone_secondary_zone_configuration_details,
        )
        self.secondary_dns_secondary_zone_update_secondary_zone_configuration = async_to_streamed_response_wrapper(
            incomings.secondary_dns_secondary_zone_update_secondary_zone_configuration,
        )
