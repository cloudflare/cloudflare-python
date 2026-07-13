# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform
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
from ....types.analytics_query.data_security import content_finding_top_n_params
from ....types.analytics_query.data_security.content_finding_top_n_response import ContentFindingTopNResponse

__all__ = ["ContentFindingsResource", "AsyncContentFindingsResource"]


class ContentFindingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentFindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ContentFindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentFindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ContentFindingsResourceWithStreamingResponse(self)

    def top_n(
        self,
        *,
        account_id: str,
        filters: Iterable[content_finding_top_n_params.Filter],
        from_: Union[str, datetime],
        n: int,
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[ContentFindingTopNResponse]:
        """
        Returns the top N integrations ranked by total content findings.

        Args:
          filters: Filters to apply. `findingType = content` is applied automatically for CASB
              data.

          from_: Start of the query time range (inclusive). RFC3339.

          n: Maximum number of integrations to return.

          to: End of the query time range (exclusive). RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/analytics/query/data-security/content-findings/top-n", account_id=account_id
            ),
            page=SyncSinglePage[ContentFindingTopNResponse],
            body=maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "n": n,
                    "to": to,
                },
                content_finding_top_n_params.ContentFindingTopNParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ContentFindingTopNResponse,
            method="post",
        )


class AsyncContentFindingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentFindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentFindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentFindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncContentFindingsResourceWithStreamingResponse(self)

    def top_n(
        self,
        *,
        account_id: str,
        filters: Iterable[content_finding_top_n_params.Filter],
        from_: Union[str, datetime],
        n: int,
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ContentFindingTopNResponse, AsyncSinglePage[ContentFindingTopNResponse]]:
        """
        Returns the top N integrations ranked by total content findings.

        Args:
          filters: Filters to apply. `findingType = content` is applied automatically for CASB
              data.

          from_: Start of the query time range (inclusive). RFC3339.

          n: Maximum number of integrations to return.

          to: End of the query time range (exclusive). RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/analytics/query/data-security/content-findings/top-n", account_id=account_id
            ),
            page=AsyncSinglePage[ContentFindingTopNResponse],
            body=maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "n": n,
                    "to": to,
                },
                content_finding_top_n_params.ContentFindingTopNParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ContentFindingTopNResponse,
            method="post",
        )


class ContentFindingsResourceWithRawResponse:
    def __init__(self, content_findings: ContentFindingsResource) -> None:
        self._content_findings = content_findings

        self.top_n = to_raw_response_wrapper(
            content_findings.top_n,
        )


class AsyncContentFindingsResourceWithRawResponse:
    def __init__(self, content_findings: AsyncContentFindingsResource) -> None:
        self._content_findings = content_findings

        self.top_n = async_to_raw_response_wrapper(
            content_findings.top_n,
        )


class ContentFindingsResourceWithStreamingResponse:
    def __init__(self, content_findings: ContentFindingsResource) -> None:
        self._content_findings = content_findings

        self.top_n = to_streamed_response_wrapper(
            content_findings.top_n,
        )


class AsyncContentFindingsResourceWithStreamingResponse:
    def __init__(self, content_findings: AsyncContentFindingsResource) -> None:
        self._content_findings = content_findings

        self.top_n = async_to_streamed_response_wrapper(
            content_findings.top_n,
        )
