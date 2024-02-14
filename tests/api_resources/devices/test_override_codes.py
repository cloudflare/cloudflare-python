# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.devices import OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOverrideCodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_list_admin_override_code_for_device(self, client: Cloudflare) -> None:
        override_code = client.devices.override_codes.devices_list_admin_override_code_for_device(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse], override_code, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_list_admin_override_code_for_device(self, client: Cloudflare) -> None:
        response = client.devices.override_codes.with_raw_response.devices_list_admin_override_code_for_device(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override_code = response.parse()
        assert_matches_type(
            Optional[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse], override_code, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_list_admin_override_code_for_device(self, client: Cloudflare) -> None:
        with client.devices.override_codes.with_streaming_response.devices_list_admin_override_code_for_device(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override_code = response.parse()
            assert_matches_type(
                Optional[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse], override_code, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_devices_list_admin_override_code_for_device(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.override_codes.with_raw_response.devices_list_admin_override_code_for_device(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncOverrideCodes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_list_admin_override_code_for_device(self, async_client: AsyncCloudflare) -> None:
        override_code = await async_client.devices.override_codes.devices_list_admin_override_code_for_device(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse], override_code, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_list_admin_override_code_for_device(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.devices.override_codes.with_raw_response.devices_list_admin_override_code_for_device(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="699d98642c564d2e855e9661899b7252",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override_code = await response.parse()
        assert_matches_type(
            Optional[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse], override_code, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_list_admin_override_code_for_device(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.override_codes.with_streaming_response.devices_list_admin_override_code_for_device(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override_code = await response.parse()
            assert_matches_type(
                Optional[OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse], override_code, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_devices_list_admin_override_code_for_device(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.override_codes.with_raw_response.devices_list_admin_override_code_for_device(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )
