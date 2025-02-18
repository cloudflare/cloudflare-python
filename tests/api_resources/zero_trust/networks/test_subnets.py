# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.networks import SubnetListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubnets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        subnet = client.zero_trust.networks.subnets.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncV4PagePaginationArray[SubnetListResponse], subnet, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        subnet = client.zero_trust.networks.subnets.list(
            account_id="699d98642c564d2e855e9661899b7252",
            address_family="v4",
            comment="example%20comment",
            existed_at="2019-10-12T07%3A20%3A50.52Z",
            is_default_network=True,
            is_deleted=True,
            name="IPv4%20Cloudflare%20Source%20IPs",
            network="172.16.0.0%2F16",
            page=1,
            per_page=1,
            sort_order="asc",
            subnet_types="cloudflare_source",
        )
        assert_matches_type(SyncV4PagePaginationArray[SubnetListResponse], subnet, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.subnets.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[SubnetListResponse], subnet, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.subnets.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[SubnetListResponse], subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.subnets.with_raw_response.list(
                account_id="",
            )


class TestAsyncSubnets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        subnet = await async_client.zero_trust.networks.subnets.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncV4PagePaginationArray[SubnetListResponse], subnet, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        subnet = await async_client.zero_trust.networks.subnets.list(
            account_id="699d98642c564d2e855e9661899b7252",
            address_family="v4",
            comment="example%20comment",
            existed_at="2019-10-12T07%3A20%3A50.52Z",
            is_default_network=True,
            is_deleted=True,
            name="IPv4%20Cloudflare%20Source%20IPs",
            network="172.16.0.0%2F16",
            page=1,
            per_page=1,
            sort_order="asc",
            subnet_types="cloudflare_source",
        )
        assert_matches_type(AsyncV4PagePaginationArray[SubnetListResponse], subnet, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.subnets.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subnet = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[SubnetListResponse], subnet, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.subnets.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subnet = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[SubnetListResponse], subnet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.subnets.with_raw_response.list(
                account_id="",
            )
