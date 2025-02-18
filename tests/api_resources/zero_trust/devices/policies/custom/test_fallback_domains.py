# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.devices import FallbackDomain

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFallbackDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        fallback_domain = client.zero_trust.devices.policies.custom.fallback_domains.update(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            domains=[{"suffix": "example.com"}],
        )
        assert_matches_type(SyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.update(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            domains=[{"suffix": "example.com"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = response.parse()
        assert_matches_type(SyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.custom.fallback_domains.with_streaming_response.update(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            domains=[{"suffix": "example.com"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = response.parse()
            assert_matches_type(SyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.update(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                domains=[{"suffix": "example.com"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.update(
                policy_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                domains=[{"suffix": "example.com"}],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        fallback_domain = client.zero_trust.devices.policies.custom.fallback_domains.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = response.parse()
        assert_matches_type(SyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.custom.fallback_domains.with_streaming_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = response.parse()
            assert_matches_type(SyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.get(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.get(
                policy_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncFallbackDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        fallback_domain = await async_client.zero_trust.devices.policies.custom.fallback_domains.update(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            domains=[{"suffix": "example.com"}],
        )
        assert_matches_type(AsyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.update(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            domains=[{"suffix": "example.com"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = await response.parse()
        assert_matches_type(AsyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.custom.fallback_domains.with_streaming_response.update(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            domains=[{"suffix": "example.com"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = await response.parse()
            assert_matches_type(AsyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.update(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                domains=[{"suffix": "example.com"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.update(
                policy_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                domains=[{"suffix": "example.com"}],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        fallback_domain = await async_client.zero_trust.devices.policies.custom.fallback_domains.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = await response.parse()
        assert_matches_type(AsyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.custom.fallback_domains.with_streaming_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = await response.parse()
            assert_matches_type(AsyncSinglePage[FallbackDomain], fallback_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.get(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.zero_trust.devices.policies.custom.fallback_domains.with_raw_response.get(
                policy_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
