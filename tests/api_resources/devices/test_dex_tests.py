# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.devices import (
    DEXTestGetResponse,
    DEXTestDeleteResponse,
    DEXTestUpdateResponse,
    DEXTestDeviceDEXTestDetailsResponse,
    DEXTestDeviceDEXTestCreateDeviceDEXTestResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDEXTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        dex_test = client.devices.dex_tests.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        )
        assert_matches_type(Optional[DEXTestUpdateResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        dex_test = client.devices.dex_tests.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            data={
                "host": "https://dash.cloudflare.com",
                "kind": "http",
                "method": "GET",
            },
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
            description="Checks the dash endpoint every 30 minutes",
        )
        assert_matches_type(Optional[DEXTestUpdateResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.devices.dex_tests.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex_test = response.parse()
        assert_matches_type(Optional[DEXTestUpdateResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.devices.dex_tests.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex_test = response.parse()
            assert_matches_type(Optional[DEXTestUpdateResponse], dex_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.dex_tests.with_raw_response.update(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
                data={},
                enabled=True,
                interval="30m",
                name="HTTP dash health check",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        dex_test = client.devices.dex_tests.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DEXTestDeleteResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.devices.dex_tests.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex_test = response.parse()
        assert_matches_type(Optional[DEXTestDeleteResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.devices.dex_tests.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex_test = response.parse()
            assert_matches_type(Optional[DEXTestDeleteResponse], dex_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.dex_tests.with_raw_response.delete(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_device_dex_test_create_device_dex_test(self, client: Cloudflare) -> None:
        dex_test = client.devices.dex_tests.device_dex_test_create_device_dex_test(
            "699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        )
        assert_matches_type(Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_device_dex_test_create_device_dex_test_with_all_params(self, client: Cloudflare) -> None:
        dex_test = client.devices.dex_tests.device_dex_test_create_device_dex_test(
            "699d98642c564d2e855e9661899b7252",
            data={
                "host": "https://dash.cloudflare.com",
                "kind": "http",
                "method": "GET",
            },
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
            description="Checks the dash endpoint every 30 minutes",
        )
        assert_matches_type(Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_device_dex_test_create_device_dex_test(self, client: Cloudflare) -> None:
        response = client.devices.dex_tests.with_raw_response.device_dex_test_create_device_dex_test(
            "699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex_test = response.parse()
        assert_matches_type(Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_device_dex_test_create_device_dex_test(self, client: Cloudflare) -> None:
        with client.devices.dex_tests.with_streaming_response.device_dex_test_create_device_dex_test(
            "699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex_test = response.parse()
            assert_matches_type(Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse], dex_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_device_dex_test_details(self, client: Cloudflare) -> None:
        dex_test = client.devices.dex_tests.device_dex_test_details(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DEXTestDeviceDEXTestDetailsResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_device_dex_test_details(self, client: Cloudflare) -> None:
        response = client.devices.dex_tests.with_raw_response.device_dex_test_details(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex_test = response.parse()
        assert_matches_type(Optional[DEXTestDeviceDEXTestDetailsResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_device_dex_test_details(self, client: Cloudflare) -> None:
        with client.devices.dex_tests.with_streaming_response.device_dex_test_details(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex_test = response.parse()
            assert_matches_type(Optional[DEXTestDeviceDEXTestDetailsResponse], dex_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dex_test = client.devices.dex_tests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DEXTestGetResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.devices.dex_tests.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex_test = response.parse()
        assert_matches_type(Optional[DEXTestGetResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.devices.dex_tests.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex_test = response.parse()
            assert_matches_type(Optional[DEXTestGetResponse], dex_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.dex_tests.with_raw_response.get(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncDEXTests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        dex_test = await async_client.devices.dex_tests.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        )
        assert_matches_type(Optional[DEXTestUpdateResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dex_test = await async_client.devices.dex_tests.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            data={
                "host": "https://dash.cloudflare.com",
                "kind": "http",
                "method": "GET",
            },
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
            description="Checks the dash endpoint every 30 minutes",
        )
        assert_matches_type(Optional[DEXTestUpdateResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.dex_tests.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex_test = await response.parse()
        assert_matches_type(Optional[DEXTestUpdateResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.dex_tests.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex_test = await response.parse()
            assert_matches_type(Optional[DEXTestUpdateResponse], dex_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.dex_tests.with_raw_response.update(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
                data={},
                enabled=True,
                interval="30m",
                name="HTTP dash health check",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        dex_test = await async_client.devices.dex_tests.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DEXTestDeleteResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.dex_tests.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex_test = await response.parse()
        assert_matches_type(Optional[DEXTestDeleteResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.dex_tests.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex_test = await response.parse()
            assert_matches_type(Optional[DEXTestDeleteResponse], dex_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.dex_tests.with_raw_response.delete(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_dex_test_create_device_dex_test(self, async_client: AsyncCloudflare) -> None:
        dex_test = await async_client.devices.dex_tests.device_dex_test_create_device_dex_test(
            "699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        )
        assert_matches_type(Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_dex_test_create_device_dex_test_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        dex_test = await async_client.devices.dex_tests.device_dex_test_create_device_dex_test(
            "699d98642c564d2e855e9661899b7252",
            data={
                "host": "https://dash.cloudflare.com",
                "kind": "http",
                "method": "GET",
            },
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
            description="Checks the dash endpoint every 30 minutes",
        )
        assert_matches_type(Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_device_dex_test_create_device_dex_test(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.dex_tests.with_raw_response.device_dex_test_create_device_dex_test(
            "699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex_test = await response.parse()
        assert_matches_type(Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_device_dex_test_create_device_dex_test(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.dex_tests.with_streaming_response.device_dex_test_create_device_dex_test(
            "699d98642c564d2e855e9661899b7252",
            data={},
            enabled=True,
            interval="30m",
            name="HTTP dash health check",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex_test = await response.parse()
            assert_matches_type(Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse], dex_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_dex_test_details(self, async_client: AsyncCloudflare) -> None:
        dex_test = await async_client.devices.dex_tests.device_dex_test_details(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DEXTestDeviceDEXTestDetailsResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_device_dex_test_details(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.dex_tests.with_raw_response.device_dex_test_details(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex_test = await response.parse()
        assert_matches_type(Optional[DEXTestDeviceDEXTestDetailsResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_device_dex_test_details(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.dex_tests.with_streaming_response.device_dex_test_details(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex_test = await response.parse()
            assert_matches_type(Optional[DEXTestDeviceDEXTestDetailsResponse], dex_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dex_test = await async_client.devices.dex_tests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DEXTestGetResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.dex_tests.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex_test = await response.parse()
        assert_matches_type(Optional[DEXTestGetResponse], dex_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.dex_tests.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex_test = await response.parse()
            assert_matches_type(Optional[DEXTestGetResponse], dex_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.dex_tests.with_raw_response.get(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )
