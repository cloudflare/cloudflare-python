# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.gateways import (
    ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse,
    ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse,
    ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_get_zero_trust_account_configuration(self, client: Cloudflare) -> None:
        configuration = client.gateways.configurations.zero_trust_accounts_get_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_accounts_get_zero_trust_account_configuration(self, client: Cloudflare) -> None:
        response = (
            client.gateways.configurations.with_raw_response.zero_trust_accounts_get_zero_trust_account_configuration(
                "699d98642c564d2e855e9661899b7252",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(
            ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_accounts_get_zero_trust_account_configuration(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.configurations.with_streaming_response.zero_trust_accounts_get_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(
                ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_patch_zero_trust_account_configuration(self, client: Cloudflare) -> None:
        configuration = client.gateways.configurations.zero_trust_accounts_patch_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_patch_zero_trust_account_configuration_with_all_params(
        self, client: Cloudflare
    ) -> None:
        configuration = client.gateways.configurations.zero_trust_accounts_patch_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
            settings={
                "activity_log": {"enabled": True},
                "antivirus": {
                    "enabled_download_phase": False,
                    "enabled_upload_phase": False,
                    "fail_closed": False,
                    "notification_settings": {
                        "enabled": True,
                        "msg": "string",
                        "support_url": "string",
                    },
                },
                "block_page": {
                    "background_color": "string",
                    "enabled": True,
                    "footer_text": "--footer--",
                    "header_text": "--header--",
                    "logo_path": "https://logos.com/a.png",
                    "mailto_address": "admin@example.com",
                    "mailto_subject": "Blocked User Inquiry",
                    "name": "Cloudflare",
                    "suppress_footer": False,
                },
                "body_scanning": {"inspection_mode": "deep"},
                "browser_isolation": {
                    "non_identity_enabled": True,
                    "url_browser_isolation_enabled": True,
                },
                "custom_certificate": {
                    "enabled": True,
                    "id": "d1b364c5-1311-466e-a194-f0e943e0799f",
                },
                "extended_email_matching": {"enabled": True},
                "fips": {"tls": True},
                "protocol_detection": {"enabled": True},
                "tls_decrypt": {"enabled": True},
            },
        )
        assert_matches_type(
            ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_accounts_patch_zero_trust_account_configuration(self, client: Cloudflare) -> None:
        response = (
            client.gateways.configurations.with_raw_response.zero_trust_accounts_patch_zero_trust_account_configuration(
                "699d98642c564d2e855e9661899b7252",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(
            ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_accounts_patch_zero_trust_account_configuration(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.configurations.with_streaming_response.zero_trust_accounts_patch_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(
                ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse,
                configuration,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_update_zero_trust_account_configuration(self, client: Cloudflare) -> None:
        configuration = client.gateways.configurations.zero_trust_accounts_update_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_accounts_update_zero_trust_account_configuration_with_all_params(
        self, client: Cloudflare
    ) -> None:
        configuration = client.gateways.configurations.zero_trust_accounts_update_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
            settings={
                "activity_log": {"enabled": True},
                "antivirus": {
                    "enabled_download_phase": False,
                    "enabled_upload_phase": False,
                    "fail_closed": False,
                    "notification_settings": {
                        "enabled": True,
                        "msg": "string",
                        "support_url": "string",
                    },
                },
                "block_page": {
                    "background_color": "string",
                    "enabled": True,
                    "footer_text": "--footer--",
                    "header_text": "--header--",
                    "logo_path": "https://logos.com/a.png",
                    "mailto_address": "admin@example.com",
                    "mailto_subject": "Blocked User Inquiry",
                    "name": "Cloudflare",
                    "suppress_footer": False,
                },
                "body_scanning": {"inspection_mode": "deep"},
                "browser_isolation": {
                    "non_identity_enabled": True,
                    "url_browser_isolation_enabled": True,
                },
                "custom_certificate": {
                    "enabled": True,
                    "id": "d1b364c5-1311-466e-a194-f0e943e0799f",
                },
                "extended_email_matching": {"enabled": True},
                "fips": {"tls": True},
                "protocol_detection": {"enabled": True},
                "tls_decrypt": {"enabled": True},
            },
        )
        assert_matches_type(
            ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_accounts_update_zero_trust_account_configuration(self, client: Cloudflare) -> None:
        response = client.gateways.configurations.with_raw_response.zero_trust_accounts_update_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(
            ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_accounts_update_zero_trust_account_configuration(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.configurations.with_streaming_response.zero_trust_accounts_update_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(
                ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse,
                configuration,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_get_zero_trust_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        configuration = (
            await async_client.gateways.configurations.zero_trust_accounts_get_zero_trust_account_configuration(
                "699d98642c564d2e855e9661899b7252",
            )
        )
        assert_matches_type(
            ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_accounts_get_zero_trust_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.gateways.configurations.with_raw_response.zero_trust_accounts_get_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(
            ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_accounts_get_zero_trust_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.configurations.with_streaming_response.zero_trust_accounts_get_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(
                ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_patch_zero_trust_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        configuration = (
            await async_client.gateways.configurations.zero_trust_accounts_patch_zero_trust_account_configuration(
                "699d98642c564d2e855e9661899b7252",
            )
        )
        assert_matches_type(
            ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_patch_zero_trust_account_configuration_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        configuration = (
            await async_client.gateways.configurations.zero_trust_accounts_patch_zero_trust_account_configuration(
                "699d98642c564d2e855e9661899b7252",
                settings={
                    "activity_log": {"enabled": True},
                    "antivirus": {
                        "enabled_download_phase": False,
                        "enabled_upload_phase": False,
                        "fail_closed": False,
                        "notification_settings": {
                            "enabled": True,
                            "msg": "string",
                            "support_url": "string",
                        },
                    },
                    "block_page": {
                        "background_color": "string",
                        "enabled": True,
                        "footer_text": "--footer--",
                        "header_text": "--header--",
                        "logo_path": "https://logos.com/a.png",
                        "mailto_address": "admin@example.com",
                        "mailto_subject": "Blocked User Inquiry",
                        "name": "Cloudflare",
                        "suppress_footer": False,
                    },
                    "body_scanning": {"inspection_mode": "deep"},
                    "browser_isolation": {
                        "non_identity_enabled": True,
                        "url_browser_isolation_enabled": True,
                    },
                    "custom_certificate": {
                        "enabled": True,
                        "id": "d1b364c5-1311-466e-a194-f0e943e0799f",
                    },
                    "extended_email_matching": {"enabled": True},
                    "fips": {"tls": True},
                    "protocol_detection": {"enabled": True},
                    "tls_decrypt": {"enabled": True},
                },
            )
        )
        assert_matches_type(
            ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_accounts_patch_zero_trust_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.gateways.configurations.with_raw_response.zero_trust_accounts_patch_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(
            ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_accounts_patch_zero_trust_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.configurations.with_streaming_response.zero_trust_accounts_patch_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(
                ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse,
                configuration,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_update_zero_trust_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        configuration = (
            await async_client.gateways.configurations.zero_trust_accounts_update_zero_trust_account_configuration(
                "699d98642c564d2e855e9661899b7252",
            )
        )
        assert_matches_type(
            ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_accounts_update_zero_trust_account_configuration_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        configuration = (
            await async_client.gateways.configurations.zero_trust_accounts_update_zero_trust_account_configuration(
                "699d98642c564d2e855e9661899b7252",
                settings={
                    "activity_log": {"enabled": True},
                    "antivirus": {
                        "enabled_download_phase": False,
                        "enabled_upload_phase": False,
                        "fail_closed": False,
                        "notification_settings": {
                            "enabled": True,
                            "msg": "string",
                            "support_url": "string",
                        },
                    },
                    "block_page": {
                        "background_color": "string",
                        "enabled": True,
                        "footer_text": "--footer--",
                        "header_text": "--header--",
                        "logo_path": "https://logos.com/a.png",
                        "mailto_address": "admin@example.com",
                        "mailto_subject": "Blocked User Inquiry",
                        "name": "Cloudflare",
                        "suppress_footer": False,
                    },
                    "body_scanning": {"inspection_mode": "deep"},
                    "browser_isolation": {
                        "non_identity_enabled": True,
                        "url_browser_isolation_enabled": True,
                    },
                    "custom_certificate": {
                        "enabled": True,
                        "id": "d1b364c5-1311-466e-a194-f0e943e0799f",
                    },
                    "extended_email_matching": {"enabled": True},
                    "fips": {"tls": True},
                    "protocol_detection": {"enabled": True},
                    "tls_decrypt": {"enabled": True},
                },
            )
        )
        assert_matches_type(
            ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_accounts_update_zero_trust_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.gateways.configurations.with_raw_response.zero_trust_accounts_update_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(
            ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_accounts_update_zero_trust_account_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.configurations.with_streaming_response.zero_trust_accounts_update_zero_trust_account_configuration(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(
                ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse,
                configuration,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
