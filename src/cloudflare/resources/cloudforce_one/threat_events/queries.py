# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events import query_edit_params, query_create_params
from ....types.cloudforce_one.threat_events.query_get_response import QueryGetResponse
from ....types.cloudforce_one.threat_events.query_edit_response import QueryEditResponse
from ....types.cloudforce_one.threat_events.query_list_response import QueryListResponse
from ....types.cloudforce_one.threat_events.query_create_response import QueryCreateResponse

__all__ = ["QueriesResource", "AsyncQueriesResource"]


class QueriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return QueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return QueriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        alert_enabled: bool,
        alert_rollup_enabled: bool,
        name: str,
        query_json: str,
        rule_enabled: bool,
        rule_scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryCreateResponse:
        """
        Create a new saved event query for the account

        Args:
          account_id: Account ID.

          alert_enabled: Enable alerts for this query

          alert_rollup_enabled: Enable alert rollup for this query

          name: Unique name for the saved query

          query_json: JSON string containing the query parameters

          rule_enabled: Enable rule for this query

          rule_scope: Scope for the rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/queries/create", account_id=account_id),
            body=maybe_transform(
                {
                    "alert_enabled": alert_enabled,
                    "alert_rollup_enabled": alert_rollup_enabled,
                    "name": name,
                    "query_json": query_json,
                    "rule_enabled": rule_enabled,
                    "rule_scope": rule_scope,
                },
                query_create_params.QueryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryCreateResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryListResponse:
        """
        Retrieve all saved event queries for the account

        Args:
          account_id: Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/queries", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryListResponse,
        )

    def delete(
        self,
        query_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a saved event query by its ID

        Args:
          account_id: Account ID.

          query_id: Event query ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/queries/{query_id}",
                account_id=account_id,
                query_id=query_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def edit(
        self,
        query_id: int,
        *,
        account_id: str,
        alert_enabled: bool | Omit = omit,
        alert_rollup_enabled: bool | Omit = omit,
        name: str | Omit = omit,
        query_json: str | Omit = omit,
        rule_enabled: bool | Omit = omit,
        rule_scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryEditResponse:
        """
        Update an existing saved event query by its ID

        Args:
          account_id: Account ID.

          query_id: Event query ID

          alert_enabled: Enable alerts for this query

          alert_rollup_enabled: Enable alert rollup for this query

          name: Unique name for the saved query

          query_json: JSON string containing the query parameters

          rule_enabled: Enable rule for this query

          rule_scope: Scope for the rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/queries/{query_id}",
                account_id=account_id,
                query_id=query_id,
            ),
            body=maybe_transform(
                {
                    "alert_enabled": alert_enabled,
                    "alert_rollup_enabled": alert_rollup_enabled,
                    "name": name,
                    "query_json": query_json,
                    "rule_enabled": rule_enabled,
                    "rule_scope": rule_scope,
                },
                query_edit_params.QueryEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryEditResponse,
        )

    def get(
        self,
        query_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryGetResponse:
        """
        Retrieve a saved event query by its ID

        Args:
          account_id: Account ID.

          query_id: Event query ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/queries/{query_id}",
                account_id=account_id,
                query_id=query_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryGetResponse,
        )


class AsyncQueriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncQueriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        alert_enabled: bool,
        alert_rollup_enabled: bool,
        name: str,
        query_json: str,
        rule_enabled: bool,
        rule_scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryCreateResponse:
        """
        Create a new saved event query for the account

        Args:
          account_id: Account ID.

          alert_enabled: Enable alerts for this query

          alert_rollup_enabled: Enable alert rollup for this query

          name: Unique name for the saved query

          query_json: JSON string containing the query parameters

          rule_enabled: Enable rule for this query

          rule_scope: Scope for the rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/queries/create", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "alert_enabled": alert_enabled,
                    "alert_rollup_enabled": alert_rollup_enabled,
                    "name": name,
                    "query_json": query_json,
                    "rule_enabled": rule_enabled,
                    "rule_scope": rule_scope,
                },
                query_create_params.QueryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryCreateResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryListResponse:
        """
        Retrieve all saved event queries for the account

        Args:
          account_id: Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/queries", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryListResponse,
        )

    async def delete(
        self,
        query_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a saved event query by its ID

        Args:
          account_id: Account ID.

          query_id: Event query ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/queries/{query_id}",
                account_id=account_id,
                query_id=query_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def edit(
        self,
        query_id: int,
        *,
        account_id: str,
        alert_enabled: bool | Omit = omit,
        alert_rollup_enabled: bool | Omit = omit,
        name: str | Omit = omit,
        query_json: str | Omit = omit,
        rule_enabled: bool | Omit = omit,
        rule_scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryEditResponse:
        """
        Update an existing saved event query by its ID

        Args:
          account_id: Account ID.

          query_id: Event query ID

          alert_enabled: Enable alerts for this query

          alert_rollup_enabled: Enable alert rollup for this query

          name: Unique name for the saved query

          query_json: JSON string containing the query parameters

          rule_enabled: Enable rule for this query

          rule_scope: Scope for the rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/queries/{query_id}",
                account_id=account_id,
                query_id=query_id,
            ),
            body=await async_maybe_transform(
                {
                    "alert_enabled": alert_enabled,
                    "alert_rollup_enabled": alert_rollup_enabled,
                    "name": name,
                    "query_json": query_json,
                    "rule_enabled": rule_enabled,
                    "rule_scope": rule_scope,
                },
                query_edit_params.QueryEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryEditResponse,
        )

    async def get(
        self,
        query_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryGetResponse:
        """
        Retrieve a saved event query by its ID

        Args:
          account_id: Account ID.

          query_id: Event query ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/queries/{query_id}",
                account_id=account_id,
                query_id=query_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryGetResponse,
        )


class QueriesResourceWithRawResponse:
    def __init__(self, queries: QueriesResource) -> None:
        self._queries = queries

        self.create = to_raw_response_wrapper(
            queries.create,
        )
        self.list = to_raw_response_wrapper(
            queries.list,
        )
        self.delete = to_raw_response_wrapper(
            queries.delete,
        )
        self.edit = to_raw_response_wrapper(
            queries.edit,
        )
        self.get = to_raw_response_wrapper(
            queries.get,
        )


class AsyncQueriesResourceWithRawResponse:
    def __init__(self, queries: AsyncQueriesResource) -> None:
        self._queries = queries

        self.create = async_to_raw_response_wrapper(
            queries.create,
        )
        self.list = async_to_raw_response_wrapper(
            queries.list,
        )
        self.delete = async_to_raw_response_wrapper(
            queries.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            queries.edit,
        )
        self.get = async_to_raw_response_wrapper(
            queries.get,
        )


class QueriesResourceWithStreamingResponse:
    def __init__(self, queries: QueriesResource) -> None:
        self._queries = queries

        self.create = to_streamed_response_wrapper(
            queries.create,
        )
        self.list = to_streamed_response_wrapper(
            queries.list,
        )
        self.delete = to_streamed_response_wrapper(
            queries.delete,
        )
        self.edit = to_streamed_response_wrapper(
            queries.edit,
        )
        self.get = to_streamed_response_wrapper(
            queries.get,
        )


class AsyncQueriesResourceWithStreamingResponse:
    def __init__(self, queries: AsyncQueriesResource) -> None:
        self._queries = queries

        self.create = async_to_streamed_response_wrapper(
            queries.create,
        )
        self.list = async_to_streamed_response_wrapper(
            queries.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            queries.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            queries.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            queries.get,
        )
