# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.casb.posture import asset_schema_list_params
from .....types.zero_trust.casb.posture.asset_schema_get_response import AssetSchemaGetResponse
from .....types.zero_trust.casb.posture.asset_schema_list_response import AssetSchemaListResponse

__all__ = ["AssetSchemasResource", "AsyncAssetSchemasResource"]


class AssetSchemasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AssetSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AssetSchemasResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        vendor: Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
            "WORKDAY",
            "ZOOM",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[AssetSchemaListResponse]:
        """
        Returns the catalog of asset classes available when authoring custom findings,
        grouped by vendor. Optionally filter to a single vendor with the `vendor` query
        parameter.

        Args:
          vendor: Restrict the result to a single vendor. Unknown values return 400.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/asset_schemas", account_id=account_id),
            page=SyncSinglePage[AssetSchemaListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"vendor": vendor}, asset_schema_list_params.AssetSchemaListParams),
            ),
            model=AssetSchemaListResponse,
        )

    def get(
        self,
        asset_class: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AssetSchemaGetResponse]:
        """
        Returns the fields and related attributes a custom finding type may reference
        for the given asset class (JSON Schema). Used by the custom finding types
        builder.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not asset_class:
            raise ValueError(f"Expected a non-empty value for `asset_class` but received {asset_class!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/data-security/posture/asset_schemas/{asset_class}",
                account_id=account_id,
                asset_class=asset_class,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AssetSchemaGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AssetSchemaGetResponse]], ResultWrapper[AssetSchemaGetResponse]),
        )


class AsyncAssetSchemasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAssetSchemasResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        vendor: Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
            "WORKDAY",
            "ZOOM",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AssetSchemaListResponse, AsyncSinglePage[AssetSchemaListResponse]]:
        """
        Returns the catalog of asset classes available when authoring custom findings,
        grouped by vendor. Optionally filter to a single vendor with the `vendor` query
        parameter.

        Args:
          vendor: Restrict the result to a single vendor. Unknown values return 400.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/asset_schemas", account_id=account_id),
            page=AsyncSinglePage[AssetSchemaListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"vendor": vendor}, asset_schema_list_params.AssetSchemaListParams),
            ),
            model=AssetSchemaListResponse,
        )

    async def get(
        self,
        asset_class: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AssetSchemaGetResponse]:
        """
        Returns the fields and related attributes a custom finding type may reference
        for the given asset class (JSON Schema). Used by the custom finding types
        builder.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not asset_class:
            raise ValueError(f"Expected a non-empty value for `asset_class` but received {asset_class!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/data-security/posture/asset_schemas/{asset_class}",
                account_id=account_id,
                asset_class=asset_class,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AssetSchemaGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AssetSchemaGetResponse]], ResultWrapper[AssetSchemaGetResponse]),
        )


class AssetSchemasResourceWithRawResponse:
    def __init__(self, asset_schemas: AssetSchemasResource) -> None:
        self._asset_schemas = asset_schemas

        self.list = to_raw_response_wrapper(
            asset_schemas.list,
        )
        self.get = to_raw_response_wrapper(
            asset_schemas.get,
        )


class AsyncAssetSchemasResourceWithRawResponse:
    def __init__(self, asset_schemas: AsyncAssetSchemasResource) -> None:
        self._asset_schemas = asset_schemas

        self.list = async_to_raw_response_wrapper(
            asset_schemas.list,
        )
        self.get = async_to_raw_response_wrapper(
            asset_schemas.get,
        )


class AssetSchemasResourceWithStreamingResponse:
    def __init__(self, asset_schemas: AssetSchemasResource) -> None:
        self._asset_schemas = asset_schemas

        self.list = to_streamed_response_wrapper(
            asset_schemas.list,
        )
        self.get = to_streamed_response_wrapper(
            asset_schemas.get,
        )


class AsyncAssetSchemasResourceWithStreamingResponse:
    def __init__(self, asset_schemas: AsyncAssetSchemasResource) -> None:
        self._asset_schemas = asset_schemas

        self.list = async_to_streamed_response_wrapper(
            asset_schemas.list,
        )
        self.get = async_to_streamed_response_wrapper(
            asset_schemas.get,
        )
