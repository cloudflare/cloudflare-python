# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloudforce_one.requests import asset_create_params, asset_update_params
from ....types.cloudforce_one.requests.asset_get_response import AssetGetResponse
from ....types.cloudforce_one.requests.asset_create_response import AssetCreateResponse
from ....types.cloudforce_one.requests.asset_delete_response import AssetDeleteResponse
from ....types.cloudforce_one.requests.asset_update_response import AssetUpdateResponse

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AssetsResourceWithStreamingResponse(self)

    def create(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
        page: int,
        per_page: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[AssetCreateResponse]:
        """
        List Request Assets

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          page: Page number of results

          per_page: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        return self._get_api_list(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/asset",
            page=SyncSinglePage[AssetCreateResponse],
            body=maybe_transform(
                {
                    "page": page,
                    "per_page": per_page,
                },
                asset_create_params.AssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AssetCreateResponse,
            method="post",
        )

    def update(
        self,
        asset_identifer: str,
        *,
        account_identifier: str,
        request_identifier: str,
        source: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AssetUpdateResponse]:
        """
        Update a Request Asset

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          asset_identifer: UUID

          source: Asset file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        if not asset_identifer:
            raise ValueError(f"Expected a non-empty value for `asset_identifer` but received {asset_identifer!r}")
        return self._put(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/asset/{asset_identifer}",
            body=maybe_transform({"source": source}, asset_update_params.AssetUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AssetUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AssetUpdateResponse]], ResultWrapper[AssetUpdateResponse]),
        )

    def delete(
        self,
        asset_identifer: str,
        *,
        account_identifier: str,
        request_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetDeleteResponse:
        """
        Delete a Request Asset

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          asset_identifer: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        if not asset_identifer:
            raise ValueError(f"Expected a non-empty value for `asset_identifer` but received {asset_identifer!r}")
        return self._delete(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/asset/{asset_identifer}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetDeleteResponse,
        )

    def get(
        self,
        asset_identifer: str,
        *,
        account_identifier: str,
        request_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[AssetGetResponse]:
        """
        Get a Request Asset

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          asset_identifer: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        if not asset_identifer:
            raise ValueError(f"Expected a non-empty value for `asset_identifer` but received {asset_identifer!r}")
        return self._get_api_list(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/asset/{asset_identifer}",
            page=SyncSinglePage[AssetGetResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AssetGetResponse,
        )


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAssetsResourceWithStreamingResponse(self)

    def create(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
        page: int,
        per_page: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AssetCreateResponse, AsyncSinglePage[AssetCreateResponse]]:
        """
        List Request Assets

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          page: Page number of results

          per_page: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        return self._get_api_list(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/asset",
            page=AsyncSinglePage[AssetCreateResponse],
            body=maybe_transform(
                {
                    "page": page,
                    "per_page": per_page,
                },
                asset_create_params.AssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AssetCreateResponse,
            method="post",
        )

    async def update(
        self,
        asset_identifer: str,
        *,
        account_identifier: str,
        request_identifier: str,
        source: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AssetUpdateResponse]:
        """
        Update a Request Asset

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          asset_identifer: UUID

          source: Asset file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        if not asset_identifer:
            raise ValueError(f"Expected a non-empty value for `asset_identifer` but received {asset_identifer!r}")
        return await self._put(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/asset/{asset_identifer}",
            body=await async_maybe_transform({"source": source}, asset_update_params.AssetUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AssetUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AssetUpdateResponse]], ResultWrapper[AssetUpdateResponse]),
        )

    async def delete(
        self,
        asset_identifer: str,
        *,
        account_identifier: str,
        request_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetDeleteResponse:
        """
        Delete a Request Asset

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          asset_identifer: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        if not asset_identifer:
            raise ValueError(f"Expected a non-empty value for `asset_identifer` but received {asset_identifer!r}")
        return await self._delete(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/asset/{asset_identifer}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetDeleteResponse,
        )

    def get(
        self,
        asset_identifer: str,
        *,
        account_identifier: str,
        request_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AssetGetResponse, AsyncSinglePage[AssetGetResponse]]:
        """
        Get a Request Asset

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          asset_identifer: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        if not asset_identifer:
            raise ValueError(f"Expected a non-empty value for `asset_identifer` but received {asset_identifer!r}")
        return self._get_api_list(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/asset/{asset_identifer}",
            page=AsyncSinglePage[AssetGetResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AssetGetResponse,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_raw_response_wrapper(
            assets.create,
        )
        self.update = to_raw_response_wrapper(
            assets.update,
        )
        self.delete = to_raw_response_wrapper(
            assets.delete,
        )
        self.get = to_raw_response_wrapper(
            assets.get,
        )


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_raw_response_wrapper(
            assets.create,
        )
        self.update = async_to_raw_response_wrapper(
            assets.update,
        )
        self.delete = async_to_raw_response_wrapper(
            assets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            assets.get,
        )


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_streamed_response_wrapper(
            assets.create,
        )
        self.update = to_streamed_response_wrapper(
            assets.update,
        )
        self.delete = to_streamed_response_wrapper(
            assets.delete,
        )
        self.get = to_streamed_response_wrapper(
            assets.get,
        )


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_streamed_response_wrapper(
            assets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            assets.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            assets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            assets.get,
        )
