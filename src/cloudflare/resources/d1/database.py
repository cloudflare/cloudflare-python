# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ...types.d1 import (
    D1CreateDatabase,
    D1DatabaseDetails,
    DatabaseQueryResponse,
    DatabaseDeleteResponse,
    database_list_params,
    database_query_params,
    database_create_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Database", "AsyncDatabase"]


class Database(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatabaseWithRawResponse:
        return DatabaseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabaseWithStreamingResponse:
        return DatabaseWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> D1CreateDatabase:
        """
        Returns the created D1 database.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/d1/database",
            body=maybe_transform({"name": name}, database_create_params.DatabaseCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[D1CreateDatabase], ResultWrapper[D1CreateDatabase]),
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
    ) -> SyncV4PagePaginationArray[D1CreateDatabase]:
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
            page=SyncV4PagePaginationArray[D1CreateDatabase],
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
            model=D1CreateDatabase,
        )

    def delete(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DatabaseDeleteResponse]:
        """
        Deletes the specified D1 database.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return cast(
            Optional[DatabaseDeleteResponse],
            self._delete(
                f"/accounts/{account_identifier}/d1/database/{database_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DatabaseDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> D1DatabaseDetails:
        """
        Returns the specified D1 database.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return self._get(
            f"/accounts/{account_identifier}/d1/database/{database_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[D1DatabaseDetails], ResultWrapper[D1DatabaseDetails]),
        )

    def query(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        sql: str,
        params: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseQueryResponse:
        """
        Returns the query result.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return self._post(
            f"/accounts/{account_identifier}/d1/database/{database_identifier}/query",
            body=maybe_transform(
                {
                    "sql": sql,
                    "params": params,
                },
                database_query_params.DatabaseQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatabaseQueryResponse], ResultWrapper[DatabaseQueryResponse]),
        )


class AsyncDatabase(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatabaseWithRawResponse:
        return AsyncDatabaseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabaseWithStreamingResponse:
        return AsyncDatabaseWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> D1CreateDatabase:
        """
        Returns the created D1 database.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/d1/database",
            body=await async_maybe_transform({"name": name}, database_create_params.DatabaseCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[D1CreateDatabase], ResultWrapper[D1CreateDatabase]),
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
    ) -> AsyncPaginator[D1CreateDatabase, AsyncV4PagePaginationArray[D1CreateDatabase]]:
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
            page=AsyncV4PagePaginationArray[D1CreateDatabase],
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
            model=D1CreateDatabase,
        )

    async def delete(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DatabaseDeleteResponse]:
        """
        Deletes the specified D1 database.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return cast(
            Optional[DatabaseDeleteResponse],
            await self._delete(
                f"/accounts/{account_identifier}/d1/database/{database_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DatabaseDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> D1DatabaseDetails:
        """
        Returns the specified D1 database.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return await self._get(
            f"/accounts/{account_identifier}/d1/database/{database_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[D1DatabaseDetails], ResultWrapper[D1DatabaseDetails]),
        )

    async def query(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        sql: str,
        params: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseQueryResponse:
        """
        Returns the query result.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return await self._post(
            f"/accounts/{account_identifier}/d1/database/{database_identifier}/query",
            body=await async_maybe_transform(
                {
                    "sql": sql,
                    "params": params,
                },
                database_query_params.DatabaseQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatabaseQueryResponse], ResultWrapper[DatabaseQueryResponse]),
        )


class DatabaseWithRawResponse:
    def __init__(self, database: Database) -> None:
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
        self.get = to_raw_response_wrapper(
            database.get,
        )
        self.query = to_raw_response_wrapper(
            database.query,
        )


class AsyncDatabaseWithRawResponse:
    def __init__(self, database: AsyncDatabase) -> None:
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
        self.get = async_to_raw_response_wrapper(
            database.get,
        )
        self.query = async_to_raw_response_wrapper(
            database.query,
        )


class DatabaseWithStreamingResponse:
    def __init__(self, database: Database) -> None:
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
        self.get = to_streamed_response_wrapper(
            database.get,
        )
        self.query = to_streamed_response_wrapper(
            database.query,
        )


class AsyncDatabaseWithStreamingResponse:
    def __init__(self, database: AsyncDatabase) -> None:
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
        self.get = async_to_streamed_response_wrapper(
            database.get,
        )
        self.query = async_to_streamed_response_wrapper(
            database.query,
        )
