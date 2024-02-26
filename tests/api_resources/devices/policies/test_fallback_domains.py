# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.devices.policies import (
    FallbackDomainGetResponse,
    FallbackDomainListResponse,
    FallbackDomainUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFallbackDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        fallback_domain = client.devices.policies.fallback_domains.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )
        assert_matches_type(Optional[FallbackDomainUpdateResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.devices.policies.fallback_domains.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = response.parse()
        assert_matches_type(Optional[FallbackDomainUpdateResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.devices.policies.fallback_domains.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = response.parse()
            assert_matches_type(Optional[FallbackDomainUpdateResponse], fallback_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.devices.policies.fallback_domains.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        fallback_domain = client.devices.policies.fallback_domains.list(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[FallbackDomainListResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.devices.policies.fallback_domains.with_raw_response.list(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = response.parse()
        assert_matches_type(Optional[FallbackDomainListResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.devices.policies.fallback_domains.with_streaming_response.list(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = response.parse()
            assert_matches_type(Optional[FallbackDomainListResponse], fallback_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        fallback_domain = client.devices.policies.fallback_domains.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[FallbackDomainGetResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.devices.policies.fallback_domains.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = response.parse()
        assert_matches_type(Optional[FallbackDomainGetResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.devices.policies.fallback_domains.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = response.parse()
            assert_matches_type(Optional[FallbackDomainGetResponse], fallback_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.devices.policies.fallback_domains.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncFallbackDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        fallback_domain = await async_client.devices.policies.fallback_domains.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )
        assert_matches_type(Optional[FallbackDomainUpdateResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.fallback_domains.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = await response.parse()
        assert_matches_type(Optional[FallbackDomainUpdateResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.policies.fallback_domains.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = await response.parse()
            assert_matches_type(Optional[FallbackDomainUpdateResponse], fallback_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.devices.policies.fallback_domains.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                body=[{"suffix": "example.com"}, {"suffix": "example.com"}, {"suffix": "example.com"}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        fallback_domain = await async_client.devices.policies.fallback_domains.list(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[FallbackDomainListResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.fallback_domains.with_raw_response.list(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = await response.parse()
        assert_matches_type(Optional[FallbackDomainListResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.policies.fallback_domains.with_streaming_response.list(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = await response.parse()
            assert_matches_type(Optional[FallbackDomainListResponse], fallback_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        fallback_domain = await async_client.devices.policies.fallback_domains.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[FallbackDomainGetResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.fallback_domains.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_domain = await response.parse()
        assert_matches_type(Optional[FallbackDomainGetResponse], fallback_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.devices.policies.fallback_domains.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_domain = await response.parse()
            assert_matches_type(Optional[FallbackDomainGetResponse], fallback_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.devices.policies.fallback_domains.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )
