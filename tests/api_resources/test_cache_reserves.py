# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import CacheReserveClearResponse, CacheReserveCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCacheReserves:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        cache_reserve = client.cache_reserves.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveCreateResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cache_reserves.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(CacheReserveCreateResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cache_reserves.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = response.parse()
            assert_matches_type(CacheReserveCreateResponse, cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache_reserves.with_raw_response.create(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_clear(self, client: Cloudflare) -> None:
        cache_reserve = client.cache_reserves.clear(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveClearResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_clear(self, client: Cloudflare) -> None:
        response = client.cache_reserves.with_raw_response.clear(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(CacheReserveClearResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_clear(self, client: Cloudflare) -> None:
        with client.cache_reserves.with_streaming_response.clear(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = response.parse()
            assert_matches_type(CacheReserveClearResponse, cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_clear(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache_reserves.with_raw_response.clear(
                "",
            )


class TestAsyncCacheReserves:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.cache_reserves.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveCreateResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache_reserves.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(CacheReserveCreateResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache_reserves.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = await response.parse()
            assert_matches_type(CacheReserveCreateResponse, cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache_reserves.with_raw_response.create(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_clear(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.cache_reserves.clear(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveClearResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache_reserves.with_raw_response.clear(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(CacheReserveClearResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache_reserves.with_streaming_response.clear(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = await response.parse()
            assert_matches_type(CacheReserveClearResponse, cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_clear(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache_reserves.with_raw_response.clear(
                "",
            )
