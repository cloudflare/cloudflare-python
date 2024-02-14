# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.caches import (
    TieredCacheSmartTopologyEnableDeleteResponse,
    TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse,
    TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse,
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
from cloudflare.types.caches import (
    tiered_cache_smart_topology_enable_smart_tiered_cache_patch_smart_tiered_cache_setting_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTieredCacheSmartTopologyEnables:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        tiered_cache_smart_topology_enable = client.caches.tiered_cache_smart_topology_enables.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            TieredCacheSmartTopologyEnableDeleteResponse, tiered_cache_smart_topology_enable, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.caches.tiered_cache_smart_topology_enables.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiered_cache_smart_topology_enable = response.parse()
        assert_matches_type(
            TieredCacheSmartTopologyEnableDeleteResponse, tiered_cache_smart_topology_enable, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.caches.tiered_cache_smart_topology_enables.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiered_cache_smart_topology_enable = response.parse()
            assert_matches_type(
                TieredCacheSmartTopologyEnableDeleteResponse, tiered_cache_smart_topology_enable, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.caches.tiered_cache_smart_topology_enables.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_smart_tiered_cache_get_smart_tiered_cache_setting(self, client: Cloudflare) -> None:
        tiered_cache_smart_topology_enable = (
            client.caches.tiered_cache_smart_topology_enables.smart_tiered_cache_get_smart_tiered_cache_setting(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )
        assert_matches_type(
            TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse,
            tiered_cache_smart_topology_enable,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_smart_tiered_cache_get_smart_tiered_cache_setting(self, client: Cloudflare) -> None:
        response = client.caches.tiered_cache_smart_topology_enables.with_raw_response.smart_tiered_cache_get_smart_tiered_cache_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiered_cache_smart_topology_enable = response.parse()
        assert_matches_type(
            TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse,
            tiered_cache_smart_topology_enable,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_smart_tiered_cache_get_smart_tiered_cache_setting(self, client: Cloudflare) -> None:
        with client.caches.tiered_cache_smart_topology_enables.with_streaming_response.smart_tiered_cache_get_smart_tiered_cache_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiered_cache_smart_topology_enable = response.parse()
            assert_matches_type(
                TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse,
                tiered_cache_smart_topology_enable,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_smart_tiered_cache_get_smart_tiered_cache_setting(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.caches.tiered_cache_smart_topology_enables.with_raw_response.smart_tiered_cache_get_smart_tiered_cache_setting(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_smart_tiered_cache_patch_smart_tiered_cache_setting(self, client: Cloudflare) -> None:
        tiered_cache_smart_topology_enable = (
            client.caches.tiered_cache_smart_topology_enables.smart_tiered_cache_patch_smart_tiered_cache_setting(
                "023e105f4ecef8ad9ca31a8372d0c353",
                value="on",
            )
        )
        assert_matches_type(
            TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse,
            tiered_cache_smart_topology_enable,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_smart_tiered_cache_patch_smart_tiered_cache_setting(self, client: Cloudflare) -> None:
        response = client.caches.tiered_cache_smart_topology_enables.with_raw_response.smart_tiered_cache_patch_smart_tiered_cache_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiered_cache_smart_topology_enable = response.parse()
        assert_matches_type(
            TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse,
            tiered_cache_smart_topology_enable,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_smart_tiered_cache_patch_smart_tiered_cache_setting(self, client: Cloudflare) -> None:
        with client.caches.tiered_cache_smart_topology_enables.with_streaming_response.smart_tiered_cache_patch_smart_tiered_cache_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiered_cache_smart_topology_enable = response.parse()
            assert_matches_type(
                TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse,
                tiered_cache_smart_topology_enable,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_smart_tiered_cache_patch_smart_tiered_cache_setting(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.caches.tiered_cache_smart_topology_enables.with_raw_response.smart_tiered_cache_patch_smart_tiered_cache_setting(
                "",
                value="on",
            )


class TestAsyncTieredCacheSmartTopologyEnables:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        tiered_cache_smart_topology_enable = await async_client.caches.tiered_cache_smart_topology_enables.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            TieredCacheSmartTopologyEnableDeleteResponse, tiered_cache_smart_topology_enable, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.caches.tiered_cache_smart_topology_enables.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiered_cache_smart_topology_enable = await response.parse()
        assert_matches_type(
            TieredCacheSmartTopologyEnableDeleteResponse, tiered_cache_smart_topology_enable, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.caches.tiered_cache_smart_topology_enables.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiered_cache_smart_topology_enable = await response.parse()
            assert_matches_type(
                TieredCacheSmartTopologyEnableDeleteResponse, tiered_cache_smart_topology_enable, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.caches.tiered_cache_smart_topology_enables.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_smart_tiered_cache_get_smart_tiered_cache_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        tiered_cache_smart_topology_enable = await async_client.caches.tiered_cache_smart_topology_enables.smart_tiered_cache_get_smart_tiered_cache_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse,
            tiered_cache_smart_topology_enable,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_smart_tiered_cache_get_smart_tiered_cache_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.caches.tiered_cache_smart_topology_enables.with_raw_response.smart_tiered_cache_get_smart_tiered_cache_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiered_cache_smart_topology_enable = await response.parse()
        assert_matches_type(
            TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse,
            tiered_cache_smart_topology_enable,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_smart_tiered_cache_get_smart_tiered_cache_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.caches.tiered_cache_smart_topology_enables.with_streaming_response.smart_tiered_cache_get_smart_tiered_cache_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiered_cache_smart_topology_enable = await response.parse()
            assert_matches_type(
                TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse,
                tiered_cache_smart_topology_enable,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_smart_tiered_cache_get_smart_tiered_cache_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.caches.tiered_cache_smart_topology_enables.with_raw_response.smart_tiered_cache_get_smart_tiered_cache_setting(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_smart_tiered_cache_patch_smart_tiered_cache_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        tiered_cache_smart_topology_enable = await async_client.caches.tiered_cache_smart_topology_enables.smart_tiered_cache_patch_smart_tiered_cache_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(
            TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse,
            tiered_cache_smart_topology_enable,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_smart_tiered_cache_patch_smart_tiered_cache_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.caches.tiered_cache_smart_topology_enables.with_raw_response.smart_tiered_cache_patch_smart_tiered_cache_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiered_cache_smart_topology_enable = await response.parse()
        assert_matches_type(
            TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse,
            tiered_cache_smart_topology_enable,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_smart_tiered_cache_patch_smart_tiered_cache_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.caches.tiered_cache_smart_topology_enables.with_streaming_response.smart_tiered_cache_patch_smart_tiered_cache_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiered_cache_smart_topology_enable = await response.parse()
            assert_matches_type(
                TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse,
                tiered_cache_smart_topology_enable,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_smart_tiered_cache_patch_smart_tiered_cache_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.caches.tiered_cache_smart_topology_enables.with_raw_response.smart_tiered_cache_patch_smart_tiered_cache_setting(
                "",
                value="on",
            )
