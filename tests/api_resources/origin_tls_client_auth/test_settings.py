# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.origin_tls_client_auth import (
    SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse,
    SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse,
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
from cloudflare.types.origin_tls_client_auth import (
    setting_zone_level_authenticated_origin_pulls_set_enablement_for_zone_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
        self, client: Cloudflare
    ) -> None:
        setting = client.origin_tls_client_auth.settings.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse, setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
        self, client: Cloudflare
    ) -> None:
        response = client.origin_tls_client_auth.settings.with_raw_response.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(
            SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse, setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
        self, client: Cloudflare
    ) -> None:
        with client.origin_tls_client_auth.settings.with_streaming_response.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(
                SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse, setting, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.origin_tls_client_auth.settings.with_raw_response.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_level_authenticated_origin_pulls_set_enablement_for_zone(self, client: Cloudflare) -> None:
        setting = client.origin_tls_client_auth.settings.zone_level_authenticated_origin_pulls_set_enablement_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(
            SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse, setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_level_authenticated_origin_pulls_set_enablement_for_zone(
        self, client: Cloudflare
    ) -> None:
        response = client.origin_tls_client_auth.settings.with_raw_response.zone_level_authenticated_origin_pulls_set_enablement_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(
            SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse, setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_level_authenticated_origin_pulls_set_enablement_for_zone(
        self, client: Cloudflare
    ) -> None:
        with client.origin_tls_client_auth.settings.with_streaming_response.zone_level_authenticated_origin_pulls_set_enablement_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(
                SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse, setting, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_level_authenticated_origin_pulls_set_enablement_for_zone(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.origin_tls_client_auth.settings.with_raw_response.zone_level_authenticated_origin_pulls_set_enablement_for_zone(
                "",
                enabled=True,
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        setting = await async_client.origin_tls_client_auth.settings.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse, setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.origin_tls_client_auth.settings.with_raw_response.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(
            SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse, setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.origin_tls_client_auth.settings.with_streaming_response.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(
                SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse, setting, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.origin_tls_client_auth.settings.with_raw_response.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_level_authenticated_origin_pulls_set_enablement_for_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        setting = await async_client.origin_tls_client_auth.settings.zone_level_authenticated_origin_pulls_set_enablement_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(
            SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse, setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_level_authenticated_origin_pulls_set_enablement_for_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.origin_tls_client_auth.settings.with_raw_response.zone_level_authenticated_origin_pulls_set_enablement_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(
            SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse, setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_level_authenticated_origin_pulls_set_enablement_for_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.origin_tls_client_auth.settings.with_streaming_response.zone_level_authenticated_origin_pulls_set_enablement_for_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(
                SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse, setting, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_level_authenticated_origin_pulls_set_enablement_for_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.origin_tls_client_auth.settings.with_raw_response.zone_level_authenticated_origin_pulls_set_enablement_for_zone(
                "",
                enabled=True,
            )
