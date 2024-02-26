# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cache import (
    CacheReserveEditResponse,
    CacheReserveListResponse,
    CacheReserveClearResponse,
    CacheReserveStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCacheReserve:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        cache_reserve = client.cache.cache_reserve.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveListResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cache.cache_reserve.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(CacheReserveListResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cache.cache_reserve.with_streaming_response.list(
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
            client.cache.cache_reserve.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_clear(self, client: Cloudflare) -> None:
        cache_reserve = client.cache.cache_reserve.clear(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveClearResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_clear(self, client: Cloudflare) -> None:
        response = client.cache.cache_reserve.with_raw_response.clear(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(CacheReserveClearResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_clear(self, client: Cloudflare) -> None:
        with client.cache.cache_reserve.with_streaming_response.clear(
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
            client.cache.cache_reserve.with_raw_response.clear(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        cache_reserve = client.cache.cache_reserve.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(CacheReserveEditResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cache.cache_reserve.with_raw_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(CacheReserveEditResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cache.cache_reserve.with_streaming_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = response.parse()
            assert_matches_type(CacheReserveEditResponse, cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.cache_reserve.with_raw_response.edit(
                "",
                value="on",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_status(self, client: Cloudflare) -> None:
        cache_reserve = client.cache.cache_reserve.status(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveStatusResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_status(self, client: Cloudflare) -> None:
        response = client.cache.cache_reserve.with_raw_response.status(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(CacheReserveStatusResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_status(self, client: Cloudflare) -> None:
        with client.cache.cache_reserve.with_streaming_response.status(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = response.parse()
            assert_matches_type(CacheReserveStatusResponse, cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_status(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.cache_reserve.with_raw_response.status(
                "",
            )


class TestAsyncCacheReserve:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.cache.cache_reserve.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveListResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.cache_reserve.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(CacheReserveListResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.cache_reserve.with_streaming_response.list(
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
            await async_client.cache.cache_reserve.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_clear(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.cache.cache_reserve.clear(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveClearResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.cache_reserve.with_raw_response.clear(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(CacheReserveClearResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.cache_reserve.with_streaming_response.clear(
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
            await async_client.cache.cache_reserve.with_raw_response.clear(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.cache.cache_reserve.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(CacheReserveEditResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.cache_reserve.with_raw_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(CacheReserveEditResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.cache_reserve.with_streaming_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = await response.parse()
            assert_matches_type(CacheReserveEditResponse, cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.cache_reserve.with_raw_response.edit(
                "",
                value="on",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_status(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.cache.cache_reserve.status(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CacheReserveStatusResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.cache_reserve.with_raw_response.status(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(CacheReserveStatusResponse, cache_reserve, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.cache_reserve.with_streaming_response.status(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = await response.parse()
            assert_matches_type(CacheReserveStatusResponse, cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_status(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.cache_reserve.with_raw_response.status(
                "",
            )
