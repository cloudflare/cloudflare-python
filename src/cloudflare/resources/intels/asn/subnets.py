# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.intels.asn import SubnetListResponse

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

__all__ = ["Subnets", "AsyncSubnets"]


class Subnets(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubnetsWithRawResponse:
        return SubnetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubnetsWithStreamingResponse:
        return SubnetsWithStreamingResponse(self)

    def list(
        self,
        asn: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubnetListResponse:
        """
        Get ASN Subnets

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
            f"/accounts/{account_id}/intel/asn/{asn}/subnets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubnetListResponse,
        )


class AsyncSubnets(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubnetsWithRawResponse:
        return AsyncSubnetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubnetsWithStreamingResponse:
        return AsyncSubnetsWithStreamingResponse(self)

    async def list(
        self,
        asn: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubnetListResponse:
        """
        Get ASN Subnets

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
            f"/accounts/{account_id}/intel/asn/{asn}/subnets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubnetListResponse,
        )


class SubnetsWithRawResponse:
    def __init__(self, subnets: Subnets) -> None:
        self._subnets = subnets

        self.list = to_raw_response_wrapper(
            subnets.list,
        )


class AsyncSubnetsWithRawResponse:
    def __init__(self, subnets: AsyncSubnets) -> None:
        self._subnets = subnets

        self.list = async_to_raw_response_wrapper(
            subnets.list,
        )


class SubnetsWithStreamingResponse:
    def __init__(self, subnets: Subnets) -> None:
        self._subnets = subnets

        self.list = to_streamed_response_wrapper(
            subnets.list,
        )


class AsyncSubnetsWithStreamingResponse:
    def __init__(self, subnets: AsyncSubnets) -> None:
        self._subnets = subnets

        self.list = async_to_streamed_response_wrapper(
            subnets.list,
        )
