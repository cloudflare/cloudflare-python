# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.devices.policies import (
    FallbackDomainDevicesGetLocalDomainFallbackListResponse,
    FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse,
    FallbackDomainDevicesSetLocalDomainFallbackListResponse,
    FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.devices.policies import fallback_domain_devices_set_local_domain_fallback_list_params
from cloudflare.types.devices.policies import (
    fallback_domain_devices_set_local_domain_fallback_list_for_a_device_settings_policy_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFallbackDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_get_local_domain_fallback_list(self, client: Cloudflare) -> None:
        fallback_domain = client.devices.policies.fallback_domains.devices_get_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[FallbackDomainDevicesGetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_get_local_domain_fallback_list(self, client: Cloudflare) -> None:
        response = client.devices.policies.fallback_domains.with_raw_response.devices_get_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = response.parse()
        assert_matches_type(
            Optional[FallbackDomainDevicesGetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_get_local_domain_fallback_list(self, client: Cloudflare) -> None:
        with client.devices.policies.fallback_domains.with_streaming_response.devices_get_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = response.parse()
            assert_matches_type(
                Optional[FallbackDomainDevicesGetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_get_local_domain_fallback_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        fallback_domain = client.devices.policies.fallback_domains.devices_get_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            fallback_domain,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_get_local_domain_fallback_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        response = client.devices.policies.fallback_domains.with_raw_response.devices_get_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = response.parse()
        assert_matches_type(
            Optional[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            fallback_domain,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_get_local_domain_fallback_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        with client.devices.policies.fallback_domains.with_streaming_response.devices_get_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = response.parse()
            assert_matches_type(
                Optional[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
                fallback_domain,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_devices_get_local_domain_fallback_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.policies.fallback_domains.with_raw_response.devices_get_local_domain_fallback_list_for_a_device_settings_policy(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_set_local_domain_fallback_list(self, client: Cloudflare) -> None:
        fallback_domain = client.devices.policies.fallback_domains.devices_set_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )
        assert_matches_type(
            Optional[FallbackDomainDevicesSetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_set_local_domain_fallback_list(self, client: Cloudflare) -> None:
        response = client.devices.policies.fallback_domains.with_raw_response.devices_set_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = response.parse()
        assert_matches_type(
            Optional[FallbackDomainDevicesSetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_set_local_domain_fallback_list(self, client: Cloudflare) -> None:
        with client.devices.policies.fallback_domains.with_streaming_response.devices_set_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = response.parse()
            assert_matches_type(
                Optional[FallbackDomainDevicesSetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_set_local_domain_fallback_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        fallback_domain = client.devices.policies.fallback_domains.devices_set_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )
        assert_matches_type(
            Optional[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            fallback_domain,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_set_local_domain_fallback_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        response = client.devices.policies.fallback_domains.with_raw_response.devices_set_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = response.parse()
        assert_matches_type(
            Optional[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            fallback_domain,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_set_local_domain_fallback_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        with client.devices.policies.fallback_domains.with_streaming_response.devices_set_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = response.parse()
            assert_matches_type(
                Optional[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
                fallback_domain,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_devices_set_local_domain_fallback_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.policies.fallback_domains.with_raw_response.devices_set_local_domain_fallback_list_for_a_device_settings_policy(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
                body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
            )


class TestAsyncFallbackDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_get_local_domain_fallback_list(self, async_client: AsyncCloudflare) -> None:
        fallback_domain = await async_client.devices.policies.fallback_domains.devices_get_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[FallbackDomainDevicesGetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_get_local_domain_fallback_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.fallback_domains.with_raw_response.devices_get_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = await response.parse()
        assert_matches_type(
            Optional[FallbackDomainDevicesGetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_get_local_domain_fallback_list(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.fallback_domains.with_streaming_response.devices_get_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = await response.parse()
            assert_matches_type(
                Optional[FallbackDomainDevicesGetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_get_local_domain_fallback_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        fallback_domain = await async_client.devices.policies.fallback_domains.devices_get_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            fallback_domain,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_get_local_domain_fallback_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.devices.policies.fallback_domains.with_raw_response.devices_get_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = await response.parse()
        assert_matches_type(
            Optional[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            fallback_domain,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_get_local_domain_fallback_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.fallback_domains.with_streaming_response.devices_get_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = await response.parse()
            assert_matches_type(
                Optional[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
                fallback_domain,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_devices_get_local_domain_fallback_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.policies.fallback_domains.with_raw_response.devices_get_local_domain_fallback_list_for_a_device_settings_policy(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_set_local_domain_fallback_list(self, async_client: AsyncCloudflare) -> None:
        fallback_domain = await async_client.devices.policies.fallback_domains.devices_set_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )
        assert_matches_type(
            Optional[FallbackDomainDevicesSetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_set_local_domain_fallback_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.fallback_domains.with_raw_response.devices_set_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = await response.parse()
        assert_matches_type(
            Optional[FallbackDomainDevicesSetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_set_local_domain_fallback_list(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.fallback_domains.with_streaming_response.devices_set_local_domain_fallback_list(
            "699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = await response.parse()
            assert_matches_type(
                Optional[FallbackDomainDevicesSetLocalDomainFallbackListResponse], fallback_domain, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_set_local_domain_fallback_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        fallback_domain = await async_client.devices.policies.fallback_domains.devices_set_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )
        assert_matches_type(
            Optional[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            fallback_domain,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_set_local_domain_fallback_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.devices.policies.fallback_domains.with_raw_response.devices_set_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = await response.parse()
        assert_matches_type(
            Optional[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            fallback_domain,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_set_local_domain_fallback_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.fallback_domains.with_streaming_response.devices_set_local_domain_fallback_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = await response.parse()
            assert_matches_type(
                Optional[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
                fallback_domain,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_devices_set_local_domain_fallback_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.policies.fallback_domains.with_raw_response.devices_set_local_domain_fallback_list_for_a_device_settings_policy(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
                body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
            )
