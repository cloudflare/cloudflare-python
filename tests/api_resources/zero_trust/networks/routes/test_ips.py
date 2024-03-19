# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.networks import TunnelTeamnet

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ip = client.zero_trust.networks.routes.ips.get(
            "10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(TunnelTeamnet, ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        ip = client.zero_trust.networks.routes.ips.get(
            "10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
            virtual_network_id={},
        )
        assert_matches_type(TunnelTeamnet, ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.routes.ips.with_raw_response.get(
            "10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = response.parse()
        assert_matches_type(TunnelTeamnet, ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.routes.ips.with_streaming_response.get(
            "10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = response.parse()
            assert_matches_type(TunnelTeamnet, ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.routes.ips.with_raw_response.get(
                "10.1.0.137",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip` but received ''"):
            client.zero_trust.networks.routes.ips.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncIPs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ip = await async_client.zero_trust.networks.routes.ips.get(
            "10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(TunnelTeamnet, ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ip = await async_client.zero_trust.networks.routes.ips.get(
            "10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
            virtual_network_id={},
        )
        assert_matches_type(TunnelTeamnet, ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.routes.ips.with_raw_response.get(
            "10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = await response.parse()
        assert_matches_type(TunnelTeamnet, ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.routes.ips.with_streaming_response.get(
            "10.1.0.137",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = await response.parse()
            assert_matches_type(TunnelTeamnet, ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.routes.ips.with_raw_response.get(
                "10.1.0.137",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip` but received ''"):
            await async_client.zero_trust.networks.routes.ips.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )
