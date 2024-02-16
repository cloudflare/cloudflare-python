# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.radar.bgp import RouteMoasResponse, RoutePfx2asResponse, RouteStatsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.bgp import route_moas_params
from cloudflare.types.radar.bgp import route_pfx2as_params
from cloudflare.types.radar.bgp import route_stats_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_moas(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.moas()
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_moas_with_all_params(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.moas(
            format="JSON",
            invalid_only=True,
            origin=0,
            prefix="string",
        )
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_moas(self, client: Cloudflare) -> None:
        response = client.radar.bgp.routes.with_raw_response.moas()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_moas(self, client: Cloudflare) -> None:
        with client.radar.bgp.routes.with_streaming_response.moas() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteMoasResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_pfx2as(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.pfx2as()
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_pfx2as_with_all_params(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.pfx2as(
            format="JSON",
            origin=0,
            prefix="1.1.1.0/24",
            rpki_status="INVALID",
        )
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_pfx2as(self, client: Cloudflare) -> None:
        response = client.radar.bgp.routes.with_raw_response.pfx2as()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_pfx2as(self, client: Cloudflare) -> None:
        with client.radar.bgp.routes.with_streaming_response.pfx2as() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RoutePfx2asResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_stats(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.stats()
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_stats_with_all_params(self, client: Cloudflare) -> None:
        route = client.radar.bgp.routes.stats(
            asn=0,
            format="JSON",
            location="US",
        )
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stats(self, client: Cloudflare) -> None:
        response = client.radar.bgp.routes.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_method_moas(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.moas()
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_moas_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.moas(
            format="JSON",
            invalid_only=True,
            origin=0,
            prefix="string",
        )
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_moas(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.routes.with_raw_response.moas()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteMoasResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_moas(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.routes.with_streaming_response.moas() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteMoasResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_pfx2as(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.pfx2as()
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_pfx2as_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.pfx2as(
            format="JSON",
            origin=0,
            prefix="1.1.1.0/24",
            rpki_status="INVALID",
        )
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_pfx2as(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.routes.with_raw_response.pfx2as()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RoutePfx2asResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_pfx2as(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.routes.with_streaming_response.pfx2as() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RoutePfx2asResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_stats(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.stats()
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_stats_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.radar.bgp.routes.stats(
            asn=0,
            format="JSON",
            location="US",
        )
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stats(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.routes.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteStatsResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stats(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.routes.with_streaming_response.stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteStatsResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True
