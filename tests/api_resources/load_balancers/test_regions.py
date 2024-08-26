# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.load_balancers import RegionGetResponse, RegionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        region = client.load_balancers.regions.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RegionListResponse, region, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        region = client.load_balancers.regions.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            country_code_a2="US",
            subdivision_code="CA",
            subdivision_code_a2="CA",
        )
        assert_matches_type(RegionListResponse, region, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.load_balancers.regions.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = response.parse()
        assert_matches_type(RegionListResponse, region, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.load_balancers.regions.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = response.parse()
            assert_matches_type(RegionListResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.regions.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        region = client.load_balancers.regions.get(
            region_id="WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RegionGetResponse, region, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.load_balancers.regions.with_raw_response.get(
            region_id="WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = response.parse()
        assert_matches_type(RegionGetResponse, region, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.load_balancers.regions.with_streaming_response.get(
            region_id="WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = response.parse()
            assert_matches_type(RegionGetResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.regions.with_raw_response.get(
                region_id="WNAM",
                account_id="",
            )


class TestAsyncRegions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        region = await async_client.load_balancers.regions.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RegionListResponse, region, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        region = await async_client.load_balancers.regions.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            country_code_a2="US",
            subdivision_code="CA",
            subdivision_code_a2="CA",
        )
        assert_matches_type(RegionListResponse, region, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.regions.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = await response.parse()
        assert_matches_type(RegionListResponse, region, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.regions.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = await response.parse()
            assert_matches_type(RegionListResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.regions.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        region = await async_client.load_balancers.regions.get(
            region_id="WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RegionGetResponse, region, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.regions.with_raw_response.get(
            region_id="WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = await response.parse()
        assert_matches_type(RegionGetResponse, region, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.regions.with_streaming_response.get(
            region_id="WNAM",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = await response.parse()
            assert_matches_type(RegionGetResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.regions.with_raw_response.get(
                region_id="WNAM",
                account_id="",
            )
