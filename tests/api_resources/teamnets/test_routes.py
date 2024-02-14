# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.teamnets import RouteTunnelRouteListTunnelRoutesResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.teamnets import route_tunnel_route_list_tunnel_routes_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_tunnel_route_list_tunnel_routes(self, client: Cloudflare) -> None:
        route = client.teamnets.routes.tunnel_route_list_tunnel_routes(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[RouteTunnelRouteListTunnelRoutesResponse], route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_tunnel_route_list_tunnel_routes_with_all_params(self, client: Cloudflare) -> None:
        route = client.teamnets.routes.tunnel_route_list_tunnel_routes(
            "699d98642c564d2e855e9661899b7252",
            comment="Example comment for this route.",
            existed_at={},
            is_deleted={},
            network_subset={},
            network_superset={},
            page=1,
            per_page=1,
            tun_types="cfd_tunnel,warp_connector",
            tunnel_id={},
            virtual_network_id={},
        )
        assert_matches_type(Optional[RouteTunnelRouteListTunnelRoutesResponse], route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_tunnel_route_list_tunnel_routes(self, client: Cloudflare) -> None:
        response = client.teamnets.routes.with_raw_response.tunnel_route_list_tunnel_routes(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(Optional[RouteTunnelRouteListTunnelRoutesResponse], route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_tunnel_route_list_tunnel_routes(self, client: Cloudflare) -> None:
        with client.teamnets.routes.with_streaming_response.tunnel_route_list_tunnel_routes(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(Optional[RouteTunnelRouteListTunnelRoutesResponse], route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_tunnel_route_list_tunnel_routes(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.teamnets.routes.with_raw_response.tunnel_route_list_tunnel_routes(
                "",
            )


class TestAsyncRoutes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_tunnel_route_list_tunnel_routes(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.teamnets.routes.tunnel_route_list_tunnel_routes(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[RouteTunnelRouteListTunnelRoutesResponse], route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_tunnel_route_list_tunnel_routes_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.teamnets.routes.tunnel_route_list_tunnel_routes(
            "699d98642c564d2e855e9661899b7252",
            comment="Example comment for this route.",
            existed_at={},
            is_deleted={},
            network_subset={},
            network_superset={},
            page=1,
            per_page=1,
            tun_types="cfd_tunnel,warp_connector",
            tunnel_id={},
            virtual_network_id={},
        )
        assert_matches_type(Optional[RouteTunnelRouteListTunnelRoutesResponse], route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_tunnel_route_list_tunnel_routes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.teamnets.routes.with_raw_response.tunnel_route_list_tunnel_routes(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(Optional[RouteTunnelRouteListTunnelRoutesResponse], route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_tunnel_route_list_tunnel_routes(self, async_client: AsyncCloudflare) -> None:
        async with async_client.teamnets.routes.with_streaming_response.tunnel_route_list_tunnel_routes(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(Optional[RouteTunnelRouteListTunnelRoutesResponse], route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_tunnel_route_list_tunnel_routes(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.teamnets.routes.with_raw_response.tunnel_route_list_tunnel_routes(
                "",
            )
