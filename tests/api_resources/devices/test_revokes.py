# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.devices import RevokeDevicesRevokeDevicesResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.devices import revoke_devices_revoke_devices_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRevokes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_revoke_devices(self, client: Cloudflare) -> None:
        revoke = client.devices.revokes.devices_revoke_devices(
            "699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        )
        assert_matches_type(Optional[RevokeDevicesRevokeDevicesResponse], revoke, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_revoke_devices(self, client: Cloudflare) -> None:
        response = client.devices.revokes.with_raw_response.devices_revoke_devices(
            "699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revoke = response.parse()
        assert_matches_type(Optional[RevokeDevicesRevokeDevicesResponse], revoke, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_revoke_devices(self, client: Cloudflare) -> None:
        with client.devices.revokes.with_streaming_response.devices_revoke_devices(
            "699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revoke = response.parse()
            assert_matches_type(Optional[RevokeDevicesRevokeDevicesResponse], revoke, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRevokes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_revoke_devices(self, async_client: AsyncCloudflare) -> None:
        revoke = await async_client.devices.revokes.devices_revoke_devices(
            "699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        )
        assert_matches_type(Optional[RevokeDevicesRevokeDevicesResponse], revoke, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_revoke_devices(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.revokes.with_raw_response.devices_revoke_devices(
            "699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revoke = await response.parse()
        assert_matches_type(Optional[RevokeDevicesRevokeDevicesResponse], revoke, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_revoke_devices(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.revokes.with_streaming_response.devices_revoke_devices(
            "699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revoke = await response.parse()
            assert_matches_type(Optional[RevokeDevicesRevokeDevicesResponse], revoke, path=["response"])

        assert cast(Any, response.is_closed) is True
