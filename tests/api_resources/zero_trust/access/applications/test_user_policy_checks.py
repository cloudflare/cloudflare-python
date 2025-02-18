# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.access.applications import UserPolicyCheckListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserPolicyChecks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        user_policy_check = client.zero_trust.access.applications.user_policy_checks.list(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[UserPolicyCheckListResponse], user_policy_check, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        user_policy_check = client.zero_trust.access.applications.user_policy_checks.list(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[UserPolicyCheckListResponse], user_policy_check, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.user_policy_checks.with_raw_response.list(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_policy_check = response.parse()
        assert_matches_type(Optional[UserPolicyCheckListResponse], user_policy_check, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.user_policy_checks.with_streaming_response.list(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_policy_check = response.parse()
            assert_matches_type(Optional[UserPolicyCheckListResponse], user_policy_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.user_policy_checks.with_raw_response.list(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.user_policy_checks.with_raw_response.list(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.user_policy_checks.with_raw_response.list(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )


class TestAsyncUserPolicyChecks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        user_policy_check = await async_client.zero_trust.access.applications.user_policy_checks.list(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[UserPolicyCheckListResponse], user_policy_check, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_policy_check = await async_client.zero_trust.access.applications.user_policy_checks.list(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[UserPolicyCheckListResponse], user_policy_check, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.user_policy_checks.with_raw_response.list(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_policy_check = await response.parse()
        assert_matches_type(Optional[UserPolicyCheckListResponse], user_policy_check, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.user_policy_checks.with_streaming_response.list(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_policy_check = await response.parse()
            assert_matches_type(Optional[UserPolicyCheckListResponse], user_policy_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.user_policy_checks.with_raw_response.list(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.user_policy_checks.with_raw_response.list(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.user_policy_checks.with_raw_response.list(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )
