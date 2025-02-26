# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.bgp import (
    RouteAsesResponse,
    RouteMoasResponse,
    RouteStatsResponse,
    RoutePfx2asResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_ases(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.ases()
        assert_matches_type(RouteAsesResponse, route, path=["response"])

    @parametrize
    def test_method_ases_with_all_params(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.ases(
            format="JSON",
            limit=5,
            location="US",
            sort_by="cone",
            sort_order="ASC",
        )
        assert_matches_type(RouteAsesResponse, route, path=["response"])

    @parametrize
    def test_raw_response_ases(self, client: Cloudflare) -> None:
        response = client.radar.bgp.routes.with_raw_response.ases()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteAsesResponse, route, path=["response"])

    @parametrize
    def test_streaming_response_ases(self, client: Cloudflare) -> None:
        with client.radar.bgp.routes.with_streaming_response.ases() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteAsesResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_moas(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.moas()
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @parametrize
    def test_method_moas_with_all_params(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.moas(
            format="JSON",
            invalid_only=True,
            origin=0,
            prefix="1.1.1.0/24",
        )
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @parametrize
    def test_raw_response_moas(self, client: Cloudflare) -> None:
        response = client.radar.bgp.routes.with_raw_response.moas()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @parametrize
    def test_streaming_response_moas(self, client: Cloudflare) -> None:
        with client.radar.bgp.routes.with_streaming_response.moas() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteMoasResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_pfx2as(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.pfx2as()
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @parametrize
    def test_method_pfx2as_with_all_params(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.pfx2as(
            format="JSON",
            longest_prefix_match=True,
            origin=0,
            prefix="1.1.1.0/24",
            rpki_status="VALID",
        )
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @parametrize
    def test_raw_response_pfx2as(self, client: Cloudflare) -> None:
        response = client.radar.bgp.routes.with_raw_response.pfx2as()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @parametrize
    def test_streaming_response_pfx2as(self, client: Cloudflare) -> None:
        with client.radar.bgp.routes.with_streaming_response.pfx2as() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RoutePfx2asResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stats(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.stats()
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @parametrize
    def test_method_stats_with_all_params(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.stats(
            asn=174,
            format="JSON",
            location="US",
        )
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @parametrize
    def test_raw_response_stats(self, client: Cloudflare) -> None:
        response = client.radar.bgp.routes.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @parametrize
    def test_streaming_response_stats(self, client: Cloudflare) -> None:
        with client.radar.bgp.routes.with_streaming_response.stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteStatsResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoutes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_ases(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.ases()
        assert_matches_type(RouteAsesResponse, route, path=["response"])

    @parametrize
    async def test_method_ases_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.ases(
            format="JSON",
            limit=5,
            location="US",
            sort_by="cone",
            sort_order="ASC",
        )
        assert_matches_type(RouteAsesResponse, route, path=["response"])

    @parametrize
    async def test_raw_response_ases(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.routes.with_raw_response.ases()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteAsesResponse, route, path=["response"])

    @parametrize
    async def test_streaming_response_ases(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.routes.with_streaming_response.ases() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteAsesResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_moas(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.moas()
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @parametrize
    async def test_method_moas_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.moas(
            format="JSON",
            invalid_only=True,
            origin=0,
            prefix="1.1.1.0/24",
        )
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @parametrize
    async def test_raw_response_moas(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.routes.with_raw_response.moas()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @parametrize
    async def test_streaming_response_moas(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.routes.with_streaming_response.moas() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteMoasResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_pfx2as(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.pfx2as()
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @parametrize
    async def test_method_pfx2as_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.pfx2as(
            format="JSON",
            longest_prefix_match=True,
            origin=0,
            prefix="1.1.1.0/24",
            rpki_status="VALID",
        )
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @parametrize
    async def test_raw_response_pfx2as(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.routes.with_raw_response.pfx2as()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @parametrize
    async def test_streaming_response_pfx2as(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.routes.with_streaming_response.pfx2as() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RoutePfx2asResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stats(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.stats()
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @parametrize
    async def test_method_stats_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.stats(
            asn=174,
            format="JSON",
            location="US",
        )
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @parametrize
    async def test_raw_response_stats(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.routes.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @parametrize
    async def test_streaming_response_stats(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.routes.with_streaming_response.stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteStatsResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True
