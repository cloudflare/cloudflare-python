# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.devices import SettingsPolicy

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        custom = client.zero_trust.devices.policies.custom.create(
            account_id="699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        )
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        custom = client.zero_trust.devices.policies.custom.create(
            account_id="699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
            allow_mode_switch=True,
            allow_updates=True,
            allowed_to_leave=True,
            auto_connect=0,
            captive_portal=180,
            description="Policy for test teams.",
            disable_auto_fallback=True,
            enabled=True,
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
            lan_allow_minutes=30,
            lan_allow_subnet_size=24,
            register_interface_ip_with_dns=True,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
            tunnel_protocol="wireguard",
        )
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.custom.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.custom.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.policies.custom.with_raw_response.create(
                account_id="",
                match='user.identity == "test@cloudflare.com"',
                name="Allow Developers",
                precedence=100,
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        custom = client.zero_trust.devices.policies.custom.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncSinglePage[SettingsPolicy], custom, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.custom.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(SyncSinglePage[SettingsPolicy], custom, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.custom.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(SyncSinglePage[SettingsPolicy], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.policies.custom.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom = client.zero_trust.devices.policies.custom.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncSinglePage[SettingsPolicy], custom, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.custom.with_raw_response.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(SyncSinglePage[SettingsPolicy], custom, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.custom.with_streaming_response.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(SyncSinglePage[SettingsPolicy], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.policies.custom.with_raw_response.delete(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.zero_trust.devices.policies.custom.with_raw_response.delete(
                policy_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        custom = client.zero_trust.devices.policies.custom.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        custom = client.zero_trust.devices.policies.custom.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            allow_mode_switch=True,
            allow_updates=True,
            allowed_to_leave=True,
            auto_connect=0,
            captive_portal=180,
            description="Policy for test teams.",
            disable_auto_fallback=True,
            enabled=True,
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
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
            register_interface_ip_with_dns=True,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
            tunnel_protocol="wireguard",
        )
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.custom.with_raw_response.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.custom.with_streaming_response.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.policies.custom.with_raw_response.edit(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.zero_trust.devices.policies.custom.with_raw_response.edit(
                policy_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom = client.zero_trust.devices.policies.custom.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.custom.with_raw_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.custom.with_streaming_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.policies.custom.with_raw_response.get(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.zero_trust.devices.policies.custom.with_raw_response.get(
                policy_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncCustom:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.devices.policies.custom.create(
            account_id="699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        )
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.devices.policies.custom.create(
            account_id="699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
            allow_mode_switch=True,
            allow_updates=True,
            allowed_to_leave=True,
            auto_connect=0,
            captive_portal=180,
            description="Policy for test teams.",
            disable_auto_fallback=True,
            enabled=True,
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
            lan_allow_minutes=30,
            lan_allow_subnet_size=24,
            register_interface_ip_with_dns=True,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
            tunnel_protocol="wireguard",
        )
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.custom.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.custom.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.with_raw_response.create(
                account_id="",
                match='user.identity == "test@cloudflare.com"',
                name="Allow Developers",
                precedence=100,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.devices.policies.custom.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncSinglePage[SettingsPolicy], custom, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.custom.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(AsyncSinglePage[SettingsPolicy], custom, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.custom.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(AsyncSinglePage[SettingsPolicy], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.devices.policies.custom.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncSinglePage[SettingsPolicy], custom, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.custom.with_raw_response.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(AsyncSinglePage[SettingsPolicy], custom, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.custom.with_streaming_response.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(AsyncSinglePage[SettingsPolicy], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.with_raw_response.delete(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.with_raw_response.delete(
                policy_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.devices.policies.custom.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.devices.policies.custom.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            allow_mode_switch=True,
            allow_updates=True,
            allowed_to_leave=True,
            auto_connect=0,
            captive_portal=180,
            description="Policy for test teams.",
            disable_auto_fallback=True,
            enabled=True,
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
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
            register_interface_ip_with_dns=True,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
            tunnel_protocol="wireguard",
        )
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.custom.with_raw_response.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.custom.with_streaming_response.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.with_raw_response.edit(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.with_raw_response.edit(
                policy_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.devices.policies.custom.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.custom.with_raw_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.custom.with_streaming_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[SettingsPolicy], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.with_raw_response.get(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.with_raw_response.get(
                policy_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
