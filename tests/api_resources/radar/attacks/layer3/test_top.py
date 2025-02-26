# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.attacks.layer3 import (
    TopAttacksResponse,
    TopIndustryResponse,
    TopVerticalResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_attacks(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer3.top.attacks()
        assert_matches_type(TopAttacksResponse, top, path=["response"])

    @parametrize
    def test_method_attacks_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer3.top.attacks(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            ip_version=["IPv4"],
            limit=5,
            limit_direction="ORIGIN",
            limit_per_location=10,
            location=["string"],
            magnitude="MITIGATED_BYTES",
            name=["main_series"],
            normalization="PERCENTAGE",
            protocol=["UDP"],
        )
        assert_matches_type(TopAttacksResponse, top, path=["response"])

    @parametrize
    def test_raw_response_attacks(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer3.top.with_raw_response.attacks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopAttacksResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_attacks(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.top.with_streaming_response.attacks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopAttacksResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_industry(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer3.top.industry()
        assert_matches_type(TopIndustryResponse, top, path=["response"])

    @parametrize
    def test_method_industry_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer3.top.industry(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            ip_version=["IPv4"],
            limit=5,
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(TopIndustryResponse, top, path=["response"])

    @parametrize
    def test_raw_response_industry(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer3.top.with_raw_response.industry()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopIndustryResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_industry(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.top.with_streaming_response.industry() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopIndustryResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_vertical(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer3.top.vertical()
        assert_matches_type(TopVerticalResponse, top, path=["response"])

    @parametrize
    def test_method_vertical_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer3.top.vertical(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            ip_version=["IPv4"],
            limit=5,
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(TopVerticalResponse, top, path=["response"])

    @parametrize
    def test_raw_response_vertical(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer3.top.with_raw_response.vertical()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopVerticalResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_vertical(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.top.with_streaming_response.vertical() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopVerticalResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_attacks(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer3.top.attacks()
        assert_matches_type(TopAttacksResponse, top, path=["response"])

    @parametrize
    async def test_method_attacks_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer3.top.attacks(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            ip_version=["IPv4"],
            limit=5,
            limit_direction="ORIGIN",
            limit_per_location=10,
            location=["string"],
            magnitude="MITIGATED_BYTES",
            name=["main_series"],
            normalization="PERCENTAGE",
            protocol=["UDP"],
        )
        assert_matches_type(TopAttacksResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_attacks(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer3.top.with_raw_response.attacks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopAttacksResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_attacks(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.top.with_streaming_response.attacks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopAttacksResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_industry(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer3.top.industry()
        assert_matches_type(TopIndustryResponse, top, path=["response"])

    @parametrize
    async def test_method_industry_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer3.top.industry(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            ip_version=["IPv4"],
            limit=5,
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(TopIndustryResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_industry(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer3.top.with_raw_response.industry()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopIndustryResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_industry(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.top.with_streaming_response.industry() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopIndustryResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_vertical(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer3.top.vertical()
        assert_matches_type(TopVerticalResponse, top, path=["response"])

    @parametrize
    async def test_method_vertical_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer3.top.vertical(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            ip_version=["IPv4"],
            limit=5,
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(TopVerticalResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_vertical(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer3.top.with_raw_response.vertical()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopVerticalResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_vertical(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.top.with_streaming_response.vertical() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopVerticalResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True
