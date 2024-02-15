# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import (
    GatewayZeroTrustAccountsCreateZeroTrustAccountResponse,
    GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse,
)

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


class TestGateways:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_create_zero_trust_account(self, client: Cloudflare) -> None:
        gateway = client.gateways.zero_trust_accounts_create_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(GatewayZeroTrustAccountsCreateZeroTrustAccountResponse, gateway, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_accounts_create_zero_trust_account(self, client: Cloudflare) -> None:
        response = client.gateways.with_raw_response.zero_trust_accounts_create_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert_matches_type(GatewayZeroTrustAccountsCreateZeroTrustAccountResponse, gateway, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_accounts_create_zero_trust_account(self, client: Cloudflare) -> None:
        with client.gateways.with_streaming_response.zero_trust_accounts_create_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert_matches_type(GatewayZeroTrustAccountsCreateZeroTrustAccountResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_get_zero_trust_account_information(self, client: Cloudflare) -> None:
        gateway = client.gateways.zero_trust_accounts_get_zero_trust_account_information(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse, gateway, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_accounts_get_zero_trust_account_information(self, client: Cloudflare) -> None:
        response = client.gateways.with_raw_response.zero_trust_accounts_get_zero_trust_account_information(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert_matches_type(GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse, gateway, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_accounts_get_zero_trust_account_information(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.with_streaming_response.zero_trust_accounts_get_zero_trust_account_information(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert_matches_type(
                GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse, gateway, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncGateways:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_create_zero_trust_account(self, async_client: AsyncCloudflare) -> None:
        gateway = await async_client.gateways.zero_trust_accounts_create_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(GatewayZeroTrustAccountsCreateZeroTrustAccountResponse, gateway, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_accounts_create_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.gateways.with_raw_response.zero_trust_accounts_create_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert_matches_type(GatewayZeroTrustAccountsCreateZeroTrustAccountResponse, gateway, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_accounts_create_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.with_streaming_response.zero_trust_accounts_create_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert_matches_type(GatewayZeroTrustAccountsCreateZeroTrustAccountResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_get_zero_trust_account_information(
        self, async_client: AsyncCloudflare
    ) -> None:
        gateway = await async_client.gateways.zero_trust_accounts_get_zero_trust_account_information(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse, gateway, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_accounts_get_zero_trust_account_information(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.gateways.with_raw_response.zero_trust_accounts_get_zero_trust_account_information(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert_matches_type(GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse, gateway, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_accounts_get_zero_trust_account_information(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.with_streaming_response.zero_trust_accounts_get_zero_trust_account_information(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert_matches_type(
                GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse, gateway, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
