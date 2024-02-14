# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.users.load_balancers.pools import HealthLoadBalancerPoolsPoolHealthDetailsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_pools_pool_health_details(self, client: Cloudflare) -> None:
        health = client.users.load_balancers.pools.health.load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(HealthLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_load_balancer_pools_pool_health_details(self, client: Cloudflare) -> None:
        response = client.users.load_balancers.pools.health.with_raw_response.load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = response.parse()
        assert_matches_type(HealthLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_load_balancer_pools_pool_health_details(self, client: Cloudflare) -> None:
        with client.users.load_balancers.pools.health.with_streaming_response.load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = response.parse()
            assert_matches_type(HealthLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_load_balancer_pools_pool_health_details(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.users.load_balancers.pools.health.with_raw_response.load_balancer_pools_pool_health_details(
                "",
            )


class TestAsyncHealth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_pools_pool_health_details(self, async_client: AsyncCloudflare) -> None:
        health = await async_client.users.load_balancers.pools.health.load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(HealthLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_load_balancer_pools_pool_health_details(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.load_balancers.pools.health.with_raw_response.load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = await response.parse()
        assert_matches_type(HealthLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_load_balancer_pools_pool_health_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.load_balancers.pools.health.with_streaming_response.load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = await response.parse()
            assert_matches_type(HealthLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_load_balancer_pools_pool_health_details(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.users.load_balancers.pools.health.with_raw_response.load_balancer_pools_pool_health_details(
                "",
            )
