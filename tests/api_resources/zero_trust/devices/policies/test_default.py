# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.devices.policies import DefaultGetResponse, DefaultEditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefault:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        default = client.zero_trust.devices.policies.default.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DefaultEditResponse], default, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        default = client.zero_trust.devices.policies.default.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            allow_mode_switch=True,
            allow_updates=True,
            allowed_to_leave=True,
            auto_connect=0,
            captive_portal=180,
            disable_auto_fallback=True,
            exclude=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                    "host": "*.example.com",
                }
            ],
            exclude_office_ips=True,
            include=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                    "host": "*.example.com",
                }
            ],
            register_interface_ip_with_dns=True,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
            tunnel_protocol="wireguard",
        )
        assert_matches_type(Optional[DefaultEditResponse], default, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.default.with_raw_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        default = response.parse()
        assert_matches_type(Optional[DefaultEditResponse], default, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.default.with_streaming_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            default = response.parse()
            assert_matches_type(Optional[DefaultEditResponse], default, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.policies.default.with_raw_response.edit(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        default = client.zero_trust.devices.policies.default.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DefaultGetResponse], default, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.default.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        default = response.parse()
        assert_matches_type(Optional[DefaultGetResponse], default, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.default.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            default = response.parse()
            assert_matches_type(Optional[DefaultGetResponse], default, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.policies.default.with_raw_response.get(
                account_id="",
            )


class TestAsyncDefault:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        default = await async_client.zero_trust.devices.policies.default.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DefaultEditResponse], default, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        default = await async_client.zero_trust.devices.policies.default.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            allow_mode_switch=True,
            allow_updates=True,
            allowed_to_leave=True,
            auto_connect=0,
            captive_portal=180,
            disable_auto_fallback=True,
            exclude=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                    "host": "*.example.com",
                }
            ],
            exclude_office_ips=True,
            include=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                    "host": "*.example.com",
                }
            ],
            register_interface_ip_with_dns=True,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
            tunnel_protocol="wireguard",
        )
        assert_matches_type(Optional[DefaultEditResponse], default, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.default.with_raw_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        default = await response.parse()
        assert_matches_type(Optional[DefaultEditResponse], default, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.default.with_streaming_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            default = await response.parse()
            assert_matches_type(Optional[DefaultEditResponse], default, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.policies.default.with_raw_response.edit(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        default = await async_client.zero_trust.devices.policies.default.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DefaultGetResponse], default, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.default.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        default = await response.parse()
        assert_matches_type(Optional[DefaultGetResponse], default, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.default.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            default = await response.parse()
            assert_matches_type(Optional[DefaultGetResponse], default, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.policies.default.with_raw_response.get(
                account_id="",
            )
