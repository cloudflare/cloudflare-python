# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.logpush import LogpushJob

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        job = client.logpush.jobs.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="string",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        job = client.logpush.jobs.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="string",
            dataset="http_requests",
            enabled=False,
            frequency="high",
            kind="edge",
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            max_upload_bytes=5000000,
            max_upload_interval_seconds=30,
            max_upload_records=1000,
            name="example.com",
            output_options={
                "cve_2021_4428": True,
                "batch_prefix": "string",
                "batch_suffix": "string",
                "field_delimiter": "string",
                "field_names": ["ClientIP", "EdgeStartTimestamp", "RayID"],
                "output_type": "ndjson",
                "record_delimiter": "string",
                "record_prefix": "string",
                "record_suffix": "string",
                "record_template": "string",
                "sample_rate": 0,
                "timestamp_format": "unixnano",
            },
            ownership_challenge="00000000000000000000",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.logpush.jobs.with_raw_response.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.logpush.jobs.with_streaming_response.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Optional[LogpushJob], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.jobs.with_raw_response.create(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logpush.jobs.with_raw_response.create(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        job = client.logpush.jobs.update(
            1,
            account_id="string",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        job = client.logpush.jobs.update(
            1,
            account_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            enabled=False,
            frequency="high",
            kind="edge",
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            max_upload_bytes=5000000,
            max_upload_interval_seconds=30,
            max_upload_records=1000,
            output_options={
                "cve_2021_4428": True,
                "batch_prefix": "string",
                "batch_suffix": "string",
                "field_delimiter": "string",
                "field_names": ["ClientIP", "EdgeStartTimestamp", "RayID"],
                "output_type": "ndjson",
                "record_delimiter": "string",
                "record_prefix": "string",
                "record_suffix": "string",
                "record_template": "string",
                "sample_rate": 0,
                "timestamp_format": "unixnano",
            },
            ownership_challenge="00000000000000000000",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.logpush.jobs.with_raw_response.update(
            1,
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.logpush.jobs.with_streaming_response.update(
            1,
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Optional[LogpushJob], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.jobs.with_raw_response.update(
                1,
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logpush.jobs.with_raw_response.update(
                1,
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        job = client.logpush.jobs.list(
            account_id="string",
        )
        assert_matches_type(SyncSinglePage[Optional[LogpushJob]], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        job = client.logpush.jobs.list(
            account_id="string",
        )
        assert_matches_type(SyncSinglePage[Optional[LogpushJob]], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.logpush.jobs.with_raw_response.list(
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(SyncSinglePage[Optional[LogpushJob]], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.logpush.jobs.with_streaming_response.list(
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(SyncSinglePage[Optional[LogpushJob]], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.jobs.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logpush.jobs.with_raw_response.list(
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        job = client.logpush.jobs.delete(
            1,
            account_id="string",
        )
        assert_matches_type(object, job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        job = client.logpush.jobs.delete(
            1,
            account_id="string",
        )
        assert_matches_type(object, job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.logpush.jobs.with_raw_response.delete(
            1,
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(object, job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.logpush.jobs.with_streaming_response.delete(
            1,
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(object, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.jobs.with_raw_response.delete(
                1,
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logpush.jobs.with_raw_response.delete(
                1,
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        job = client.logpush.jobs.get(
            1,
            account_id="string",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        job = client.logpush.jobs.get(
            1,
            account_id="string",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.logpush.jobs.with_raw_response.get(
            1,
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.logpush.jobs.with_streaming_response.get(
            1,
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Optional[LogpushJob], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.jobs.with_raw_response.get(
                1,
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logpush.jobs.with_raw_response.get(
                1,
                account_id="string",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.logpush.jobs.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="string",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.logpush.jobs.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="string",
            dataset="http_requests",
            enabled=False,
            frequency="high",
            kind="edge",
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            max_upload_bytes=5000000,
            max_upload_interval_seconds=30,
            max_upload_records=1000,
            name="example.com",
            output_options={
                "cve_2021_4428": True,
                "batch_prefix": "string",
                "batch_suffix": "string",
                "field_delimiter": "string",
                "field_names": ["ClientIP", "EdgeStartTimestamp", "RayID"],
                "output_type": "ndjson",
                "record_delimiter": "string",
                "record_prefix": "string",
                "record_suffix": "string",
                "record_template": "string",
                "sample_rate": 0,
                "timestamp_format": "unixnano",
            },
            ownership_challenge="00000000000000000000",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.jobs.with_raw_response.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.jobs.with_streaming_response.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Optional[LogpushJob], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.jobs.with_raw_response.create(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logpush.jobs.with_raw_response.create(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.logpush.jobs.update(
            1,
            account_id="string",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.logpush.jobs.update(
            1,
            account_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            enabled=False,
            frequency="high",
            kind="edge",
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            max_upload_bytes=5000000,
            max_upload_interval_seconds=30,
            max_upload_records=1000,
            output_options={
                "cve_2021_4428": True,
                "batch_prefix": "string",
                "batch_suffix": "string",
                "field_delimiter": "string",
                "field_names": ["ClientIP", "EdgeStartTimestamp", "RayID"],
                "output_type": "ndjson",
                "record_delimiter": "string",
                "record_prefix": "string",
                "record_suffix": "string",
                "record_template": "string",
                "sample_rate": 0,
                "timestamp_format": "unixnano",
            },
            ownership_challenge="00000000000000000000",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.jobs.with_raw_response.update(
            1,
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.jobs.with_streaming_response.update(
            1,
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Optional[LogpushJob], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.jobs.with_raw_response.update(
                1,
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logpush.jobs.with_raw_response.update(
                1,
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.logpush.jobs.list(
            account_id="string",
        )
        assert_matches_type(AsyncSinglePage[Optional[LogpushJob]], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.logpush.jobs.list(
            account_id="string",
        )
        assert_matches_type(AsyncSinglePage[Optional[LogpushJob]], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.jobs.with_raw_response.list(
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(AsyncSinglePage[Optional[LogpushJob]], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.jobs.with_streaming_response.list(
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(AsyncSinglePage[Optional[LogpushJob]], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.jobs.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logpush.jobs.with_raw_response.list(
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.logpush.jobs.delete(
            1,
            account_id="string",
        )
        assert_matches_type(object, job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.logpush.jobs.delete(
            1,
            account_id="string",
        )
        assert_matches_type(object, job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.jobs.with_raw_response.delete(
            1,
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(object, job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.jobs.with_streaming_response.delete(
            1,
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(object, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.jobs.with_raw_response.delete(
                1,
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logpush.jobs.with_raw_response.delete(
                1,
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.logpush.jobs.get(
            1,
            account_id="string",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.logpush.jobs.get(
            1,
            account_id="string",
        )
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.jobs.with_raw_response.get(
            1,
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Optional[LogpushJob], job, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.jobs.with_streaming_response.get(
            1,
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Optional[LogpushJob], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.jobs.with_raw_response.get(
                1,
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logpush.jobs.with_raw_response.get(
                1,
                account_id="string",
            )
