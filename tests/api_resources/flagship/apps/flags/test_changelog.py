# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPaginationAfter, AsyncCursorPaginationAfter
from cloudflare.types.flagship.apps.flags import ChangelogListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChangelog:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        changelog = client.flagship.apps.flags.changelog.list(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )
        assert_matches_type(SyncCursorPaginationAfter[ChangelogListResponse], changelog, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        changelog = client.flagship.apps.flags.changelog.list(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
            cursor="cursor",
            limit="limit",
        )
        assert_matches_type(SyncCursorPaginationAfter[ChangelogListResponse], changelog, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.flagship.apps.flags.changelog.with_raw_response.list(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        changelog = response.parse()
        assert_matches_type(SyncCursorPaginationAfter[ChangelogListResponse], changelog, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.flagship.apps.flags.changelog.with_streaming_response.list(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            changelog = response.parse()
            assert_matches_type(SyncCursorPaginationAfter[ChangelogListResponse], changelog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.flagship.apps.flags.changelog.with_raw_response.list(
                flag_key="flag_key",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.flagship.apps.flags.changelog.with_raw_response.list(
                flag_key="flag_key",
                account_id="account_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_key` but received ''"):
            client.flagship.apps.flags.changelog.with_raw_response.list(
                flag_key="",
                account_id="account_id",
                app_id="app_id",
            )


class TestAsyncChangelog:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        changelog = await async_client.flagship.apps.flags.changelog.list(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )
        assert_matches_type(AsyncCursorPaginationAfter[ChangelogListResponse], changelog, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        changelog = await async_client.flagship.apps.flags.changelog.list(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
            cursor="cursor",
            limit="limit",
        )
        assert_matches_type(AsyncCursorPaginationAfter[ChangelogListResponse], changelog, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.flagship.apps.flags.changelog.with_raw_response.list(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        changelog = await response.parse()
        assert_matches_type(AsyncCursorPaginationAfter[ChangelogListResponse], changelog, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.flagship.apps.flags.changelog.with_streaming_response.list(
            flag_key="flag_key",
            account_id="account_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            changelog = await response.parse()
            assert_matches_type(AsyncCursorPaginationAfter[ChangelogListResponse], changelog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.flagship.apps.flags.changelog.with_raw_response.list(
                flag_key="flag_key",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.flagship.apps.flags.changelog.with_raw_response.list(
                flag_key="flag_key",
                account_id="account_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_key` but received ''"):
            await async_client.flagship.apps.flags.changelog.with_raw_response.list(
                flag_key="",
                account_id="account_id",
                app_id="app_id",
            )
