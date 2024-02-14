# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from typing import Type

from ...types.secondary_dns import ForceAxfrSecondaryDNSSecondaryZoneForceAxfrResponse

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["ForceAxfrs", "AsyncForceAxfrs"]


class ForceAxfrs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ForceAxfrsWithRawResponse:
        return ForceAxfrsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ForceAxfrsWithStreamingResponse:
        return ForceAxfrsWithStreamingResponse(self)

    def secondary_dns_secondary_zone_force_axfr(
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
        Sends AXFR zone transfer request to primary nameserver(s).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/zones/{zone_identifier}/secondary_dns/force_axfr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncForceAxfrs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncForceAxfrsWithRawResponse:
        return AsyncForceAxfrsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncForceAxfrsWithStreamingResponse:
        return AsyncForceAxfrsWithStreamingResponse(self)

    async def secondary_dns_secondary_zone_force_axfr(
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
        Sends AXFR zone transfer request to primary nameserver(s).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/zones/{zone_identifier}/secondary_dns/force_axfr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class ForceAxfrsWithRawResponse:
    def __init__(self, force_axfrs: ForceAxfrs) -> None:
        self._force_axfrs = force_axfrs

        self.secondary_dns_secondary_zone_force_axfr = to_raw_response_wrapper(
            force_axfrs.secondary_dns_secondary_zone_force_axfr,
        )


class AsyncForceAxfrsWithRawResponse:
    def __init__(self, force_axfrs: AsyncForceAxfrs) -> None:
        self._force_axfrs = force_axfrs

        self.secondary_dns_secondary_zone_force_axfr = async_to_raw_response_wrapper(
            force_axfrs.secondary_dns_secondary_zone_force_axfr,
        )


class ForceAxfrsWithStreamingResponse:
    def __init__(self, force_axfrs: ForceAxfrs) -> None:
        self._force_axfrs = force_axfrs

        self.secondary_dns_secondary_zone_force_axfr = to_streamed_response_wrapper(
            force_axfrs.secondary_dns_secondary_zone_force_axfr,
        )


class AsyncForceAxfrsWithStreamingResponse:
    def __init__(self, force_axfrs: AsyncForceAxfrs) -> None:
        self._force_axfrs = force_axfrs

        self.secondary_dns_secondary_zone_force_axfr = async_to_streamed_response_wrapper(
            force_axfrs.secondary_dns_secondary_zone_force_axfr,
        )
