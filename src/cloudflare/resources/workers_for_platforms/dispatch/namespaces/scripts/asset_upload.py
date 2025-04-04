# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Optional, cast

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import make_request_options
from ......types.workers_for_platforms.dispatch.namespaces.scripts import asset_upload_create_params
from ......types.workers_for_platforms.dispatch.namespaces.scripts.asset_upload_create_response import (
    AssetUploadCreateResponse,
)

__all__ = ["AssetUploadResource", "AsyncAssetUploadResource"]


class AssetUploadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetUploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AssetUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetUploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AssetUploadResourceWithStreamingResponse(self)

    def create(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        manifest: Dict[str, asset_upload_create_params.Manifest] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AssetUploadCreateResponse]:
        """Start uploading a collection of assets for use in a Worker version.

        To learn
        more about the direct uploads of assets, see
        https://developers.cloudflare.com/workers/static-assets/direct-upload/

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          manifest: A manifest ([path]: {hash, size}) map of files to upload. As an example,
              `/blog/hello-world.html` would be a valid path key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._post(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/assets-upload-session",
            body=maybe_transform({"manifest": manifest}, asset_upload_create_params.AssetUploadCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AssetUploadCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AssetUploadCreateResponse]], ResultWrapper[AssetUploadCreateResponse]),
        )


class AsyncAssetUploadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetUploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetUploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAssetUploadResourceWithStreamingResponse(self)

    async def create(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        manifest: Dict[str, asset_upload_create_params.Manifest] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AssetUploadCreateResponse]:
        """Start uploading a collection of assets for use in a Worker version.

        To learn
        more about the direct uploads of assets, see
        https://developers.cloudflare.com/workers/static-assets/direct-upload/

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          manifest: A manifest ([path]: {hash, size}) map of files to upload. As an example,
              `/blog/hello-world.html` would be a valid path key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._post(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/assets-upload-session",
            body=await async_maybe_transform(
                {"manifest": manifest}, asset_upload_create_params.AssetUploadCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AssetUploadCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AssetUploadCreateResponse]], ResultWrapper[AssetUploadCreateResponse]),
        )


class AssetUploadResourceWithRawResponse:
    def __init__(self, asset_upload: AssetUploadResource) -> None:
        self._asset_upload = asset_upload

        self.create = to_raw_response_wrapper(
            asset_upload.create,
        )


class AsyncAssetUploadResourceWithRawResponse:
    def __init__(self, asset_upload: AsyncAssetUploadResource) -> None:
        self._asset_upload = asset_upload

        self.create = async_to_raw_response_wrapper(
            asset_upload.create,
        )


class AssetUploadResourceWithStreamingResponse:
    def __init__(self, asset_upload: AssetUploadResource) -> None:
        self._asset_upload = asset_upload

        self.create = to_streamed_response_wrapper(
            asset_upload.create,
        )


class AsyncAssetUploadResourceWithStreamingResponse:
    def __init__(self, asset_upload: AsyncAssetUploadResource) -> None:
        self._asset_upload = asset_upload

        self.create = async_to_streamed_response_wrapper(
            asset_upload.create,
        )
