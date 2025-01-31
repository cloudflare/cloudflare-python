# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.intel.attack_surface_report.issue_type_get_response import IssueTypeGetResponse

__all__ = ["IssueTypesResource", "AsyncIssueTypesResource"]


class IssueTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IssueTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IssueTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IssueTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IssueTypesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[IssueTypeGetResponse]:
        """
        Get Security Center Issues Types

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/intel/attack-surface-report/issue-types",
            page=SyncSinglePage[IssueTypeGetResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
        )


class AsyncIssueTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIssueTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIssueTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIssueTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIssueTypesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IssueTypeGetResponse, AsyncSinglePage[IssueTypeGetResponse]]:
        """
        Get Security Center Issues Types

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/intel/attack-surface-report/issue-types",
            page=AsyncSinglePage[IssueTypeGetResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
        )


class IssueTypesResourceWithRawResponse:
    def __init__(self, issue_types: IssueTypesResource) -> None:
        self._issue_types = issue_types

        self.get = to_raw_response_wrapper(
            issue_types.get,
        )


class AsyncIssueTypesResourceWithRawResponse:
    def __init__(self, issue_types: AsyncIssueTypesResource) -> None:
        self._issue_types = issue_types

        self.get = async_to_raw_response_wrapper(
            issue_types.get,
        )


class IssueTypesResourceWithStreamingResponse:
    def __init__(self, issue_types: IssueTypesResource) -> None:
        self._issue_types = issue_types

        self.get = to_streamed_response_wrapper(
            issue_types.get,
        )


class AsyncIssueTypesResourceWithStreamingResponse:
    def __init__(self, issue_types: AsyncIssueTypesResource) -> None:
        self._issue_types = issue_types

        self.get = async_to_streamed_response_wrapper(
            issue_types.get,
        )
