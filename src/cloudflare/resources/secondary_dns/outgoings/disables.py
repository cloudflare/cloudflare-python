# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from typing import Type

from ....types.secondary_dns.outgoings import DisableSecondaryDNSPrimaryZoneDisableOutgoingZoneTransfersResponse

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

__all__ = ["Disables", "AsyncDisables"]


class Disables(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DisablesWithRawResponse:
        return DisablesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DisablesWithStreamingResponse:
        return DisablesWithStreamingResponse(self)

    def secondary_dns_primary_zone_disable_outgoing_zone_transfers(
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
        Disable outgoing zone transfers for primary zone and clears IXFR backlog of
        primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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


class AsyncDisables(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDisablesWithRawResponse:
        return AsyncDisablesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDisablesWithStreamingResponse:
        return AsyncDisablesWithStreamingResponse(self)

    async def secondary_dns_primary_zone_disable_outgoing_zone_transfers(
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
        Disable outgoing zone transfers for primary zone and clears IXFR backlog of
        primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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


class DisablesWithRawResponse:
    def __init__(self, disables: Disables) -> None:
        self._disables = disables

        self.secondary_dns_primary_zone_disable_outgoing_zone_transfers = to_raw_response_wrapper(
            disables.secondary_dns_primary_zone_disable_outgoing_zone_transfers,
        )


class AsyncDisablesWithRawResponse:
    def __init__(self, disables: AsyncDisables) -> None:
        self._disables = disables

        self.secondary_dns_primary_zone_disable_outgoing_zone_transfers = async_to_raw_response_wrapper(
            disables.secondary_dns_primary_zone_disable_outgoing_zone_transfers,
        )


class DisablesWithStreamingResponse:
    def __init__(self, disables: Disables) -> None:
        self._disables = disables

        self.secondary_dns_primary_zone_disable_outgoing_zone_transfers = to_streamed_response_wrapper(
            disables.secondary_dns_primary_zone_disable_outgoing_zone_transfers,
        )


class AsyncDisablesWithStreamingResponse:
    def __init__(self, disables: AsyncDisables) -> None:
        self._disables = disables

        self.secondary_dns_primary_zone_disable_outgoing_zone_transfers = async_to_streamed_response_wrapper(
            disables.secondary_dns_primary_zone_disable_outgoing_zone_transfers,
        )
