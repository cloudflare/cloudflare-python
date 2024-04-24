# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ...types.d1 import database_list_params, database_query_params, database_create_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...types.d1.d1 import D1
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.d1.database_list_response import DatabaseListResponse
from ...types.d1.database_query_response import DatabaseQueryResponse
from ...types.d1.database_create_response import DatabaseCreateResponse
from ...types.d1.database_delete_response import DatabaseDeleteResponse

__all__ = ["DatabaseResource", "AsyncDatabaseResource"]


class DatabaseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatabaseResourceWithRawResponse:
        return DatabaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabaseResourceWithStreamingResponse:
        return DatabaseResourceWithStreamingResponse(self)

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
    ) -> DatabaseCreateResponse:
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
                post_parser=ResultWrapper[DatabaseCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatabaseCreateResponse], ResultWrapper[DatabaseCreateResponse]),
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
        database_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseDeleteResponse:
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
            DatabaseDeleteResponse,
            self._delete(
                f"/accounts/{account_identifier}/d1/database/{database_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[DatabaseDeleteResponse]._unwrapper,
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
    ) -> D1:
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
                post_parser=ResultWrapper[D1]._unwrapper,
            ),
            cast_to=cast(Type[D1], ResultWrapper[D1]),
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
                post_parser=ResultWrapper[DatabaseQueryResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatabaseQueryResponse], ResultWrapper[DatabaseQueryResponse]),
        )


class AsyncDatabaseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatabaseResourceWithRawResponse:
        return AsyncDatabaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabaseResourceWithStreamingResponse:
        return AsyncDatabaseResourceWithStreamingResponse(self)

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
    ) -> DatabaseCreateResponse:
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
                post_parser=ResultWrapper[DatabaseCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatabaseCreateResponse], ResultWrapper[DatabaseCreateResponse]),
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
        database_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseDeleteResponse:
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
            DatabaseDeleteResponse,
            await self._delete(
                f"/accounts/{account_identifier}/d1/database/{database_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[DatabaseDeleteResponse]._unwrapper,
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
    ) -> D1:
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
                post_parser=ResultWrapper[D1]._unwrapper,
            ),
            cast_to=cast(Type[D1], ResultWrapper[D1]),
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
                post_parser=ResultWrapper[DatabaseQueryResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatabaseQueryResponse], ResultWrapper[DatabaseQueryResponse]),
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
        self.get = to_raw_response_wrapper(
            database.get,
        )
        self.query = to_raw_response_wrapper(
            database.query,
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
        self.get = async_to_raw_response_wrapper(
            database.get,
        )
        self.query = async_to_raw_response_wrapper(
            database.query,
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
        self.get = to_streamed_response_wrapper(
            database.get,
        )
        self.query = to_streamed_response_wrapper(
            database.query,
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
        self.get = async_to_streamed_response_wrapper(
            database.get,
        )
        self.query = async_to_streamed_response_wrapper(
            database.query,
        )
