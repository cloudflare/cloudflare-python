# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cache import (
    CacheReserveGetResponse,
    CacheReserveEditResponse,
    CacheReserveClearResponse,
    CacheReserveStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCacheReserve:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_clear(self, client: Cloudflare) -> None:
        cache_reserve = client.cache.cache_reserve.clear(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[CacheReserveClearResponse], cache_reserve, path=["response"])

    @parametrize
    def test_raw_response_clear(self, client: Cloudflare) -> None:
        response = client.cache.cache_reserve.with_raw_response.clear(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(Optional[CacheReserveClearResponse], cache_reserve, path=["response"])

    @parametrize
    def test_streaming_response_clear(self, client: Cloudflare) -> None:
        with client.cache.cache_reserve.with_streaming_response.clear(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = response.parse()
            assert_matches_type(Optional[CacheReserveClearResponse], cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_clear(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.cache_reserve.with_raw_response.clear(
                zone_id="",
                body={},
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        cache_reserve = client.cache.cache_reserve.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(Optional[CacheReserveEditResponse], cache_reserve, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cache.cache_reserve.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(Optional[CacheReserveEditResponse], cache_reserve, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cache.cache_reserve.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = response.parse()
            assert_matches_type(Optional[CacheReserveEditResponse], cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.cache_reserve.with_raw_response.edit(
                zone_id="",
                value="on",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        cache_reserve = client.cache.cache_reserve.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheReserveGetResponse], cache_reserve, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cache.cache_reserve.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(Optional[CacheReserveGetResponse], cache_reserve, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cache.cache_reserve.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = response.parse()
            assert_matches_type(Optional[CacheReserveGetResponse], cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.cache_reserve.with_raw_response.get(
                zone_id="",
            )

    @parametrize
    def test_method_status(self, client: Cloudflare) -> None:
        cache_reserve = client.cache.cache_reserve.status(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheReserveStatusResponse], cache_reserve, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Cloudflare) -> None:
        response = client.cache.cache_reserve.with_raw_response.status(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = response.parse()
        assert_matches_type(Optional[CacheReserveStatusResponse], cache_reserve, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Cloudflare) -> None:
        with client.cache.cache_reserve.with_streaming_response.status(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = response.parse()
            assert_matches_type(Optional[CacheReserveStatusResponse], cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.cache_reserve.with_raw_response.status(
                zone_id="",
            )


class TestAsyncCacheReserve:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_clear(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.cache.cache_reserve.clear(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[CacheReserveClearResponse], cache_reserve, path=["response"])

    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.cache_reserve.with_raw_response.clear(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(Optional[CacheReserveClearResponse], cache_reserve, path=["response"])

    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.cache_reserve.with_streaming_response.clear(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = await response.parse()
            assert_matches_type(Optional[CacheReserveClearResponse], cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_clear(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.cache_reserve.with_raw_response.clear(
                zone_id="",
                body={},
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.cache.cache_reserve.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(Optional[CacheReserveEditResponse], cache_reserve, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.cache_reserve.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(Optional[CacheReserveEditResponse], cache_reserve, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.cache_reserve.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = await response.parse()
            assert_matches_type(Optional[CacheReserveEditResponse], cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.cache_reserve.with_raw_response.edit(
                zone_id="",
                value="on",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.cache.cache_reserve.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheReserveGetResponse], cache_reserve, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.cache_reserve.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(Optional[CacheReserveGetResponse], cache_reserve, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.cache_reserve.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = await response.parse()
            assert_matches_type(Optional[CacheReserveGetResponse], cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.cache_reserve.with_raw_response.get(
                zone_id="",
            )

    @parametrize
    async def test_method_status(self, async_client: AsyncCloudflare) -> None:
        cache_reserve = await async_client.cache.cache_reserve.status(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheReserveStatusResponse], cache_reserve, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.cache_reserve.with_raw_response.status(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache_reserve = await response.parse()
        assert_matches_type(Optional[CacheReserveStatusResponse], cache_reserve, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.cache_reserve.with_streaming_response.status(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache_reserve = await response.parse()
            assert_matches_type(Optional[CacheReserveStatusResponse], cache_reserve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.cache_reserve.with_raw_response.status(
                zone_id="",
            )
