# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.bgp.ips import TopAsesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_ases(self, client: Cloudflare) -> None:
        top = client.radar.bgp.ips.top.ases()
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @parametrize
    def test_method_ases_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.bgp.ips.top.ases(
            country="US",
            date=parse_datetime("2024-09-19T00:00:00Z"),
            format="JSON",
            limit=5,
            metric="v4_24s",
        )
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @parametrize
    def test_raw_response_ases(self, client: Cloudflare) -> None:
        response = client.radar.bgp.ips.top.with_raw_response.ases()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_ases(self, client: Cloudflare) -> None:
        with client.radar.bgp.ips.top.with_streaming_response.ases() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopAsesResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTop:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_ases(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.bgp.ips.top.ases()
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @parametrize
    async def test_method_ases_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.bgp.ips.top.ases(
            country="US",
            date=parse_datetime("2024-09-19T00:00:00Z"),
            format="JSON",
            limit=5,
            metric="v4_24s",
        )
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_ases(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.ips.top.with_raw_response.ases()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_ases(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.ips.top.with_streaming_response.ases() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopAsesResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True
