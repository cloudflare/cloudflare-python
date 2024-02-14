# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers.queues import (
    ConsumerListResponse,
    ConsumerDeleteResponse,
    ConsumerUpdateResponse,
    ConsumerQueueCreateQueueConsumerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConsumers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        consumer = client.workers.queues.consumers.update(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
            body={
                "dead_letter_queue": "updated-example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {"batch_size": 100},
            },
        )
        assert_matches_type(Optional[ConsumerUpdateResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.workers.queues.consumers.with_raw_response.update(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
            body={
                "dead_letter_queue": "updated-example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {"batch_size": 100},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = response.parse()
        assert_matches_type(Optional[ConsumerUpdateResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers.queues.consumers.with_streaming_response.update(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
            body={
                "dead_letter_queue": "updated-example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {"batch_size": 100},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = response.parse()
            assert_matches_type(Optional[ConsumerUpdateResponse], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.queues.consumers.with_raw_response.update(
                "example-consumer",
                account_id="",
                name="example-queue",
                body={
                    "dead_letter_queue": "updated-example-dlq",
                    "environment": "production",
                    "script_name": "example-consumer",
                    "settings": {"batch_size": 100},
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.workers.queues.consumers.with_raw_response.update(
                "example-consumer",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="",
                body={
                    "dead_letter_queue": "updated-example-dlq",
                    "environment": "production",
                    "script_name": "example-consumer",
                    "settings": {"batch_size": 100},
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_name` but received ''"):
            client.workers.queues.consumers.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example-queue",
                body={
                    "dead_letter_queue": "updated-example-dlq",
                    "environment": "production",
                    "script_name": "example-consumer",
                    "settings": {"batch_size": 100},
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        consumer = client.workers.queues.consumers.list(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ConsumerListResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workers.queues.consumers.with_raw_response.list(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = response.parse()
        assert_matches_type(Optional[ConsumerListResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers.queues.consumers.with_streaming_response.list(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = response.parse()
            assert_matches_type(Optional[ConsumerListResponse], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.queues.consumers.with_raw_response.list(
                "example-queue",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.workers.queues.consumers.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        consumer = client.workers.queues.consumers.delete(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
        )
        assert_matches_type(Optional[ConsumerDeleteResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers.queues.consumers.with_raw_response.delete(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = response.parse()
        assert_matches_type(Optional[ConsumerDeleteResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers.queues.consumers.with_streaming_response.delete(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = response.parse()
            assert_matches_type(Optional[ConsumerDeleteResponse], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.queues.consumers.with_raw_response.delete(
                "example-consumer",
                account_id="",
                name="example-queue",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.workers.queues.consumers.with_raw_response.delete(
                "example-consumer",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_name` but received ''"):
            client.workers.queues.consumers.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example-queue",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_queue_create_queue_consumer(self, client: Cloudflare) -> None:
        consumer = client.workers.queues.consumers.queue_create_queue_consumer(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "dead_letter_queue": "example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {
                    "batch_size": 10,
                    "max_retries": 3,
                    "max_wait_time_ms": 5000,
                },
            },
        )
        assert_matches_type(Optional[ConsumerQueueCreateQueueConsumerResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_queue_create_queue_consumer(self, client: Cloudflare) -> None:
        response = client.workers.queues.consumers.with_raw_response.queue_create_queue_consumer(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "dead_letter_queue": "example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {
                    "batch_size": 10,
                    "max_retries": 3,
                    "max_wait_time_ms": 5000,
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = response.parse()
        assert_matches_type(Optional[ConsumerQueueCreateQueueConsumerResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_queue_create_queue_consumer(self, client: Cloudflare) -> None:
        with client.workers.queues.consumers.with_streaming_response.queue_create_queue_consumer(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "dead_letter_queue": "example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {
                    "batch_size": 10,
                    "max_retries": 3,
                    "max_wait_time_ms": 5000,
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = response.parse()
            assert_matches_type(Optional[ConsumerQueueCreateQueueConsumerResponse], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_queue_create_queue_consumer(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.queues.consumers.with_raw_response.queue_create_queue_consumer(
                "example-queue",
                account_id="",
                body={
                    "dead_letter_queue": "example-dlq",
                    "environment": "production",
                    "script_name": "example-consumer",
                    "settings": {
                        "batch_size": 10,
                        "max_retries": 3,
                        "max_wait_time_ms": 5000,
                    },
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.workers.queues.consumers.with_raw_response.queue_create_queue_consumer(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={
                    "dead_letter_queue": "example-dlq",
                    "environment": "production",
                    "script_name": "example-consumer",
                    "settings": {
                        "batch_size": 10,
                        "max_retries": 3,
                        "max_wait_time_ms": 5000,
                    },
                },
            )


class TestAsyncConsumers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.workers.queues.consumers.update(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
            body={
                "dead_letter_queue": "updated-example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {"batch_size": 100},
            },
        )
        assert_matches_type(Optional[ConsumerUpdateResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.queues.consumers.with_raw_response.update(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
            body={
                "dead_letter_queue": "updated-example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {"batch_size": 100},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = await response.parse()
        assert_matches_type(Optional[ConsumerUpdateResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.queues.consumers.with_streaming_response.update(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
            body={
                "dead_letter_queue": "updated-example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {"batch_size": 100},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = await response.parse()
            assert_matches_type(Optional[ConsumerUpdateResponse], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.queues.consumers.with_raw_response.update(
                "example-consumer",
                account_id="",
                name="example-queue",
                body={
                    "dead_letter_queue": "updated-example-dlq",
                    "environment": "production",
                    "script_name": "example-consumer",
                    "settings": {"batch_size": 100},
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.workers.queues.consumers.with_raw_response.update(
                "example-consumer",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="",
                body={
                    "dead_letter_queue": "updated-example-dlq",
                    "environment": "production",
                    "script_name": "example-consumer",
                    "settings": {"batch_size": 100},
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_name` but received ''"):
            await async_client.workers.queues.consumers.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example-queue",
                body={
                    "dead_letter_queue": "updated-example-dlq",
                    "environment": "production",
                    "script_name": "example-consumer",
                    "settings": {"batch_size": 100},
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.workers.queues.consumers.list(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ConsumerListResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.queues.consumers.with_raw_response.list(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = await response.parse()
        assert_matches_type(Optional[ConsumerListResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.queues.consumers.with_streaming_response.list(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = await response.parse()
            assert_matches_type(Optional[ConsumerListResponse], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.queues.consumers.with_raw_response.list(
                "example-queue",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.workers.queues.consumers.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.workers.queues.consumers.delete(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
        )
        assert_matches_type(Optional[ConsumerDeleteResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.queues.consumers.with_raw_response.delete(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = await response.parse()
        assert_matches_type(Optional[ConsumerDeleteResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.queues.consumers.with_streaming_response.delete(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = await response.parse()
            assert_matches_type(Optional[ConsumerDeleteResponse], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.queues.consumers.with_raw_response.delete(
                "example-consumer",
                account_id="",
                name="example-queue",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.workers.queues.consumers.with_raw_response.delete(
                "example-consumer",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_name` but received ''"):
            await async_client.workers.queues.consumers.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example-queue",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_queue_create_queue_consumer(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.workers.queues.consumers.queue_create_queue_consumer(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "dead_letter_queue": "example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {
                    "batch_size": 10,
                    "max_retries": 3,
                    "max_wait_time_ms": 5000,
                },
            },
        )
        assert_matches_type(Optional[ConsumerQueueCreateQueueConsumerResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_queue_create_queue_consumer(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.queues.consumers.with_raw_response.queue_create_queue_consumer(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "dead_letter_queue": "example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {
                    "batch_size": 10,
                    "max_retries": 3,
                    "max_wait_time_ms": 5000,
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = await response.parse()
        assert_matches_type(Optional[ConsumerQueueCreateQueueConsumerResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_queue_create_queue_consumer(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.queues.consumers.with_streaming_response.queue_create_queue_consumer(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "dead_letter_queue": "example-dlq",
                "environment": "production",
                "script_name": "example-consumer",
                "settings": {
                    "batch_size": 10,
                    "max_retries": 3,
                    "max_wait_time_ms": 5000,
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = await response.parse()
            assert_matches_type(Optional[ConsumerQueueCreateQueueConsumerResponse], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_queue_create_queue_consumer(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.queues.consumers.with_raw_response.queue_create_queue_consumer(
                "example-queue",
                account_id="",
                body={
                    "dead_letter_queue": "example-dlq",
                    "environment": "production",
                    "script_name": "example-consumer",
                    "settings": {
                        "batch_size": 10,
                        "max_retries": 3,
                        "max_wait_time_ms": 5000,
                    },
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.workers.queues.consumers.with_raw_response.queue_create_queue_consumer(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={
                    "dead_letter_queue": "example-dlq",
                    "environment": "production",
                    "script_name": "example-consumer",
                    "settings": {
                        "batch_size": 10,
                        "max_retries": 3,
                        "max_wait_time_ms": 5000,
                    },
                },
            )
