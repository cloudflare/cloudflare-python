# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ...types.d1 import (
    database_raw_params,
    database_list_params,
    database_query_params,
    database_create_params,
    database_export_params,
    database_import_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...types.d1.d1 import D1
from ..._base_client import AsyncPaginator, make_request_options
from ...types.d1.query_result import QueryResult
from ...types.d1.database_raw_response import DatabaseRawResponse
from ...types.d1.database_list_response import DatabaseListResponse
from ...types.d1.database_export_response import DatabaseExportResponse
from ...types.d1.database_import_response import DatabaseImportResponse

__all__ = ["DatabaseResource", "AsyncDatabaseResource"]


class DatabaseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatabaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DatabaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DatabaseResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        primary_location_hint: Literal["wnam", "enam", "weur", "eeur", "apac", "oc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> D1:
        """
        Returns the created D1 database.

        Args:
          account_id: Account identifier tag.

          name: D1 database name.

          primary_location_hint: Specify the region to create the D1 primary, if available. If this option is
              omitted, the D1 will be created as close as possible to the current user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/d1/database",
            body=maybe_transform(
                {
                    "name": name,
                    "primary_location_hint": primary_location_hint,
                },
                database_create_params.DatabaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[D1]._unwrapper,
            ),
            cast_to=cast(Type[D1], ResultWrapper[D1]),
        )

    def list(
        self,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[DatabaseListResponse]:
        """
        Returns a list of D1 databases.

        Args:
          account_id: Account identifier tag.

          name: a database name to search for.

          page: Page number of paginated results.

          per_page: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/d1/database",
            page=SyncV4PagePaginationArray[DatabaseListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    database_list_params.DatabaseListParams,
                ),
            ),
            model=DatabaseListResponse,
        )

    def delete(
        self,
        database_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes the specified D1 database.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return self._delete(
            f"/accounts/{account_id}/d1/database/{database_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def export(
        self,
        database_id: str,
        *,
        account_id: str,
        output_format: Literal["polling"],
        current_bookmark: str | NotGiven = NOT_GIVEN,
        dump_options: database_export_params.DumpOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseExportResponse:
        """Returns a URL where the SQL contents of your D1 can be downloaded.

        Note: this
        process may take some time for larger DBs, during which your D1 will be
        unavailable to serve queries. To avoid blocking your DB unnecessarily, an
        in-progress export must be continually polled or will automatically cancel.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          output_format: Specifies that you will poll this endpoint until the export completes

          current_bookmark: To poll an in-progress export, provide the current bookmark (returned by your
              first polling response)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return self._post(
            f"/accounts/{account_id}/d1/database/{database_id}/export",
            body=maybe_transform(
                {
                    "output_format": output_format,
                    "current_bookmark": current_bookmark,
                    "dump_options": dump_options,
                },
                database_export_params.DatabaseExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DatabaseExportResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatabaseExportResponse], ResultWrapper[DatabaseExportResponse]),
        )

    def get(
        self,
        database_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> D1:
        """
        Returns the specified D1 database.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return self._get(
            f"/accounts/{account_id}/d1/database/{database_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[D1]._unwrapper,
            ),
            cast_to=cast(Type[D1], ResultWrapper[D1]),
        )

    @overload
    def import_(
        self,
        database_id: str,
        *,
        account_id: str,
        action: Literal["init"],
        etag: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseImportResponse:
        """
        Generates a temporary URL for uploading an SQL file to, then instructing the D1
        to import it and polling it for status updates. Imports block the D1 for their
        duration.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          action: Indicates you have a new SQL file to upload.

          etag: Required when action is 'init' or 'ingest'. An md5 hash of the file you're
              uploading. Used to check if it already exists, and validate its contents before
              ingesting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def import_(
        self,
        database_id: str,
        *,
        account_id: str,
        action: Literal["ingest"],
        etag: str,
        filename: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseImportResponse:
        """
        Generates a temporary URL for uploading an SQL file to, then instructing the D1
        to import it and polling it for status updates. Imports block the D1 for their
        duration.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          action: Indicates you've finished uploading to tell the D1 to start consuming it

          etag: An md5 hash of the file you're uploading. Used to check if it already exists,
              and validate its contents before ingesting.

          filename: The filename you have successfully uploaded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def import_(
        self,
        database_id: str,
        *,
        account_id: str,
        action: Literal["poll"],
        current_bookmark: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseImportResponse:
        """
        Generates a temporary URL for uploading an SQL file to, then instructing the D1
        to import it and polling it for status updates. Imports block the D1 for their
        duration.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          action: Indicates you've finished uploading to tell the D1 to start consuming it

          current_bookmark: This identifies the currently-running import, checking its status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "action", "etag"],
        ["account_id", "action", "etag", "filename"],
        ["account_id", "action", "current_bookmark"],
    )
    def import_(
        self,
        database_id: str,
        *,
        account_id: str,
        action: Literal["init"] | Literal["ingest"] | Literal["poll"],
        etag: str | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        current_bookmark: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseImportResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return self._post(
            f"/accounts/{account_id}/d1/database/{database_id}/import",
            body=maybe_transform(
                {
                    "action": action,
                    "etag": etag,
                    "filename": filename,
                    "current_bookmark": current_bookmark,
                },
                database_import_params.DatabaseImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DatabaseImportResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatabaseImportResponse], ResultWrapper[DatabaseImportResponse]),
        )

    def query(
        self,
        database_id: str,
        *,
        account_id: str,
        sql: str,
        params: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[QueryResult]:
        """
        Returns the query result as an object.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          sql: Your SQL query. Supports multiple statements, joined by semicolons, which will
              be executed as a batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/d1/database/{database_id}/query",
            page=SyncSinglePage[QueryResult],
            body=maybe_transform(
                {
                    "sql": sql,
                    "params": params,
                },
                database_query_params.DatabaseQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=QueryResult,
            method="post",
        )

    def raw(
        self,
        database_id: str,
        *,
        account_id: str,
        sql: str,
        params: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[DatabaseRawResponse]:
        """Returns the query result rows as arrays rather than objects.

        This is a
        performance-optimized version of the /query endpoint.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          sql: Your SQL query. Supports multiple statements, joined by semicolons, which will
              be executed as a batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/d1/database/{database_id}/raw",
            page=SyncSinglePage[DatabaseRawResponse],
            body=maybe_transform(
                {
                    "sql": sql,
                    "params": params,
                },
                database_raw_params.DatabaseRawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DatabaseRawResponse,
            method="post",
        )


class AsyncDatabaseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatabaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatabaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDatabaseResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        primary_location_hint: Literal["wnam", "enam", "weur", "eeur", "apac", "oc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> D1:
        """
        Returns the created D1 database.

        Args:
          account_id: Account identifier tag.

          name: D1 database name.

          primary_location_hint: Specify the region to create the D1 primary, if available. If this option is
              omitted, the D1 will be created as close as possible to the current user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/d1/database",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "primary_location_hint": primary_location_hint,
                },
                database_create_params.DatabaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[D1]._unwrapper,
            ),
            cast_to=cast(Type[D1], ResultWrapper[D1]),
        )

    def list(
        self,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DatabaseListResponse, AsyncV4PagePaginationArray[DatabaseListResponse]]:
        """
        Returns a list of D1 databases.

        Args:
          account_id: Account identifier tag.

          name: a database name to search for.

          page: Page number of paginated results.

          per_page: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/d1/database",
            page=AsyncV4PagePaginationArray[DatabaseListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    database_list_params.DatabaseListParams,
                ),
            ),
            model=DatabaseListResponse,
        )

    async def delete(
        self,
        database_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes the specified D1 database.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/d1/database/{database_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def export(
        self,
        database_id: str,
        *,
        account_id: str,
        output_format: Literal["polling"],
        current_bookmark: str | NotGiven = NOT_GIVEN,
        dump_options: database_export_params.DumpOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseExportResponse:
        """Returns a URL where the SQL contents of your D1 can be downloaded.

        Note: this
        process may take some time for larger DBs, during which your D1 will be
        unavailable to serve queries. To avoid blocking your DB unnecessarily, an
        in-progress export must be continually polled or will automatically cancel.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          output_format: Specifies that you will poll this endpoint until the export completes

          current_bookmark: To poll an in-progress export, provide the current bookmark (returned by your
              first polling response)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return await self._post(
            f"/accounts/{account_id}/d1/database/{database_id}/export",
            body=await async_maybe_transform(
                {
                    "output_format": output_format,
                    "current_bookmark": current_bookmark,
                    "dump_options": dump_options,
                },
                database_export_params.DatabaseExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DatabaseExportResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatabaseExportResponse], ResultWrapper[DatabaseExportResponse]),
        )

    async def get(
        self,
        database_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> D1:
        """
        Returns the specified D1 database.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return await self._get(
            f"/accounts/{account_id}/d1/database/{database_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[D1]._unwrapper,
            ),
            cast_to=cast(Type[D1], ResultWrapper[D1]),
        )

    @overload
    async def import_(
        self,
        database_id: str,
        *,
        account_id: str,
        action: Literal["init"],
        etag: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseImportResponse:
        """
        Generates a temporary URL for uploading an SQL file to, then instructing the D1
        to import it and polling it for status updates. Imports block the D1 for their
        duration.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          action: Indicates you have a new SQL file to upload.

          etag: Required when action is 'init' or 'ingest'. An md5 hash of the file you're
              uploading. Used to check if it already exists, and validate its contents before
              ingesting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def import_(
        self,
        database_id: str,
        *,
        account_id: str,
        action: Literal["ingest"],
        etag: str,
        filename: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseImportResponse:
        """
        Generates a temporary URL for uploading an SQL file to, then instructing the D1
        to import it and polling it for status updates. Imports block the D1 for their
        duration.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          action: Indicates you've finished uploading to tell the D1 to start consuming it

          etag: An md5 hash of the file you're uploading. Used to check if it already exists,
              and validate its contents before ingesting.

          filename: The filename you have successfully uploaded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def import_(
        self,
        database_id: str,
        *,
        account_id: str,
        action: Literal["poll"],
        current_bookmark: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseImportResponse:
        """
        Generates a temporary URL for uploading an SQL file to, then instructing the D1
        to import it and polling it for status updates. Imports block the D1 for their
        duration.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          action: Indicates you've finished uploading to tell the D1 to start consuming it

          current_bookmark: This identifies the currently-running import, checking its status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "action", "etag"],
        ["account_id", "action", "etag", "filename"],
        ["account_id", "action", "current_bookmark"],
    )
    async def import_(
        self,
        database_id: str,
        *,
        account_id: str,
        action: Literal["init"] | Literal["ingest"] | Literal["poll"],
        etag: str | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        current_bookmark: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseImportResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return await self._post(
            f"/accounts/{account_id}/d1/database/{database_id}/import",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "etag": etag,
                    "filename": filename,
                    "current_bookmark": current_bookmark,
                },
                database_import_params.DatabaseImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DatabaseImportResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatabaseImportResponse], ResultWrapper[DatabaseImportResponse]),
        )

    def query(
        self,
        database_id: str,
        *,
        account_id: str,
        sql: str,
        params: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[QueryResult, AsyncSinglePage[QueryResult]]:
        """
        Returns the query result as an object.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          sql: Your SQL query. Supports multiple statements, joined by semicolons, which will
              be executed as a batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/d1/database/{database_id}/query",
            page=AsyncSinglePage[QueryResult],
            body=maybe_transform(
                {
                    "sql": sql,
                    "params": params,
                },
                database_query_params.DatabaseQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=QueryResult,
            method="post",
        )

    def raw(
        self,
        database_id: str,
        *,
        account_id: str,
        sql: str,
        params: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DatabaseRawResponse, AsyncSinglePage[DatabaseRawResponse]]:
        """Returns the query result rows as arrays rather than objects.

        This is a
        performance-optimized version of the /query endpoint.

        Args:
          account_id: Account identifier tag.

          database_id: D1 database identifier (UUID).

          sql: Your SQL query. Supports multiple statements, joined by semicolons, which will
              be executed as a batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/d1/database/{database_id}/raw",
            page=AsyncSinglePage[DatabaseRawResponse],
            body=maybe_transform(
                {
                    "sql": sql,
                    "params": params,
                },
                database_raw_params.DatabaseRawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DatabaseRawResponse,
            method="post",
        )


class DatabaseResourceWithRawResponse:
    def __init__(self, database: DatabaseResource) -> None:
        self._database = database

        self.create = to_raw_response_wrapper(
            database.create,
        )
        self.list = to_raw_response_wrapper(
            database.list,
        )
        self.delete = to_raw_response_wrapper(
            database.delete,
        )
        self.export = to_raw_response_wrapper(
            database.export,
        )
        self.get = to_raw_response_wrapper(
            database.get,
        )
        self.import_ = to_raw_response_wrapper(
            database.import_,
        )
        self.query = to_raw_response_wrapper(
            database.query,
        )
        self.raw = to_raw_response_wrapper(
            database.raw,
        )


class AsyncDatabaseResourceWithRawResponse:
    def __init__(self, database: AsyncDatabaseResource) -> None:
        self._database = database

        self.create = async_to_raw_response_wrapper(
            database.create,
        )
        self.list = async_to_raw_response_wrapper(
            database.list,
        )
        self.delete = async_to_raw_response_wrapper(
            database.delete,
        )
        self.export = async_to_raw_response_wrapper(
            database.export,
        )
        self.get = async_to_raw_response_wrapper(
            database.get,
        )
        self.import_ = async_to_raw_response_wrapper(
            database.import_,
        )
        self.query = async_to_raw_response_wrapper(
            database.query,
        )
        self.raw = async_to_raw_response_wrapper(
            database.raw,
        )


class DatabaseResourceWithStreamingResponse:
    def __init__(self, database: DatabaseResource) -> None:
        self._database = database

        self.create = to_streamed_response_wrapper(
            database.create,
        )
        self.list = to_streamed_response_wrapper(
            database.list,
        )
        self.delete = to_streamed_response_wrapper(
            database.delete,
        )
        self.export = to_streamed_response_wrapper(
            database.export,
        )
        self.get = to_streamed_response_wrapper(
            database.get,
        )
        self.import_ = to_streamed_response_wrapper(
            database.import_,
        )
        self.query = to_streamed_response_wrapper(
            database.query,
        )
        self.raw = to_streamed_response_wrapper(
            database.raw,
        )


class AsyncDatabaseResourceWithStreamingResponse:
    def __init__(self, database: AsyncDatabaseResource) -> None:
        self._database = database

        self.create = async_to_streamed_response_wrapper(
            database.create,
        )
        self.list = async_to_streamed_response_wrapper(
            database.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            database.delete,
        )
        self.export = async_to_streamed_response_wrapper(
            database.export,
        )
        self.get = async_to_streamed_response_wrapper(
            database.get,
        )
        self.import_ = async_to_streamed_response_wrapper(
            database.import_,
        )
        self.query = async_to_streamed_response_wrapper(
            database.query,
        )
        self.raw = async_to_streamed_response_wrapper(
            database.raw,
        )
