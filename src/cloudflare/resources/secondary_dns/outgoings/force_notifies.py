# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

__all__ = ["ForceNotifies", "AsyncForceNotifies"]


class ForceNotifies(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ForceNotifiesWithRawResponse:
        return ForceNotifiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ForceNotifiesWithStreamingResponse:
        return ForceNotifiesWithStreamingResponse(self)

    def secondary_dns_primary_zone_force_dns_notify(
        self,
        zone_identifier: object,
        *,
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
        return self._post(
            f"/zones/{zone_identifier}/secondary_dns/outgoing/force_notify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncForceNotifies(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncForceNotifiesWithRawResponse:
        return AsyncForceNotifiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncForceNotifiesWithStreamingResponse:
        return AsyncForceNotifiesWithStreamingResponse(self)

    async def secondary_dns_primary_zone_force_dns_notify(
        self,
        zone_identifier: object,
        *,
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
        return await self._post(
            f"/zones/{zone_identifier}/secondary_dns/outgoing/force_notify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class ForceNotifiesWithRawResponse:
    def __init__(self, force_notifies: ForceNotifies) -> None:
        self._force_notifies = force_notifies

        self.secondary_dns_primary_zone_force_dns_notify = to_raw_response_wrapper(
            force_notifies.secondary_dns_primary_zone_force_dns_notify,
        )


class AsyncForceNotifiesWithRawResponse:
    def __init__(self, force_notifies: AsyncForceNotifies) -> None:
        self._force_notifies = force_notifies

        self.secondary_dns_primary_zone_force_dns_notify = async_to_raw_response_wrapper(
            force_notifies.secondary_dns_primary_zone_force_dns_notify,
        )


class ForceNotifiesWithStreamingResponse:
    def __init__(self, force_notifies: ForceNotifies) -> None:
        self._force_notifies = force_notifies

        self.secondary_dns_primary_zone_force_dns_notify = to_streamed_response_wrapper(
            force_notifies.secondary_dns_primary_zone_force_dns_notify,
        )


class AsyncForceNotifiesWithStreamingResponse:
    def __init__(self, force_notifies: AsyncForceNotifies) -> None:
        self._force_notifies = force_notifies

        self.secondary_dns_primary_zone_force_dns_notify = async_to_streamed_response_wrapper(
            force_notifies.secondary_dns_primary_zone_force_dns_notify,
        )
