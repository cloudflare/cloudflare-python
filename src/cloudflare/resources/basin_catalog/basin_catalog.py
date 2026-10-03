# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .credentials import (
    CredentialsResource,
    AsyncCredentialsResource,
    CredentialsResourceWithRawResponse,
    AsyncCredentialsResourceWithRawResponse,
    CredentialsResourceWithStreamingResponse,
    AsyncCredentialsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .maintenance_configs import (
    MaintenanceConfigsResource,
    AsyncMaintenanceConfigsResource,
    MaintenanceConfigsResourceWithRawResponse,
    AsyncMaintenanceConfigsResourceWithRawResponse,
    MaintenanceConfigsResourceWithStreamingResponse,
    AsyncMaintenanceConfigsResourceWithStreamingResponse,
)
from ...types.basin_catalog import basin_catalog_delete_params
from .namespaces.namespaces import (
    NamespacesResource,
    AsyncNamespacesResource,
    NamespacesResourceWithRawResponse,
    AsyncNamespacesResourceWithRawResponse,
    NamespacesResourceWithStreamingResponse,
    AsyncNamespacesResourceWithStreamingResponse,
)
from ...types.basin_catalog.basin_catalog_get_response import BasinCatalogGetResponse
from ...types.basin_catalog.basin_catalog_list_response import BasinCatalogListResponse
from ...types.basin_catalog.basin_catalog_enable_response import BasinCatalogEnableResponse

__all__ = ["BasinCatalogResource", "AsyncBasinCatalogResource"]


class BasinCatalogResource(SyncAPIResource):
    @cached_property
    def maintenance_configs(self) -> MaintenanceConfigsResource:
        return MaintenanceConfigsResource(self._client)

    @cached_property
    def credentials(self) -> CredentialsResource:
        return CredentialsResource(self._client)

    @cached_property
    def namespaces(self) -> NamespacesResource:
        return NamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BasinCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BasinCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BasinCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BasinCatalogResourceWithStreamingResponse(self)

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
    ) -> Optional[BasinCatalogListResponse]:
        """
        Returns a list of R2 buckets that have been enabled as Apache Iceberg catalogs
        for the specified account. Each catalog represents an R2 bucket configured to
        store Iceberg metadata and data files.

        Args:
          account_id: Use this to identify the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/basin-catalog", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BasinCatalogListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BasinCatalogListResponse]], ResultWrapper[BasinCatalogListResponse]),
        )

    def delete(
        self,
        bucket_name: str,
        *,
        account_id: str,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes the catalog from the control plane without deleting R2 bucket objects.
        Set force=true to remove catalog namespaces, tables, views, and maintenance
        metadata. Force deletion is limited to a configured catalog object count.

        Args:
          account_id: Use this to identify the account.

          bucket_name: Specifies the R2 bucket name.

          force: Remove child metadata before deleting the catalog.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/accounts/{account_id}/basin-catalog/{bucket_name}/delete",
                account_id=account_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, basin_catalog_delete_params.BasinCatalogDeleteParams),
            ),
            cast_to=NoneType,
        )

    def disable(
        self,
        bucket_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Disable an R2 bucket as a catalog.

        This operation deactivates the catalog but
        preserves existing metadata and data files. The catalog can be re-enabled later.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/accounts/{account_id}/basin-catalog/{bucket_name}/disable",
                account_id=account_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def enable(
        self,
        bucket_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BasinCatalogEnableResponse]:
        """Enable an R2 bucket as an Apache Iceberg catalog.

        This operation creates the
        necessary catalog infrastructure and activates the bucket for storing Iceberg
        metadata and data files.

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
        return self._post(
            path_template(
                "/accounts/{account_id}/basin-catalog/{bucket_name}/enable",
                account_id=account_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BasinCatalogEnableResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BasinCatalogEnableResponse]], ResultWrapper[BasinCatalogEnableResponse]),
        )

    def get(
        self,
        bucket_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BasinCatalogGetResponse]:
        """
        Retrieve detailed information about a specific Basin Catalog by bucket name.
        Returns catalog status, maintenance configuration, and credential status.

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
        return self._get(
            path_template(
                "/accounts/{account_id}/basin-catalog/{bucket_name}", account_id=account_id, bucket_name=bucket_name
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BasinCatalogGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BasinCatalogGetResponse]], ResultWrapper[BasinCatalogGetResponse]),
        )


class AsyncBasinCatalogResource(AsyncAPIResource):
    @cached_property
    def maintenance_configs(self) -> AsyncMaintenanceConfigsResource:
        return AsyncMaintenanceConfigsResource(self._client)

    @cached_property
    def credentials(self) -> AsyncCredentialsResource:
        return AsyncCredentialsResource(self._client)

    @cached_property
    def namespaces(self) -> AsyncNamespacesResource:
        return AsyncNamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBasinCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBasinCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBasinCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBasinCatalogResourceWithStreamingResponse(self)

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
    ) -> Optional[BasinCatalogListResponse]:
        """
        Returns a list of R2 buckets that have been enabled as Apache Iceberg catalogs
        for the specified account. Each catalog represents an R2 bucket configured to
        store Iceberg metadata and data files.

        Args:
          account_id: Use this to identify the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/basin-catalog", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BasinCatalogListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BasinCatalogListResponse]], ResultWrapper[BasinCatalogListResponse]),
        )

    async def delete(
        self,
        bucket_name: str,
        *,
        account_id: str,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes the catalog from the control plane without deleting R2 bucket objects.
        Set force=true to remove catalog namespaces, tables, views, and maintenance
        metadata. Force deletion is limited to a configured catalog object count.

        Args:
          account_id: Use this to identify the account.

          bucket_name: Specifies the R2 bucket name.

          force: Remove child metadata before deleting the catalog.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/accounts/{account_id}/basin-catalog/{bucket_name}/delete",
                account_id=account_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force": force}, basin_catalog_delete_params.BasinCatalogDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def disable(
        self,
        bucket_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Disable an R2 bucket as a catalog.

        This operation deactivates the catalog but
        preserves existing metadata and data files. The catalog can be re-enabled later.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/accounts/{account_id}/basin-catalog/{bucket_name}/disable",
                account_id=account_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def enable(
        self,
        bucket_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BasinCatalogEnableResponse]:
        """Enable an R2 bucket as an Apache Iceberg catalog.

        This operation creates the
        necessary catalog infrastructure and activates the bucket for storing Iceberg
        metadata and data files.

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
        return await self._post(
            path_template(
                "/accounts/{account_id}/basin-catalog/{bucket_name}/enable",
                account_id=account_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BasinCatalogEnableResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BasinCatalogEnableResponse]], ResultWrapper[BasinCatalogEnableResponse]),
        )

    async def get(
        self,
        bucket_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BasinCatalogGetResponse]:
        """
        Retrieve detailed information about a specific Basin Catalog by bucket name.
        Returns catalog status, maintenance configuration, and credential status.

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
        return await self._get(
            path_template(
                "/accounts/{account_id}/basin-catalog/{bucket_name}", account_id=account_id, bucket_name=bucket_name
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BasinCatalogGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BasinCatalogGetResponse]], ResultWrapper[BasinCatalogGetResponse]),
        )


class BasinCatalogResourceWithRawResponse:
    def __init__(self, basin_catalog: BasinCatalogResource) -> None:
        self._basin_catalog = basin_catalog

        self.list = to_raw_response_wrapper(
            basin_catalog.list,
        )
        self.delete = to_raw_response_wrapper(
            basin_catalog.delete,
        )
        self.disable = to_raw_response_wrapper(
            basin_catalog.disable,
        )
        self.enable = to_raw_response_wrapper(
            basin_catalog.enable,
        )
        self.get = to_raw_response_wrapper(
            basin_catalog.get,
        )

    @cached_property
    def maintenance_configs(self) -> MaintenanceConfigsResourceWithRawResponse:
        return MaintenanceConfigsResourceWithRawResponse(self._basin_catalog.maintenance_configs)

    @cached_property
    def credentials(self) -> CredentialsResourceWithRawResponse:
        return CredentialsResourceWithRawResponse(self._basin_catalog.credentials)

    @cached_property
    def namespaces(self) -> NamespacesResourceWithRawResponse:
        return NamespacesResourceWithRawResponse(self._basin_catalog.namespaces)


class AsyncBasinCatalogResourceWithRawResponse:
    def __init__(self, basin_catalog: AsyncBasinCatalogResource) -> None:
        self._basin_catalog = basin_catalog

        self.list = async_to_raw_response_wrapper(
            basin_catalog.list,
        )
        self.delete = async_to_raw_response_wrapper(
            basin_catalog.delete,
        )
        self.disable = async_to_raw_response_wrapper(
            basin_catalog.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            basin_catalog.enable,
        )
        self.get = async_to_raw_response_wrapper(
            basin_catalog.get,
        )

    @cached_property
    def maintenance_configs(self) -> AsyncMaintenanceConfigsResourceWithRawResponse:
        return AsyncMaintenanceConfigsResourceWithRawResponse(self._basin_catalog.maintenance_configs)

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithRawResponse:
        return AsyncCredentialsResourceWithRawResponse(self._basin_catalog.credentials)

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithRawResponse:
        return AsyncNamespacesResourceWithRawResponse(self._basin_catalog.namespaces)


class BasinCatalogResourceWithStreamingResponse:
    def __init__(self, basin_catalog: BasinCatalogResource) -> None:
        self._basin_catalog = basin_catalog

        self.list = to_streamed_response_wrapper(
            basin_catalog.list,
        )
        self.delete = to_streamed_response_wrapper(
            basin_catalog.delete,
        )
        self.disable = to_streamed_response_wrapper(
            basin_catalog.disable,
        )
        self.enable = to_streamed_response_wrapper(
            basin_catalog.enable,
        )
        self.get = to_streamed_response_wrapper(
            basin_catalog.get,
        )

    @cached_property
    def maintenance_configs(self) -> MaintenanceConfigsResourceWithStreamingResponse:
        return MaintenanceConfigsResourceWithStreamingResponse(self._basin_catalog.maintenance_configs)

    @cached_property
    def credentials(self) -> CredentialsResourceWithStreamingResponse:
        return CredentialsResourceWithStreamingResponse(self._basin_catalog.credentials)

    @cached_property
    def namespaces(self) -> NamespacesResourceWithStreamingResponse:
        return NamespacesResourceWithStreamingResponse(self._basin_catalog.namespaces)


class AsyncBasinCatalogResourceWithStreamingResponse:
    def __init__(self, basin_catalog: AsyncBasinCatalogResource) -> None:
        self._basin_catalog = basin_catalog

        self.list = async_to_streamed_response_wrapper(
            basin_catalog.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            basin_catalog.delete,
        )
        self.disable = async_to_streamed_response_wrapper(
            basin_catalog.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            basin_catalog.enable,
        )
        self.get = async_to_streamed_response_wrapper(
            basin_catalog.get,
        )

    @cached_property
    def maintenance_configs(self) -> AsyncMaintenanceConfigsResourceWithStreamingResponse:
        return AsyncMaintenanceConfigsResourceWithStreamingResponse(self._basin_catalog.maintenance_configs)

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithStreamingResponse:
        return AsyncCredentialsResourceWithStreamingResponse(self._basin_catalog.credentials)

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithStreamingResponse:
        return AsyncNamespacesResourceWithStreamingResponse(self._basin_catalog.namespaces)
