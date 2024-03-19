# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import AuditLogListResponse, audit_log_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["AuditLogs", "AsyncAuditLogs"]


class AuditLogs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditLogsWithRawResponse:
        return AuditLogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogsWithStreamingResponse:
        return AuditLogsWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: audit_log_list_params.Action | NotGiven = NOT_GIVEN,
        actor: audit_log_list_params.Actor | NotGiven = NOT_GIVEN,
        before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        export: bool | NotGiven = NOT_GIVEN,
        hide_user_logs: bool | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        zone: audit_log_list_params.Zone | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[AuditLogListResponse]:
        """Gets a list of audit logs for an account.

        Can be filtered by who made the
        change, on which zone, and the timeframe of the change.

        Args:
          account_id: Identifier

          id: Finds a specific log by its ID.

          before: Limits the returned results to logs older than the specified date. This can be a
              date string `2019-04-30` or an absolute timestamp that conforms to RFC3339.

          direction: Changes the direction of the chronological sorting.

          export: Indicates that this request is an export of logs in CSV format.

          hide_user_logs: Indicates whether or not to hide user level audit logs.

          page: Defines which page of results to return.

          per_page: Sets the number of results to return per page.

          since: Limits the returned results to logs newer than the specified date. This can be a
              date string `2019-04-30` or an absolute timestamp that conforms to RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/audit_logs",
            page=SyncV4PagePaginationArray[AuditLogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "action": action,
                        "actor": actor,
                        "before": before,
                        "direction": direction,
                        "export": export,
                        "hide_user_logs": hide_user_logs,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "zone": zone,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogListResponse,
        )


class AsyncAuditLogs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditLogsWithRawResponse:
        return AsyncAuditLogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogsWithStreamingResponse:
        return AsyncAuditLogsWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: audit_log_list_params.Action | NotGiven = NOT_GIVEN,
        actor: audit_log_list_params.Actor | NotGiven = NOT_GIVEN,
        before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        export: bool | NotGiven = NOT_GIVEN,
        hide_user_logs: bool | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        zone: audit_log_list_params.Zone | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AuditLogListResponse, AsyncV4PagePaginationArray[AuditLogListResponse]]:
        """Gets a list of audit logs for an account.

        Can be filtered by who made the
        change, on which zone, and the timeframe of the change.

        Args:
          account_id: Identifier

          id: Finds a specific log by its ID.

          before: Limits the returned results to logs older than the specified date. This can be a
              date string `2019-04-30` or an absolute timestamp that conforms to RFC3339.

          direction: Changes the direction of the chronological sorting.

          export: Indicates that this request is an export of logs in CSV format.

          hide_user_logs: Indicates whether or not to hide user level audit logs.

          page: Defines which page of results to return.

          per_page: Sets the number of results to return per page.

          since: Limits the returned results to logs newer than the specified date. This can be a
              date string `2019-04-30` or an absolute timestamp that conforms to RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/audit_logs",
            page=AsyncV4PagePaginationArray[AuditLogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "action": action,
                        "actor": actor,
                        "before": before,
                        "direction": direction,
                        "export": export,
                        "hide_user_logs": hide_user_logs,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "zone": zone,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogListResponse,
        )


class AuditLogsWithRawResponse:
    def __init__(self, audit_logs: AuditLogs) -> None:
        self._audit_logs = audit_logs

        self.list = to_raw_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogs) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_raw_response_wrapper(
            audit_logs.list,
        )


class AuditLogsWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogs) -> None:
        self._audit_logs = audit_logs

        self.list = to_streamed_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogs) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_streamed_response_wrapper(
            audit_logs.list,
        )
