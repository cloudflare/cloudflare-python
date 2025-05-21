# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.access.applications import (
    SettingEditResponse,
    SettingUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        setting = client.zero_trust.access.applications.settings.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        setting = client.zero_trust.access.applications.settings.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
            allow_iframe=True,
            skip_interstitial=True,
        )
        assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.settings.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.settings.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.settings.with_raw_response.update(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.settings.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.settings.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        setting = client.zero_trust.access.applications.settings.edit(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        setting = client.zero_trust.access.applications.settings.edit(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
            allow_iframe=True,
            skip_interstitial=True,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.settings.with_raw_response.edit(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.settings.with_streaming_response.edit(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.settings.with_raw_response.edit(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.settings.with_raw_response.edit(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.settings.with_raw_response.edit(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.access.applications.settings.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.access.applications.settings.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
            allow_iframe=True,
            skip_interstitial=True,
        )
        assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.settings.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.settings.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.settings.with_raw_response.update(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.settings.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.settings.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.access.applications.settings.edit(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.access.applications.settings.edit(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
            allow_iframe=True,
            skip_interstitial=True,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.settings.with_raw_response.edit(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.settings.with_streaming_response.edit(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.settings.with_raw_response.edit(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.settings.with_raw_response.edit(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.settings.with_raw_response.edit(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )
