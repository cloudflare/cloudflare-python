# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.networks.subnets import (
    WARPGetResponse,
    WARPEditResponse,
    WARPCreateResponse,
    WARPDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWARP:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        warp = client.zero_trust.networks.subnets.warp.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
        )
        assert_matches_type(WARPCreateResponse, warp, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        warp = client.zero_trust.networks.subnets.warp.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
            comment="example comment",
            is_default_network=True,
        )
        assert_matches_type(WARPCreateResponse, warp, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.subnets.warp.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp = response.parse()
        assert_matches_type(WARPCreateResponse, warp, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.subnets.warp.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp = response.parse()
            assert_matches_type(WARPCreateResponse, warp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.subnets.warp.with_raw_response.create(
                account_id="",
                name="IPv4 Cloudflare Source IPs",
                network="100.64.0.0/12",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        warp = client.zero_trust.networks.subnets.warp.delete(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[WARPDeleteResponse], warp, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.subnets.warp.with_raw_response.delete(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp = response.parse()
        assert_matches_type(Optional[WARPDeleteResponse], warp, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.subnets.warp.with_streaming_response.delete(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp = response.parse()
            assert_matches_type(Optional[WARPDeleteResponse], warp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.subnets.warp.with_raw_response.delete(
                subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            client.zero_trust.networks.subnets.warp.with_raw_response.delete(
                subnet_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        warp = client.zero_trust.networks.subnets.warp.edit(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(WARPEditResponse, warp, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        warp = client.zero_trust.networks.subnets.warp.edit(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            comment="example comment",
            is_default_network=True,
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
        )
        assert_matches_type(WARPEditResponse, warp, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.subnets.warp.with_raw_response.edit(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp = response.parse()
        assert_matches_type(WARPEditResponse, warp, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.subnets.warp.with_streaming_response.edit(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp = response.parse()
            assert_matches_type(WARPEditResponse, warp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.subnets.warp.with_raw_response.edit(
                subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            client.zero_trust.networks.subnets.warp.with_raw_response.edit(
                subnet_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        warp = client.zero_trust.networks.subnets.warp.get(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(WARPGetResponse, warp, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.subnets.warp.with_raw_response.get(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp = response.parse()
        assert_matches_type(WARPGetResponse, warp, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.subnets.warp.with_streaming_response.get(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp = response.parse()
            assert_matches_type(WARPGetResponse, warp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.subnets.warp.with_raw_response.get(
                subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            client.zero_trust.networks.subnets.warp.with_raw_response.get(
                subnet_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncWARP:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        warp = await async_client.zero_trust.networks.subnets.warp.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
        )
        assert_matches_type(WARPCreateResponse, warp, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        warp = await async_client.zero_trust.networks.subnets.warp.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
            comment="example comment",
            is_default_network=True,
        )
        assert_matches_type(WARPCreateResponse, warp, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.subnets.warp.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp = await response.parse()
        assert_matches_type(WARPCreateResponse, warp, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.subnets.warp.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp = await response.parse()
            assert_matches_type(WARPCreateResponse, warp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.subnets.warp.with_raw_response.create(
                account_id="",
                name="IPv4 Cloudflare Source IPs",
                network="100.64.0.0/12",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        warp = await async_client.zero_trust.networks.subnets.warp.delete(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[WARPDeleteResponse], warp, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.subnets.warp.with_raw_response.delete(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp = await response.parse()
        assert_matches_type(Optional[WARPDeleteResponse], warp, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.subnets.warp.with_streaming_response.delete(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp = await response.parse()
            assert_matches_type(Optional[WARPDeleteResponse], warp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.subnets.warp.with_raw_response.delete(
                subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            await async_client.zero_trust.networks.subnets.warp.with_raw_response.delete(
                subnet_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        warp = await async_client.zero_trust.networks.subnets.warp.edit(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(WARPEditResponse, warp, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        warp = await async_client.zero_trust.networks.subnets.warp.edit(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            comment="example comment",
            is_default_network=True,
            name="IPv4 Cloudflare Source IPs",
            network="100.64.0.0/12",
        )
        assert_matches_type(WARPEditResponse, warp, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.subnets.warp.with_raw_response.edit(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp = await response.parse()
        assert_matches_type(WARPEditResponse, warp, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.subnets.warp.with_streaming_response.edit(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp = await response.parse()
            assert_matches_type(WARPEditResponse, warp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.subnets.warp.with_raw_response.edit(
                subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            await async_client.zero_trust.networks.subnets.warp.with_raw_response.edit(
                subnet_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        warp = await async_client.zero_trust.networks.subnets.warp.get(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(WARPGetResponse, warp, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.subnets.warp.with_raw_response.get(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp = await response.parse()
        assert_matches_type(WARPGetResponse, warp, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.subnets.warp.with_streaming_response.get(
            subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp = await response.parse()
            assert_matches_type(WARPGetResponse, warp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.subnets.warp.with_raw_response.get(
                subnet_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subnet_id` but received ''"):
            await async_client.zero_trust.networks.subnets.warp.with_raw_response.get(
                subnet_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
