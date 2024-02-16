# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    CacheRegionalTieredCachesResponse,
    CacheUpdateRegionalTieredCacheResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCache:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_regional_tiered_caches(self, client: Cloudflare) -> None:
        cache = client.cache.regional_tiered_caches(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheRegionalTieredCachesResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_regional_tiered_caches(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.regional_tiered_caches(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(CacheRegionalTieredCachesResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_regional_tiered_caches(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.regional_tiered_caches(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(CacheRegionalTieredCachesResponse, cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_regional_tiered_caches(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.regional_tiered_caches(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_regional_tiered_cache(self, client: Cloudflare) -> None:
        cache = client.cache.update_regional_tiered_cache(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(CacheUpdateRegionalTieredCacheResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_regional_tiered_cache(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.update_regional_tiered_cache(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(CacheUpdateRegionalTieredCacheResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_regional_tiered_cache(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.update_regional_tiered_cache(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(CacheUpdateRegionalTieredCacheResponse, cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_regional_tiered_cache(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.update_regional_tiered_cache(
                "",
                value="on",
            )


class TestAsyncCache:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_regional_tiered_caches(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.regional_tiered_caches(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheRegionalTieredCachesResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_regional_tiered_caches(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.regional_tiered_caches(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(CacheRegionalTieredCachesResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_regional_tiered_caches(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.regional_tiered_caches(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(CacheRegionalTieredCachesResponse, cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_regional_tiered_caches(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.regional_tiered_caches(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_regional_tiered_cache(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.update_regional_tiered_cache(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(CacheUpdateRegionalTieredCacheResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_regional_tiered_cache(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.update_regional_tiered_cache(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(CacheUpdateRegionalTieredCacheResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_regional_tiered_cache(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.update_regional_tiered_cache(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(CacheUpdateRegionalTieredCacheResponse, cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_regional_tiered_cache(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.update_regional_tiered_cache(
                "",
                value="on",
            )
