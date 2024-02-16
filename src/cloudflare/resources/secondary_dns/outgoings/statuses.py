# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from typing import Type

from ....types.secondary_dns.outgoings import StatusSecondaryDNSPrimaryZoneGetOutgoingZoneTransferStatusResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Statuses", "AsyncStatuses"]


class Statuses(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusesWithRawResponse:
        return StatusesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusesWithStreamingResponse:
        return StatusesWithStreamingResponse(self)

    def secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
        self,
        zone_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get primary zone transfer status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/zones/{zone_id}/secondary_dns/outgoing/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncStatuses(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusesWithRawResponse:
        return AsyncStatusesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusesWithStreamingResponse:
        return AsyncStatusesWithStreamingResponse(self)

    async def secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
        self,
        zone_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get primary zone transfer status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/zones/{zone_id}/secondary_dns/outgoing/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class StatusesWithRawResponse:
    def __init__(self, statuses: Statuses) -> None:
        self._statuses = statuses

        self.secondary_dns_primary_zone_get_outgoing_zone_transfer_status = to_raw_response_wrapper(
            statuses.secondary_dns_primary_zone_get_outgoing_zone_transfer_status,
        )


class AsyncStatusesWithRawResponse:
    def __init__(self, statuses: AsyncStatuses) -> None:
        self._statuses = statuses

        self.secondary_dns_primary_zone_get_outgoing_zone_transfer_status = async_to_raw_response_wrapper(
            statuses.secondary_dns_primary_zone_get_outgoing_zone_transfer_status,
        )


class StatusesWithStreamingResponse:
    def __init__(self, statuses: Statuses) -> None:
        self._statuses = statuses

        self.secondary_dns_primary_zone_get_outgoing_zone_transfer_status = to_streamed_response_wrapper(
            statuses.secondary_dns_primary_zone_get_outgoing_zone_transfer_status,
        )


class AsyncStatusesWithStreamingResponse:
    def __init__(self, statuses: AsyncStatuses) -> None:
        self._statuses = statuses

        self.secondary_dns_primary_zone_get_outgoing_zone_transfer_status = async_to_streamed_response_wrapper(
            statuses.secondary_dns_primary_zone_get_outgoing_zone_transfer_status,
        )
