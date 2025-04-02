# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.r2.super_slurper.jobs import LogListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        log = client.r2.super_slurper.jobs.logs.list(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[LogListResponse], log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        log = client.r2.super_slurper.jobs.logs.list(
            job_id="job_id",
            account_id="account_id",
            limit=50,
            offset=0,
        )
        assert_matches_type(SyncSinglePage[LogListResponse], log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.jobs.logs.with_raw_response.list(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(SyncSinglePage[LogListResponse], log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.jobs.logs.with_streaming_response.list(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(SyncSinglePage[LogListResponse], log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.jobs.logs.with_raw_response.list(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.r2.super_slurper.jobs.logs.with_raw_response.list(
                job_id="",
                account_id="account_id",
            )


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.r2.super_slurper.jobs.logs.list(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[LogListResponse], log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.r2.super_slurper.jobs.logs.list(
            job_id="job_id",
            account_id="account_id",
            limit=50,
            offset=0,
        )
        assert_matches_type(AsyncSinglePage[LogListResponse], log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.jobs.logs.with_raw_response.list(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(AsyncSinglePage[LogListResponse], log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.jobs.logs.with_streaming_response.list(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(AsyncSinglePage[LogListResponse], log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.jobs.logs.with_raw_response.list(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.r2.super_slurper.jobs.logs.with_raw_response.list(
                job_id="",
                account_id="account_id",
            )
