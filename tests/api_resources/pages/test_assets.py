# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.pages import (
    AssetUploadResponse,
    AssetCheckMissingResponse,
    AssetUpsertHashesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_check_missing(self, client: Cloudflare) -> None:
        asset = client.pages.assets.check_missing(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        )
        assert_matches_type(SyncSinglePage[AssetCheckMissingResponse], asset, path=["response"])

    @parametrize
    def test_raw_response_check_missing(self, client: Cloudflare) -> None:
        response = client.pages.assets.with_raw_response.check_missing(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(SyncSinglePage[AssetCheckMissingResponse], asset, path=["response"])

    @parametrize
    def test_streaming_response_check_missing(self, client: Cloudflare) -> None:
        with client.pages.assets.with_streaming_response.check_missing(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(SyncSinglePage[AssetCheckMissingResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload(self, client: Cloudflare) -> None:
        asset = client.pages.assets.upload(
            body=[
                {
                    "base64": True,
                    "key": "b026324c6904b2a9cb4b88d6d61c81d1",
                    "metadata": {"content_type": "text/plain"},
                    "value": "SGVsbG8sIFdvcmxkIQ==",
                }
            ],
        )
        assert_matches_type(AssetUploadResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Cloudflare) -> None:
        response = client.pages.assets.with_raw_response.upload(
            body=[
                {
                    "base64": True,
                    "key": "b026324c6904b2a9cb4b88d6d61c81d1",
                    "metadata": {"content_type": "text/plain"},
                    "value": "SGVsbG8sIFdvcmxkIQ==",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetUploadResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Cloudflare) -> None:
        with client.pages.assets.with_streaming_response.upload(
            body=[
                {
                    "base64": True,
                    "key": "b026324c6904b2a9cb4b88d6d61c81d1",
                    "metadata": {"content_type": "text/plain"},
                    "value": "SGVsbG8sIFdvcmxkIQ==",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetUploadResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upsert_hashes(self, client: Cloudflare) -> None:
        asset = client.pages.assets.upsert_hashes(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        )
        assert_matches_type(AssetUpsertHashesResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_upsert_hashes(self, client: Cloudflare) -> None:
        response = client.pages.assets.with_raw_response.upsert_hashes(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetUpsertHashesResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_upsert_hashes(self, client: Cloudflare) -> None:
        with client.pages.assets.with_streaming_response.upsert_hashes(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetUpsertHashesResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_check_missing(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.pages.assets.check_missing(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        )
        assert_matches_type(AsyncSinglePage[AssetCheckMissingResponse], asset, path=["response"])

    @parametrize
    async def test_raw_response_check_missing(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.assets.with_raw_response.check_missing(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AsyncSinglePage[AssetCheckMissingResponse], asset, path=["response"])

    @parametrize
    async def test_streaming_response_check_missing(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.assets.with_streaming_response.check_missing(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AsyncSinglePage[AssetCheckMissingResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.pages.assets.upload(
            body=[
                {
                    "base64": True,
                    "key": "b026324c6904b2a9cb4b88d6d61c81d1",
                    "metadata": {"content_type": "text/plain"},
                    "value": "SGVsbG8sIFdvcmxkIQ==",
                }
            ],
        )
        assert_matches_type(AssetUploadResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.assets.with_raw_response.upload(
            body=[
                {
                    "base64": True,
                    "key": "b026324c6904b2a9cb4b88d6d61c81d1",
                    "metadata": {"content_type": "text/plain"},
                    "value": "SGVsbG8sIFdvcmxkIQ==",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetUploadResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.assets.with_streaming_response.upload(
            body=[
                {
                    "base64": True,
                    "key": "b026324c6904b2a9cb4b88d6d61c81d1",
                    "metadata": {"content_type": "text/plain"},
                    "value": "SGVsbG8sIFdvcmxkIQ==",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetUploadResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upsert_hashes(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.pages.assets.upsert_hashes(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        )
        assert_matches_type(AssetUpsertHashesResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_upsert_hashes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.assets.with_raw_response.upsert_hashes(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetUpsertHashesResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_upsert_hashes(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.assets.with_streaming_response.upsert_hashes(
            hashes=["a948904f2f0f479b8f936b8a0c5d9882", "b026324c6904b2a9cb4b88d6d61c81d1"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetUpsertHashesResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True
