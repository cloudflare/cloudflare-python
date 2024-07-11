# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.access.users import FailedLoginListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFailedLogins:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        failed_login = client.zero_trust.access.users.failed_logins.list(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[FailedLoginListResponse], failed_login, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.users.failed_logins.with_raw_response.list(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        failed_login = response.parse()
        assert_matches_type(SyncSinglePage[FailedLoginListResponse], failed_login, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.users.failed_logins.with_streaming_response.list(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            failed_login = response.parse()
            assert_matches_type(SyncSinglePage[FailedLoginListResponse], failed_login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.users.failed_logins.with_raw_response.list(
                user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.access.users.failed_logins.with_raw_response.list(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncFailedLogins:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        failed_login = await async_client.zero_trust.access.users.failed_logins.list(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[FailedLoginListResponse], failed_login, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.users.failed_logins.with_raw_response.list(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        failed_login = await response.parse()
        assert_matches_type(AsyncSinglePage[FailedLoginListResponse], failed_login, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.users.failed_logins.with_streaming_response.list(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            failed_login = await response.parse()
            assert_matches_type(AsyncSinglePage[FailedLoginListResponse], failed_login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.users.failed_logins.with_raw_response.list(
                user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.access.users.failed_logins.with_raw_response.list(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
