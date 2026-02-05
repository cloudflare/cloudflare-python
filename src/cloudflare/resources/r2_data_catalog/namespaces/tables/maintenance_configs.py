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
from .....types.r2_data_catalog.namespaces.tables import maintenance_config_update_params
from .....types.r2_data_catalog.namespaces.tables.maintenance_config_get_response import MaintenanceConfigGetResponse
from .....types.r2_data_catalog.namespaces.tables.maintenance_config_update_response import (
    MaintenanceConfigUpdateResponse,
)

__all__ = ["MaintenanceConfigsResource", "AsyncMaintenanceConfigsResource"]


class MaintenanceConfigsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MaintenanceConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MaintenanceConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MaintenanceConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MaintenanceConfigsResourceWithStreamingResponse(self)

    def update(
        self,
        table_name: str,
        *,
        account_id: str,
        bucket_name: str,
        namespace: str,
        compaction: maintenance_config_update_params.Compaction | Omit = omit,
        snapshot_expiration: maintenance_config_update_params.SnapshotExpiration | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[MaintenanceConfigUpdateResponse]:
        """Update the maintenance configuration for a specific table.

        This allows you to
        enable or disable compaction and adjust target file sizes for optimization.

        Args:
          account_id: Use this to identify the account.

          bucket_name: Specifies the R2 bucket name.

          compaction: Updates compaction configuration (all fields optional).

          snapshot_expiration: Updates snapshot expiration configuration (all fields optional).

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
        if not table_name:
            raise ValueError(f"Expected a non-empty value for `table_name` but received {table_name!r}")
        return self._post(
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs",
            body=maybe_transform(
                {
                    "compaction": compaction,
                    "snapshot_expiration": snapshot_expiration,
                },
                maintenance_config_update_params.MaintenanceConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MaintenanceConfigUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[MaintenanceConfigUpdateResponse]], ResultWrapper[MaintenanceConfigUpdateResponse]
            ),
        )

    def get(
        self,
        table_name: str,
        *,
        account_id: str,
        bucket_name: str,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[MaintenanceConfigGetResponse]:
        """
        Retrieve the maintenance configuration for a specific table, including
        compaction settings.

        Args:
          account_id: Use this to identify the account.

          bucket_name: Specifies the R2 bucket name.

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
        if not table_name:
            raise ValueError(f"Expected a non-empty value for `table_name` but received {table_name!r}")
        return self._get(
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MaintenanceConfigGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MaintenanceConfigGetResponse]], ResultWrapper[MaintenanceConfigGetResponse]),
        )


class AsyncMaintenanceConfigsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMaintenanceConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMaintenanceConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMaintenanceConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMaintenanceConfigsResourceWithStreamingResponse(self)

    async def update(
        self,
        table_name: str,
        *,
        account_id: str,
        bucket_name: str,
        namespace: str,
        compaction: maintenance_config_update_params.Compaction | Omit = omit,
        snapshot_expiration: maintenance_config_update_params.SnapshotExpiration | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[MaintenanceConfigUpdateResponse]:
        """Update the maintenance configuration for a specific table.

        This allows you to
        enable or disable compaction and adjust target file sizes for optimization.

        Args:
          account_id: Use this to identify the account.

          bucket_name: Specifies the R2 bucket name.

          compaction: Updates compaction configuration (all fields optional).

          snapshot_expiration: Updates snapshot expiration configuration (all fields optional).

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
        if not table_name:
            raise ValueError(f"Expected a non-empty value for `table_name` but received {table_name!r}")
        return await self._post(
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs",
            body=await async_maybe_transform(
                {
                    "compaction": compaction,
                    "snapshot_expiration": snapshot_expiration,
                },
                maintenance_config_update_params.MaintenanceConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MaintenanceConfigUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[MaintenanceConfigUpdateResponse]], ResultWrapper[MaintenanceConfigUpdateResponse]
            ),
        )

    async def get(
        self,
        table_name: str,
        *,
        account_id: str,
        bucket_name: str,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[MaintenanceConfigGetResponse]:
        """
        Retrieve the maintenance configuration for a specific table, including
        compaction settings.

        Args:
          account_id: Use this to identify the account.

          bucket_name: Specifies the R2 bucket name.

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
        if not table_name:
            raise ValueError(f"Expected a non-empty value for `table_name` but received {table_name!r}")
        return await self._get(
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MaintenanceConfigGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MaintenanceConfigGetResponse]], ResultWrapper[MaintenanceConfigGetResponse]),
        )


class MaintenanceConfigsResourceWithRawResponse:
    def __init__(self, maintenance_configs: MaintenanceConfigsResource) -> None:
        self._maintenance_configs = maintenance_configs

        self.update = to_raw_response_wrapper(
            maintenance_configs.update,
        )
        self.get = to_raw_response_wrapper(
            maintenance_configs.get,
        )


class AsyncMaintenanceConfigsResourceWithRawResponse:
    def __init__(self, maintenance_configs: AsyncMaintenanceConfigsResource) -> None:
        self._maintenance_configs = maintenance_configs

        self.update = async_to_raw_response_wrapper(
            maintenance_configs.update,
        )
        self.get = async_to_raw_response_wrapper(
            maintenance_configs.get,
        )


class MaintenanceConfigsResourceWithStreamingResponse:
    def __init__(self, maintenance_configs: MaintenanceConfigsResource) -> None:
        self._maintenance_configs = maintenance_configs

        self.update = to_streamed_response_wrapper(
            maintenance_configs.update,
        )
        self.get = to_streamed_response_wrapper(
            maintenance_configs.get,
        )


class AsyncMaintenanceConfigsResourceWithStreamingResponse:
    def __init__(self, maintenance_configs: AsyncMaintenanceConfigsResource) -> None:
        self._maintenance_configs = maintenance_configs

        self.update = async_to_streamed_response_wrapper(
            maintenance_configs.update,
        )
        self.get = async_to_streamed_response_wrapper(
            maintenance_configs.get,
        )
