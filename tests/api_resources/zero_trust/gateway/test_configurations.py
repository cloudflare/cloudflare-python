# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.gateway import (
    ConfigurationGetResponse,
    ConfigurationEditResponse,
    ConfigurationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        configuration = client.zero_trust.gateway.configurations.update(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        configuration = client.zero_trust.gateway.configurations.update(
            account_id="699d98642c564d2e855e9661899b7252",
            settings={
                "activity_log": {"enabled": True},
                "antivirus": {
                    "enabled_download_phase": False,
                    "enabled_upload_phase": False,
                    "fail_closed": False,
                    "notification_settings": {
                        "enabled": True,
                        "msg": "msg",
                        "support_url": "support_url",
                    },
                },
                "block_page": {
                    "background_color": "background_color",
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
                "certificate": {"id": "d1b364c5-1311-466e-a194-f0e943e0799f"},
                "custom_certificate": {
                    "enabled": True,
                    "id": "d1b364c5-1311-466e-a194-f0e943e0799f",
                },
                "extended_email_matching": {"enabled": True},
                "fips": {"tls": True},
                "protocol_detection": {"enabled": True},
                "sandbox": {
                    "enabled": True,
                    "fallback_action": "allow",
                },
                "tls_decrypt": {"enabled": True},
            },
        )
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.configurations.with_raw_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.configurations.with_streaming_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.configurations.with_raw_response.update(
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        configuration = client.zero_trust.gateway.configurations.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ConfigurationEditResponse], configuration, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        configuration = client.zero_trust.gateway.configurations.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            settings={
                "activity_log": {"enabled": True},
                "antivirus": {
                    "enabled_download_phase": False,
                    "enabled_upload_phase": False,
                    "fail_closed": False,
                    "notification_settings": {
                        "enabled": True,
                        "msg": "msg",
                        "support_url": "support_url",
                    },
                },
                "block_page": {
                    "background_color": "background_color",
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
                "certificate": {"id": "d1b364c5-1311-466e-a194-f0e943e0799f"},
                "custom_certificate": {
                    "enabled": True,
                    "id": "d1b364c5-1311-466e-a194-f0e943e0799f",
                },
                "extended_email_matching": {"enabled": True},
                "fips": {"tls": True},
                "protocol_detection": {"enabled": True},
                "sandbox": {
                    "enabled": True,
                    "fallback_action": "allow",
                },
                "tls_decrypt": {"enabled": True},
            },
        )
        assert_matches_type(Optional[ConfigurationEditResponse], configuration, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.configurations.with_raw_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(Optional[ConfigurationEditResponse], configuration, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.configurations.with_streaming_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(Optional[ConfigurationEditResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.configurations.with_raw_response.edit(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        configuration = client.zero_trust.gateway.configurations.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.configurations.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.configurations.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.configurations.with_raw_response.get(
                account_id="",
            )


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.zero_trust.gateway.configurations.update(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.zero_trust.gateway.configurations.update(
            account_id="699d98642c564d2e855e9661899b7252",
            settings={
                "activity_log": {"enabled": True},
                "antivirus": {
                    "enabled_download_phase": False,
                    "enabled_upload_phase": False,
                    "fail_closed": False,
                    "notification_settings": {
                        "enabled": True,
                        "msg": "msg",
                        "support_url": "support_url",
                    },
                },
                "block_page": {
                    "background_color": "background_color",
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
                "certificate": {"id": "d1b364c5-1311-466e-a194-f0e943e0799f"},
                "custom_certificate": {
                    "enabled": True,
                    "id": "d1b364c5-1311-466e-a194-f0e943e0799f",
                },
                "extended_email_matching": {"enabled": True},
                "fips": {"tls": True},
                "protocol_detection": {"enabled": True},
                "sandbox": {
                    "enabled": True,
                    "fallback_action": "allow",
                },
                "tls_decrypt": {"enabled": True},
            },
        )
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.configurations.with_raw_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.configurations.with_streaming_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.configurations.with_raw_response.update(
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.zero_trust.gateway.configurations.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ConfigurationEditResponse], configuration, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.zero_trust.gateway.configurations.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            settings={
                "activity_log": {"enabled": True},
                "antivirus": {
                    "enabled_download_phase": False,
                    "enabled_upload_phase": False,
                    "fail_closed": False,
                    "notification_settings": {
                        "enabled": True,
                        "msg": "msg",
                        "support_url": "support_url",
                    },
                },
                "block_page": {
                    "background_color": "background_color",
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
                "certificate": {"id": "d1b364c5-1311-466e-a194-f0e943e0799f"},
                "custom_certificate": {
                    "enabled": True,
                    "id": "d1b364c5-1311-466e-a194-f0e943e0799f",
                },
                "extended_email_matching": {"enabled": True},
                "fips": {"tls": True},
                "protocol_detection": {"enabled": True},
                "sandbox": {
                    "enabled": True,
                    "fallback_action": "allow",
                },
                "tls_decrypt": {"enabled": True},
            },
        )
        assert_matches_type(Optional[ConfigurationEditResponse], configuration, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.configurations.with_raw_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(Optional[ConfigurationEditResponse], configuration, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.configurations.with_streaming_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(Optional[ConfigurationEditResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.configurations.with_raw_response.edit(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.zero_trust.gateway.configurations.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.configurations.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.configurations.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.configurations.with_raw_response.get(
                account_id="",
            )
