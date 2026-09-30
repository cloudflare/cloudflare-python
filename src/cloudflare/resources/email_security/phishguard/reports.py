# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.email_security.phishguard import report_list_params
from ....types.email_security.phishguard.report_list_response import ReportListResponse

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ReportsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        end: Union[str, datetime] | Omit = omit,
        from_date: Union[str, date] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        to_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ReportListResponse]:
        """Retrieves PhishGuard security alert reports for a specified date range.

        Reports
        include detected threats, dispositions, and contextual information. Use for
        security monitoring and threat analysis.

        Args:
          account_id: Identifier.

          end: End of the time range (RFC3339). Takes precedence over to_date.

          from_date: Deprecated, use `start` instead. Start date in YYYY-MM-DD format.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          start: Start of the time range (RFC3339). Takes precedence over from_date.

          to_date: Deprecated, use `end` instead. End date in YYYY-MM-DD format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/phishguard/reports", account_id=account_id),
            page=SyncV4PagePaginationArray[ReportListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "from_date": from_date,
                        "page": page,
                        "per_page": per_page,
                        "start": start,
                        "to_date": to_date,
                    },
                    report_list_params.ReportListParams,
                ),
            ),
            model=ReportListResponse,
        )


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncReportsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        end: Union[str, datetime] | Omit = omit,
        from_date: Union[str, date] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        to_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ReportListResponse, AsyncV4PagePaginationArray[ReportListResponse]]:
        """Retrieves PhishGuard security alert reports for a specified date range.

        Reports
        include detected threats, dispositions, and contextual information. Use for
        security monitoring and threat analysis.

        Args:
          account_id: Identifier.

          end: End of the time range (RFC3339). Takes precedence over to_date.

          from_date: Deprecated, use `start` instead. Start date in YYYY-MM-DD format.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          start: Start of the time range (RFC3339). Takes precedence over from_date.

          to_date: Deprecated, use `end` instead. End date in YYYY-MM-DD format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/phishguard/reports", account_id=account_id),
            page=AsyncV4PagePaginationArray[ReportListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "from_date": from_date,
                        "page": page,
                        "per_page": per_page,
                        "start": start,
                        "to_date": to_date,
                    },
                    report_list_params.ReportListParams,
                ),
            ),
            model=ReportListResponse,
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.list = to_raw_response_wrapper(
            reports.list,
        )


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.list = async_to_raw_response_wrapper(
            reports.list,
        )


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.list = to_streamed_response_wrapper(
            reports.list,
        )


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.list = async_to_streamed_response_wrapper(
            reports.list,
        )
