# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePagination, AsyncV4PagePagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.abuse_reports import mitigation_list_params, mitigation_review_params
from ...types.abuse_reports.mitigation_list_response import MitigationListResponse
from ...types.abuse_reports.mitigation_review_response import MitigationReviewResponse

__all__ = ["MitigationsResource", "AsyncMitigationsResource"]


class MitigationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MitigationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MitigationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MitigationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MitigationsResourceWithStreamingResponse(self)

    def list(
        self,
        report_id: str,
        *,
        account_id: str,
        effective_after: str | Omit = omit,
        effective_before: str | Omit = omit,
        entity_type: Literal["url_pattern", "account", "zone"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: Literal[
            "type,asc",
            "type,desc",
            "effective_date,asc",
            "effective_date,desc",
            "status,asc",
            "status,desc",
            "entity_type,asc",
            "entity_type,desc",
        ]
        | Omit = omit,
        status: Literal["pending", "active", "in_review", "cancelled", "removed"] | Omit = omit,
        type: Literal[
            "legal_block",
            "phishing_interstitial",
            "network_block",
            "rate_limit_cache",
            "account_suspend",
            "redirect_video_stream",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePagination[Optional[MitigationListResponse]]:
        """
        List mitigations done to remediate the abuse report.

        Args:
          effective_after: Returns mitigation that were dispatched after the given date

          effective_before: Returns mitigations that were dispatched before the given date

          entity_type: Filter by the type of entity the mitigation impacts.

          page: Where in pagination to start listing abuse reports

          per_page: How many abuse reports per page to list

          sort: A property to sort by, followed by the order

          status: Filter by the status of the mitigation.

          type: Filter by the type of mitigation. This filter parameter can be specified
              multiple times to include multiple types of mitigations in the result set, e.g.
              ?type=rate_limit_cache&type=legal_block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/abuse-reports/{report_id}/mitigations",
            page=SyncV4PagePagination[Optional[MitigationListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "effective_after": effective_after,
                        "effective_before": effective_before,
                        "entity_type": entity_type,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                        "type": type,
                    },
                    mitigation_list_params.MitigationListParams,
                ),
            ),
            model=MitigationListResponse,
        )

    def review(
        self,
        report_id: str,
        *,
        account_id: str,
        appeals: Iterable[mitigation_review_params.Appeal],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[MitigationReviewResponse]:
        """
        Request a review for mitigations on an account.

        Args:
          appeals: List of mitigations to appeal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/abuse-reports/{report_id}/mitigations/appeal",
            page=SyncSinglePage[MitigationReviewResponse],
            body=maybe_transform({"appeals": appeals}, mitigation_review_params.MitigationReviewParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MitigationReviewResponse,
            method="post",
        )


class AsyncMitigationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMitigationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMitigationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMitigationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMitigationsResourceWithStreamingResponse(self)

    def list(
        self,
        report_id: str,
        *,
        account_id: str,
        effective_after: str | Omit = omit,
        effective_before: str | Omit = omit,
        entity_type: Literal["url_pattern", "account", "zone"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: Literal[
            "type,asc",
            "type,desc",
            "effective_date,asc",
            "effective_date,desc",
            "status,asc",
            "status,desc",
            "entity_type,asc",
            "entity_type,desc",
        ]
        | Omit = omit,
        status: Literal["pending", "active", "in_review", "cancelled", "removed"] | Omit = omit,
        type: Literal[
            "legal_block",
            "phishing_interstitial",
            "network_block",
            "rate_limit_cache",
            "account_suspend",
            "redirect_video_stream",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Optional[MitigationListResponse], AsyncV4PagePagination[Optional[MitigationListResponse]]]:
        """
        List mitigations done to remediate the abuse report.

        Args:
          effective_after: Returns mitigation that were dispatched after the given date

          effective_before: Returns mitigations that were dispatched before the given date

          entity_type: Filter by the type of entity the mitigation impacts.

          page: Where in pagination to start listing abuse reports

          per_page: How many abuse reports per page to list

          sort: A property to sort by, followed by the order

          status: Filter by the status of the mitigation.

          type: Filter by the type of mitigation. This filter parameter can be specified
              multiple times to include multiple types of mitigations in the result set, e.g.
              ?type=rate_limit_cache&type=legal_block.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/abuse-reports/{report_id}/mitigations",
            page=AsyncV4PagePagination[Optional[MitigationListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "effective_after": effective_after,
                        "effective_before": effective_before,
                        "entity_type": entity_type,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                        "type": type,
                    },
                    mitigation_list_params.MitigationListParams,
                ),
            ),
            model=MitigationListResponse,
        )

    def review(
        self,
        report_id: str,
        *,
        account_id: str,
        appeals: Iterable[mitigation_review_params.Appeal],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MitigationReviewResponse, AsyncSinglePage[MitigationReviewResponse]]:
        """
        Request a review for mitigations on an account.

        Args:
          appeals: List of mitigations to appeal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/abuse-reports/{report_id}/mitigations/appeal",
            page=AsyncSinglePage[MitigationReviewResponse],
            body=maybe_transform({"appeals": appeals}, mitigation_review_params.MitigationReviewParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MitigationReviewResponse,
            method="post",
        )


class MitigationsResourceWithRawResponse:
    def __init__(self, mitigations: MitigationsResource) -> None:
        self._mitigations = mitigations

        self.list = to_raw_response_wrapper(
            mitigations.list,
        )
        self.review = to_raw_response_wrapper(
            mitigations.review,
        )


class AsyncMitigationsResourceWithRawResponse:
    def __init__(self, mitigations: AsyncMitigationsResource) -> None:
        self._mitigations = mitigations

        self.list = async_to_raw_response_wrapper(
            mitigations.list,
        )
        self.review = async_to_raw_response_wrapper(
            mitigations.review,
        )


class MitigationsResourceWithStreamingResponse:
    def __init__(self, mitigations: MitigationsResource) -> None:
        self._mitigations = mitigations

        self.list = to_streamed_response_wrapper(
            mitigations.list,
        )
        self.review = to_streamed_response_wrapper(
            mitigations.review,
        )


class AsyncMitigationsResourceWithStreamingResponse:
    def __init__(self, mitigations: AsyncMitigationsResource) -> None:
        self._mitigations = mitigations

        self.list = async_to_streamed_response_wrapper(
            mitigations.list,
        )
        self.review = async_to_streamed_response_wrapper(
            mitigations.review,
        )
