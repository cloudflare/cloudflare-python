# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.magic_transit import RouteCreateResponse, RouteUpdateResponse, RouteListResponse, RouteDeleteResponse, RouteEmptyResponse, RouteGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_transit import route_create_params
from cloudflare.types.magic_transit import route_update_params
from cloudflare.types.magic_transit import Scope

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        route = client.magic_transit.routes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(RouteCreateResponse, route, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:

        response = client.magic_transit.routes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = response.parse()
        assert_matches_type(RouteCreateResponse, route, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_transit.routes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = response.parse()
            assert_matches_type(RouteCreateResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.magic_transit.routes.with_raw_response.create(
              account_id="",
              body={},
          )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        route = client.magic_transit.routes.update(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        )
        assert_matches_type(RouteUpdateResponse, route, path=['response'])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        route = client.magic_transit.routes.update(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(RouteUpdateResponse, route, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:

        response = client.magic_transit.routes.with_raw_response.update(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = response.parse()
        assert_matches_type(RouteUpdateResponse, route, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_transit.routes.with_streaming_response.update(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = response.parse()
            assert_matches_type(RouteUpdateResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.magic_transit.routes.with_raw_response.update(
              route_id="023e105f4ecef8ad9ca31a8372d0c353",
              account_id="",
              nexthop="203.0.113.1",
              prefix="192.0.2.0/24",
              priority=0,
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
          client.magic_transit.routes.with_raw_response.update(
              route_id="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
              nexthop="203.0.113.1",
              prefix="192.0.2.0/24",
              priority=0,
          )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        route = client.magic_transit.routes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteListResponse, route, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:

        response = client.magic_transit.routes.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = response.parse()
        assert_matches_type(RouteListResponse, route, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.routes.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = response.parse()
            assert_matches_type(RouteListResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.magic_transit.routes.with_raw_response.list(
              account_id="",
          )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        route = client.magic_transit.routes.delete(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteDeleteResponse, route, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:

        response = client.magic_transit.routes.with_raw_response.delete(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = response.parse()
        assert_matches_type(RouteDeleteResponse, route, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_transit.routes.with_streaming_response.delete(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = response.parse()
            assert_matches_type(RouteDeleteResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.magic_transit.routes.with_raw_response.delete(
              route_id="023e105f4ecef8ad9ca31a8372d0c353",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
          client.magic_transit.routes.with_raw_response.delete(
              route_id="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )

    @parametrize
    def test_method_empty(self, client: Cloudflare) -> None:
        route = client.magic_transit.routes.empty(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteEmptyResponse, route, path=['response'])

    @parametrize
    def test_raw_response_empty(self, client: Cloudflare) -> None:

        response = client.magic_transit.routes.with_raw_response.empty(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = response.parse()
        assert_matches_type(RouteEmptyResponse, route, path=['response'])

    @parametrize
    def test_streaming_response_empty(self, client: Cloudflare) -> None:
        with client.magic_transit.routes.with_streaming_response.empty(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = response.parse()
            assert_matches_type(RouteEmptyResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_empty(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.magic_transit.routes.with_raw_response.empty(
              account_id="",
          )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        route = client.magic_transit.routes.get(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteGetResponse, route, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.magic_transit.routes.with_raw_response.get(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = response.parse()
        assert_matches_type(RouteGetResponse, route, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.routes.with_streaming_response.get(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = response.parse()
            assert_matches_type(RouteGetResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.magic_transit.routes.with_raw_response.get(
              route_id="023e105f4ecef8ad9ca31a8372d0c353",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
          client.magic_transit.routes.with_raw_response.get(
              route_id="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )
class TestAsyncRoutes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magic_transit.routes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(RouteCreateResponse, route, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.magic_transit.routes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = await response.parse()
        assert_matches_type(RouteCreateResponse, route, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.routes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = await response.parse()
            assert_matches_type(RouteCreateResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.magic_transit.routes.with_raw_response.create(
              account_id="",
              body={},
          )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magic_transit.routes.update(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        )
        assert_matches_type(RouteUpdateResponse, route, path=['response'])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magic_transit.routes.update(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(RouteUpdateResponse, route, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.magic_transit.routes.with_raw_response.update(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = await response.parse()
        assert_matches_type(RouteUpdateResponse, route, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.routes.with_streaming_response.update(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            nexthop="203.0.113.1",
            prefix="192.0.2.0/24",
            priority=0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = await response.parse()
            assert_matches_type(RouteUpdateResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.magic_transit.routes.with_raw_response.update(
              route_id="023e105f4ecef8ad9ca31a8372d0c353",
              account_id="",
              nexthop="203.0.113.1",
              prefix="192.0.2.0/24",
              priority=0,
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
          await async_client.magic_transit.routes.with_raw_response.update(
              route_id="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
              nexthop="203.0.113.1",
              prefix="192.0.2.0/24",
              priority=0,
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magic_transit.routes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteListResponse, route, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.magic_transit.routes.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = await response.parse()
        assert_matches_type(RouteListResponse, route, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.routes.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = await response.parse()
            assert_matches_type(RouteListResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.magic_transit.routes.with_raw_response.list(
              account_id="",
          )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magic_transit.routes.delete(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteDeleteResponse, route, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.magic_transit.routes.with_raw_response.delete(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = await response.parse()
        assert_matches_type(RouteDeleteResponse, route, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.routes.with_streaming_response.delete(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = await response.parse()
            assert_matches_type(RouteDeleteResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.magic_transit.routes.with_raw_response.delete(
              route_id="023e105f4ecef8ad9ca31a8372d0c353",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
          await async_client.magic_transit.routes.with_raw_response.delete(
              route_id="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )

    @parametrize
    async def test_method_empty(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magic_transit.routes.empty(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteEmptyResponse, route, path=['response'])

    @parametrize
    async def test_raw_response_empty(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.magic_transit.routes.with_raw_response.empty(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = await response.parse()
        assert_matches_type(RouteEmptyResponse, route, path=['response'])

    @parametrize
    async def test_streaming_response_empty(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.routes.with_streaming_response.empty(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = await response.parse()
            assert_matches_type(RouteEmptyResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_empty(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.magic_transit.routes.with_raw_response.empty(
              account_id="",
          )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.magic_transit.routes.get(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteGetResponse, route, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.magic_transit.routes.with_raw_response.get(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        route = await response.parse()
        assert_matches_type(RouteGetResponse, route, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.routes.with_streaming_response.get(
            route_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            route = await response.parse()
            assert_matches_type(RouteGetResponse, route, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.magic_transit.routes.with_raw_response.get(
              route_id="023e105f4ecef8ad9ca31a8372d0c353",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
          await async_client.magic_transit.routes.with_raw_response.get(
              route_id="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )