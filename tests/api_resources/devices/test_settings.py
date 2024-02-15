# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.devices import (
    SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse,
    SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_get_device_settings_for_zero_trust_account(self, client: Cloudflare) -> None:
        setting = client.devices.settings.zero_trust_accounts_get_device_settings_for_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse], setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_accounts_get_device_settings_for_zero_trust_account(
        self, client: Cloudflare
    ) -> None:
        response = (
            client.devices.settings.with_raw_response.zero_trust_accounts_get_device_settings_for_zero_trust_account(
                "699d98642c564d2e855e9661899b7252",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(
            Optional[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse], setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_accounts_get_device_settings_for_zero_trust_account(
        self, client: Cloudflare
    ) -> None:
        with client.devices.settings.with_streaming_response.zero_trust_accounts_get_device_settings_for_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(
                Optional[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse],
                setting,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
        self, client: Cloudflare
    ) -> None:
        setting = client.devices.settings.zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse],
            setting,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_update_device_settings_for_the_zero_trust_account_with_all_params(
        self, client: Cloudflare
    ) -> None:
        setting = client.devices.settings.zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
            gateway_proxy_enabled=True,
            gateway_udp_proxy_enabled=True,
            root_certificate_installation_enabled=True,
            use_zt_virtual_ip=True,
        )
        assert_matches_type(
            Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse],
            setting,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
        self, client: Cloudflare
    ) -> None:
        response = client.devices.settings.with_raw_response.zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(
            Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse],
            setting,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
        self, client: Cloudflare
    ) -> None:
        with client.devices.settings.with_streaming_response.zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(
                Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse],
                setting,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_get_device_settings_for_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        setting = await async_client.devices.settings.zero_trust_accounts_get_device_settings_for_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse], setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_accounts_get_device_settings_for_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.devices.settings.with_raw_response.zero_trust_accounts_get_device_settings_for_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(
            Optional[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse], setting, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_accounts_get_device_settings_for_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.settings.with_streaming_response.zero_trust_accounts_get_device_settings_for_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(
                Optional[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse],
                setting,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        setting = (
            await async_client.devices.settings.zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
                "699d98642c564d2e855e9661899b7252",
            )
        )
        assert_matches_type(
            Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse],
            setting,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_update_device_settings_for_the_zero_trust_account_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        setting = (
            await async_client.devices.settings.zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
                "699d98642c564d2e855e9661899b7252",
                gateway_proxy_enabled=True,
                gateway_udp_proxy_enabled=True,
                root_certificate_installation_enabled=True,
                use_zt_virtual_ip=True,
            )
        )
        assert_matches_type(
            Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse],
            setting,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.devices.settings.with_raw_response.zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(
            Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse],
            setting,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.settings.with_streaming_response.zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(
                Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse],
                setting,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
