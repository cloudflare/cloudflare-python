# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.emails.routings import EnableEmailRoutingSettingsEnableEmailRoutingResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnables:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_email_routing_settings_enable_email_routing(self, client: Cloudflare) -> None:
        enable = client.emails.routings.enables.email_routing_settings_enable_email_routing(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(EnableEmailRoutingSettingsEnableEmailRoutingResponse, enable, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_email_routing_settings_enable_email_routing(self, client: Cloudflare) -> None:
        response = client.emails.routings.enables.with_raw_response.email_routing_settings_enable_email_routing(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enable = response.parse()
        assert_matches_type(EnableEmailRoutingSettingsEnableEmailRoutingResponse, enable, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_email_routing_settings_enable_email_routing(self, client: Cloudflare) -> None:
        with client.emails.routings.enables.with_streaming_response.email_routing_settings_enable_email_routing(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enable = response.parse()
            assert_matches_type(EnableEmailRoutingSettingsEnableEmailRoutingResponse, enable, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_email_routing_settings_enable_email_routing(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.emails.routings.enables.with_raw_response.email_routing_settings_enable_email_routing(
                "",
            )


class TestAsyncEnables:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_email_routing_settings_enable_email_routing(self, async_client: AsyncCloudflare) -> None:
        enable = await async_client.emails.routings.enables.email_routing_settings_enable_email_routing(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(EnableEmailRoutingSettingsEnableEmailRoutingResponse, enable, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_email_routing_settings_enable_email_routing(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.emails.routings.enables.with_raw_response.email_routing_settings_enable_email_routing(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enable = await response.parse()
        assert_matches_type(EnableEmailRoutingSettingsEnableEmailRoutingResponse, enable, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_email_routing_settings_enable_email_routing(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.emails.routings.enables.with_streaming_response.email_routing_settings_enable_email_routing(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enable = await response.parse()
            assert_matches_type(EnableEmailRoutingSettingsEnableEmailRoutingResponse, enable, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_email_routing_settings_enable_email_routing(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.emails.routings.enables.with_raw_response.email_routing_settings_enable_email_routing(
                "",
            )
