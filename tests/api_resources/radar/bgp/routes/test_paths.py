# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.bgp.routes import PathListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaths:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        path = client.radar.bgp.routes.paths.list(
            asn=174,
        )
        assert_matches_type(PathListResponse, path, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        path = client.radar.bgp.routes.paths.list(
            asn=174,
            collector="route-views3",
            format="JSON",
            ip_version="IPv4",
        )
        assert_matches_type(PathListResponse, path, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.bgp.routes.paths.with_raw_response.list(
            asn=174,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        path = response.parse()
        assert_matches_type(PathListResponse, path, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.bgp.routes.paths.with_streaming_response.list(
            asn=174,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            path = response.parse()
            assert_matches_type(PathListResponse, path, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaths:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        path = await async_client.radar.bgp.routes.paths.list(
            asn=174,
        )
        assert_matches_type(PathListResponse, path, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        path = await async_client.radar.bgp.routes.paths.list(
            asn=174,
            collector="route-views3",
            format="JSON",
            ip_version="IPv4",
        )
        assert_matches_type(PathListResponse, path, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.routes.paths.with_raw_response.list(
            asn=174,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        path = await response.parse()
        assert_matches_type(PathListResponse, path, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.routes.paths.with_streaming_response.list(
            asn=174,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            path = await response.parse()
            assert_matches_type(PathListResponse, path, path=["response"])

        assert cast(Any, response.is_closed) is True
