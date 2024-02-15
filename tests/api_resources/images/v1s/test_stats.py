# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.images.v1s import StatCloudflareImagesImagesUsageStatisticsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_images_images_usage_statistics(self, client: Cloudflare) -> None:
        stat = client.images.v1s.stats.cloudflare_images_images_usage_statistics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StatCloudflareImagesImagesUsageStatisticsResponse, stat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cloudflare_images_images_usage_statistics(self, client: Cloudflare) -> None:
        response = client.images.v1s.stats.with_raw_response.cloudflare_images_images_usage_statistics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatCloudflareImagesImagesUsageStatisticsResponse, stat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cloudflare_images_images_usage_statistics(self, client: Cloudflare) -> None:
        with client.images.v1s.stats.with_streaming_response.cloudflare_images_images_usage_statistics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatCloudflareImagesImagesUsageStatisticsResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cloudflare_images_images_usage_statistics(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.stats.with_raw_response.cloudflare_images_images_usage_statistics(
                "",
            )


class TestAsyncStats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_images_images_usage_statistics(self, async_client: AsyncCloudflare) -> None:
        stat = await async_client.images.v1s.stats.cloudflare_images_images_usage_statistics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StatCloudflareImagesImagesUsageStatisticsResponse, stat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cloudflare_images_images_usage_statistics(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1s.stats.with_raw_response.cloudflare_images_images_usage_statistics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatCloudflareImagesImagesUsageStatisticsResponse, stat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cloudflare_images_images_usage_statistics(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.images.v1s.stats.with_streaming_response.cloudflare_images_images_usage_statistics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatCloudflareImagesImagesUsageStatisticsResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cloudflare_images_images_usage_statistics(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.stats.with_raw_response.cloudflare_images_images_usage_statistics(
                "",
            )
