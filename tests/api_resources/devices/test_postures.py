# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.devices import (
    PostureUpdateResponse,
    PostureDeleteResponse,
    PostureDevicePostureRulesCreateDevicePostureRuleResponse,
    PostureDevicePostureRulesListDevicePostureRulesResponse,
    PostureGetResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.devices import posture_update_params
from cloudflare.types.devices import posture_device_posture_rules_create_device_posture_rule_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPostures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        posture = client.devices.postures.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )
        assert_matches_type(Optional[PostureUpdateResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        posture = client.devices.postures.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
            description="The rule for admin serial numbers",
            expiration="1h",
            input={
                "exists": True,
                "operating_system": "mac",
                "path": "/bin/cat",
                "sha256": "https://api.us-2.crowdstrike.com",
                "thumbprint": "0aabab210bdb998e9cf45da2c9ce352977ab531c681b74cf1e487be1bbe9fe6e",
            },
            match=[{"platform": "windows"}, {"platform": "windows"}, {"platform": "windows"}],
            schedule="1h",
        )
        assert_matches_type(Optional[PostureUpdateResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.devices.postures.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = response.parse()
        assert_matches_type(Optional[PostureUpdateResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.devices.postures.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = response.parse()
            assert_matches_type(Optional[PostureUpdateResponse], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.postures.with_raw_response.update(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
                name="Admin Serial Numbers",
                type="file",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        posture = client.devices.postures.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.devices.postures.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = response.parse()
        assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.devices.postures.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = response.parse()
            assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.postures.with_raw_response.delete(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_device_posture_rules_create_device_posture_rule(self, client: Cloudflare) -> None:
        posture = client.devices.postures.device_posture_rules_create_device_posture_rule(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )
        assert_matches_type(
            Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse], posture, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_device_posture_rules_create_device_posture_rule_with_all_params(self, client: Cloudflare) -> None:
        posture = client.devices.postures.device_posture_rules_create_device_posture_rule(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
            description="The rule for admin serial numbers",
            expiration="1h",
            input={
                "exists": True,
                "operating_system": "mac",
                "path": "/bin/cat",
                "sha256": "https://api.us-2.crowdstrike.com",
                "thumbprint": "0aabab210bdb998e9cf45da2c9ce352977ab531c681b74cf1e487be1bbe9fe6e",
            },
            match=[{"platform": "windows"}, {"platform": "windows"}, {"platform": "windows"}],
            schedule="1h",
        )
        assert_matches_type(
            Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse], posture, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_device_posture_rules_create_device_posture_rule(self, client: Cloudflare) -> None:
        response = client.devices.postures.with_raw_response.device_posture_rules_create_device_posture_rule(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = response.parse()
        assert_matches_type(
            Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse], posture, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_device_posture_rules_create_device_posture_rule(self, client: Cloudflare) -> None:
        with client.devices.postures.with_streaming_response.device_posture_rules_create_device_posture_rule(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = response.parse()
            assert_matches_type(
                Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse], posture, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_device_posture_rules_list_device_posture_rules(self, client: Cloudflare) -> None:
        posture = client.devices.postures.device_posture_rules_list_device_posture_rules(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[PostureDevicePostureRulesListDevicePostureRulesResponse], posture, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_device_posture_rules_list_device_posture_rules(self, client: Cloudflare) -> None:
        response = client.devices.postures.with_raw_response.device_posture_rules_list_device_posture_rules(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = response.parse()
        assert_matches_type(
            Optional[PostureDevicePostureRulesListDevicePostureRulesResponse], posture, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_device_posture_rules_list_device_posture_rules(self, client: Cloudflare) -> None:
        with client.devices.postures.with_streaming_response.device_posture_rules_list_device_posture_rules(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = response.parse()
            assert_matches_type(
                Optional[PostureDevicePostureRulesListDevicePostureRulesResponse], posture, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        posture = client.devices.postures.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PostureGetResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.devices.postures.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = response.parse()
        assert_matches_type(Optional[PostureGetResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.devices.postures.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = response.parse()
            assert_matches_type(Optional[PostureGetResponse], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.postures.with_raw_response.get(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncPostures:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.devices.postures.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )
        assert_matches_type(Optional[PostureUpdateResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.devices.postures.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
            description="The rule for admin serial numbers",
            expiration="1h",
            input={
                "exists": True,
                "operating_system": "mac",
                "path": "/bin/cat",
                "sha256": "https://api.us-2.crowdstrike.com",
                "thumbprint": "0aabab210bdb998e9cf45da2c9ce352977ab531c681b74cf1e487be1bbe9fe6e",
            },
            match=[{"platform": "windows"}, {"platform": "windows"}, {"platform": "windows"}],
            schedule="1h",
        )
        assert_matches_type(Optional[PostureUpdateResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.postures.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = await response.parse()
        assert_matches_type(Optional[PostureUpdateResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.postures.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = await response.parse()
            assert_matches_type(Optional[PostureUpdateResponse], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.postures.with_raw_response.update(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
                name="Admin Serial Numbers",
                type="file",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.devices.postures.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.postures.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = await response.parse()
        assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.postures.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = await response.parse()
            assert_matches_type(Optional[PostureDeleteResponse], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.postures.with_raw_response.delete(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_posture_rules_create_device_posture_rule(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.devices.postures.device_posture_rules_create_device_posture_rule(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        )
        assert_matches_type(
            Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse], posture, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_posture_rules_create_device_posture_rule_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        posture = await async_client.devices.postures.device_posture_rules_create_device_posture_rule(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
            description="The rule for admin serial numbers",
            expiration="1h",
            input={
                "exists": True,
                "operating_system": "mac",
                "path": "/bin/cat",
                "sha256": "https://api.us-2.crowdstrike.com",
                "thumbprint": "0aabab210bdb998e9cf45da2c9ce352977ab531c681b74cf1e487be1bbe9fe6e",
            },
            match=[{"platform": "windows"}, {"platform": "windows"}, {"platform": "windows"}],
            schedule="1h",
        )
        assert_matches_type(
            Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse], posture, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_device_posture_rules_create_device_posture_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.devices.postures.with_raw_response.device_posture_rules_create_device_posture_rule(
                "699d98642c564d2e855e9661899b7252",
                name="Admin Serial Numbers",
                type="file",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = await response.parse()
        assert_matches_type(
            Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse], posture, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_device_posture_rules_create_device_posture_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.postures.with_streaming_response.device_posture_rules_create_device_posture_rule(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = await response.parse()
            assert_matches_type(
                Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse], posture, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_posture_rules_list_device_posture_rules(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.devices.postures.device_posture_rules_list_device_posture_rules(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[PostureDevicePostureRulesListDevicePostureRulesResponse], posture, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_device_posture_rules_list_device_posture_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.devices.postures.with_raw_response.device_posture_rules_list_device_posture_rules(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = await response.parse()
        assert_matches_type(
            Optional[PostureDevicePostureRulesListDevicePostureRulesResponse], posture, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_device_posture_rules_list_device_posture_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.postures.with_streaming_response.device_posture_rules_list_device_posture_rules(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = await response.parse()
            assert_matches_type(
                Optional[PostureDevicePostureRulesListDevicePostureRulesResponse], posture, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        posture = await async_client.devices.postures.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PostureGetResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.postures.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        posture = await response.parse()
        assert_matches_type(Optional[PostureGetResponse], posture, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.postures.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            posture = await response.parse()
            assert_matches_type(Optional[PostureGetResponse], posture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.postures.with_raw_response.get(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )
