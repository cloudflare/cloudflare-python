# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSinglePage, AsyncSinglePage
from ...types.pages import asset_upload_params, asset_check_missing_params, asset_upsert_hashes_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.pages.asset_upload_response import AssetUploadResponse
from ...types.pages.asset_check_missing_response import AssetCheckMissingResponse
from ...types.pages.asset_upsert_hashes_response import AssetUpsertHashesResponse

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

    def check_missing(
        self,
        *,
        hashes: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[AssetCheckMissingResponse]:
        """
        Check which of the provided file hashes are missing from the Pages asset store.
        Returns a list of missing hashes that need to be uploaded. Used as part of the
        Pages Direct Upload workflow.

        Authenticate with the JWT obtained from the upload-token endpoint: GET
        /accounts/{account_id}/pages/projects/{project_name}/upload-token

        Args:
          hashes: List of file content hashes to check for existence in the asset store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/pages/assets/check-missing",
            page=SyncSinglePage[AssetCheckMissingResponse],
            body=maybe_transform({"hashes": hashes}, asset_check_missing_params.AssetCheckMissingParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
            method="post",
        )

    def upload(
        self,
        *,
        body: Iterable[asset_upload_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUploadResponse:
        """Upload one or more files to the Pages asset store.

        Each file is identified by
        its content hash and is uploaded using the same JSON shape as the Cloudflare KV
        bulk write API. Used as part of the Pages Direct Upload workflow.

        Authenticate with the JWT obtained from the upload-token endpoint: GET
        /accounts/{account_id}/pages/projects/{project_name}/upload-token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pages/assets/upload",
            body=maybe_transform(body, Iterable[asset_upload_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUploadResponse,
        )

    def upsert_hashes(
        self,
        *,
        hashes: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUpsertHashesResponse:
        """
        Register the provided file hashes as recently uploaded to the Pages asset store.
        Used as part of the Pages Direct Upload workflow so future deployments can avoid
        re-uploading files that are already present.

        Authenticate with the JWT obtained from the upload-token endpoint: GET
        /accounts/{account_id}/pages/projects/{project_name}/upload-token

        Args:
          hashes: List of file content hashes to register in the asset store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pages/assets/upsert-hashes",
            body=maybe_transform({"hashes": hashes}, asset_upsert_hashes_params.AssetUpsertHashesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUpsertHashesResponse,
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

    def check_missing(
        self,
        *,
        hashes: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AssetCheckMissingResponse, AsyncSinglePage[AssetCheckMissingResponse]]:
        """
        Check which of the provided file hashes are missing from the Pages asset store.
        Returns a list of missing hashes that need to be uploaded. Used as part of the
        Pages Direct Upload workflow.

        Authenticate with the JWT obtained from the upload-token endpoint: GET
        /accounts/{account_id}/pages/projects/{project_name}/upload-token

        Args:
          hashes: List of file content hashes to check for existence in the asset store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/pages/assets/check-missing",
            page=AsyncSinglePage[AssetCheckMissingResponse],
            body=maybe_transform({"hashes": hashes}, asset_check_missing_params.AssetCheckMissingParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
            method="post",
        )

    async def upload(
        self,
        *,
        body: Iterable[asset_upload_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUploadResponse:
        """Upload one or more files to the Pages asset store.

        Each file is identified by
        its content hash and is uploaded using the same JSON shape as the Cloudflare KV
        bulk write API. Used as part of the Pages Direct Upload workflow.

        Authenticate with the JWT obtained from the upload-token endpoint: GET
        /accounts/{account_id}/pages/projects/{project_name}/upload-token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pages/assets/upload",
            body=await async_maybe_transform(body, Iterable[asset_upload_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUploadResponse,
        )

    async def upsert_hashes(
        self,
        *,
        hashes: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUpsertHashesResponse:
        """
        Register the provided file hashes as recently uploaded to the Pages asset store.
        Used as part of the Pages Direct Upload workflow so future deployments can avoid
        re-uploading files that are already present.

        Authenticate with the JWT obtained from the upload-token endpoint: GET
        /accounts/{account_id}/pages/projects/{project_name}/upload-token

        Args:
          hashes: List of file content hashes to register in the asset store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pages/assets/upsert-hashes",
            body=await async_maybe_transform({"hashes": hashes}, asset_upsert_hashes_params.AssetUpsertHashesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUpsertHashesResponse,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.check_missing = to_raw_response_wrapper(
            assets.check_missing,
        )
        self.upload = to_raw_response_wrapper(
            assets.upload,
        )
        self.upsert_hashes = to_raw_response_wrapper(
            assets.upsert_hashes,
        )


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.check_missing = async_to_raw_response_wrapper(
            assets.check_missing,
        )
        self.upload = async_to_raw_response_wrapper(
            assets.upload,
        )
        self.upsert_hashes = async_to_raw_response_wrapper(
            assets.upsert_hashes,
        )


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.check_missing = to_streamed_response_wrapper(
            assets.check_missing,
        )
        self.upload = to_streamed_response_wrapper(
            assets.upload,
        )
        self.upsert_hashes = to_streamed_response_wrapper(
            assets.upsert_hashes,
        )


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.check_missing = async_to_streamed_response_wrapper(
            assets.check_missing,
        )
        self.upload = async_to_streamed_response_wrapper(
            assets.upload,
        )
        self.upsert_hashes = async_to_streamed_response_wrapper(
            assets.upsert_hashes,
        )
