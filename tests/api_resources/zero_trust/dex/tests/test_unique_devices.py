# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dex.tests import UniqueDevices

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUniqueDevices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        unique_device = client.zero_trust.dex.tests.unique_devices.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[UniqueDevices], unique_device, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        unique_device = client.zero_trust.dex.tests.unique_devices.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            device_id=["string"],
            test_name="testName",
        )
        assert_matches_type(Optional[UniqueDevices], unique_device, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.tests.unique_devices.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unique_device = response.parse()
        assert_matches_type(Optional[UniqueDevices], unique_device, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.tests.unique_devices.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unique_device = response.parse()
            assert_matches_type(Optional[UniqueDevices], unique_device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.tests.unique_devices.with_raw_response.list(
                account_id="",
            )


class TestAsyncUniqueDevices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        unique_device = await async_client.zero_trust.dex.tests.unique_devices.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[UniqueDevices], unique_device, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        unique_device = await async_client.zero_trust.dex.tests.unique_devices.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            device_id=["string"],
            test_name="testName",
        )
        assert_matches_type(Optional[UniqueDevices], unique_device, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.tests.unique_devices.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unique_device = await response.parse()
        assert_matches_type(Optional[UniqueDevices], unique_device, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.tests.unique_devices.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unique_device = await response.parse()
            assert_matches_type(Optional[UniqueDevices], unique_device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.tests.unique_devices.with_raw_response.list(
                account_id="",
            )
