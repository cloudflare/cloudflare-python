# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.load_balancers.pools import HealthAccountLoadBalancerPoolsPoolHealthDetailsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_load_balancer_pools_pool_health_details(self, client: Cloudflare) -> None:
        health = client.load_balancers.pools.health.account_load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HealthAccountLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_load_balancer_pools_pool_health_details(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.health.with_raw_response.account_load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = response.parse()
        assert_matches_type(HealthAccountLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_load_balancer_pools_pool_health_details(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.health.with_streaming_response.account_load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = response.parse()
            assert_matches_type(HealthAccountLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_load_balancer_pools_pool_health_details(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.load_balancers.pools.health.with_raw_response.account_load_balancer_pools_pool_health_details(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.load_balancers.pools.health.with_raw_response.account_load_balancer_pools_pool_health_details(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncHealth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_load_balancer_pools_pool_health_details(self, async_client: AsyncCloudflare) -> None:
        health = await async_client.load_balancers.pools.health.account_load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HealthAccountLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_load_balancer_pools_pool_health_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.load_balancers.pools.health.with_raw_response.account_load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = await response.parse()
        assert_matches_type(HealthAccountLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_load_balancer_pools_pool_health_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.load_balancers.pools.health.with_streaming_response.account_load_balancer_pools_pool_health_details(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = await response.parse()
            assert_matches_type(HealthAccountLoadBalancerPoolsPoolHealthDetailsResponse, health, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_load_balancer_pools_pool_health_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.load_balancers.pools.health.with_raw_response.account_load_balancer_pools_pool_health_details(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.load_balancers.pools.health.with_raw_response.account_load_balancer_pools_pool_health_details(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
