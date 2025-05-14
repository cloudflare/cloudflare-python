# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zones import SettingGetResponse, SettingEditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_edit_overload_1(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_method_edit_with_all_params_overload_1(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_1(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_1(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit_overload_2(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_method_edit_with_all_params_overload_2(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "enabled": True,
                "pool_id": "pool-id",
            },
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_2(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_2(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        setting = client.zones.settings.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.get(
                setting_id="always_online",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.get(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "enabled": True,
                "pool_id": "pool-id",
            },
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.get(
                setting_id="always_online",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.get(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
