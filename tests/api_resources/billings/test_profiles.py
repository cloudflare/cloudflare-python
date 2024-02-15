# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.billings import ProfileAccountBillingProfileBillingProfileDetailsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_billing_profile_billing_profile_details(self, client: Cloudflare) -> None:
        profile = client.billings.profiles.account_billing_profile_billing_profile_details(
            {},
        )
        assert_matches_type(ProfileAccountBillingProfileBillingProfileDetailsResponse, profile, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_billing_profile_billing_profile_details(self, client: Cloudflare) -> None:
        response = client.billings.profiles.with_raw_response.account_billing_profile_billing_profile_details(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileAccountBillingProfileBillingProfileDetailsResponse, profile, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_billing_profile_billing_profile_details(self, client: Cloudflare) -> None:
        with client.billings.profiles.with_streaming_response.account_billing_profile_billing_profile_details(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileAccountBillingProfileBillingProfileDetailsResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_billing_profile_billing_profile_details(self, async_client: AsyncCloudflare) -> None:
        profile = await async_client.billings.profiles.account_billing_profile_billing_profile_details(
            {},
        )
        assert_matches_type(ProfileAccountBillingProfileBillingProfileDetailsResponse, profile, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_billing_profile_billing_profile_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.billings.profiles.with_raw_response.account_billing_profile_billing_profile_details(
                {},
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileAccountBillingProfileBillingProfileDetailsResponse, profile, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_billing_profile_billing_profile_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.billings.profiles.with_streaming_response.account_billing_profile_billing_profile_details(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileAccountBillingProfileBillingProfileDetailsResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
