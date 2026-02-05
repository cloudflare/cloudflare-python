# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .maintenance_configs import (
    MaintenanceConfigsResource,
    AsyncMaintenanceConfigsResource,
    MaintenanceConfigsResourceWithRawResponse,
    AsyncMaintenanceConfigsResourceWithRawResponse,
    MaintenanceConfigsResourceWithStreamingResponse,
    AsyncMaintenanceConfigsResourceWithStreamingResponse,
)
from .....types.r2_data_catalog.namespaces import table_list_params
from .....types.r2_data_catalog.namespaces.table_list_response import TableListResponse

__all__ = ["TablesResource", "AsyncTablesResource"]


class TablesResource(SyncAPIResource):
    @cached_property
    def maintenance_configs(self) -> MaintenanceConfigsResource:
        return MaintenanceConfigsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TablesResourceWithStreamingResponse(self)

    def list(
        self,
        namespace: str,
        *,
        account_id: str,
        bucket_name: str,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        return_details: bool | Omit = omit,
        return_uuids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TableListResponse]:
        """
        Returns a list of tables in the specified namespace within an R2 catalog.
        Supports pagination for efficient traversal of large table collections.

        Args:
          account_id: Use this to identify the account.

          bucket_name: Specifies the R2 bucket name.

          page_size: Maximum number of tables to return per page. Defaults to 100, maximum 1000.

          page_token: Opaque pagination token from a previous response. Use this to fetch the next
              page of results.

          return_details: Whether to include additional metadata (timestamps, locations). When true,
              response includes created_at, updated_at, metadata_locations, and locations
              arrays.

          return_uuids: Whether to include table UUIDs in the response. Set to true to receive the
              table_uuids array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._get(
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "return_details": return_details,
                        "return_uuids": return_uuids,
                    },
                    table_list_params.TableListParams,
                ),
                post_parser=ResultWrapper[Optional[TableListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TableListResponse]], ResultWrapper[TableListResponse]),
        )


class AsyncTablesResource(AsyncAPIResource):
    @cached_property
    def maintenance_configs(self) -> AsyncMaintenanceConfigsResource:
        return AsyncMaintenanceConfigsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTablesResourceWithStreamingResponse(self)

    async def list(
        self,
        namespace: str,
        *,
        account_id: str,
        bucket_name: str,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        return_details: bool | Omit = omit,
        return_uuids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TableListResponse]:
        """
        Returns a list of tables in the specified namespace within an R2 catalog.
        Supports pagination for efficient traversal of large table collections.

        Args:
          account_id: Use this to identify the account.

          bucket_name: Specifies the R2 bucket name.

          page_size: Maximum number of tables to return per page. Defaults to 100, maximum 1000.

          page_token: Opaque pagination token from a previous response. Use this to fetch the next
              page of results.

          return_details: Whether to include additional metadata (timestamps, locations). When true,
              response includes created_at, updated_at, metadata_locations, and locations
              arrays.

          return_uuids: Whether to include table UUIDs in the response. Set to true to receive the
              table_uuids array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._get(
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "return_details": return_details,
                        "return_uuids": return_uuids,
                    },
                    table_list_params.TableListParams,
                ),
                post_parser=ResultWrapper[Optional[TableListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TableListResponse]], ResultWrapper[TableListResponse]),
        )


class TablesResourceWithRawResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.list = to_raw_response_wrapper(
            tables.list,
        )

    @cached_property
    def maintenance_configs(self) -> MaintenanceConfigsResourceWithRawResponse:
        return MaintenanceConfigsResourceWithRawResponse(self._tables.maintenance_configs)


class AsyncTablesResourceWithRawResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.list = async_to_raw_response_wrapper(
            tables.list,
        )

    @cached_property
    def maintenance_configs(self) -> AsyncMaintenanceConfigsResourceWithRawResponse:
        return AsyncMaintenanceConfigsResourceWithRawResponse(self._tables.maintenance_configs)


class TablesResourceWithStreamingResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.list = to_streamed_response_wrapper(
            tables.list,
        )

    @cached_property
    def maintenance_configs(self) -> MaintenanceConfigsResourceWithStreamingResponse:
        return MaintenanceConfigsResourceWithStreamingResponse(self._tables.maintenance_configs)


class AsyncTablesResourceWithStreamingResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.list = async_to_streamed_response_wrapper(
            tables.list,
        )

    @cached_property
    def maintenance_configs(self) -> AsyncMaintenanceConfigsResourceWithStreamingResponse:
        return AsyncMaintenanceConfigsResourceWithStreamingResponse(self._tables.maintenance_configs)
