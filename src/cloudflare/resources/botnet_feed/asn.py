# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.botnet_feed.asn_day_report_response import ASNDayReportResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, Union

from ..._base_client import make_request_options

from datetime import datetime

from ...types.botnet_feed.asn_full_report_response import ASNFullReportResponse

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
from ...types import shared_params
from ...types.botnet_feed import asn_day_report_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ASNResource", "AsyncASNResource"]


class ASNResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ASNResourceWithRawResponse:
        return ASNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ASNResourceWithStreamingResponse:
        return ASNResourceWithStreamingResponse(self)

    def day_report(
        self,
        asn_id: int,
        *,
        account_id: str,
        date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNDayReportResponse]:
        """
        Gets all the data the botnet tracking database has for a given ASN registered to
        user account for given date. If no date is given, it will return results for the
        previous day.

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
            f"/accounts/{account_id}/botnet_feed/asn/{asn_id}/day_report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, asn_day_report_params.ASNDayReportParams),
                post_parser=ResultWrapper[Optional[ASNDayReportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNDayReportResponse]], ResultWrapper[ASNDayReportResponse]),
        )

    def full_report(
        self,
        asn_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNFullReportResponse]:
        """
        Gets all the data the botnet threat feed tracking database has for a given ASN
        registered to user account.

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
            f"/accounts/{account_id}/botnet_feed/asn/{asn_id}/full_report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASNFullReportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNFullReportResponse]], ResultWrapper[ASNFullReportResponse]),
        )


class AsyncASNResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncASNResourceWithRawResponse:
        return AsyncASNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncASNResourceWithStreamingResponse:
        return AsyncASNResourceWithStreamingResponse(self)

    async def day_report(
        self,
        asn_id: int,
        *,
        account_id: str,
        date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNDayReportResponse]:
        """
        Gets all the data the botnet tracking database has for a given ASN registered to
        user account for given date. If no date is given, it will return results for the
        previous day.

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
            f"/accounts/{account_id}/botnet_feed/asn/{asn_id}/day_report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"date": date}, asn_day_report_params.ASNDayReportParams),
                post_parser=ResultWrapper[Optional[ASNDayReportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNDayReportResponse]], ResultWrapper[ASNDayReportResponse]),
        )

    async def full_report(
        self,
        asn_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNFullReportResponse]:
        """
        Gets all the data the botnet threat feed tracking database has for a given ASN
        registered to user account.

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
            f"/accounts/{account_id}/botnet_feed/asn/{asn_id}/full_report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASNFullReportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNFullReportResponse]], ResultWrapper[ASNFullReportResponse]),
        )


class ASNResourceWithRawResponse:
    def __init__(self, asn: ASNResource) -> None:
        self._asn = asn

        self.day_report = to_raw_response_wrapper(
            asn.day_report,
        )
        self.full_report = to_raw_response_wrapper(
            asn.full_report,
        )


class AsyncASNResourceWithRawResponse:
    def __init__(self, asn: AsyncASNResource) -> None:
        self._asn = asn

        self.day_report = async_to_raw_response_wrapper(
            asn.day_report,
        )
        self.full_report = async_to_raw_response_wrapper(
            asn.full_report,
        )


class ASNResourceWithStreamingResponse:
    def __init__(self, asn: ASNResource) -> None:
        self._asn = asn

        self.day_report = to_streamed_response_wrapper(
            asn.day_report,
        )
        self.full_report = to_streamed_response_wrapper(
            asn.full_report,
        )


class AsyncASNResourceWithStreamingResponse:
    def __init__(self, asn: AsyncASNResource) -> None:
        self._asn = asn

        self.day_report = async_to_streamed_response_wrapper(
            asn.day_report,
        )
        self.full_report = async_to_streamed_response_wrapper(
            asn.full_report,
        )
