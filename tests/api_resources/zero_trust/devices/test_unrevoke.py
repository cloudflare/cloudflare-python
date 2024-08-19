# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.devices import UnrevokeCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUnrevoke:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        unrevoke = client.zero_trust.devices.unrevoke.create(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        )
        assert_matches_type(UnrevokeCreateResponse, unrevoke, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.unrevoke.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unrevoke = response.parse()
        assert_matches_type(UnrevokeCreateResponse, unrevoke, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.unrevoke.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unrevoke = response.parse()
            assert_matches_type(UnrevokeCreateResponse, unrevoke, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.unrevoke.with_raw_response.create(
                account_id="",
                body=[
                    "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                ],
            )


class TestAsyncUnrevoke:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        unrevoke = await async_client.zero_trust.devices.unrevoke.create(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        )
        assert_matches_type(UnrevokeCreateResponse, unrevoke, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.unrevoke.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unrevoke = await response.parse()
        assert_matches_type(UnrevokeCreateResponse, unrevoke, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.unrevoke.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unrevoke = await response.parse()
            assert_matches_type(UnrevokeCreateResponse, unrevoke, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.unrevoke.with_raw_response.create(
                account_id="",
                body=[
                    "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                ],
            )
