# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.cws import workload_list_params, workload_create_params, workload_update_params
from ....types.zero_trust.cws.workload import Workload
from ....types.zero_trust.cws.workload_delete_response import WorkloadDeleteResponse

__all__ = ["WorkloadsResource", "AsyncWorkloadsResource"]


class WorkloadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WorkloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WorkloadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        filter: str,
        name: str,
        description: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workload:
        """
        Creates a reusable workload selector from a filter expression.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          filter: Filter expression selecting the requests this workload matches. Maximum 4096
              UTF-8 bytes.

          name: Human-readable handle; unique per account.

          description: Optional free-form description.

          tags: Tags to attach. Keys are limited to 256 UTF-8 bytes and values to 1024 UTF-8
              bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cws/workloads", account_id=account_id),
            body=maybe_transform(
                {
                    "filter": filter,
                    "name": name,
                    "description": description,
                    "tags": tags,
                },
                workload_create_params.WorkloadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Workload]._unwrapper,
            ),
            cast_to=cast(Type[Workload], ResultWrapper[Workload]),
        )

    def update(
        self,
        workload_id: str,
        *,
        account_id: str,
        filter: str,
        name: str,
        description: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workload:
        """Replaces the workload's configuration.

        Omit tags or use {} to clear them.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          workload_id: ID of the workload to update

          filter: Filter expression selecting the requests this workload matches. Maximum 4096
              UTF-8 bytes.

          name: Human-readable handle; unique per account.

          description: Optional free-form description.

          tags: Replacement tag set. Omit or use {} to clear. Keys are limited to 256 UTF-8
              bytes and values to 1024 UTF-8 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not workload_id:
            raise ValueError(f"Expected a non-empty value for `workload_id` but received {workload_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/cws/workloads/{workload_id}", account_id=account_id, workload_id=workload_id
            ),
            body=maybe_transform(
                {
                    "filter": filter,
                    "name": name,
                    "description": description,
                    "tags": tags,
                },
                workload_update_params.WorkloadUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Workload]._unwrapper,
            ),
            cast_to=cast(Type[Workload], ResultWrapper[Workload]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        policy_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[Workload]:
        """
        Returns a paginated list of workloads in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          name: Filter by workload name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          policy_set_id: Filter to workloads attached to this policy set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/workloads", account_id=account_id),
            page=SyncCursorPagination[Workload],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                        "policy_set_id": policy_set_id,
                    },
                    workload_list_params.WorkloadListParams,
                ),
            ),
            model=Workload,
        )

    def delete(
        self,
        workload_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkloadDeleteResponse:
        """
        Deletes the workload if it is not targeted by a policy set.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          workload_id: ID of the workload to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not workload_id:
            raise ValueError(f"Expected a non-empty value for `workload_id` but received {workload_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cws/workloads/{workload_id}", account_id=account_id, workload_id=workload_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WorkloadDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[WorkloadDeleteResponse], ResultWrapper[WorkloadDeleteResponse]),
        )

    def get(
        self,
        workload_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workload:
        """
        Returns the workload with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          workload_id: ID of the workload to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not workload_id:
            raise ValueError(f"Expected a non-empty value for `workload_id` but received {workload_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cws/workloads/{workload_id}", account_id=account_id, workload_id=workload_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Workload]._unwrapper,
            ),
            cast_to=cast(Type[Workload], ResultWrapper[Workload]),
        )


class AsyncWorkloadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWorkloadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        filter: str,
        name: str,
        description: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workload:
        """
        Creates a reusable workload selector from a filter expression.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          filter: Filter expression selecting the requests this workload matches. Maximum 4096
              UTF-8 bytes.

          name: Human-readable handle; unique per account.

          description: Optional free-form description.

          tags: Tags to attach. Keys are limited to 256 UTF-8 bytes and values to 1024 UTF-8
              bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cws/workloads", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "name": name,
                    "description": description,
                    "tags": tags,
                },
                workload_create_params.WorkloadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Workload]._unwrapper,
            ),
            cast_to=cast(Type[Workload], ResultWrapper[Workload]),
        )

    async def update(
        self,
        workload_id: str,
        *,
        account_id: str,
        filter: str,
        name: str,
        description: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workload:
        """Replaces the workload's configuration.

        Omit tags or use {} to clear them.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          workload_id: ID of the workload to update

          filter: Filter expression selecting the requests this workload matches. Maximum 4096
              UTF-8 bytes.

          name: Human-readable handle; unique per account.

          description: Optional free-form description.

          tags: Replacement tag set. Omit or use {} to clear. Keys are limited to 256 UTF-8
              bytes and values to 1024 UTF-8 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not workload_id:
            raise ValueError(f"Expected a non-empty value for `workload_id` but received {workload_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/cws/workloads/{workload_id}", account_id=account_id, workload_id=workload_id
            ),
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "name": name,
                    "description": description,
                    "tags": tags,
                },
                workload_update_params.WorkloadUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Workload]._unwrapper,
            ),
            cast_to=cast(Type[Workload], ResultWrapper[Workload]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        policy_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Workload, AsyncCursorPagination[Workload]]:
        """
        Returns a paginated list of workloads in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          name: Filter by workload name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          policy_set_id: Filter to workloads attached to this policy set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/workloads", account_id=account_id),
            page=AsyncCursorPagination[Workload],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                        "policy_set_id": policy_set_id,
                    },
                    workload_list_params.WorkloadListParams,
                ),
            ),
            model=Workload,
        )

    async def delete(
        self,
        workload_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkloadDeleteResponse:
        """
        Deletes the workload if it is not targeted by a policy set.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          workload_id: ID of the workload to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not workload_id:
            raise ValueError(f"Expected a non-empty value for `workload_id` but received {workload_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cws/workloads/{workload_id}", account_id=account_id, workload_id=workload_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WorkloadDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[WorkloadDeleteResponse], ResultWrapper[WorkloadDeleteResponse]),
        )

    async def get(
        self,
        workload_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workload:
        """
        Returns the workload with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          workload_id: ID of the workload to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not workload_id:
            raise ValueError(f"Expected a non-empty value for `workload_id` but received {workload_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cws/workloads/{workload_id}", account_id=account_id, workload_id=workload_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Workload]._unwrapper,
            ),
            cast_to=cast(Type[Workload], ResultWrapper[Workload]),
        )


class WorkloadsResourceWithRawResponse:
    def __init__(self, workloads: WorkloadsResource) -> None:
        self._workloads = workloads

        self.create = to_raw_response_wrapper(
            workloads.create,
        )
        self.update = to_raw_response_wrapper(
            workloads.update,
        )
        self.list = to_raw_response_wrapper(
            workloads.list,
        )
        self.delete = to_raw_response_wrapper(
            workloads.delete,
        )
        self.get = to_raw_response_wrapper(
            workloads.get,
        )


class AsyncWorkloadsResourceWithRawResponse:
    def __init__(self, workloads: AsyncWorkloadsResource) -> None:
        self._workloads = workloads

        self.create = async_to_raw_response_wrapper(
            workloads.create,
        )
        self.update = async_to_raw_response_wrapper(
            workloads.update,
        )
        self.list = async_to_raw_response_wrapper(
            workloads.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workloads.delete,
        )
        self.get = async_to_raw_response_wrapper(
            workloads.get,
        )


class WorkloadsResourceWithStreamingResponse:
    def __init__(self, workloads: WorkloadsResource) -> None:
        self._workloads = workloads

        self.create = to_streamed_response_wrapper(
            workloads.create,
        )
        self.update = to_streamed_response_wrapper(
            workloads.update,
        )
        self.list = to_streamed_response_wrapper(
            workloads.list,
        )
        self.delete = to_streamed_response_wrapper(
            workloads.delete,
        )
        self.get = to_streamed_response_wrapper(
            workloads.get,
        )


class AsyncWorkloadsResourceWithStreamingResponse:
    def __init__(self, workloads: AsyncWorkloadsResource) -> None:
        self._workloads = workloads

        self.create = async_to_streamed_response_wrapper(
            workloads.create,
        )
        self.update = async_to_streamed_response_wrapper(
            workloads.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workloads.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workloads.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            workloads.get,
        )
