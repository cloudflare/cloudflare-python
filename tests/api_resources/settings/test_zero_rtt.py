# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.settings import (
    ZeroRttGetResponse,
    ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestZeroRtt:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        zero_rtt = client.settings.zero_rtt.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZeroRttGetResponse], zero_rtt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.settings.zero_rtt.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zero_rtt = response.parse()
        assert_matches_type(Optional[ZeroRttGetResponse], zero_rtt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.settings.zero_rtt.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zero_rtt = response.parse()
            assert_matches_type(Optional[ZeroRttGetResponse], zero_rtt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.zero_rtt.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_settings_change_0_rtt_session_resumption_setting(self, client: Cloudflare) -> None:
        zero_rtt = client.settings.zero_rtt.zone_settings_change_0_rtt_session_resumption_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(
            Optional[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse], zero_rtt, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_settings_change_0_rtt_session_resumption_setting(self, client: Cloudflare) -> None:
        response = client.settings.zero_rtt.with_raw_response.zone_settings_change_0_rtt_session_resumption_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zero_rtt = response.parse()
        assert_matches_type(
            Optional[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse], zero_rtt, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_settings_change_0_rtt_session_resumption_setting(self, client: Cloudflare) -> None:
        with client.settings.zero_rtt.with_streaming_response.zone_settings_change_0_rtt_session_resumption_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zero_rtt = response.parse()
            assert_matches_type(
                Optional[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse], zero_rtt, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_settings_change_0_rtt_session_resumption_setting(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.zero_rtt.with_raw_response.zone_settings_change_0_rtt_session_resumption_setting(
                "",
                value="on",
            )


class TestAsyncZeroRtt:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        zero_rtt = await async_client.settings.zero_rtt.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZeroRttGetResponse], zero_rtt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.zero_rtt.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zero_rtt = await response.parse()
        assert_matches_type(Optional[ZeroRttGetResponse], zero_rtt, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.zero_rtt.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zero_rtt = await response.parse()
            assert_matches_type(Optional[ZeroRttGetResponse], zero_rtt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.zero_rtt.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_settings_change_0_rtt_session_resumption_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        zero_rtt = await async_client.settings.zero_rtt.zone_settings_change_0_rtt_session_resumption_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(
            Optional[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse], zero_rtt, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_settings_change_0_rtt_session_resumption_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.settings.zero_rtt.with_raw_response.zone_settings_change_0_rtt_session_resumption_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zero_rtt = await response.parse()
        assert_matches_type(
            Optional[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse], zero_rtt, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_settings_change_0_rtt_session_resumption_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.settings.zero_rtt.with_streaming_response.zone_settings_change_0_rtt_session_resumption_setting(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zero_rtt = await response.parse()
            assert_matches_type(
                Optional[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse], zero_rtt, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_settings_change_0_rtt_session_resumption_setting(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await (
                async_client.settings.zero_rtt.with_raw_response.zone_settings_change_0_rtt_session_resumption_setting(
                    "",
                    value="on",
                )
            )
