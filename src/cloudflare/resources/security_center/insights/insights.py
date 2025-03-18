# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from .type import (
    TypeResource,
    AsyncTypeResource,
    TypeResourceWithRawResponse,
    AsyncTypeResourceWithRawResponse,
    TypeResourceWithStreamingResponse,
    AsyncTypeResourceWithStreamingResponse,
)
from .class_ import (
    ClassResource,
    AsyncClassResource,
    ClassResourceWithRawResponse,
    AsyncClassResourceWithRawResponse,
    ClassResourceWithStreamingResponse,
    AsyncClassResourceWithStreamingResponse,
)
from .severity import (
    SeverityResource,
    AsyncSeverityResource,
    SeverityResourceWithRawResponse,
    AsyncSeverityResourceWithRawResponse,
    SeverityResourceWithStreamingResponse,
    AsyncSeverityResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncV4PagePagination, AsyncV4PagePagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.security_center import insight_list_params, insight_dismiss_params
from ....types.security_center.insight_list_response import InsightListResponse
from ....types.intel.attack_surface_report.issue_type import IssueType
from ....types.security_center.insight_dismiss_response import InsightDismissResponse
from ....types.intel.attack_surface_report.severity_query_param import SeverityQueryParam

__all__ = ["InsightsResource", "AsyncInsightsResource"]


class InsightsResource(SyncAPIResource):
    @cached_property
    def class_(self) -> ClassResource:
        return ClassResource(self._client)

    @cached_property
    def severity(self) -> SeverityResource:
        return SeverityResource(self._client)

    @cached_property
    def type(self) -> TypeResource:
        return TypeResource(self._client)

    @cached_property
    def with_raw_response(self) -> InsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InsightsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        product: List[str] | NotGiven = NOT_GIVEN,
        product_neq: List[str] | NotGiven = NOT_GIVEN,
        severity: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        severity_neq: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        subject: List[str] | NotGiven = NOT_GIVEN,
        subject_neq: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePagination[Optional[InsightListResponse]]:
        """
        Get Security Center Insights

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          page: Current page within paginated list of results

          per_page: Number of results per page of results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/security-center/insights",
            page=SyncV4PagePagination[Optional[InsightListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dismissed": dismissed,
                        "issue_class": issue_class,
                        "issue_class_neq": issue_class_neq,
                        "issue_type": issue_type,
                        "issue_type_neq": issue_type_neq,
                        "page": page,
                        "per_page": per_page,
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    insight_list_params.InsightListParams,
                ),
            ),
            model=InsightListResponse,
        )

    def dismiss(
        self,
        issue_id: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        dismiss: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightDismissResponse:
        """
        Archive Security Center Insight

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not issue_id:
            raise ValueError(f"Expected a non-empty value for `issue_id` but received {issue_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._put(
            f"/{account_or_zone}/{account_or_zone_id}/security-center/insights/{issue_id}/dismiss",
            body=maybe_transform({"dismiss": dismiss}, insight_dismiss_params.InsightDismissParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightDismissResponse,
        )


class AsyncInsightsResource(AsyncAPIResource):
    @cached_property
    def class_(self) -> AsyncClassResource:
        return AsyncClassResource(self._client)

    @cached_property
    def severity(self) -> AsyncSeverityResource:
        return AsyncSeverityResource(self._client)

    @cached_property
    def type(self) -> AsyncTypeResource:
        return AsyncTypeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInsightsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        product: List[str] | NotGiven = NOT_GIVEN,
        product_neq: List[str] | NotGiven = NOT_GIVEN,
        severity: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        severity_neq: List[SeverityQueryParam] | NotGiven = NOT_GIVEN,
        subject: List[str] | NotGiven = NOT_GIVEN,
        subject_neq: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Optional[InsightListResponse], AsyncV4PagePagination[Optional[InsightListResponse]]]:
        """
        Get Security Center Insights

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          page: Current page within paginated list of results

          per_page: Number of results per page of results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/security-center/insights",
            page=AsyncV4PagePagination[Optional[InsightListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dismissed": dismissed,
                        "issue_class": issue_class,
                        "issue_class_neq": issue_class_neq,
                        "issue_type": issue_type,
                        "issue_type_neq": issue_type_neq,
                        "page": page,
                        "per_page": per_page,
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    insight_list_params.InsightListParams,
                ),
            ),
            model=InsightListResponse,
        )

    async def dismiss(
        self,
        issue_id: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        dismiss: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightDismissResponse:
        """
        Archive Security Center Insight

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not issue_id:
            raise ValueError(f"Expected a non-empty value for `issue_id` but received {issue_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._put(
            f"/{account_or_zone}/{account_or_zone_id}/security-center/insights/{issue_id}/dismiss",
            body=await async_maybe_transform({"dismiss": dismiss}, insight_dismiss_params.InsightDismissParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightDismissResponse,
        )


class InsightsResourceWithRawResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.list = to_raw_response_wrapper(
            insights.list,
        )
        self.dismiss = to_raw_response_wrapper(
            insights.dismiss,
        )

    @cached_property
    def class_(self) -> ClassResourceWithRawResponse:
        return ClassResourceWithRawResponse(self._insights.class_)

    @cached_property
    def severity(self) -> SeverityResourceWithRawResponse:
        return SeverityResourceWithRawResponse(self._insights.severity)

    @cached_property
    def type(self) -> TypeResourceWithRawResponse:
        return TypeResourceWithRawResponse(self._insights.type)


class AsyncInsightsResourceWithRawResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.list = async_to_raw_response_wrapper(
            insights.list,
        )
        self.dismiss = async_to_raw_response_wrapper(
            insights.dismiss,
        )

    @cached_property
    def class_(self) -> AsyncClassResourceWithRawResponse:
        return AsyncClassResourceWithRawResponse(self._insights.class_)

    @cached_property
    def severity(self) -> AsyncSeverityResourceWithRawResponse:
        return AsyncSeverityResourceWithRawResponse(self._insights.severity)

    @cached_property
    def type(self) -> AsyncTypeResourceWithRawResponse:
        return AsyncTypeResourceWithRawResponse(self._insights.type)


class InsightsResourceWithStreamingResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.list = to_streamed_response_wrapper(
            insights.list,
        )
        self.dismiss = to_streamed_response_wrapper(
            insights.dismiss,
        )

    @cached_property
    def class_(self) -> ClassResourceWithStreamingResponse:
        return ClassResourceWithStreamingResponse(self._insights.class_)

    @cached_property
    def severity(self) -> SeverityResourceWithStreamingResponse:
        return SeverityResourceWithStreamingResponse(self._insights.severity)

    @cached_property
    def type(self) -> TypeResourceWithStreamingResponse:
        return TypeResourceWithStreamingResponse(self._insights.type)


class AsyncInsightsResourceWithStreamingResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.list = async_to_streamed_response_wrapper(
            insights.list,
        )
        self.dismiss = async_to_streamed_response_wrapper(
            insights.dismiss,
        )

    @cached_property
    def class_(self) -> AsyncClassResourceWithStreamingResponse:
        return AsyncClassResourceWithStreamingResponse(self._insights.class_)

    @cached_property
    def severity(self) -> AsyncSeverityResourceWithStreamingResponse:
        return AsyncSeverityResourceWithStreamingResponse(self._insights.severity)

    @cached_property
    def type(self) -> AsyncTypeResourceWithStreamingResponse:
        return AsyncTypeResourceWithStreamingResponse(self._insights.type)
