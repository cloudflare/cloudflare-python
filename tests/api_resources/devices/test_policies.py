# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.devices import (
    PolicyUpdateResponse,
    PolicyDeleteResponse,
    PolicyDevicesCreateDeviceSettingsPolicyResponse,
    PolicyDevicesGetDefaultDeviceSettingsPolicyResponse,
    PolicyDevicesListDeviceSettingsPoliciesResponse,
    PolicyDevicesUpdateDefaultDeviceSettingsPolicyResponse,
    PolicyGetResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.devices import policy_update_params
from cloudflare.types.devices import policy_devices_create_device_settings_policy_params
from cloudflare.types.devices import policy_devices_update_default_device_settings_policy_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        policy = client.devices.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        policy = client.devices.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            allow_mode_switch=True,
            allow_updates=True,
            allowed_to_leave=True,
            auto_connect=0,
            captive_portal=180,
            description="Policy for test teams.",
            disable_auto_fallback=True,
            enabled=True,
            exclude_office_ips=True,
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
        )
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.devices.policies.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.devices.policies.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.policies.with_raw_response.update(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        policy = client.devices.policies.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyDeleteResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.devices.policies.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[PolicyDeleteResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.devices.policies.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Optional[PolicyDeleteResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.policies.with_raw_response.delete(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_create_device_settings_policy(self, client: Cloudflare) -> None:
        policy = client.devices.policies.devices_create_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        )
        assert_matches_type(Optional[PolicyDevicesCreateDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_create_device_settings_policy_with_all_params(self, client: Cloudflare) -> None:
        policy = client.devices.policies.devices_create_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
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
            exclude_office_ips=True,
            lan_allow_minutes=30,
            lan_allow_subnet_size=24,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
        )
        assert_matches_type(Optional[PolicyDevicesCreateDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_create_device_settings_policy(self, client: Cloudflare) -> None:
        response = client.devices.policies.with_raw_response.devices_create_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[PolicyDevicesCreateDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_create_device_settings_policy(self, client: Cloudflare) -> None:
        with client.devices.policies.with_streaming_response.devices_create_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Optional[PolicyDevicesCreateDeviceSettingsPolicyResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_get_default_device_settings_policy(self, client: Cloudflare) -> None:
        policy = client.devices.policies.devices_get_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyDevicesGetDefaultDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_get_default_device_settings_policy(self, client: Cloudflare) -> None:
        response = client.devices.policies.with_raw_response.devices_get_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[PolicyDevicesGetDefaultDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_get_default_device_settings_policy(self, client: Cloudflare) -> None:
        with client.devices.policies.with_streaming_response.devices_get_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(
                Optional[PolicyDevicesGetDefaultDeviceSettingsPolicyResponse], policy, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_list_device_settings_policies(self, client: Cloudflare) -> None:
        policy = client.devices.policies.devices_list_device_settings_policies(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyDevicesListDeviceSettingsPoliciesResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_list_device_settings_policies(self, client: Cloudflare) -> None:
        response = client.devices.policies.with_raw_response.devices_list_device_settings_policies(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[PolicyDevicesListDeviceSettingsPoliciesResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_list_device_settings_policies(self, client: Cloudflare) -> None:
        with client.devices.policies.with_streaming_response.devices_list_device_settings_policies(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Optional[PolicyDevicesListDeviceSettingsPoliciesResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_update_default_device_settings_policy(self, client: Cloudflare) -> None:
        policy = client.devices.policies.devices_update_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyDevicesUpdateDefaultDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_update_default_device_settings_policy_with_all_params(self, client: Cloudflare) -> None:
        policy = client.devices.policies.devices_update_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
            allow_mode_switch=True,
            allow_updates=True,
            allowed_to_leave=True,
            auto_connect=0,
            captive_portal=180,
            disable_auto_fallback=True,
            exclude_office_ips=True,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
        )
        assert_matches_type(Optional[PolicyDevicesUpdateDefaultDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_update_default_device_settings_policy(self, client: Cloudflare) -> None:
        response = client.devices.policies.with_raw_response.devices_update_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[PolicyDevicesUpdateDefaultDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_update_default_device_settings_policy(self, client: Cloudflare) -> None:
        with client.devices.policies.with_streaming_response.devices_update_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(
                Optional[PolicyDevicesUpdateDefaultDeviceSettingsPolicyResponse], policy, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        policy = client.devices.policies.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyGetResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.devices.policies.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[PolicyGetResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.devices.policies.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Optional[PolicyGetResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.policies.with_raw_response.get(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.devices.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.devices.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            allow_mode_switch=True,
            allow_updates=True,
            allowed_to_leave=True,
            auto_connect=0,
            captive_portal=180,
            description="Policy for test teams.",
            disable_auto_fallback=True,
            enabled=True,
            exclude_office_ips=True,
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
        )
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.policies.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.policies.with_raw_response.update(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.devices.policies.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyDeleteResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[PolicyDeleteResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.policies.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Optional[PolicyDeleteResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.policies.with_raw_response.delete(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_create_device_settings_policy(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.devices.policies.devices_create_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        )
        assert_matches_type(Optional[PolicyDevicesCreateDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_create_device_settings_policy_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        policy = await async_client.devices.policies.devices_create_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
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
            exclude_office_ips=True,
            lan_allow_minutes=30,
            lan_allow_subnet_size=24,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
        )
        assert_matches_type(Optional[PolicyDevicesCreateDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_create_device_settings_policy(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.with_raw_response.devices_create_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[PolicyDevicesCreateDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_create_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.with_streaming_response.devices_create_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
            match='user.identity == "test@cloudflare.com"',
            name="Allow Developers",
            precedence=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Optional[PolicyDevicesCreateDeviceSettingsPolicyResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_get_default_device_settings_policy(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.devices.policies.devices_get_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyDevicesGetDefaultDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_get_default_device_settings_policy(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.with_raw_response.devices_get_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[PolicyDevicesGetDefaultDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_get_default_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.with_streaming_response.devices_get_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(
                Optional[PolicyDevicesGetDefaultDeviceSettingsPolicyResponse], policy, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_list_device_settings_policies(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.devices.policies.devices_list_device_settings_policies(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyDevicesListDeviceSettingsPoliciesResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_list_device_settings_policies(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.with_raw_response.devices_list_device_settings_policies(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[PolicyDevicesListDeviceSettingsPoliciesResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_list_device_settings_policies(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.with_streaming_response.devices_list_device_settings_policies(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Optional[PolicyDevicesListDeviceSettingsPoliciesResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_update_default_device_settings_policy(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.devices.policies.devices_update_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyDevicesUpdateDefaultDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_update_default_device_settings_policy_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        policy = await async_client.devices.policies.devices_update_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
            allow_mode_switch=True,
            allow_updates=True,
            allowed_to_leave=True,
            auto_connect=0,
            captive_portal=180,
            disable_auto_fallback=True,
            exclude_office_ips=True,
            service_mode_v2={
                "mode": "proxy",
                "port": 3000,
            },
            support_url="https://1.1.1.1/help",
            switch_locked=True,
        )
        assert_matches_type(Optional[PolicyDevicesUpdateDefaultDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_update_default_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.devices.policies.with_raw_response.devices_update_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[PolicyDevicesUpdateDefaultDeviceSettingsPolicyResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_update_default_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.with_streaming_response.devices_update_default_device_settings_policy(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(
                Optional[PolicyDevicesUpdateDefaultDeviceSettingsPolicyResponse], policy, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.devices.policies.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PolicyGetResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[PolicyGetResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.policies.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Optional[PolicyGetResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.policies.with_raw_response.get(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )
