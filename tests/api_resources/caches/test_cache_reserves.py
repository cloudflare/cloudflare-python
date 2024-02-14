# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.caches import (
    CacheReserveListResponse,
    CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.caches import cache_reserve_zone_cache_settings_change_cache_reserve_setting_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCacheReserves:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        cache_reserve = client.caches.cache_reserves.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveListResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.caches.cache_reserves.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(CacheReserveListResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.caches.cache_reserves.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = response.parse()
            assert_matches_type(CacheReserveListResponse, cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.caches.cache_reserves.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_cache_settings_change_cache_reserve_setting(self, client: Cloudflare) -> None:
        cache_reserve = client.caches.cache_reserves.zone_cache_settings_change_cache_reserve_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(
            CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse, cache_reserve, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_cache_settings_change_cache_reserve_setting(self, client: Cloudflare) -> None:
        response = client.caches.cache_reserves.with_raw_response.zone_cache_settings_change_cache_reserve_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(
            CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse, cache_reserve, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_cache_settings_change_cache_reserve_setting(self, client: Cloudflare) -> None:
        with client.caches.cache_reserves.with_streaming_response.zone_cache_settings_change_cache_reserve_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = response.parse()
            assert_matches_type(
                CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse, cache_reserve, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_cache_settings_change_cache_reserve_setting(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.caches.cache_reserves.with_raw_response.zone_cache_settings_change_cache_reserve_setting(
                "",
                value="on",
            )


class TestAsyncCacheReserves:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.caches.cache_reserves.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveListResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.caches.cache_reserves.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(CacheReserveListResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.caches.cache_reserves.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = await response.parse()
            assert_matches_type(CacheReserveListResponse, cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.caches.cache_reserves.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_cache_settings_change_cache_reserve_setting(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.caches.cache_reserves.zone_cache_settings_change_cache_reserve_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(
            CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse, cache_reserve, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_cache_settings_change_cache_reserve_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.caches.cache_reserves.with_raw_response.zone_cache_settings_change_cache_reserve_setting(
                "023e105f4ecef8ad9ca31a8372d0c353",
                value="on",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(
            CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse, cache_reserve, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_cache_settings_change_cache_reserve_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.caches.cache_reserves.with_streaming_response.zone_cache_settings_change_cache_reserve_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = await response.parse()
            assert_matches_type(
                CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse, cache_reserve, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_cache_settings_change_cache_reserve_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.caches.cache_reserves.with_raw_response.zone_cache_settings_change_cache_reserve_setting(
                "",
                value="on",
            )
