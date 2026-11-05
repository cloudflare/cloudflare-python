# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from .nodes import (
    NodesResource,
    AsyncNodesResource,
    NodesResourceWithRawResponse,
    AsyncNodesResourceWithRawResponse,
    NodesResourceWithStreamingResponse,
    AsyncNodesResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncCursorPagination, AsyncCursorPagination
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.cws import (
    tenant_structure_list_params,
    tenant_structure_create_params,
    tenant_structure_update_params,
)
from .....types.zero_trust.cws.tenant_structure import TenantStructure
from .....types.zero_trust.cws.tenant_structure_delete_response import TenantStructureDeleteResponse

__all__ = ["TenantStructuresResource", "AsyncTenantStructuresResource"]


class TenantStructuresResource(SyncAPIResource):
    @cached_property
    def nodes(self) -> NodesResource:
        return NodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TenantStructuresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TenantStructuresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenantStructuresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TenantStructuresResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        application: Literal["aws", "cloudflare"],
        name: str,
        import_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructure:
        """
        Creates an empty tenant hierarchy for the selected cloud application.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          application: Platform this structure models. Immutable after creation.

          name: Human-readable name; unique per account

          import_path: Optional unique Rego mount path in the form tenant.<application>.<name>;
              application must match. Omit to leave unmounted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cws/tenant-structures", account_id=account_id),
            body=maybe_transform(
                {
                    "application": application,
                    "name": name,
                    "import_path": import_path,
                },
                tenant_structure_create_params.TenantStructureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructure]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructure], ResultWrapper[TenantStructure]),
        )

    def update(
        self,
        structure_id: str,
        *,
        account_id: str,
        application: Literal["aws", "cloudflare"],
        name: str,
        import_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructure:
        """
        Updates the tenant structure's name and import path; its application remains
        immutable.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the tenant structure to update

          application: Platform this structure models. Must match the existing value.

          name: Human-readable name; unique per account

          import_path: Optional unique Rego mount path in the form tenant.<application>.<name>;
              application must match. Omit to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}",
                account_id=account_id,
                structure_id=structure_id,
            ),
            body=maybe_transform(
                {
                    "application": application,
                    "name": name,
                    "import_path": import_path,
                },
                tenant_structure_update_params.TenantStructureUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructure]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructure], ResultWrapper[TenantStructure]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        import_path: str | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[TenantStructure]:
        """
        Returns a paginated list of tenant structures in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          import_path: Filter by import path (case-sensitive literal substring match)

          name: Filter by tenant structure name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/tenant-structures", account_id=account_id),
            page=SyncCursorPagination[TenantStructure],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "import_path": import_path,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                    },
                    tenant_structure_list_params.TenantStructureListParams,
                ),
            ),
            model=TenantStructure,
        )

    def delete(
        self,
        structure_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructureDeleteResponse:
        """
        Deletes the tenant structure and all nodes in its hierarchy.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the tenant structure to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}",
                account_id=account_id,
                structure_id=structure_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructureDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructureDeleteResponse], ResultWrapper[TenantStructureDeleteResponse]),
        )

    def get(
        self,
        structure_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructure:
        """
        Returns the tenant structure with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the tenant structure to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}",
                account_id=account_id,
                structure_id=structure_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructure]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructure], ResultWrapper[TenantStructure]),
        )


class AsyncTenantStructuresResource(AsyncAPIResource):
    @cached_property
    def nodes(self) -> AsyncNodesResource:
        return AsyncNodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTenantStructuresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTenantStructuresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenantStructuresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTenantStructuresResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        application: Literal["aws", "cloudflare"],
        name: str,
        import_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructure:
        """
        Creates an empty tenant hierarchy for the selected cloud application.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          application: Platform this structure models. Immutable after creation.

          name: Human-readable name; unique per account

          import_path: Optional unique Rego mount path in the form tenant.<application>.<name>;
              application must match. Omit to leave unmounted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cws/tenant-structures", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "application": application,
                    "name": name,
                    "import_path": import_path,
                },
                tenant_structure_create_params.TenantStructureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructure]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructure], ResultWrapper[TenantStructure]),
        )

    async def update(
        self,
        structure_id: str,
        *,
        account_id: str,
        application: Literal["aws", "cloudflare"],
        name: str,
        import_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructure:
        """
        Updates the tenant structure's name and import path; its application remains
        immutable.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the tenant structure to update

          application: Platform this structure models. Must match the existing value.

          name: Human-readable name; unique per account

          import_path: Optional unique Rego mount path in the form tenant.<application>.<name>;
              application must match. Omit to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}",
                account_id=account_id,
                structure_id=structure_id,
            ),
            body=await async_maybe_transform(
                {
                    "application": application,
                    "name": name,
                    "import_path": import_path,
                },
                tenant_structure_update_params.TenantStructureUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructure]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructure], ResultWrapper[TenantStructure]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        import_path: str | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TenantStructure, AsyncCursorPagination[TenantStructure]]:
        """
        Returns a paginated list of tenant structures in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          import_path: Filter by import path (case-sensitive literal substring match)

          name: Filter by tenant structure name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/tenant-structures", account_id=account_id),
            page=AsyncCursorPagination[TenantStructure],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "import_path": import_path,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                    },
                    tenant_structure_list_params.TenantStructureListParams,
                ),
            ),
            model=TenantStructure,
        )

    async def delete(
        self,
        structure_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructureDeleteResponse:
        """
        Deletes the tenant structure and all nodes in its hierarchy.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the tenant structure to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}",
                account_id=account_id,
                structure_id=structure_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructureDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructureDeleteResponse], ResultWrapper[TenantStructureDeleteResponse]),
        )

    async def get(
        self,
        structure_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructure:
        """
        Returns the tenant structure with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the tenant structure to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}",
                account_id=account_id,
                structure_id=structure_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructure]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructure], ResultWrapper[TenantStructure]),
        )


class TenantStructuresResourceWithRawResponse:
    def __init__(self, tenant_structures: TenantStructuresResource) -> None:
        self._tenant_structures = tenant_structures

        self.create = to_raw_response_wrapper(
            tenant_structures.create,
        )
        self.update = to_raw_response_wrapper(
            tenant_structures.update,
        )
        self.list = to_raw_response_wrapper(
            tenant_structures.list,
        )
        self.delete = to_raw_response_wrapper(
            tenant_structures.delete,
        )
        self.get = to_raw_response_wrapper(
            tenant_structures.get,
        )

    @cached_property
    def nodes(self) -> NodesResourceWithRawResponse:
        return NodesResourceWithRawResponse(self._tenant_structures.nodes)


class AsyncTenantStructuresResourceWithRawResponse:
    def __init__(self, tenant_structures: AsyncTenantStructuresResource) -> None:
        self._tenant_structures = tenant_structures

        self.create = async_to_raw_response_wrapper(
            tenant_structures.create,
        )
        self.update = async_to_raw_response_wrapper(
            tenant_structures.update,
        )
        self.list = async_to_raw_response_wrapper(
            tenant_structures.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tenant_structures.delete,
        )
        self.get = async_to_raw_response_wrapper(
            tenant_structures.get,
        )

    @cached_property
    def nodes(self) -> AsyncNodesResourceWithRawResponse:
        return AsyncNodesResourceWithRawResponse(self._tenant_structures.nodes)


class TenantStructuresResourceWithStreamingResponse:
    def __init__(self, tenant_structures: TenantStructuresResource) -> None:
        self._tenant_structures = tenant_structures

        self.create = to_streamed_response_wrapper(
            tenant_structures.create,
        )
        self.update = to_streamed_response_wrapper(
            tenant_structures.update,
        )
        self.list = to_streamed_response_wrapper(
            tenant_structures.list,
        )
        self.delete = to_streamed_response_wrapper(
            tenant_structures.delete,
        )
        self.get = to_streamed_response_wrapper(
            tenant_structures.get,
        )

    @cached_property
    def nodes(self) -> NodesResourceWithStreamingResponse:
        return NodesResourceWithStreamingResponse(self._tenant_structures.nodes)


class AsyncTenantStructuresResourceWithStreamingResponse:
    def __init__(self, tenant_structures: AsyncTenantStructuresResource) -> None:
        self._tenant_structures = tenant_structures

        self.create = async_to_streamed_response_wrapper(
            tenant_structures.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tenant_structures.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tenant_structures.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tenant_structures.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            tenant_structures.get,
        )

    @cached_property
    def nodes(self) -> AsyncNodesResourceWithStreamingResponse:
        return AsyncNodesResourceWithStreamingResponse(self._tenant_structures.nodes)
