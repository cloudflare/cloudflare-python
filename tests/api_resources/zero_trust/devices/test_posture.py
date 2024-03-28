# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.devices import (
    DevicePostureRules,
    PostureListResponse,
    PostureDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPosture:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        posture = client.zero_trust.devices.posture.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        posture = client.zero_trust.devices.posture.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
            description="The rule for admin serial numbers",
            expiration="1h",
            input={
                "exists": True,
                "operating_system": "linux",
                "path": "/bin/cat",
                "sha256": "https://api.us-2.crowdstrike.com",
                "thumbprint": "0aabab210bdb998e9cf45da2c9ce352977ab531c681b74cf1e487be1bbe9fe6e",
            },
            match=[{"platform": "windows"}, {"platform": "windows"}, {"platform": "windows"}],
            schedule="1h",
        )
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.posture.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = response.parse()
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.posture.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = response.parse()
            assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.posture.with_raw_response.create(
                account_id="",
                name="Admin Serial Numbers",
                type="file",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        posture = client.zero_trust.devices.posture.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        posture = client.zero_trust.devices.posture.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
            description="The rule for admin serial numbers",
            expiration="1h",
            input={
                "exists": True,
                "operating_system": "linux",
                "path": "/bin/cat",
                "sha256": "https://api.us-2.crowdstrike.com",
                "thumbprint": "0aabab210bdb998e9cf45da2c9ce352977ab531c681b74cf1e487be1bbe9fe6e",
            },
            match=[{"platform": "windows"}, {"platform": "windows"}, {"platform": "windows"}],
            schedule="1h",
        )
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.posture.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = response.parse()
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.posture.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = response.parse()
            assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.posture.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                name="Admin Serial Numbers",
                type="file",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.devices.posture.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                name="Admin Serial Numbers",
                type="file",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        posture = client.zero_trust.devices.posture.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PostureListResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.posture.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = response.parse()
        assert_matches_type(Optional[PostureListResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.posture.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = response.parse()
            assert_matches_type(Optional[PostureListResponse], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.posture.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        posture = client.zero_trust.devices.posture.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.posture.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = response.parse()
        assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.posture.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = response.parse()
            assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.posture.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.devices.posture.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        posture = client.zero_trust.devices.posture.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.posture.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = response.parse()
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.posture.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = response.parse()
            assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.posture.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.devices.posture.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncPosture:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.zero_trust.devices.posture.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.zero_trust.devices.posture.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
            description="The rule for admin serial numbers",
            expiration="1h",
            input={
                "exists": True,
                "operating_system": "linux",
                "path": "/bin/cat",
                "sha256": "https://api.us-2.crowdstrike.com",
                "thumbprint": "0aabab210bdb998e9cf45da2c9ce352977ab531c681b74cf1e487be1bbe9fe6e",
            },
            match=[{"platform": "windows"}, {"platform": "windows"}, {"platform": "windows"}],
            schedule="1h",
        )
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.posture.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = await response.parse()
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.posture.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = await response.parse()
            assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.posture.with_raw_response.create(
                account_id="",
                name="Admin Serial Numbers",
                type="file",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.zero_trust.devices.posture.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.zero_trust.devices.posture.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
            description="The rule for admin serial numbers",
            expiration="1h",
            input={
                "exists": True,
                "operating_system": "linux",
                "path": "/bin/cat",
                "sha256": "https://api.us-2.crowdstrike.com",
                "thumbprint": "0aabab210bdb998e9cf45da2c9ce352977ab531c681b74cf1e487be1bbe9fe6e",
            },
            match=[{"platform": "windows"}, {"platform": "windows"}, {"platform": "windows"}],
            schedule="1h",
        )
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.posture.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = await response.parse()
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.posture.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = await response.parse()
            assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.posture.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                name="Admin Serial Numbers",
                type="file",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.devices.posture.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                name="Admin Serial Numbers",
                type="file",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.zero_trust.devices.posture.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PostureListResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.posture.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = await response.parse()
        assert_matches_type(Optional[PostureListResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.posture.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = await response.parse()
            assert_matches_type(Optional[PostureListResponse], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.posture.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.zero_trust.devices.posture.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.posture.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = await response.parse()
        assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.posture.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = await response.parse()
            assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.posture.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.devices.posture.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.zero_trust.devices.posture.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.posture.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = await response.parse()
        assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.posture.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = await response.parse()
            assert_matches_type(Optional[DevicePostureRules], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.posture.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.devices.posture.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )
