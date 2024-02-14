# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.intels import WhoisWhoisRecordGetWhoisRecordResponse

from typing import Type

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
from ...types.intels import whois_whois_record_get_whois_record_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Whois", "AsyncWhois"]


class Whois(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WhoisWithRawResponse:
        return WhoisWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhoisWithStreamingResponse:
        return WhoisWithStreamingResponse(self)

    def whois_record_get_whois_record(
        self,
        account_id: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WhoisWhoisRecordGetWhoisRecordResponse:
        """
        Get WHOIS Record

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
            f"/accounts/{account_id}/intel/whois",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"domain": domain}, whois_whois_record_get_whois_record_params.WhoisWhoisRecordGetWhoisRecordParams
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[WhoisWhoisRecordGetWhoisRecordResponse], ResultWrapper[WhoisWhoisRecordGetWhoisRecordResponse]
            ),
        )


class AsyncWhois(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWhoisWithRawResponse:
        return AsyncWhoisWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhoisWithStreamingResponse:
        return AsyncWhoisWithStreamingResponse(self)

    async def whois_record_get_whois_record(
        self,
        account_id: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WhoisWhoisRecordGetWhoisRecordResponse:
        """
        Get WHOIS Record

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
            f"/accounts/{account_id}/intel/whois",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"domain": domain}, whois_whois_record_get_whois_record_params.WhoisWhoisRecordGetWhoisRecordParams
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[WhoisWhoisRecordGetWhoisRecordResponse], ResultWrapper[WhoisWhoisRecordGetWhoisRecordResponse]
            ),
        )


class WhoisWithRawResponse:
    def __init__(self, whois: Whois) -> None:
        self._whois = whois

        self.whois_record_get_whois_record = to_raw_response_wrapper(
            whois.whois_record_get_whois_record,
        )


class AsyncWhoisWithRawResponse:
    def __init__(self, whois: AsyncWhois) -> None:
        self._whois = whois

        self.whois_record_get_whois_record = async_to_raw_response_wrapper(
            whois.whois_record_get_whois_record,
        )


class WhoisWithStreamingResponse:
    def __init__(self, whois: Whois) -> None:
        self._whois = whois

        self.whois_record_get_whois_record = to_streamed_response_wrapper(
            whois.whois_record_get_whois_record,
        )


class AsyncWhoisWithStreamingResponse:
    def __init__(self, whois: AsyncWhois) -> None:
        self._whois = whois

        self.whois_record_get_whois_record = async_to_streamed_response_wrapper(
            whois.whois_record_get_whois_record,
        )
