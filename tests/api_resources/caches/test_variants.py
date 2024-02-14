# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.caches import (
    VariantListResponse,
    VariantDeleteResponse,
    VariantZoneCacheSettingsChangeVariantsSettingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVariants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        variant = client.caches.variants.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(VariantListResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.caches.variants.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(VariantListResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.caches.variants.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(VariantListResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.caches.variants.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        variant = client.caches.variants.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.caches.variants.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.caches.variants.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(VariantDeleteResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.caches.variants.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_cache_settings_change_variants_setting(self, client: Cloudflare) -> None:
        variant = client.caches.variants.zone_cache_settings_change_variants_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        )
        assert_matches_type(VariantZoneCacheSettingsChangeVariantsSettingResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_cache_settings_change_variants_setting_with_all_params(self, client: Cloudflare) -> None:
        variant = client.caches.variants.zone_cache_settings_change_variants_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "avif": ["image/webp", "image/jpeg"],
                "bmp": ["image/webp", "image/jpeg"],
                "gif": ["image/webp", "image/jpeg"],
                "jp2": ["image/webp", "image/avif"],
                "jpeg": ["image/webp", "image/avif"],
                "jpg": ["image/webp", "image/avif"],
                "jpg2": ["image/webp", "image/avif"],
                "png": ["image/webp", "image/avif"],
                "tif": ["image/webp", "image/avif"],
                "tiff": ["image/webp", "image/avif"],
                "webp": ["image/jpeg", "image/avif"],
            },
        )
        assert_matches_type(VariantZoneCacheSettingsChangeVariantsSettingResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_cache_settings_change_variants_setting(self, client: Cloudflare) -> None:
        response = client.caches.variants.with_raw_response.zone_cache_settings_change_variants_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(VariantZoneCacheSettingsChangeVariantsSettingResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_cache_settings_change_variants_setting(self, client: Cloudflare) -> None:
        with client.caches.variants.with_streaming_response.zone_cache_settings_change_variants_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(VariantZoneCacheSettingsChangeVariantsSettingResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_cache_settings_change_variants_setting(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.caches.variants.with_raw_response.zone_cache_settings_change_variants_setting(
                "",
                value={},
            )


class TestAsyncVariants:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.caches.variants.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(VariantListResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.caches.variants.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(VariantListResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.caches.variants.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(VariantListResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.caches.variants.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.caches.variants.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.caches.variants.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.caches.variants.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(VariantDeleteResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.caches.variants.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_cache_settings_change_variants_setting(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.caches.variants.zone_cache_settings_change_variants_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        )
        assert_matches_type(VariantZoneCacheSettingsChangeVariantsSettingResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_cache_settings_change_variants_setting_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        variant = await async_client.caches.variants.zone_cache_settings_change_variants_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "avif": ["image/webp", "image/jpeg"],
                "bmp": ["image/webp", "image/jpeg"],
                "gif": ["image/webp", "image/jpeg"],
                "jp2": ["image/webp", "image/avif"],
                "jpeg": ["image/webp", "image/avif"],
                "jpg": ["image/webp", "image/avif"],
                "jpg2": ["image/webp", "image/avif"],
                "png": ["image/webp", "image/avif"],
                "tif": ["image/webp", "image/avif"],
                "tiff": ["image/webp", "image/avif"],
                "webp": ["image/jpeg", "image/avif"],
            },
        )
        assert_matches_type(VariantZoneCacheSettingsChangeVariantsSettingResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_cache_settings_change_variants_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.caches.variants.with_raw_response.zone_cache_settings_change_variants_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(VariantZoneCacheSettingsChangeVariantsSettingResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_cache_settings_change_variants_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.caches.variants.with_streaming_response.zone_cache_settings_change_variants_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(VariantZoneCacheSettingsChangeVariantsSettingResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_cache_settings_change_variants_setting(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.caches.variants.with_raw_response.zone_cache_settings_change_variants_setting(
                "",
                value={},
            )
