# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.zero_trust.networks import Teamnet

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.networks.routes import ip_get_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ip = client.zero_trust.networks.routes.ips.get(
            ip="10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Teamnet, ip, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        ip = client.zero_trust.networks.routes.ips.get(
            ip="10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
            virtual_network_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Teamnet, ip, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.routes.ips.with_raw_response.get(
            ip="10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = response.parse()
        assert_matches_type(Teamnet, ip, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.routes.ips.with_streaming_response.get(
            ip="10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = response.parse()
            assert_matches_type(Teamnet, ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.routes.ips.with_raw_response.get(
                ip="10.1.0.137",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip` but received ''"):
            client.zero_trust.networks.routes.ips.with_raw_response.get(
                ip="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncIPs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ip = await async_client.zero_trust.networks.routes.ips.get(
            ip="10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Teamnet, ip, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ip = await async_client.zero_trust.networks.routes.ips.get(
            ip="10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
            virtual_network_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Teamnet, ip, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.routes.ips.with_raw_response.get(
            ip="10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = await response.parse()
        assert_matches_type(Teamnet, ip, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.routes.ips.with_streaming_response.get(
            ip="10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = await response.parse()
            assert_matches_type(Teamnet, ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.routes.ips.with_raw_response.get(
                ip="10.1.0.137",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip` but received ''"):
            await async_client.zero_trust.networks.routes.ips.with_raw_response.get(
                ip="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
