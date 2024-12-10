# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        queue = client.r2.buckets.event_notifications.configuration.queues.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        queue = client.r2.buckets.event_notifications.configuration.queues.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            rules=[
                {
                    "actions": ["PutObject", "CopyObject"],
                    "description": "Notifications from source bucket to queue",
                    "prefix": "img/",
                    "suffix": ".jpeg",
                }
            ],
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.r2.buckets.event_notifications.configuration.queues.with_raw_response.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.r2.buckets.event_notifications.configuration.queues.with_streaming_response.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(object, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.event_notifications.configuration.queues.with_raw_response.update(
                queue_id="queue_id",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.event_notifications.configuration.queues.with_raw_response.update(
                queue_id="queue_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.r2.buckets.event_notifications.configuration.queues.with_raw_response.update(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        queue = client.r2.buckets.event_notifications.configuration.queues.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        queue = client.r2.buckets.event_notifications.configuration.queues.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.r2.buckets.event_notifications.configuration.queues.with_raw_response.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.r2.buckets.event_notifications.configuration.queues.with_streaming_response.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(object, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.event_notifications.configuration.queues.with_raw_response.delete(
                queue_id="queue_id",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.event_notifications.configuration.queues.with_raw_response.delete(
                queue_id="queue_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.r2.buckets.event_notifications.configuration.queues.with_raw_response.delete(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )


class TestAsyncQueues:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        queue = await async_client.r2.buckets.event_notifications.configuration.queues.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        queue = await async_client.r2.buckets.event_notifications.configuration.queues.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            rules=[
                {
                    "actions": ["PutObject", "CopyObject"],
                    "description": "Notifications from source bucket to queue",
                    "prefix": "img/",
                    "suffix": ".jpeg",
                }
            ],
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.event_notifications.configuration.queues.with_raw_response.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.event_notifications.configuration.queues.with_streaming_response.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(object, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.event_notifications.configuration.queues.with_raw_response.update(
                queue_id="queue_id",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.event_notifications.configuration.queues.with_raw_response.update(
                queue_id="queue_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.r2.buckets.event_notifications.configuration.queues.with_raw_response.update(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        queue = await async_client.r2.buckets.event_notifications.configuration.queues.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        queue = await async_client.r2.buckets.event_notifications.configuration.queues.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            cf_r2_jurisdiction="default",
        )
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.event_notifications.configuration.queues.with_raw_response.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(object, queue, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.event_notifications.configuration.queues.with_streaming_response.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(object, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.event_notifications.configuration.queues.with_raw_response.delete(
                queue_id="queue_id",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.event_notifications.configuration.queues.with_raw_response.delete(
                queue_id="queue_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.r2.buckets.event_notifications.configuration.queues.with_raw_response.delete(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )