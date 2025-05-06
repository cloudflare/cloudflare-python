# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.devices.resilience import (
    GlobalWARPOverrideGetResponse,
    GlobalWARPOverrideCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGlobalWARPOverride:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        global_warp_override = client.zero_trust.devices.resilience.global_warp_override.create(
            account_id="699d98642c564d2e855e9661899b7252",
            disconnect=False,
        )
        assert_matches_type(Optional[GlobalWARPOverrideCreateResponse], global_warp_override, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        global_warp_override = client.zero_trust.devices.resilience.global_warp_override.create(
            account_id="699d98642c564d2e855e9661899b7252",
            disconnect=False,
            justification="Turning off WARP for testing purposes.",
        )
        assert_matches_type(Optional[GlobalWARPOverrideCreateResponse], global_warp_override, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.resilience.global_warp_override.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            disconnect=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_warp_override = response.parse()
        assert_matches_type(Optional[GlobalWARPOverrideCreateResponse], global_warp_override, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.resilience.global_warp_override.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            disconnect=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_warp_override = response.parse()
            assert_matches_type(Optional[GlobalWARPOverrideCreateResponse], global_warp_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.resilience.global_warp_override.with_raw_response.create(
                account_id="",
                disconnect=False,
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        global_warp_override = client.zero_trust.devices.resilience.global_warp_override.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[GlobalWARPOverrideGetResponse], global_warp_override, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.resilience.global_warp_override.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_warp_override = response.parse()
        assert_matches_type(Optional[GlobalWARPOverrideGetResponse], global_warp_override, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.resilience.global_warp_override.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_warp_override = response.parse()
            assert_matches_type(Optional[GlobalWARPOverrideGetResponse], global_warp_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.resilience.global_warp_override.with_raw_response.get(
                account_id="",
            )


class TestAsyncGlobalWARPOverride:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        global_warp_override = await async_client.zero_trust.devices.resilience.global_warp_override.create(
            account_id="699d98642c564d2e855e9661899b7252",
            disconnect=False,
        )
        assert_matches_type(Optional[GlobalWARPOverrideCreateResponse], global_warp_override, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        global_warp_override = await async_client.zero_trust.devices.resilience.global_warp_override.create(
            account_id="699d98642c564d2e855e9661899b7252",
            disconnect=False,
            justification="Turning off WARP for testing purposes.",
        )
        assert_matches_type(Optional[GlobalWARPOverrideCreateResponse], global_warp_override, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.resilience.global_warp_override.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            disconnect=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_warp_override = await response.parse()
        assert_matches_type(Optional[GlobalWARPOverrideCreateResponse], global_warp_override, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.resilience.global_warp_override.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            disconnect=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_warp_override = await response.parse()
            assert_matches_type(Optional[GlobalWARPOverrideCreateResponse], global_warp_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.resilience.global_warp_override.with_raw_response.create(
                account_id="",
                disconnect=False,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        global_warp_override = await async_client.zero_trust.devices.resilience.global_warp_override.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[GlobalWARPOverrideGetResponse], global_warp_override, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.resilience.global_warp_override.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_warp_override = await response.parse()
        assert_matches_type(Optional[GlobalWARPOverrideGetResponse], global_warp_override, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.resilience.global_warp_override.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_warp_override = await response.parse()
            assert_matches_type(Optional[GlobalWARPOverrideGetResponse], global_warp_override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.resilience.global_warp_override.with_raw_response.get(
                account_id="",
            )
