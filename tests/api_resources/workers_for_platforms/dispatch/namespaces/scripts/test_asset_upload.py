# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import (
    AssetUploadCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssetUpload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        asset_upload = client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(Optional[AssetUploadCreateResponse], asset_upload, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        asset_upload = client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            manifest={
                "foo": {
                    "hash": "hash",
                    "size": 0,
                }
            },
        )
        assert_matches_type(Optional[AssetUploadCreateResponse], asset_upload, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.with_raw_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset_upload = response.parse()
        assert_matches_type(Optional[AssetUploadCreateResponse], asset_upload, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.with_streaming_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset_upload = response.parse()
            assert_matches_type(Optional[AssetUploadCreateResponse], asset_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.with_raw_response.create(
                script_name="this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.with_raw_response.create(
                script_name="this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.with_raw_response.create(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )


class TestAsyncAssetUpload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        asset_upload = await async_client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(Optional[AssetUploadCreateResponse], asset_upload, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asset_upload = await async_client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            manifest={
                "foo": {
                    "hash": "hash",
                    "size": 0,
                }
            },
        )
        assert_matches_type(Optional[AssetUploadCreateResponse], asset_upload, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.with_raw_response.create(
                script_name="this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset_upload = await response.parse()
        assert_matches_type(Optional[AssetUploadCreateResponse], asset_upload, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with (
            async_client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.with_streaming_response.create(
                script_name="this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset_upload = await response.parse()
            assert_matches_type(Optional[AssetUploadCreateResponse], asset_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.with_raw_response.create(
                script_name="this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.with_raw_response.create(
                script_name="this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.with_raw_response.create(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )
