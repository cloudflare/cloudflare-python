# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.r2.buckets import (
    JobGetResponse,
    JobListResponse,
    JobCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        job = client.r2.buckets.jobs.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="prefixDelete",
            prefix="path/to/",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        job = client.r2.buckets.jobs.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="prefixDelete",
            prefix="path/to/",
            cf_r2_data_catalog_check="cf-r2-data-catalog-check",
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.r2.buckets.jobs.with_raw_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="prefixDelete",
            prefix="path/to/",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.r2.buckets.jobs.with_streaming_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="prefixDelete",
            prefix="path/to/",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.jobs.with_raw_response.create(
                bucket_name="example-bucket",
                account_id="",
                job_type="prefixDelete",
                prefix="path/to/",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.jobs.with_raw_response.create(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                job_type="prefixDelete",
                prefix="path/to/",
            )

    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        job = client.r2.buckets.jobs.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="storageClassMigration",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        job = client.r2.buckets.jobs.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="storageClassMigration",
            destination_storage_class="Standard",
            source_storage_class="Standard",
            cf_r2_data_catalog_check="cf-r2-data-catalog-check",
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.r2.buckets.jobs.with_raw_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="storageClassMigration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.r2.buckets.jobs.with_streaming_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="storageClassMigration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.jobs.with_raw_response.create(
                bucket_name="example-bucket",
                account_id="",
                job_type="storageClassMigration",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.jobs.with_raw_response.create(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                job_type="storageClassMigration",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        job = client.r2.buckets.jobs.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        job = client.r2.buckets.jobs.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            continuation_token="continuationToken",
            job_type="prefixDelete",
            max_keys=0,
            status="ENQUEUED",
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.r2.buckets.jobs.with_raw_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.r2.buckets.jobs.with_streaming_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.jobs.with_raw_response.list(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.jobs.with_raw_response.list(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        job = client.r2.buckets.jobs.get(
            job_id="job_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(JobGetResponse, job, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        job = client.r2.buckets.jobs.get(
            job_id="job_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(JobGetResponse, job, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.r2.buckets.jobs.with_raw_response.get(
            job_id="job_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobGetResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.r2.buckets.jobs.with_streaming_response.get(
            job_id="job_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobGetResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.jobs.with_raw_response.get(
                job_id="job_id",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.jobs.with_raw_response.get(
                job_id="job_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.r2.buckets.jobs.with_raw_response.get(
                job_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.buckets.jobs.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="prefixDelete",
            prefix="path/to/",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.buckets.jobs.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="prefixDelete",
            prefix="path/to/",
            cf_r2_data_catalog_check="cf-r2-data-catalog-check",
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.jobs.with_raw_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="prefixDelete",
            prefix="path/to/",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.jobs.with_streaming_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="prefixDelete",
            prefix="path/to/",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.jobs.with_raw_response.create(
                bucket_name="example-bucket",
                account_id="",
                job_type="prefixDelete",
                prefix="path/to/",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.jobs.with_raw_response.create(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                job_type="prefixDelete",
                prefix="path/to/",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.buckets.jobs.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="storageClassMigration",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.buckets.jobs.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="storageClassMigration",
            destination_storage_class="Standard",
            source_storage_class="Standard",
            cf_r2_data_catalog_check="cf-r2-data-catalog-check",
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.jobs.with_raw_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="storageClassMigration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.jobs.with_streaming_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            job_type="storageClassMigration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.jobs.with_raw_response.create(
                bucket_name="example-bucket",
                account_id="",
                job_type="storageClassMigration",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.jobs.with_raw_response.create(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                job_type="storageClassMigration",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.buckets.jobs.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.buckets.jobs.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            continuation_token="continuationToken",
            job_type="prefixDelete",
            max_keys=0,
            status="ENQUEUED",
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.jobs.with_raw_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.jobs.with_streaming_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.jobs.with_raw_response.list(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.jobs.with_raw_response.list(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.buckets.jobs.get(
            job_id="job_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(JobGetResponse, job, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.r2.buckets.jobs.get(
            job_id="job_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(JobGetResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.jobs.with_raw_response.get(
            job_id="job_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobGetResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.jobs.with_streaming_response.get(
            job_id="job_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobGetResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.jobs.with_raw_response.get(
                job_id="job_id",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.jobs.with_raw_response.get(
                job_id="job_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.r2.buckets.jobs.with_raw_response.get(
                job_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )
