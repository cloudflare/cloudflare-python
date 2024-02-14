# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.d1 import DatabaseCreateResponse, DatabaseListResponse

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.d1 import database_create_params
from ...types.d1 import database_list_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Databases", "AsyncDatabases"]


class Databases(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatabasesWithRawResponse:
        return DatabasesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabasesWithStreamingResponse:
        return DatabasesWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatabaseCreateResponse], ResultWrapper[DatabaseCreateResponse]),
        )

    def list(
        self,
        account_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseListResponse:
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
        return self._get(
            f"/accounts/{account_id}/d1/database",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatabaseListResponse], ResultWrapper[DatabaseListResponse]),
        )


class AsyncDatabases(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatabasesWithRawResponse:
        return AsyncDatabasesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabasesWithStreamingResponse:
        return AsyncDatabasesWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
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
            body=maybe_transform({"name": name}, database_create_params.DatabaseCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatabaseCreateResponse], ResultWrapper[DatabaseCreateResponse]),
        )

    async def list(
        self,
        account_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseListResponse:
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
        return await self._get(
            f"/accounts/{account_id}/d1/database",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatabaseListResponse], ResultWrapper[DatabaseListResponse]),
        )


class DatabasesWithRawResponse:
    def __init__(self, databases: Databases) -> None:
        self._databases = databases

        self.create = to_raw_response_wrapper(
            databases.create,
        )
        self.list = to_raw_response_wrapper(
            databases.list,
        )


class AsyncDatabasesWithRawResponse:
    def __init__(self, databases: AsyncDatabases) -> None:
        self._databases = databases

        self.create = async_to_raw_response_wrapper(
            databases.create,
        )
        self.list = async_to_raw_response_wrapper(
            databases.list,
        )


class DatabasesWithStreamingResponse:
    def __init__(self, databases: Databases) -> None:
        self._databases = databases

        self.create = to_streamed_response_wrapper(
            databases.create,
        )
        self.list = to_streamed_response_wrapper(
            databases.list,
        )


class AsyncDatabasesWithStreamingResponse:
    def __init__(self, databases: AsyncDatabases) -> None:
        self._databases = databases

        self.create = async_to_streamed_response_wrapper(
            databases.create,
        )
        self.list = async_to_streamed_response_wrapper(
            databases.list,
        )
