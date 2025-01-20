# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.email_security import submission_list_params
from ...types.email_security.submission_list_response import SubmissionListResponse

__all__ = ["SubmissionsResource", "AsyncSubmissionsResource"]


class SubmissionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SubmissionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        submission_id: str | NotGiven = NOT_GIVEN,
        type: Literal["TEAM", "USER"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[SubmissionListResponse]:
        """
        This endpoint returns information for submissions to made to reclassify emails.

        Args:
          account_id: Account Identifier

          end: The end of the search date range. Defaults to `now`.

          page: The page number of paginated results.

          per_page: The number of results per page.

          start: The beginning of the search date range. Defaults to `now - 30 days`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/submissions",
            page=SyncV4PagePaginationArray[SubmissionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "page": page,
                        "per_page": per_page,
                        "start": start,
                        "submission_id": submission_id,
                        "type": type,
                    },
                    submission_list_params.SubmissionListParams,
                ),
            ),
            model=SubmissionListResponse,
        )


class AsyncSubmissionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSubmissionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        submission_id: str | NotGiven = NOT_GIVEN,
        type: Literal["TEAM", "USER"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SubmissionListResponse, AsyncV4PagePaginationArray[SubmissionListResponse]]:
        """
        This endpoint returns information for submissions to made to reclassify emails.

        Args:
          account_id: Account Identifier

          end: The end of the search date range. Defaults to `now`.

          page: The page number of paginated results.

          per_page: The number of results per page.

          start: The beginning of the search date range. Defaults to `now - 30 days`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/submissions",
            page=AsyncV4PagePaginationArray[SubmissionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "page": page,
                        "per_page": per_page,
                        "start": start,
                        "submission_id": submission_id,
                        "type": type,
                    },
                    submission_list_params.SubmissionListParams,
                ),
            ),
            model=SubmissionListResponse,
        )


class SubmissionsResourceWithRawResponse:
    def __init__(self, submissions: SubmissionsResource) -> None:
        self._submissions = submissions

        self.list = to_raw_response_wrapper(
            submissions.list,
        )


class AsyncSubmissionsResourceWithRawResponse:
    def __init__(self, submissions: AsyncSubmissionsResource) -> None:
        self._submissions = submissions

        self.list = async_to_raw_response_wrapper(
            submissions.list,
        )


class SubmissionsResourceWithStreamingResponse:
    def __init__(self, submissions: SubmissionsResource) -> None:
        self._submissions = submissions

        self.list = to_streamed_response_wrapper(
            submissions.list,
        )


class AsyncSubmissionsResourceWithStreamingResponse:
    def __init__(self, submissions: AsyncSubmissionsResource) -> None:
        self._submissions = submissions

        self.list = async_to_streamed_response_wrapper(
            submissions.list,
        )
