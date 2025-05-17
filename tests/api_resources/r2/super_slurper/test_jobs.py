# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.r2.super_slurper import (
    JobGetResponse,
    JobListResponse,
    JobCreateResponse,
    JobProgressResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        job = client.r2.super_slurper.jobs.create(
            account_id="account_id",
        )
        assert_matches_type(Optional[JobCreateResponse], job, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        job = client.r2.super_slurper.jobs.create(
            account_id="account_id",
            overwrite=True,
            source={
                "bucket": "bucket",
                "endpoint": "endpoint",
                "secret": {
                    "access_key_id": "accessKeyId",
                    "secret_access_key": "secretAccessKey",
                },
                "vendor": "s3",
            },
            target={
                "bucket": "bucket",
                "jurisdiction": "default",
                "secret": {
                    "access_key_id": "accessKeyId",
                    "secret_access_key": "secretAccessKey",
                },
                "vendor": "r2",
            },
        )
        assert_matches_type(Optional[JobCreateResponse], job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.jobs.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Optional[JobCreateResponse], job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.jobs.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Optional[JobCreateResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        job = client.r2.super_slurper.jobs.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[JobListResponse], job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        job = client.r2.super_slurper.jobs.list(
            account_id="account_id",
            limit=50,
            offset=0,
        )
        assert_matches_type(SyncSinglePage[JobListResponse], job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.jobs.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(SyncSinglePage[JobListResponse], job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.jobs.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(SyncSinglePage[JobListResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_abort(self, client: Cloudflare) -> None:
        job = client.r2.super_slurper.jobs.abort(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(str, job, path=["response"])

    @parametrize
    def test_raw_response_abort(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.jobs.with_raw_response.abort(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(str, job, path=["response"])

    @parametrize
    def test_streaming_response_abort(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.jobs.with_streaming_response.abort(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(str, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_abort(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.abort(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.abort(
                job_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_abort_all(self, client: Cloudflare) -> None:
        job = client.r2.super_slurper.jobs.abort_all(
            account_id="account_id",
        )
        assert_matches_type(str, job, path=["response"])

    @parametrize
    def test_raw_response_abort_all(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.jobs.with_raw_response.abort_all(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(str, job, path=["response"])

    @parametrize
    def test_streaming_response_abort_all(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.jobs.with_streaming_response.abort_all(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(str, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_abort_all(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.abort_all(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        job = client.r2.super_slurper.jobs.get(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(Optional[JobGetResponse], job, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.jobs.with_raw_response.get(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Optional[JobGetResponse], job, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.jobs.with_streaming_response.get(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Optional[JobGetResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.get(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.get(
                job_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_pause(self, client: Cloudflare) -> None:
        job = client.r2.super_slurper.jobs.pause(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(str, job, path=["response"])

    @parametrize
    def test_raw_response_pause(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.jobs.with_raw_response.pause(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(str, job, path=["response"])

    @parametrize
    def test_streaming_response_pause(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.jobs.with_streaming_response.pause(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(str, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_pause(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.pause(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.pause(
                job_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_progress(self, client: Cloudflare) -> None:
        job = client.r2.super_slurper.jobs.progress(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(Optional[JobProgressResponse], job, path=["response"])

    @parametrize
    def test_raw_response_progress(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.jobs.with_raw_response.progress(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Optional[JobProgressResponse], job, path=["response"])

    @parametrize
    def test_streaming_response_progress(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.jobs.with_streaming_response.progress(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Optional[JobProgressResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_progress(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.progress(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.progress(
                job_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_resume(self, client: Cloudflare) -> None:
        job = client.r2.super_slurper.jobs.resume(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(str, job, path=["response"])

    @parametrize
    def test_raw_response_resume(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.jobs.with_raw_response.resume(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(str, job, path=["response"])

    @parametrize
    def test_streaming_response_resume(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.jobs.with_streaming_response.resume(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(str, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resume(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.resume(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.r2.super_slurper.jobs.with_raw_response.resume(
                job_id="",
                account_id="account_id",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.super_slurper.jobs.create(
            account_id="account_id",
        )
        assert_matches_type(Optional[JobCreateResponse], job, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.super_slurper.jobs.create(
            account_id="account_id",
            overwrite=True,
            source={
                "bucket": "bucket",
                "endpoint": "endpoint",
                "secret": {
                    "access_key_id": "accessKeyId",
                    "secret_access_key": "secretAccessKey",
                },
                "vendor": "s3",
            },
            target={
                "bucket": "bucket",
                "jurisdiction": "default",
                "secret": {
                    "access_key_id": "accessKeyId",
                    "secret_access_key": "secretAccessKey",
                },
                "vendor": "r2",
            },
        )
        assert_matches_type(Optional[JobCreateResponse], job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.jobs.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Optional[JobCreateResponse], job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.jobs.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Optional[JobCreateResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.super_slurper.jobs.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[JobListResponse], job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.super_slurper.jobs.list(
            account_id="account_id",
            limit=50,
            offset=0,
        )
        assert_matches_type(AsyncSinglePage[JobListResponse], job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.jobs.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(AsyncSinglePage[JobListResponse], job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.jobs.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(AsyncSinglePage[JobListResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_abort(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.super_slurper.jobs.abort(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(str, job, path=["response"])

    @parametrize
    async def test_raw_response_abort(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.jobs.with_raw_response.abort(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(str, job, path=["response"])

    @parametrize
    async def test_streaming_response_abort(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.jobs.with_streaming_response.abort(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(str, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_abort(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.abort(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.abort(
                job_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_abort_all(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.super_slurper.jobs.abort_all(
            account_id="account_id",
        )
        assert_matches_type(str, job, path=["response"])

    @parametrize
    async def test_raw_response_abort_all(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.jobs.with_raw_response.abort_all(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(str, job, path=["response"])

    @parametrize
    async def test_streaming_response_abort_all(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.jobs.with_streaming_response.abort_all(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(str, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_abort_all(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.abort_all(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.super_slurper.jobs.get(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(Optional[JobGetResponse], job, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.jobs.with_raw_response.get(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Optional[JobGetResponse], job, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.jobs.with_streaming_response.get(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Optional[JobGetResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.get(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.get(
                job_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_pause(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.super_slurper.jobs.pause(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(str, job, path=["response"])

    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.jobs.with_raw_response.pause(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(str, job, path=["response"])

    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.jobs.with_streaming_response.pause(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(str, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_pause(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.pause(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.pause(
                job_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_progress(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.super_slurper.jobs.progress(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(Optional[JobProgressResponse], job, path=["response"])

    @parametrize
    async def test_raw_response_progress(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.jobs.with_raw_response.progress(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Optional[JobProgressResponse], job, path=["response"])

    @parametrize
    async def test_streaming_response_progress(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.jobs.with_streaming_response.progress(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Optional[JobProgressResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_progress(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.progress(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.progress(
                job_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_resume(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.super_slurper.jobs.resume(
            job_id="job_id",
            account_id="account_id",
        )
        assert_matches_type(str, job, path=["response"])

    @parametrize
    async def test_raw_response_resume(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.jobs.with_raw_response.resume(
            job_id="job_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(str, job, path=["response"])

    @parametrize
    async def test_streaming_response_resume(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.jobs.with_streaming_response.resume(
            job_id="job_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(str, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resume(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.resume(
                job_id="job_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.r2.super_slurper.jobs.with_raw_response.resume(
                job_id="",
                account_id="account_id",
            )
