# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.networks.subnets import CloudflareSourceUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCloudflareSource:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        cloudflare_source = client.zero_trust.networks.subnets.cloudflare_source.update(
            address_family="v4",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(CloudflareSourceUpdateResponse, cloudflare_source, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        cloudflare_source = client.zero_trust.networks.subnets.cloudflare_source.update(
            address_family="v4",
            account_id="699d98642c564d2e855e9661899b7252",
            comment="example comment",
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
        )
        assert_matches_type(CloudflareSourceUpdateResponse, cloudflare_source, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.subnets.cloudflare_source.with_raw_response.update(
            address_family="v4",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloudflare_source = response.parse()
        assert_matches_type(CloudflareSourceUpdateResponse, cloudflare_source, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.subnets.cloudflare_source.with_streaming_response.update(
            address_family="v4",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloudflare_source = response.parse()
            assert_matches_type(CloudflareSourceUpdateResponse, cloudflare_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.subnets.cloudflare_source.with_raw_response.update(
                address_family="v4",
                account_id="",
            )


class TestAsyncCloudflareSource:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        cloudflare_source = await async_client.zero_trust.networks.subnets.cloudflare_source.update(
            address_family="v4",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(CloudflareSourceUpdateResponse, cloudflare_source, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cloudflare_source = await async_client.zero_trust.networks.subnets.cloudflare_source.update(
            address_family="v4",
            account_id="699d98642c564d2e855e9661899b7252",
            comment="example comment",
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
        )
        assert_matches_type(CloudflareSourceUpdateResponse, cloudflare_source, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.subnets.cloudflare_source.with_raw_response.update(
            address_family="v4",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloudflare_source = await response.parse()
        assert_matches_type(CloudflareSourceUpdateResponse, cloudflare_source, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.subnets.cloudflare_source.with_streaming_response.update(
            address_family="v4",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloudflare_source = await response.parse()
            assert_matches_type(CloudflareSourceUpdateResponse, cloudflare_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.subnets.cloudflare_source.with_raw_response.update(
                address_family="v4",
                account_id="",
            )
