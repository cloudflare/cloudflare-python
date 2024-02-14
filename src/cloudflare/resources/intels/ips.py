# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.intels import IPIPIntelligenceGetIPOverviewResponse

from typing import Type, Optional

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
from ...types.intels import ip_ip_intelligence_get_ip_overview_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["IPs", "AsyncIPs"]


class IPs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPsWithRawResponse:
        return IPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPsWithStreamingResponse:
        return IPsWithStreamingResponse(self)

    def ip_intelligence_get_ip_overview(
        self,
        account_id: str,
        *,
        ipv4: str | NotGiven = NOT_GIVEN,
        ipv6: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPIPIntelligenceGetIPOverviewResponse]:
        """
        Get IP Overview

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ipv4": ipv4,
                        "ipv6": ipv6,
                    },
                    ip_ip_intelligence_get_ip_overview_params.IPIPIntelligenceGetIPOverviewParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IPIPIntelligenceGetIPOverviewResponse]],
                ResultWrapper[IPIPIntelligenceGetIPOverviewResponse],
            ),
        )


class AsyncIPs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPsWithRawResponse:
        return AsyncIPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPsWithStreamingResponse:
        return AsyncIPsWithStreamingResponse(self)

    async def ip_intelligence_get_ip_overview(
        self,
        account_id: str,
        *,
        ipv4: str | NotGiven = NOT_GIVEN,
        ipv6: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPIPIntelligenceGetIPOverviewResponse]:
        """
        Get IP Overview

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ipv4": ipv4,
                        "ipv6": ipv6,
                    },
                    ip_ip_intelligence_get_ip_overview_params.IPIPIntelligenceGetIPOverviewParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IPIPIntelligenceGetIPOverviewResponse]],
                ResultWrapper[IPIPIntelligenceGetIPOverviewResponse],
            ),
        )


class IPsWithRawResponse:
    def __init__(self, ips: IPs) -> None:
        self._ips = ips

        self.ip_intelligence_get_ip_overview = to_raw_response_wrapper(
            ips.ip_intelligence_get_ip_overview,
        )


class AsyncIPsWithRawResponse:
    def __init__(self, ips: AsyncIPs) -> None:
        self._ips = ips

        self.ip_intelligence_get_ip_overview = async_to_raw_response_wrapper(
            ips.ip_intelligence_get_ip_overview,
        )


class IPsWithStreamingResponse:
    def __init__(self, ips: IPs) -> None:
        self._ips = ips

        self.ip_intelligence_get_ip_overview = to_streamed_response_wrapper(
            ips.ip_intelligence_get_ip_overview,
        )


class AsyncIPsWithStreamingResponse:
    def __init__(self, ips: AsyncIPs) -> None:
        self._ips = ips

        self.ip_intelligence_get_ip_overview = async_to_streamed_response_wrapper(
            ips.ip_intelligence_get_ip_overview,
        )
