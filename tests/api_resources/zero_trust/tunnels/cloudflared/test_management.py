# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManagement:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        management = client.zero_trust.tunnels.cloudflared.management.create(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            resources=["logs"],
        )
        assert_matches_type(str, management, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.tunnels.cloudflared.management.with_raw_response.create(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            resources=["logs"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        management = response.parse()
        assert_matches_type(str, management, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.tunnels.cloudflared.management.with_streaming_response.create(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            resources=["logs"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            management = response.parse()
            assert_matches_type(str, management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.tunnels.cloudflared.management.with_raw_response.create(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
                resources=["logs"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.zero_trust.tunnels.cloudflared.management.with_raw_response.create(
                tunnel_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                resources=["logs"],
            )


class TestAsyncManagement:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        management = await async_client.zero_trust.tunnels.cloudflared.management.create(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            resources=["logs"],
        )
        assert_matches_type(str, management, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.tunnels.cloudflared.management.with_raw_response.create(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            resources=["logs"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        management = await response.parse()
        assert_matches_type(str, management, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.tunnels.cloudflared.management.with_streaming_response.create(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            resources=["logs"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            management = await response.parse()
            assert_matches_type(str, management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.tunnels.cloudflared.management.with_raw_response.create(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
                resources=["logs"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.zero_trust.tunnels.cloudflared.management.with_raw_response.create(
                tunnel_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                resources=["logs"],
            )
