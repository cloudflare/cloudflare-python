# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.queues import Consumer, ConsumerDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConsumers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dead_letter_queue="example-queue",
            script_name="my-consumer-worker",
            settings={
                "batch_size": 50,
                "max_concurrency": 10,
                "max_retries": 3,
                "max_wait_time_ms": 5000,
                "retry_delay": 10,
            },
            type="worker",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.queues.consumers.with_raw_response.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = response.parse()
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.queues.consumers.with_streaming_response.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = response.parse()
            assert_matches_type(Optional[Consumer], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.consumers.with_raw_response.create(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.queues.consumers.with_raw_response.create(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dead_letter_queue="example-queue",
            settings={
                "batch_size": 50,
                "max_retries": 3,
                "retry_delay": 10,
                "visibility_timeout_ms": 6000,
            },
            type="http_pull",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.queues.consumers.with_raw_response.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = response.parse()
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.queues.consumers.with_streaming_response.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = response.parse()
            assert_matches_type(Optional[Consumer], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.consumers.with_raw_response.create(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.queues.consumers.with_raw_response.create(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            dead_letter_queue="example-queue",
            script_name="my-consumer-worker",
            settings={
                "batch_size": 50,
                "max_concurrency": 10,
                "max_retries": 3,
                "max_wait_time_ms": 5000,
                "retry_delay": 10,
            },
            type="worker",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.queues.consumers.with_raw_response.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = response.parse()
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.queues.consumers.with_streaming_response.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = response.parse()
            assert_matches_type(Optional[Consumer], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.consumers.with_raw_response.update(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.queues.consumers.with_raw_response.update(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_id` but received ''"):
            client.queues.consumers.with_raw_response.update(
                consumer_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            dead_letter_queue="example-queue",
            settings={
                "batch_size": 50,
                "max_retries": 3,
                "retry_delay": 10,
                "visibility_timeout_ms": 6000,
            },
            type="http_pull",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.queues.consumers.with_raw_response.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = response.parse()
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.queues.consumers.with_streaming_response.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = response.parse()
            assert_matches_type(Optional[Consumer], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.consumers.with_raw_response.update(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.queues.consumers.with_raw_response.update(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_id` but received ''"):
            client.queues.consumers.with_raw_response.update(
                consumer_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.delete(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConsumerDeleteResponse, consumer, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.queues.consumers.with_raw_response.delete(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = response.parse()
        assert_matches_type(ConsumerDeleteResponse, consumer, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.queues.consumers.with_streaming_response.delete(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = response.parse()
            assert_matches_type(ConsumerDeleteResponse, consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.consumers.with_raw_response.delete(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.queues.consumers.with_raw_response.delete(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_id` but received ''"):
            client.queues.consumers.with_raw_response.delete(
                consumer_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.get(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Consumer], consumer, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.queues.consumers.with_raw_response.get(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = response.parse()
        assert_matches_type(SyncSinglePage[Consumer], consumer, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.queues.consumers.with_streaming_response.get(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = response.parse()
            assert_matches_type(SyncSinglePage[Consumer], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.consumers.with_raw_response.get(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.queues.consumers.with_raw_response.get(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncConsumers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dead_letter_queue="example-queue",
            script_name="my-consumer-worker",
            settings={
                "batch_size": 50,
                "max_concurrency": 10,
                "max_retries": 3,
                "max_wait_time_ms": 5000,
                "retry_delay": 10,
            },
            type="worker",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.consumers.with_raw_response.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = await response.parse()
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.consumers.with_streaming_response.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = await response.parse()
            assert_matches_type(Optional[Consumer], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.create(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.create(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dead_letter_queue="example-queue",
            settings={
                "batch_size": 50,
                "max_retries": 3,
                "retry_delay": 10,
                "visibility_timeout_ms": 6000,
            },
            type="http_pull",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.consumers.with_raw_response.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = await response.parse()
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.consumers.with_streaming_response.create(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = await response.parse()
            assert_matches_type(Optional[Consumer], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.create(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.create(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            dead_letter_queue="example-queue",
            script_name="my-consumer-worker",
            settings={
                "batch_size": 50,
                "max_concurrency": 10,
                "max_retries": 3,
                "max_wait_time_ms": 5000,
                "retry_delay": 10,
            },
            type="worker",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.consumers.with_raw_response.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = await response.parse()
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.consumers.with_streaming_response.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = await response.parse()
            assert_matches_type(Optional[Consumer], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.update(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.update(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.update(
                consumer_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            dead_letter_queue="example-queue",
            settings={
                "batch_size": 50,
                "max_retries": 3,
                "retry_delay": 10,
                "visibility_timeout_ms": 6000,
            },
            type="http_pull",
        )
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.consumers.with_raw_response.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = await response.parse()
        assert_matches_type(Optional[Consumer], consumer, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.consumers.with_streaming_response.update(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = await response.parse()
            assert_matches_type(Optional[Consumer], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.update(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.update(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.update(
                consumer_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.delete(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConsumerDeleteResponse, consumer, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.consumers.with_raw_response.delete(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = await response.parse()
        assert_matches_type(ConsumerDeleteResponse, consumer, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.consumers.with_streaming_response.delete(
            consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = await response.parse()
            assert_matches_type(ConsumerDeleteResponse, consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.delete(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.delete(
                consumer_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.delete(
                consumer_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.get(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Consumer], consumer, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.consumers.with_raw_response.get(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = await response.parse()
        assert_matches_type(AsyncSinglePage[Consumer], consumer, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.consumers.with_streaming_response.get(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = await response.parse()
            assert_matches_type(AsyncSinglePage[Consumer], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.get(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.get(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
