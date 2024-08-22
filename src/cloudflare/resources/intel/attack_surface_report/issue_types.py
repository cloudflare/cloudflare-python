# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.intel.attack_surface_report.issue_type_get_response import IssueTypeGetResponse

__all__ = ["IssueTypesResource", "AsyncIssueTypesResource"]


class IssueTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IssueTypesResourceWithRawResponse:
        return IssueTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IssueTypesResourceWithStreamingResponse:
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
    ) -> Optional[IssueTypeGetResponse]:
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
        return self._get(
            f"/accounts/{account_id}/intel/attack-surface-report/issue-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IssueTypeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IssueTypeGetResponse]], ResultWrapper[IssueTypeGetResponse]),
        )


class AsyncIssueTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIssueTypesResourceWithRawResponse:
        return AsyncIssueTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIssueTypesResourceWithStreamingResponse:
        return AsyncIssueTypesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IssueTypeGetResponse]:
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
        return await self._get(
            f"/accounts/{account_id}/intel/attack-surface-report/issue-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IssueTypeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IssueTypeGetResponse]], ResultWrapper[IssueTypeGetResponse]),
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
