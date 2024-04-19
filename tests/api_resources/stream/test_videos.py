# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import VideoStorageUsageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_storage_usage(self, client: Cloudflare) -> None:
        video = client.stream.videos.storage_usage(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VideoStorageUsageResponse], video, path=["response"])

    @parametrize
    def test_method_storage_usage_with_all_params(self, client: Cloudflare) -> None:
        video = client.stream.videos.storage_usage(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            creator="creator-id_abcde12345",
        )
        assert_matches_type(Optional[VideoStorageUsageResponse], video, path=["response"])

    @parametrize
    def test_raw_response_storage_usage(self, client: Cloudflare) -> None:
        response = client.stream.videos.with_raw_response.storage_usage(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(Optional[VideoStorageUsageResponse], video, path=["response"])

    @parametrize
    def test_streaming_response_storage_usage(self, client: Cloudflare) -> None:
        with client.stream.videos.with_streaming_response.storage_usage(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(Optional[VideoStorageUsageResponse], video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_storage_usage(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.videos.with_raw_response.storage_usage(
                account_id="",
            )


class TestAsyncVideos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_storage_usage(self, async_client: AsyncCloudflare) -> None:
        video = await async_client.stream.videos.storage_usage(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VideoStorageUsageResponse], video, path=["response"])

    @parametrize
    async def test_method_storage_usage_with_all_params(self, async_client: AsyncCloudflare) -> None:
        video = await async_client.stream.videos.storage_usage(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            creator="creator-id_abcde12345",
        )
        assert_matches_type(Optional[VideoStorageUsageResponse], video, path=["response"])

    @parametrize
    async def test_raw_response_storage_usage(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.videos.with_raw_response.storage_usage(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(Optional[VideoStorageUsageResponse], video, path=["response"])

    @parametrize
    async def test_streaming_response_storage_usage(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.videos.with_streaming_response.storage_usage(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(Optional[VideoStorageUsageResponse], video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_storage_usage(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.videos.with_raw_response.storage_usage(
                account_id="",
            )
