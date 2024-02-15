# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magics import (
    RouteGetResponse,
    RouteDeleteResponse,
    RouteUpdateResponse,
    RouteMagicStaticRoutesListRoutesResponse,
    RouteMagicStaticRoutesCreateRoutesResponse,
    RouteMagicStaticRoutesUpdateManyRoutesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        route = client.magics.routes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        route = client.magics.routes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
            description="New route for new prefix 203.0.113.1",
            scope={
                "colo_names": ["den01", "den01", "den01"],
                "colo_regions": ["APAC", "APAC", "APAC"],
            },
            weight=0,
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magics.routes.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magics.routes.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteUpdateResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.routes.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                nexthop="203.0.113.1",
                prefix="192.0.2.0/24",
                priority=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_identifier` but received ''"):
            client.magics.routes.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                nexthop="203.0.113.1",
                prefix="192.0.2.0/24",
                priority=0,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        route = client.magics.routes.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magics.routes.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magics.routes.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteDeleteResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.routes.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_identifier` but received ''"):
            client.magics.routes.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        route = client.magics.routes.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteGetResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magics.routes.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteGetResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magics.routes.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteGetResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.routes.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_identifier` but received ''"):
            client.magics.routes.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_static_routes_create_routes(self, client: Cloudflare) -> None:
        route = client.magics.routes.magic_static_routes_create_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(RouteMagicStaticRoutesCreateRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_static_routes_create_routes(self, client: Cloudflare) -> None:
        response = client.magics.routes.with_raw_response.magic_static_routes_create_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteMagicStaticRoutesCreateRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_static_routes_create_routes(self, client: Cloudflare) -> None:
        with client.magics.routes.with_streaming_response.magic_static_routes_create_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteMagicStaticRoutesCreateRoutesResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_static_routes_create_routes(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.routes.with_raw_response.magic_static_routes_create_routes(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_static_routes_list_routes(self, client: Cloudflare) -> None:
        route = client.magics.routes.magic_static_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteMagicStaticRoutesListRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_static_routes_list_routes(self, client: Cloudflare) -> None:
        response = client.magics.routes.with_raw_response.magic_static_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteMagicStaticRoutesListRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_static_routes_list_routes(self, client: Cloudflare) -> None:
        with client.magics.routes.with_streaming_response.magic_static_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteMagicStaticRoutesListRoutesResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_static_routes_list_routes(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.routes.with_raw_response.magic_static_routes_list_routes(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_static_routes_update_many_routes(self, client: Cloudflare) -> None:
        route = client.magics.routes.magic_static_routes_update_many_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            routes=[
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
            ],
        )
        assert_matches_type(RouteMagicStaticRoutesUpdateManyRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_static_routes_update_many_routes(self, client: Cloudflare) -> None:
        response = client.magics.routes.with_raw_response.magic_static_routes_update_many_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            routes=[
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteMagicStaticRoutesUpdateManyRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_static_routes_update_many_routes(self, client: Cloudflare) -> None:
        with client.magics.routes.with_streaming_response.magic_static_routes_update_many_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            routes=[
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteMagicStaticRoutesUpdateManyRoutesResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_static_routes_update_many_routes(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.routes.with_raw_response.magic_static_routes_update_many_routes(
                "",
                routes=[
                    {
                        "nexthop": "203.0.113.1",
                        "prefix": "192.0.2.0/24",
                        "priority": 0,
                    },
                    {
                        "nexthop": "203.0.113.1",
                        "prefix": "192.0.2.0/24",
                        "priority": 0,
                    },
                    {
                        "nexthop": "203.0.113.1",
                        "prefix": "192.0.2.0/24",
                        "priority": 0,
                    },
                ],
            )


class TestAsyncRoutes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magics.routes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magics.routes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
            description="New route for new prefix 203.0.113.1",
            scope={
                "colo_names": ["den01", "den01", "den01"],
                "colo_regions": ["APAC", "APAC", "APAC"],
            },
            weight=0,
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.routes.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.routes.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteUpdateResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.routes.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                nexthop="203.0.113.1",
                prefix="192.0.2.0/24",
                priority=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_identifier` but received ''"):
            await async_client.magics.routes.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                nexthop="203.0.113.1",
                prefix="192.0.2.0/24",
                priority=0,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magics.routes.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.routes.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.routes.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteDeleteResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.routes.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_identifier` but received ''"):
            await async_client.magics.routes.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magics.routes.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteGetResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.routes.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteGetResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.routes.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteGetResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.routes.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_identifier` but received ''"):
            await async_client.magics.routes.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_static_routes_create_routes(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magics.routes.magic_static_routes_create_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(RouteMagicStaticRoutesCreateRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_static_routes_create_routes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.routes.with_raw_response.magic_static_routes_create_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteMagicStaticRoutesCreateRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_static_routes_create_routes(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.routes.with_streaming_response.magic_static_routes_create_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteMagicStaticRoutesCreateRoutesResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_static_routes_create_routes(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.routes.with_raw_response.magic_static_routes_create_routes(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_static_routes_list_routes(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magics.routes.magic_static_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteMagicStaticRoutesListRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_static_routes_list_routes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.routes.with_raw_response.magic_static_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteMagicStaticRoutesListRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_static_routes_list_routes(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.routes.with_streaming_response.magic_static_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteMagicStaticRoutesListRoutesResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_static_routes_list_routes(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.routes.with_raw_response.magic_static_routes_list_routes(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_static_routes_update_many_routes(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magics.routes.magic_static_routes_update_many_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            routes=[
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
            ],
        )
        assert_matches_type(RouteMagicStaticRoutesUpdateManyRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_static_routes_update_many_routes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.routes.with_raw_response.magic_static_routes_update_many_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            routes=[
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteMagicStaticRoutesUpdateManyRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_static_routes_update_many_routes(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.magics.routes.with_streaming_response.magic_static_routes_update_many_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
            routes=[
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
                {
                    "nexthop": "203.0.113.1",
                    "prefix": "192.0.2.0/24",
                    "priority": 0,
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteMagicStaticRoutesUpdateManyRoutesResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_static_routes_update_many_routes(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.routes.with_raw_response.magic_static_routes_update_many_routes(
                "",
                routes=[
                    {
                        "nexthop": "203.0.113.1",
                        "prefix": "192.0.2.0/24",
                        "priority": 0,
                    },
                    {
                        "nexthop": "203.0.113.1",
                        "prefix": "192.0.2.0/24",
                        "priority": 0,
                    },
                    {
                        "nexthop": "203.0.113.1",
                        "prefix": "192.0.2.0/24",
                        "priority": 0,
                    },
                ],
            )
