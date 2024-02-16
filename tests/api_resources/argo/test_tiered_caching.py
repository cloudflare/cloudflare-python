# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.argo import (
    TieredCachingTieredCachingGetTieredCachingSettingResponse,
    TieredCachingTieredCachingPatchTieredCachingSettingResponse,
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
from cloudflare.types.argo import tiered_caching_tiered_caching_patch_tiered_caching_setting_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTieredCaching:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_tiered_caching_get_tiered_caching_setting(self, client: Cloudflare) -> None:
        tiered_caching = client.argo.tiered_caching.tiered_caching_get_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            TieredCachingTieredCachingGetTieredCachingSettingResponse, tiered_caching, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_tiered_caching_get_tiered_caching_setting(self, client: Cloudflare) -> None:
        response = client.argo.tiered_caching.with_raw_response.tiered_caching_get_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiered_caching = response.parse()
        assert_matches_type(
            TieredCachingTieredCachingGetTieredCachingSettingResponse, tiered_caching, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_tiered_caching_get_tiered_caching_setting(self, client: Cloudflare) -> None:
        with client.argo.tiered_caching.with_streaming_response.tiered_caching_get_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiered_caching = response.parse()
            assert_matches_type(
                TieredCachingTieredCachingGetTieredCachingSettingResponse, tiered_caching, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_tiered_caching_get_tiered_caching_setting(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.argo.tiered_caching.with_raw_response.tiered_caching_get_tiered_caching_setting(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_tiered_caching_patch_tiered_caching_setting(self, client: Cloudflare) -> None:
        tiered_caching = client.argo.tiered_caching.tiered_caching_patch_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(
            TieredCachingTieredCachingPatchTieredCachingSettingResponse, tiered_caching, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_tiered_caching_patch_tiered_caching_setting(self, client: Cloudflare) -> None:
        response = client.argo.tiered_caching.with_raw_response.tiered_caching_patch_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiered_caching = response.parse()
        assert_matches_type(
            TieredCachingTieredCachingPatchTieredCachingSettingResponse, tiered_caching, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_tiered_caching_patch_tiered_caching_setting(self, client: Cloudflare) -> None:
        with client.argo.tiered_caching.with_streaming_response.tiered_caching_patch_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiered_caching = response.parse()
            assert_matches_type(
                TieredCachingTieredCachingPatchTieredCachingSettingResponse, tiered_caching, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_tiered_caching_patch_tiered_caching_setting(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.argo.tiered_caching.with_raw_response.tiered_caching_patch_tiered_caching_setting(
                "",
                value="on",
            )


class TestAsyncTieredCaching:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_tiered_caching_get_tiered_caching_setting(self, async_client: AsyncCloudflare) -> None:
        tiered_caching = await async_client.argo.tiered_caching.tiered_caching_get_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            TieredCachingTieredCachingGetTieredCachingSettingResponse, tiered_caching, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_tiered_caching_get_tiered_caching_setting(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.argo.tiered_caching.with_raw_response.tiered_caching_get_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiered_caching = await response.parse()
        assert_matches_type(
            TieredCachingTieredCachingGetTieredCachingSettingResponse, tiered_caching, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_tiered_caching_get_tiered_caching_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.argo.tiered_caching.with_streaming_response.tiered_caching_get_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiered_caching = await response.parse()
            assert_matches_type(
                TieredCachingTieredCachingGetTieredCachingSettingResponse, tiered_caching, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_tiered_caching_get_tiered_caching_setting(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.argo.tiered_caching.with_raw_response.tiered_caching_get_tiered_caching_setting(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_tiered_caching_patch_tiered_caching_setting(self, async_client: AsyncCloudflare) -> None:
        tiered_caching = await async_client.argo.tiered_caching.tiered_caching_patch_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(
            TieredCachingTieredCachingPatchTieredCachingSettingResponse, tiered_caching, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_tiered_caching_patch_tiered_caching_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.argo.tiered_caching.with_raw_response.tiered_caching_patch_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiered_caching = await response.parse()
        assert_matches_type(
            TieredCachingTieredCachingPatchTieredCachingSettingResponse, tiered_caching, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_tiered_caching_patch_tiered_caching_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.argo.tiered_caching.with_streaming_response.tiered_caching_patch_tiered_caching_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiered_caching = await response.parse()
            assert_matches_type(
                TieredCachingTieredCachingPatchTieredCachingSettingResponse, tiered_caching, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_tiered_caching_patch_tiered_caching_setting(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.argo.tiered_caching.with_raw_response.tiered_caching_patch_tiered_caching_setting(
                "",
                value="on",
            )
