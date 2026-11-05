# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ....pagination import SyncCursorPaginationAfter, AsyncCursorPaginationAfter
from ...._base_client import AsyncPaginator, make_request_options
from ....types.billing.spend_policies import activity_list_params
from ....types.billing.spend_policies.activity_list_response import ActivityListResponse

__all__ = ["ActivityResource", "AsyncActivityResource"]


class ActivityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ActivityResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        period: Literal["current_billing_cycle", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPaginationAfter[ActivityListResponse]:
        """
        Returns configuration history from immutable policy revisions for the account,
        including deleted policies. Entries contain before/after values and verified
        actor attribution. Pages use descending revision IDs, not event or commit order;
        refresh the first page for new entries. This cursor is not an incremental
        consumer checkpoint. Defaults to `period=current_billing_cycle`: each revision's
        timestamp must be within its product's current subscription cycle (inclusive
        start, exclusive end). Each product's cycle is resolved independently from
        canonical aggregates, including for disabled or deleted policies. Set
        `period=all` for history across cycles. Filtering happens before pagination. No
        current cycles returns an empty page; unavailable or disabled cycle resolution
        returns `503` with code `1013`. Cursors pin resolved cycle bounds across pages
        and must be used with the same period selection. Cursors obtained before this
        filter was introduced must be refreshed.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          cursor: Opaque token from the preceding response's result_info.cursor. Pass it unchanged
              to retrieve older entries.

          limit: Maximum number of audit entries to return. Defaults to 50. Values above 100 are
              capped at 100 rather than rejected.

          period: Select current subscription billing-cycle history or history across all cycles.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/billing/spend-policies/activity", account_id=account_id),
            page=SyncCursorPaginationAfter[ActivityListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "period": period,
                    },
                    activity_list_params.ActivityListParams,
                ),
            ),
            model=ActivityListResponse,
        )


class AsyncActivityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncActivityResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        period: Literal["current_billing_cycle", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ActivityListResponse, AsyncCursorPaginationAfter[ActivityListResponse]]:
        """
        Returns configuration history from immutable policy revisions for the account,
        including deleted policies. Entries contain before/after values and verified
        actor attribution. Pages use descending revision IDs, not event or commit order;
        refresh the first page for new entries. This cursor is not an incremental
        consumer checkpoint. Defaults to `period=current_billing_cycle`: each revision's
        timestamp must be within its product's current subscription cycle (inclusive
        start, exclusive end). Each product's cycle is resolved independently from
        canonical aggregates, including for disabled or deleted policies. Set
        `period=all` for history across cycles. Filtering happens before pagination. No
        current cycles returns an empty page; unavailable or disabled cycle resolution
        returns `503` with code `1013`. Cursors pin resolved cycle bounds across pages
        and must be used with the same period selection. Cursors obtained before this
        filter was introduced must be refreshed.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          cursor: Opaque token from the preceding response's result_info.cursor. Pass it unchanged
              to retrieve older entries.

          limit: Maximum number of audit entries to return. Defaults to 50. Values above 100 are
              capped at 100 rather than rejected.

          period: Select current subscription billing-cycle history or history across all cycles.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/billing/spend-policies/activity", account_id=account_id),
            page=AsyncCursorPaginationAfter[ActivityListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "period": period,
                    },
                    activity_list_params.ActivityListParams,
                ),
            ),
            model=ActivityListResponse,
        )


class ActivityResourceWithRawResponse:
    def __init__(self, activity: ActivityResource) -> None:
        self._activity = activity

        self.list = to_raw_response_wrapper(
            activity.list,
        )


class AsyncActivityResourceWithRawResponse:
    def __init__(self, activity: AsyncActivityResource) -> None:
        self._activity = activity

        self.list = async_to_raw_response_wrapper(
            activity.list,
        )


class ActivityResourceWithStreamingResponse:
    def __init__(self, activity: ActivityResource) -> None:
        self._activity = activity

        self.list = to_streamed_response_wrapper(
            activity.list,
        )


class AsyncActivityResourceWithStreamingResponse:
    def __init__(self, activity: AsyncActivityResource) -> None:
        self._activity = activity

        self.list = async_to_streamed_response_wrapper(
            activity.list,
        )
