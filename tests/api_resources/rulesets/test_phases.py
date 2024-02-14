# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.rulesets import PhaseGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        phase = client.rulesets.phases.get(
            "http_request_firewall_custom",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(PhaseGetResponse, phase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rulesets.phases.with_raw_response.get(
            "http_request_firewall_custom",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phase = response.parse()
        assert_matches_type(PhaseGetResponse, phase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rulesets.phases.with_streaming_response.get(
            "http_request_firewall_custom",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phase = response.parse()
            assert_matches_type(PhaseGetResponse, phase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.phases.with_raw_response.get(
                "http_request_firewall_custom",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.phases.with_raw_response.get(
                "http_request_firewall_custom",
                account_or_zone="string",
                account_or_zone_id="",
            )


class TestAsyncPhases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        phase = await async_client.rulesets.phases.get(
            "http_request_firewall_custom",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(PhaseGetResponse, phase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.phases.with_raw_response.get(
            "http_request_firewall_custom",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phase = await response.parse()
        assert_matches_type(PhaseGetResponse, phase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.phases.with_streaming_response.get(
            "http_request_firewall_custom",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phase = await response.parse()
            assert_matches_type(PhaseGetResponse, phase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.phases.with_raw_response.get(
                "http_request_firewall_custom",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.phases.with_raw_response.get(
                "http_request_firewall_custom",
                account_or_zone="string",
                account_or_zone_id="",
            )
