# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    PageShieldListResponse,
    PageShieldPageShieldUpdatePageShieldSettingsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPageShields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        page_shield = client.page_shields.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PageShieldListResponse, page_shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.page_shields.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_shield = response.parse()
        assert_matches_type(PageShieldListResponse, page_shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.page_shields.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_shield = response.parse()
            assert_matches_type(PageShieldListResponse, page_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_shields.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_page_shield_update_page_shield_settings(self, client: Cloudflare) -> None:
        page_shield = client.page_shields.page_shield_update_page_shield_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PageShieldPageShieldUpdatePageShieldSettingsResponse, page_shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_page_shield_update_page_shield_settings_with_all_params(self, client: Cloudflare) -> None:
        page_shield = client.page_shields.page_shield_update_page_shield_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            use_cloudflare_reporting_endpoint=True,
            use_connection_url_path=True,
        )
        assert_matches_type(PageShieldPageShieldUpdatePageShieldSettingsResponse, page_shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_page_shield_update_page_shield_settings(self, client: Cloudflare) -> None:
        response = client.page_shields.with_raw_response.page_shield_update_page_shield_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_shield = response.parse()
        assert_matches_type(PageShieldPageShieldUpdatePageShieldSettingsResponse, page_shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_page_shield_update_page_shield_settings(self, client: Cloudflare) -> None:
        with client.page_shields.with_streaming_response.page_shield_update_page_shield_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_shield = response.parse()
            assert_matches_type(PageShieldPageShieldUpdatePageShieldSettingsResponse, page_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_page_shield_update_page_shield_settings(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_shields.with_raw_response.page_shield_update_page_shield_settings(
                "",
            )


class TestAsyncPageShields:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        page_shield = await async_client.page_shields.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PageShieldListResponse, page_shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.page_shields.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_shield = await response.parse()
        assert_matches_type(PageShieldListResponse, page_shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.page_shields.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_shield = await response.parse()
            assert_matches_type(PageShieldListResponse, page_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_shields.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_page_shield_update_page_shield_settings(self, async_client: AsyncCloudflare) -> None:
        page_shield = await async_client.page_shields.page_shield_update_page_shield_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PageShieldPageShieldUpdatePageShieldSettingsResponse, page_shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_page_shield_update_page_shield_settings_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        page_shield = await async_client.page_shields.page_shield_update_page_shield_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            use_cloudflare_reporting_endpoint=True,
            use_connection_url_path=True,
        )
        assert_matches_type(PageShieldPageShieldUpdatePageShieldSettingsResponse, page_shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_page_shield_update_page_shield_settings(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.page_shields.with_raw_response.page_shield_update_page_shield_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_shield = await response.parse()
        assert_matches_type(PageShieldPageShieldUpdatePageShieldSettingsResponse, page_shield, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_page_shield_update_page_shield_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.page_shields.with_streaming_response.page_shield_update_page_shield_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_shield = await response.parse()
            assert_matches_type(PageShieldPageShieldUpdatePageShieldSettingsResponse, page_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_page_shield_update_page_shield_settings(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_shields.with_raw_response.page_shield_update_page_shield_settings(
                "",
            )
