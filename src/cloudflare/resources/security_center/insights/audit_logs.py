# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
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
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.security_center.insights import audit_log_list_params, audit_log_list_by_insight_params
from ....types.security_center.insights.audit_log_list_response import AuditLogListResponse
from ....types.security_center.insights.audit_log_list_by_insight_response import AuditLogListByInsightResponse

__all__ = ["AuditLogsResource", "AsyncAuditLogsResource"]


class AuditLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        before: Union[str, datetime] | Omit = omit,
        changed_by: str | Omit = omit,
        cursor: str | Omit = omit,
        field_changed: Literal["status", "user_classification"] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        per_page: int | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[AuditLogListResponse]:
        """
        Lists audit log entries for all Security Center insights in the account or zone,
        showing changes to insight status and classification.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          before: Filter entries changed before this timestamp (RFC 3339).

          changed_by: Filter by the actor that made the change.

          cursor: Opaque cursor for pagination. Use the cursor value from result_info of the
              previous response.

          field_changed: Filter by the field that was changed.

          order: Sort order for results. Use 'asc' for oldest first or 'desc' for newest first.

          per_page: Number of results per page.

          since: Filter entries changed at or after this timestamp (RFC 3339).

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
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/security-center/insights/audit-log",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=SyncCursorPagination[AuditLogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "changed_by": changed_by,
                        "cursor": cursor,
                        "field_changed": field_changed,
                        "order": order,
                        "per_page": per_page,
                        "since": since,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogListResponse,
        )

    def list_by_insight(
        self,
        issue_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        before: Union[str, datetime] | Omit = omit,
        changed_by: str | Omit = omit,
        cursor: str | Omit = omit,
        field_changed: Literal["status", "user_classification"] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        per_page: int | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[AuditLogListByInsightResponse]:
        """
        Lists audit log entries for a specific Security Center insight, showing changes
        to its status and classification over time.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          before: Filter entries changed before this timestamp (RFC 3339).

          changed_by: Filter by the actor that made the change.

          cursor: Opaque cursor for pagination. Use the cursor value from result_info of the
              previous response.

          field_changed: Filter by the field that was changed.

          order: Sort order for results. Use 'asc' for oldest first or 'desc' for newest first.

          per_page: Number of results per page.

          since: Filter entries changed at or after this timestamp (RFC 3339).

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
        return self._get_api_list(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/security-center/insights/{issue_id}/audit-log",
                issue_id=issue_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=SyncCursorPagination[AuditLogListByInsightResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "changed_by": changed_by,
                        "cursor": cursor,
                        "field_changed": field_changed,
                        "order": order,
                        "per_page": per_page,
                        "since": since,
                    },
                    audit_log_list_by_insight_params.AuditLogListByInsightParams,
                ),
            ),
            model=AuditLogListByInsightResponse,
        )


class AsyncAuditLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        before: Union[str, datetime] | Omit = omit,
        changed_by: str | Omit = omit,
        cursor: str | Omit = omit,
        field_changed: Literal["status", "user_classification"] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        per_page: int | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuditLogListResponse, AsyncCursorPagination[AuditLogListResponse]]:
        """
        Lists audit log entries for all Security Center insights in the account or zone,
        showing changes to insight status and classification.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          before: Filter entries changed before this timestamp (RFC 3339).

          changed_by: Filter by the actor that made the change.

          cursor: Opaque cursor for pagination. Use the cursor value from result_info of the
              previous response.

          field_changed: Filter by the field that was changed.

          order: Sort order for results. Use 'asc' for oldest first or 'desc' for newest first.

          per_page: Number of results per page.

          since: Filter entries changed at or after this timestamp (RFC 3339).

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
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/security-center/insights/audit-log",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=AsyncCursorPagination[AuditLogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "changed_by": changed_by,
                        "cursor": cursor,
                        "field_changed": field_changed,
                        "order": order,
                        "per_page": per_page,
                        "since": since,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogListResponse,
        )

    def list_by_insight(
        self,
        issue_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        before: Union[str, datetime] | Omit = omit,
        changed_by: str | Omit = omit,
        cursor: str | Omit = omit,
        field_changed: Literal["status", "user_classification"] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        per_page: int | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuditLogListByInsightResponse, AsyncCursorPagination[AuditLogListByInsightResponse]]:
        """
        Lists audit log entries for a specific Security Center insight, showing changes
        to its status and classification over time.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          before: Filter entries changed before this timestamp (RFC 3339).

          changed_by: Filter by the actor that made the change.

          cursor: Opaque cursor for pagination. Use the cursor value from result_info of the
              previous response.

          field_changed: Filter by the field that was changed.

          order: Sort order for results. Use 'asc' for oldest first or 'desc' for newest first.

          per_page: Number of results per page.

          since: Filter entries changed at or after this timestamp (RFC 3339).

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
        return self._get_api_list(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/security-center/insights/{issue_id}/audit-log",
                issue_id=issue_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=AsyncCursorPagination[AuditLogListByInsightResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "changed_by": changed_by,
                        "cursor": cursor,
                        "field_changed": field_changed,
                        "order": order,
                        "per_page": per_page,
                        "since": since,
                    },
                    audit_log_list_by_insight_params.AuditLogListByInsightParams,
                ),
            ),
            model=AuditLogListByInsightResponse,
        )


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_raw_response_wrapper(
            audit_logs.list,
        )
        self.list_by_insight = to_raw_response_wrapper(
            audit_logs.list_by_insight,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_raw_response_wrapper(
            audit_logs.list,
        )
        self.list_by_insight = async_to_raw_response_wrapper(
            audit_logs.list_by_insight,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_streamed_response_wrapper(
            audit_logs.list,
        )
        self.list_by_insight = to_streamed_response_wrapper(
            audit_logs.list_by_insight,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_streamed_response_wrapper(
            audit_logs.list,
        )
        self.list_by_insight = async_to_streamed_response_wrapper(
            audit_logs.list_by_insight,
        )
