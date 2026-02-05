# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from .tables.tables import (
    TablesResource,
    AsyncTablesResource,
    TablesResourceWithRawResponse,
    AsyncTablesResourceWithRawResponse,
    TablesResourceWithStreamingResponse,
    AsyncTablesResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.r2_data_catalog import namespace_list_params
from ....types.r2_data_catalog.namespace_list_response import NamespaceListResponse

__all__ = ["NamespacesResource", "AsyncNamespacesResource"]


class NamespacesResource(SyncAPIResource):
    @cached_property
    def tables(self) -> TablesResource:
        return TablesResource(self._client)

    @cached_property
    def with_raw_response(self) -> NamespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return NamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return NamespacesResourceWithStreamingResponse(self)

    def list(
        self,
        bucket_name: str,
        *,
        account_id: str,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        parent: str | Omit = omit,
        return_details: bool | Omit = omit,
        return_uuids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[NamespaceListResponse]:
        """Returns a list of namespaces in the specified R2 catalog.

        Supports hierarchical
        filtering and pagination for efficient traversal of large namespace hierarchies.

        Args:
          account_id: Use this to identify the account.

          bucket_name: Specifies the R2 bucket name.

          page_size: Maximum number of namespaces to return per page. Defaults to 100, maximum 1000.

          page_token: Opaque pagination token from a previous response. Use this to fetch the next
              page of results.

          parent: Parent namespace to filter by. Only returns direct children of this namespace.
              For nested namespaces, use %1F as separator (e.g., "bronze%1Fanalytics"). Omit
              this parameter to list top-level namespaces.

          return_details: Whether to include additional metadata (timestamps). When true, response
              includes created_at and updated_at arrays.

          return_uuids: Whether to include namespace UUIDs in the response. Set to true to receive the
              namespace_uuids array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._get(
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "parent": parent,
                        "return_details": return_details,
                        "return_uuids": return_uuids,
                    },
                    namespace_list_params.NamespaceListParams,
                ),
                post_parser=ResultWrapper[Optional[NamespaceListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceListResponse]], ResultWrapper[NamespaceListResponse]),
        )


class AsyncNamespacesResource(AsyncAPIResource):
    @cached_property
    def tables(self) -> AsyncTablesResource:
        return AsyncTablesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncNamespacesResourceWithStreamingResponse(self)

    async def list(
        self,
        bucket_name: str,
        *,
        account_id: str,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        parent: str | Omit = omit,
        return_details: bool | Omit = omit,
        return_uuids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[NamespaceListResponse]:
        """Returns a list of namespaces in the specified R2 catalog.

        Supports hierarchical
        filtering and pagination for efficient traversal of large namespace hierarchies.

        Args:
          account_id: Use this to identify the account.

          bucket_name: Specifies the R2 bucket name.

          page_size: Maximum number of namespaces to return per page. Defaults to 100, maximum 1000.

          page_token: Opaque pagination token from a previous response. Use this to fetch the next
              page of results.

          parent: Parent namespace to filter by. Only returns direct children of this namespace.
              For nested namespaces, use %1F as separator (e.g., "bronze%1Fanalytics"). Omit
              this parameter to list top-level namespaces.

          return_details: Whether to include additional metadata (timestamps). When true, response
              includes created_at and updated_at arrays.

          return_uuids: Whether to include namespace UUIDs in the response. Set to true to receive the
              namespace_uuids array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._get(
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "parent": parent,
                        "return_details": return_details,
                        "return_uuids": return_uuids,
                    },
                    namespace_list_params.NamespaceListParams,
                ),
                post_parser=ResultWrapper[Optional[NamespaceListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceListResponse]], ResultWrapper[NamespaceListResponse]),
        )


class NamespacesResourceWithRawResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = to_raw_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def tables(self) -> TablesResourceWithRawResponse:
        return TablesResourceWithRawResponse(self._namespaces.tables)


class AsyncNamespacesResourceWithRawResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = async_to_raw_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def tables(self) -> AsyncTablesResourceWithRawResponse:
        return AsyncTablesResourceWithRawResponse(self._namespaces.tables)


class NamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = to_streamed_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def tables(self) -> TablesResourceWithStreamingResponse:
        return TablesResourceWithStreamingResponse(self._namespaces.tables)


class AsyncNamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = async_to_streamed_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def tables(self) -> AsyncTablesResourceWithStreamingResponse:
        return AsyncTablesResourceWithStreamingResponse(self._namespaces.tables)
