# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.verified_bots import (
    TopBotsResponse,
    TopCategoriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_bots(self, client: Cloudflare) -> None:
        top = client.radar.verified_bots.top.bots()
        assert_matches_type(TopBotsResponse, top, path=["response"])

    @parametrize
    def test_method_bots_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.verified_bots.top.bots(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopBotsResponse, top, path=["response"])

    @parametrize
    def test_raw_response_bots(self, client: Cloudflare) -> None:
        response = client.radar.verified_bots.top.with_raw_response.bots()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopBotsResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_bots(self, client: Cloudflare) -> None:
        with client.radar.verified_bots.top.with_streaming_response.bots() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopBotsResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_categories(self, client: Cloudflare) -> None:
        top = client.radar.verified_bots.top.categories()
        assert_matches_type(TopCategoriesResponse, top, path=["response"])

    @parametrize
    def test_method_categories_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.verified_bots.top.categories(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopCategoriesResponse, top, path=["response"])

    @parametrize
    def test_raw_response_categories(self, client: Cloudflare) -> None:
        response = client.radar.verified_bots.top.with_raw_response.categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopCategoriesResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_categories(self, client: Cloudflare) -> None:
        with client.radar.verified_bots.top.with_streaming_response.categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopCategoriesResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_bots(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.verified_bots.top.bots()
        assert_matches_type(TopBotsResponse, top, path=["response"])

    @parametrize
    async def test_method_bots_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.verified_bots.top.bots(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopBotsResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_bots(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.verified_bots.top.with_raw_response.bots()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopBotsResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_bots(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.verified_bots.top.with_streaming_response.bots() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopBotsResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_categories(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.verified_bots.top.categories()
        assert_matches_type(TopCategoriesResponse, top, path=["response"])

    @parametrize
    async def test_method_categories_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.verified_bots.top.categories(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopCategoriesResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_categories(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.verified_bots.top.with_raw_response.categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopCategoriesResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_categories(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.verified_bots.top.with_streaming_response.categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopCategoriesResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True
