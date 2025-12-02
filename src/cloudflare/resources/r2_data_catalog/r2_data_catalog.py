# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
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
from .namespaces.namespaces import (
    NamespacesResource,
    AsyncNamespacesResource,
    NamespacesResourceWithRawResponse,
    AsyncNamespacesResourceWithRawResponse,
    NamespacesResourceWithStreamingResponse,
    AsyncNamespacesResourceWithStreamingResponse,
)
from ...types.r2_data_catalog.r2_data_catalog_get_response import R2DataCatalogGetResponse
from ...types.r2_data_catalog.r2_data_catalog_list_response import R2DataCatalogListResponse
from ...types.r2_data_catalog.r2_data_catalog_enable_response import R2DataCatalogEnableResponse

__all__ = ["R2DataCatalogResource", "AsyncR2DataCatalogResource"]


class R2DataCatalogResource(SyncAPIResource):
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
    def with_raw_response(self) -> R2DataCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return R2DataCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> R2DataCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return R2DataCatalogResourceWithStreamingResponse(self)

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
    ) -> Optional[R2DataCatalogListResponse]:
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
            f"/accounts/{account_id}/r2-catalog",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[R2DataCatalogListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[R2DataCatalogListResponse]], ResultWrapper[R2DataCatalogListResponse]),
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
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/disable",
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
    ) -> Optional[R2DataCatalogEnableResponse]:
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
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[R2DataCatalogEnableResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[R2DataCatalogEnableResponse]], ResultWrapper[R2DataCatalogEnableResponse]),
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
    ) -> Optional[R2DataCatalogGetResponse]:
        """
        Retrieve detailed information about a specific R2 catalog by bucket name.
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
            f"/accounts/{account_id}/r2-catalog/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[R2DataCatalogGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[R2DataCatalogGetResponse]], ResultWrapper[R2DataCatalogGetResponse]),
        )


class AsyncR2DataCatalogResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncR2DataCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncR2DataCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncR2DataCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncR2DataCatalogResourceWithStreamingResponse(self)

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
    ) -> Optional[R2DataCatalogListResponse]:
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
            f"/accounts/{account_id}/r2-catalog",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[R2DataCatalogListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[R2DataCatalogListResponse]], ResultWrapper[R2DataCatalogListResponse]),
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
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/disable",
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
    ) -> Optional[R2DataCatalogEnableResponse]:
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
            f"/accounts/{account_id}/r2-catalog/{bucket_name}/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[R2DataCatalogEnableResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[R2DataCatalogEnableResponse]], ResultWrapper[R2DataCatalogEnableResponse]),
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
    ) -> Optional[R2DataCatalogGetResponse]:
        """
        Retrieve detailed information about a specific R2 catalog by bucket name.
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
            f"/accounts/{account_id}/r2-catalog/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[R2DataCatalogGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[R2DataCatalogGetResponse]], ResultWrapper[R2DataCatalogGetResponse]),
        )


class R2DataCatalogResourceWithRawResponse:
    def __init__(self, r2_data_catalog: R2DataCatalogResource) -> None:
        self._r2_data_catalog = r2_data_catalog

        self.list = to_raw_response_wrapper(
            r2_data_catalog.list,
        )
        self.disable = to_raw_response_wrapper(
            r2_data_catalog.disable,
        )
        self.enable = to_raw_response_wrapper(
            r2_data_catalog.enable,
        )
        self.get = to_raw_response_wrapper(
            r2_data_catalog.get,
        )

    @cached_property
    def maintenance_configs(self) -> MaintenanceConfigsResourceWithRawResponse:
        return MaintenanceConfigsResourceWithRawResponse(self._r2_data_catalog.maintenance_configs)

    @cached_property
    def credentials(self) -> CredentialsResourceWithRawResponse:
        return CredentialsResourceWithRawResponse(self._r2_data_catalog.credentials)

    @cached_property
    def namespaces(self) -> NamespacesResourceWithRawResponse:
        return NamespacesResourceWithRawResponse(self._r2_data_catalog.namespaces)


class AsyncR2DataCatalogResourceWithRawResponse:
    def __init__(self, r2_data_catalog: AsyncR2DataCatalogResource) -> None:
        self._r2_data_catalog = r2_data_catalog

        self.list = async_to_raw_response_wrapper(
            r2_data_catalog.list,
        )
        self.disable = async_to_raw_response_wrapper(
            r2_data_catalog.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            r2_data_catalog.enable,
        )
        self.get = async_to_raw_response_wrapper(
            r2_data_catalog.get,
        )

    @cached_property
    def maintenance_configs(self) -> AsyncMaintenanceConfigsResourceWithRawResponse:
        return AsyncMaintenanceConfigsResourceWithRawResponse(self._r2_data_catalog.maintenance_configs)

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithRawResponse:
        return AsyncCredentialsResourceWithRawResponse(self._r2_data_catalog.credentials)

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithRawResponse:
        return AsyncNamespacesResourceWithRawResponse(self._r2_data_catalog.namespaces)


class R2DataCatalogResourceWithStreamingResponse:
    def __init__(self, r2_data_catalog: R2DataCatalogResource) -> None:
        self._r2_data_catalog = r2_data_catalog

        self.list = to_streamed_response_wrapper(
            r2_data_catalog.list,
        )
        self.disable = to_streamed_response_wrapper(
            r2_data_catalog.disable,
        )
        self.enable = to_streamed_response_wrapper(
            r2_data_catalog.enable,
        )
        self.get = to_streamed_response_wrapper(
            r2_data_catalog.get,
        )

    @cached_property
    def maintenance_configs(self) -> MaintenanceConfigsResourceWithStreamingResponse:
        return MaintenanceConfigsResourceWithStreamingResponse(self._r2_data_catalog.maintenance_configs)

    @cached_property
    def credentials(self) -> CredentialsResourceWithStreamingResponse:
        return CredentialsResourceWithStreamingResponse(self._r2_data_catalog.credentials)

    @cached_property
    def namespaces(self) -> NamespacesResourceWithStreamingResponse:
        return NamespacesResourceWithStreamingResponse(self._r2_data_catalog.namespaces)


class AsyncR2DataCatalogResourceWithStreamingResponse:
    def __init__(self, r2_data_catalog: AsyncR2DataCatalogResource) -> None:
        self._r2_data_catalog = r2_data_catalog

        self.list = async_to_streamed_response_wrapper(
            r2_data_catalog.list,
        )
        self.disable = async_to_streamed_response_wrapper(
            r2_data_catalog.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            r2_data_catalog.enable,
        )
        self.get = async_to_streamed_response_wrapper(
            r2_data_catalog.get,
        )

    @cached_property
    def maintenance_configs(self) -> AsyncMaintenanceConfigsResourceWithStreamingResponse:
        return AsyncMaintenanceConfigsResourceWithStreamingResponse(self._r2_data_catalog.maintenance_configs)

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithStreamingResponse:
        return AsyncCredentialsResourceWithStreamingResponse(self._r2_data_catalog.credentials)

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithStreamingResponse:
        return AsyncNamespacesResourceWithStreamingResponse(self._r2_data_catalog.namespaces)
