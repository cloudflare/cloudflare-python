# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.load_balancers import RegionGetResponse, RegionLoadBalancerRegionsListRegionsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.load_balancers import region_load_balancer_regions_list_regions_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        region = client.load_balancers.regions.get(
            "WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RegionGetResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.load_balancers.regions.with_raw_response.get(
            "WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = response.parse()
        assert_matches_type(RegionGetResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.load_balancers.regions.with_streaming_response.get(
            "WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = response.parse()
            assert_matches_type(RegionGetResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.regions.with_raw_response.get(
                "WNAM",
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_regions_list_regions(self, client: Cloudflare) -> None:
        region = client.load_balancers.regions.load_balancer_regions_list_regions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RegionLoadBalancerRegionsListRegionsResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_regions_list_regions_with_all_params(self, client: Cloudflare) -> None:
        region = client.load_balancers.regions.load_balancer_regions_list_regions(
            "023e105f4ecef8ad9ca31a8372d0c353",
            country_code_a2="US",
            subdivision_code="CA",
            subdivision_code_a2="CA",
        )
        assert_matches_type(RegionLoadBalancerRegionsListRegionsResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_load_balancer_regions_list_regions(self, client: Cloudflare) -> None:
        response = client.load_balancers.regions.with_raw_response.load_balancer_regions_list_regions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = response.parse()
        assert_matches_type(RegionLoadBalancerRegionsListRegionsResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_load_balancer_regions_list_regions(self, client: Cloudflare) -> None:
        with client.load_balancers.regions.with_streaming_response.load_balancer_regions_list_regions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = response.parse()
            assert_matches_type(RegionLoadBalancerRegionsListRegionsResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_load_balancer_regions_list_regions(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.regions.with_raw_response.load_balancer_regions_list_regions(
                "",
            )


class TestAsyncRegions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        region = await async_client.load_balancers.regions.get(
            "WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RegionGetResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.regions.with_raw_response.get(
            "WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = await response.parse()
        assert_matches_type(RegionGetResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.regions.with_streaming_response.get(
            "WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = await response.parse()
            assert_matches_type(RegionGetResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.regions.with_raw_response.get(
                "WNAM",
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_regions_list_regions(self, async_client: AsyncCloudflare) -> None:
        region = await async_client.load_balancers.regions.load_balancer_regions_list_regions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RegionLoadBalancerRegionsListRegionsResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_regions_list_regions_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        region = await async_client.load_balancers.regions.load_balancer_regions_list_regions(
            "023e105f4ecef8ad9ca31a8372d0c353",
            country_code_a2="US",
            subdivision_code="CA",
            subdivision_code_a2="CA",
        )
        assert_matches_type(RegionLoadBalancerRegionsListRegionsResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_load_balancer_regions_list_regions(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.regions.with_raw_response.load_balancer_regions_list_regions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = await response.parse()
        assert_matches_type(RegionLoadBalancerRegionsListRegionsResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_load_balancer_regions_list_regions(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.regions.with_streaming_response.load_balancer_regions_list_regions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = await response.parse()
            assert_matches_type(RegionLoadBalancerRegionsListRegionsResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_load_balancer_regions_list_regions(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.regions.with_raw_response.load_balancer_regions_list_regions(
                "",
            )
