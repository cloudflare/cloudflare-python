# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import httpx

from ...._files import read_file_content
from ...._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    BinaryTypes,
    FileContent,
    omit,
    not_given,
)
from ...._utils import path_template
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
from ....types.logs.log_explorer.query_sql_response import QuerySqlResponse

__all__ = ["QueryResource", "AsyncQueryResource"]


class QueryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return QueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return QueryResourceWithStreamingResponse(self)

    def sql(
        self,
        body: FileContent | BinaryTypes,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[QuerySqlResponse]:
        """
        Run a SQL query against account or zone-level datasets.

        Timestamp fields are RFC3339 strings. Filter with: WHERE {timestamp_field} >=
        now() - INTERVAL '30' DAY WHERE {timestamp_field} >= '2026-04-01T00:00:00Z'
        WHERE {timestamp_field} BETWEEN '2026-04-01T00:00:00Z' AND
        '2026-04-30T23:59:59Z'

        Check /account or zones/{account or zone_id}/logs/explorer/datasets to see
        enabled account or zone level datasets. Zone-level datasets will not appear
        here. Check /account or zones/{account or
        zone_id}/logs/explorer/datasets/available for the schemas, and the name of the
        timestamp fields.

        For zone-level datasets use the zone-scoped endpoint: POST
        /zones/{zone_id}/logs/explorer/query/sql

        For more information about the datasets, and the meaning of each field, check
        out https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/

        Args:
          body: SQL query to execute.

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
        extra_headers = {"Content-Type": "text/plain", **(extra_headers or {})}
        return self._get_api_list(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/query/sql",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=SyncSinglePage[QuerySqlResponse],
            content=read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=QuerySqlResponse,
            method="post",
        )


class AsyncQueryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncQueryResourceWithStreamingResponse(self)

    def sql(
        self,
        body: FileContent | BinaryTypes,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[QuerySqlResponse, AsyncSinglePage[QuerySqlResponse]]:
        """
        Run a SQL query against account or zone-level datasets.

        Timestamp fields are RFC3339 strings. Filter with: WHERE {timestamp_field} >=
        now() - INTERVAL '30' DAY WHERE {timestamp_field} >= '2026-04-01T00:00:00Z'
        WHERE {timestamp_field} BETWEEN '2026-04-01T00:00:00Z' AND
        '2026-04-30T23:59:59Z'

        Check /account or zones/{account or zone_id}/logs/explorer/datasets to see
        enabled account or zone level datasets. Zone-level datasets will not appear
        here. Check /account or zones/{account or
        zone_id}/logs/explorer/datasets/available for the schemas, and the name of the
        timestamp fields.

        For zone-level datasets use the zone-scoped endpoint: POST
        /zones/{zone_id}/logs/explorer/query/sql

        For more information about the datasets, and the meaning of each field, check
        out https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/

        Args:
          body: SQL query to execute.

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
        extra_headers = {"Content-Type": "text/plain", **(extra_headers or {})}
        return self._get_api_list(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/query/sql",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=AsyncSinglePage[QuerySqlResponse],
            content=read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=QuerySqlResponse,
            method="post",
        )


class QueryResourceWithRawResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.sql = to_raw_response_wrapper(
            query.sql,
        )


class AsyncQueryResourceWithRawResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.sql = async_to_raw_response_wrapper(
            query.sql,
        )


class QueryResourceWithStreamingResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.sql = to_streamed_response_wrapper(
            query.sql,
        )


class AsyncQueryResourceWithStreamingResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.sql = async_to_streamed_response_wrapper(
            query.sql,
        )
