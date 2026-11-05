# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

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
from .....types.zero_trust.cws.tenant_structures import (
    node_list_params,
    node_batch_params,
    node_create_params,
    node_update_params,
)
from .....types.zero_trust.cws.tenant_structures.node_batch_response import NodeBatchResponse
from .....types.zero_trust.cws.tenant_structures.node_delete_response import NodeDeleteResponse
from .....types.zero_trust.cws.tenant_structures.tenant_structure_node import TenantStructureNode

__all__ = ["NodesResource", "AsyncNodesResource"]


class NodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return NodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return NodesResourceWithStreamingResponse(self)

    def create(
        self,
        structure_id: str,
        *,
        account_id: str,
        native_id: str,
        node_kind: str,
        name: str | Omit = omit,
        parent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructureNode:
        """
        Adds a validated cloud-native node to the tenant hierarchy.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          native_id: Cloud-native identifier of this node, unique within the structure; the
              parent-reference target. Shape depends on the structure's application. Immutable
              after create.

          node_kind:
              Position in the tree. Legal values depend on the structure's application (aws:
              root/ou/account; cloudflare: org/account/zone). At most one root per structure.
              Immutable after create.

          name: Display name (e.g. an OU or account name), mutable. Optional; empty by default.

          parent: Native ID of this node's parent. Required for non-root nodes and omitted for the
              root. The parent must be in the same structure and able to contain this node
              kind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes",
                account_id=account_id,
                structure_id=structure_id,
            ),
            body=maybe_transform(
                {
                    "native_id": native_id,
                    "node_kind": node_kind,
                    "name": name,
                    "parent": parent,
                },
                node_create_params.NodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructureNode]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructureNode], ResultWrapper[TenantStructureNode]),
        )

    def update(
        self,
        node_id: str,
        *,
        account_id: str,
        structure_id: str,
        native_id: str,
        node_kind: str,
        name: str | Omit = omit,
        parent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructureNode:
        """
        Updates the node's display name or parent while preserving its immutable
        identity fields.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          node_id: ID of the node to update

          native_id: Cloud-native identifier of this node, unique within the structure; the
              parent-reference target. Shape depends on the structure's application. Immutable
              after create.

          node_kind:
              Position in the tree. Legal values depend on the structure's application (aws:
              root/ou/account; cloudflare: org/account/zone). At most one root per structure.
              Immutable after create.

          name: Display name (e.g. an OU or account name), mutable. Optional; empty by default.

          parent: Native ID of this node's parent. Required for non-root nodes and omitted for the
              root. The parent must be in the same structure and able to contain this node
              kind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes/{node_id}",
                account_id=account_id,
                structure_id=structure_id,
                node_id=node_id,
            ),
            body=maybe_transform(
                {
                    "native_id": native_id,
                    "node_kind": node_kind,
                    "name": name,
                    "parent": parent,
                },
                node_update_params.NodeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructureNode]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructureNode], ResultWrapper[TenantStructureNode]),
        )

    def list(
        self,
        structure_id: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        native_id: str | Omit = omit,
        node_kind: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        parent: str | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[TenantStructureNode]:
        """
        Returns a paginated list of nodes in the tenant structure.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          name: Filter by node name (case-insensitive substring match)

          native_id: Filter by exact cloud-native identifier

          node_kind: Filter by exact node kind

          order: Field to order results by (default: created_at)

          parent: Filter by exact parent native ID

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes",
                account_id=account_id,
                structure_id=structure_id,
            ),
            page=SyncCursorPagination[TenantStructureNode],
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
                        "native_id": native_id,
                        "node_kind": node_kind,
                        "order": order,
                        "parent": parent,
                        "per_page": per_page,
                    },
                    node_list_params.NodeListParams,
                ),
            ),
            model=TenantStructureNode,
        )

    def delete(
        self,
        node_id: str,
        *,
        account_id: str,
        structure_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NodeDeleteResponse:
        """
        Deletes a childless node from the tenant hierarchy.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          node_id: ID of the node to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes/{node_id}",
                account_id=account_id,
                structure_id=structure_id,
                node_id=node_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NodeDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[NodeDeleteResponse], ResultWrapper[NodeDeleteResponse]),
        )

    def batch(
        self,
        structure_id: str,
        *,
        account_id: str,
        creates: Iterable[node_batch_params.Create],
        deletes: Iterable[node_batch_params.Delete],
        updates: Iterable[node_batch_params.Update],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NodeBatchResponse:
        """Atomically validates and applies 1 to 500 unordered node operations.

        Creates may
        reference new parents but cannot reuse a native_id deleted in the same batch.
        Maximum body size: 1 MiB.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          creates: Nodes to create; parents may be created elsewhere in this request

          deletes: Nodes to delete; every descendant that will not be reparented must also be
              deleted

          updates: Nodes whose mutable fields should be fully replaced

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes/batch",
                account_id=account_id,
                structure_id=structure_id,
            ),
            body=maybe_transform(
                {
                    "creates": creates,
                    "deletes": deletes,
                    "updates": updates,
                },
                node_batch_params.NodeBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NodeBatchResponse]._unwrapper,
            ),
            cast_to=cast(Type[NodeBatchResponse], ResultWrapper[NodeBatchResponse]),
        )

    def get(
        self,
        node_id: str,
        *,
        account_id: str,
        structure_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructureNode:
        """
        Returns the tenant node with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          node_id: ID of the node to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes/{node_id}",
                account_id=account_id,
                structure_id=structure_id,
                node_id=node_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructureNode]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructureNode], ResultWrapper[TenantStructureNode]),
        )


class AsyncNodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncNodesResourceWithStreamingResponse(self)

    async def create(
        self,
        structure_id: str,
        *,
        account_id: str,
        native_id: str,
        node_kind: str,
        name: str | Omit = omit,
        parent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructureNode:
        """
        Adds a validated cloud-native node to the tenant hierarchy.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          native_id: Cloud-native identifier of this node, unique within the structure; the
              parent-reference target. Shape depends on the structure's application. Immutable
              after create.

          node_kind:
              Position in the tree. Legal values depend on the structure's application (aws:
              root/ou/account; cloudflare: org/account/zone). At most one root per structure.
              Immutable after create.

          name: Display name (e.g. an OU or account name), mutable. Optional; empty by default.

          parent: Native ID of this node's parent. Required for non-root nodes and omitted for the
              root. The parent must be in the same structure and able to contain this node
              kind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes",
                account_id=account_id,
                structure_id=structure_id,
            ),
            body=await async_maybe_transform(
                {
                    "native_id": native_id,
                    "node_kind": node_kind,
                    "name": name,
                    "parent": parent,
                },
                node_create_params.NodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructureNode]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructureNode], ResultWrapper[TenantStructureNode]),
        )

    async def update(
        self,
        node_id: str,
        *,
        account_id: str,
        structure_id: str,
        native_id: str,
        node_kind: str,
        name: str | Omit = omit,
        parent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructureNode:
        """
        Updates the node's display name or parent while preserving its immutable
        identity fields.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          node_id: ID of the node to update

          native_id: Cloud-native identifier of this node, unique within the structure; the
              parent-reference target. Shape depends on the structure's application. Immutable
              after create.

          node_kind:
              Position in the tree. Legal values depend on the structure's application (aws:
              root/ou/account; cloudflare: org/account/zone). At most one root per structure.
              Immutable after create.

          name: Display name (e.g. an OU or account name), mutable. Optional; empty by default.

          parent: Native ID of this node's parent. Required for non-root nodes and omitted for the
              root. The parent must be in the same structure and able to contain this node
              kind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes/{node_id}",
                account_id=account_id,
                structure_id=structure_id,
                node_id=node_id,
            ),
            body=await async_maybe_transform(
                {
                    "native_id": native_id,
                    "node_kind": node_kind,
                    "name": name,
                    "parent": parent,
                },
                node_update_params.NodeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructureNode]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructureNode], ResultWrapper[TenantStructureNode]),
        )

    def list(
        self,
        structure_id: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        native_id: str | Omit = omit,
        node_kind: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        parent: str | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TenantStructureNode, AsyncCursorPagination[TenantStructureNode]]:
        """
        Returns a paginated list of nodes in the tenant structure.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          name: Filter by node name (case-insensitive substring match)

          native_id: Filter by exact cloud-native identifier

          node_kind: Filter by exact node kind

          order: Field to order results by (default: created_at)

          parent: Filter by exact parent native ID

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes",
                account_id=account_id,
                structure_id=structure_id,
            ),
            page=AsyncCursorPagination[TenantStructureNode],
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
                        "native_id": native_id,
                        "node_kind": node_kind,
                        "order": order,
                        "parent": parent,
                        "per_page": per_page,
                    },
                    node_list_params.NodeListParams,
                ),
            ),
            model=TenantStructureNode,
        )

    async def delete(
        self,
        node_id: str,
        *,
        account_id: str,
        structure_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NodeDeleteResponse:
        """
        Deletes a childless node from the tenant hierarchy.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          node_id: ID of the node to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes/{node_id}",
                account_id=account_id,
                structure_id=structure_id,
                node_id=node_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NodeDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[NodeDeleteResponse], ResultWrapper[NodeDeleteResponse]),
        )

    async def batch(
        self,
        structure_id: str,
        *,
        account_id: str,
        creates: Iterable[node_batch_params.Create],
        deletes: Iterable[node_batch_params.Delete],
        updates: Iterable[node_batch_params.Update],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NodeBatchResponse:
        """Atomically validates and applies 1 to 500 unordered node operations.

        Creates may
        reference new parents but cannot reuse a native_id deleted in the same batch.
        Maximum body size: 1 MiB.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          creates: Nodes to create; parents may be created elsewhere in this request

          deletes: Nodes to delete; every descendant that will not be reparented must also be
              deleted

          updates: Nodes whose mutable fields should be fully replaced

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes/batch",
                account_id=account_id,
                structure_id=structure_id,
            ),
            body=await async_maybe_transform(
                {
                    "creates": creates,
                    "deletes": deletes,
                    "updates": updates,
                },
                node_batch_params.NodeBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NodeBatchResponse]._unwrapper,
            ),
            cast_to=cast(Type[NodeBatchResponse], ResultWrapper[NodeBatchResponse]),
        )

    async def get(
        self,
        node_id: str,
        *,
        account_id: str,
        structure_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantStructureNode:
        """
        Returns the tenant node with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          structure_id: ID of the parent tenant structure

          node_id: ID of the node to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not structure_id:
            raise ValueError(f"Expected a non-empty value for `structure_id` but received {structure_id!r}")
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cws/tenant-structures/{structure_id}/nodes/{node_id}",
                account_id=account_id,
                structure_id=structure_id,
                node_id=node_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TenantStructureNode]._unwrapper,
            ),
            cast_to=cast(Type[TenantStructureNode], ResultWrapper[TenantStructureNode]),
        )


class NodesResourceWithRawResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.create = to_raw_response_wrapper(
            nodes.create,
        )
        self.update = to_raw_response_wrapper(
            nodes.update,
        )
        self.list = to_raw_response_wrapper(
            nodes.list,
        )
        self.delete = to_raw_response_wrapper(
            nodes.delete,
        )
        self.batch = to_raw_response_wrapper(
            nodes.batch,
        )
        self.get = to_raw_response_wrapper(
            nodes.get,
        )


class AsyncNodesResourceWithRawResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.create = async_to_raw_response_wrapper(
            nodes.create,
        )
        self.update = async_to_raw_response_wrapper(
            nodes.update,
        )
        self.list = async_to_raw_response_wrapper(
            nodes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            nodes.delete,
        )
        self.batch = async_to_raw_response_wrapper(
            nodes.batch,
        )
        self.get = async_to_raw_response_wrapper(
            nodes.get,
        )


class NodesResourceWithStreamingResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.create = to_streamed_response_wrapper(
            nodes.create,
        )
        self.update = to_streamed_response_wrapper(
            nodes.update,
        )
        self.list = to_streamed_response_wrapper(
            nodes.list,
        )
        self.delete = to_streamed_response_wrapper(
            nodes.delete,
        )
        self.batch = to_streamed_response_wrapper(
            nodes.batch,
        )
        self.get = to_streamed_response_wrapper(
            nodes.get,
        )


class AsyncNodesResourceWithStreamingResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.create = async_to_streamed_response_wrapper(
            nodes.create,
        )
        self.update = async_to_streamed_response_wrapper(
            nodes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            nodes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            nodes.delete,
        )
        self.batch = async_to_streamed_response_wrapper(
            nodes.batch,
        )
        self.get = async_to_streamed_response_wrapper(
            nodes.get,
        )
