# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

import httpx

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
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.security_center.insights import severity_get_params
from ....types.intel.attack_surface_report.issue_type import IssueType
from ....types.security_center.insights.severity_get_response import SeverityGetResponse
from ....types.intel.attack_surface_report.severity_query_param import SeverityQueryParam

__all__ = ["SeverityResource", "AsyncSeverityResource"]


class SeverityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SeverityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SeverityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeverityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SeverityResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
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
    ) -> Optional[SeverityGetResponse]:
        """
        Get Security Center Insight Counts by Severity

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/security-center/insights/severity",
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
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    severity_get_params.SeverityGetParams,
                ),
                post_parser=ResultWrapper[Optional[SeverityGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SeverityGetResponse]], ResultWrapper[SeverityGetResponse]),
        )


class AsyncSeverityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSeverityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSeverityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeverityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSeverityResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        dismissed: bool | NotGiven = NOT_GIVEN,
        issue_class: List[str] | NotGiven = NOT_GIVEN,
        issue_class_neq: List[str] | NotGiven = NOT_GIVEN,
        issue_type: List[IssueType] | NotGiven = NOT_GIVEN,
        issue_type_neq: List[IssueType] | NotGiven = NOT_GIVEN,
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
    ) -> Optional[SeverityGetResponse]:
        """
        Get Security Center Insight Counts by Severity

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/security-center/insights/severity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dismissed": dismissed,
                        "issue_class": issue_class,
                        "issue_class_neq": issue_class_neq,
                        "issue_type": issue_type,
                        "issue_type_neq": issue_type_neq,
                        "product": product,
                        "product_neq": product_neq,
                        "severity": severity,
                        "severity_neq": severity_neq,
                        "subject": subject,
                        "subject_neq": subject_neq,
                    },
                    severity_get_params.SeverityGetParams,
                ),
                post_parser=ResultWrapper[Optional[SeverityGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SeverityGetResponse]], ResultWrapper[SeverityGetResponse]),
        )


class SeverityResourceWithRawResponse:
    def __init__(self, severity: SeverityResource) -> None:
        self._severity = severity

        self.get = to_raw_response_wrapper(
            severity.get,
        )


class AsyncSeverityResourceWithRawResponse:
    def __init__(self, severity: AsyncSeverityResource) -> None:
        self._severity = severity

        self.get = async_to_raw_response_wrapper(
            severity.get,
        )


class SeverityResourceWithStreamingResponse:
    def __init__(self, severity: SeverityResource) -> None:
        self._severity = severity

        self.get = to_streamed_response_wrapper(
            severity.get,
        )


class AsyncSeverityResourceWithStreamingResponse:
    def __init__(self, severity: AsyncSeverityResource) -> None:
        self._severity = severity

        self.get = async_to_streamed_response_wrapper(
            severity.get,
        )
