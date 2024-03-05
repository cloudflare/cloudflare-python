# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.queues import (
    ConsumerGetResponse,
    ConsumerDeleteResponse,
    WorkersConsumerCreated,
    WorkersConsumerUpdated,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConsumers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.create(
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
        assert_matches_type(Optional[WorkersConsumerCreated], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.queues.consumers.with_raw_response.create(
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
        assert_matches_type(Optional[WorkersConsumerCreated], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.queues.consumers.with_streaming_response.create(
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
            assert_matches_type(Optional[WorkersConsumerCreated], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.consumers.with_raw_response.create(
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
            client.queues.consumers.with_raw_response.create(
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

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.update(
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
        assert_matches_type(Optional[WorkersConsumerUpdated], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.queues.consumers.with_raw_response.update(
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
        assert_matches_type(Optional[WorkersConsumerUpdated], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.queues.consumers.with_streaming_response.update(
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
            assert_matches_type(Optional[WorkersConsumerUpdated], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.consumers.with_raw_response.update(
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
            client.queues.consumers.with_raw_response.update(
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
            client.queues.consumers.with_raw_response.update(
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
    def test_method_delete(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.delete(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
        )
        assert_matches_type(Optional[ConsumerDeleteResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.queues.consumers.with_raw_response.delete(
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
        with client.queues.consumers.with_streaming_response.delete(
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
            client.queues.consumers.with_raw_response.delete(
                "example-consumer",
                account_id="",
                name="example-queue",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.queues.consumers.with_raw_response.delete(
                "example-consumer",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_name` but received ''"):
            client.queues.consumers.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example-queue",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        consumer = client.queues.consumers.get(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ConsumerGetResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.queues.consumers.with_raw_response.get(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = response.parse()
        assert_matches_type(Optional[ConsumerGetResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.queues.consumers.with_streaming_response.get(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = response.parse()
            assert_matches_type(Optional[ConsumerGetResponse], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.consumers.with_raw_response.get(
                "example-queue",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.queues.consumers.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncConsumers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.create(
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
        assert_matches_type(Optional[WorkersConsumerCreated], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.consumers.with_raw_response.create(
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
        assert_matches_type(Optional[WorkersConsumerCreated], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.consumers.with_streaming_response.create(
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
            assert_matches_type(Optional[WorkersConsumerCreated], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.create(
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
            await async_client.queues.consumers.with_raw_response.create(
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

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.update(
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
        assert_matches_type(Optional[WorkersConsumerUpdated], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.consumers.with_raw_response.update(
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
        assert_matches_type(Optional[WorkersConsumerUpdated], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.consumers.with_streaming_response.update(
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
            assert_matches_type(Optional[WorkersConsumerUpdated], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.update(
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
            await async_client.queues.consumers.with_raw_response.update(
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
            await async_client.queues.consumers.with_raw_response.update(
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
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.delete(
            "example-consumer",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example-queue",
        )
        assert_matches_type(Optional[ConsumerDeleteResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.consumers.with_raw_response.delete(
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
        async with async_client.queues.consumers.with_streaming_response.delete(
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
            await async_client.queues.consumers.with_raw_response.delete(
                "example-consumer",
                account_id="",
                name="example-queue",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.queues.consumers.with_raw_response.delete(
                "example-consumer",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consumer_name` but received ''"):
            await async_client.queues.consumers.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example-queue",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        consumer = await async_client.queues.consumers.get(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ConsumerGetResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.consumers.with_raw_response.get(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumer = await response.parse()
        assert_matches_type(Optional[ConsumerGetResponse], consumer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.consumers.with_streaming_response.get(
            "example-queue",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumer = await response.parse()
            assert_matches_type(Optional[ConsumerGetResponse], consumer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.consumers.with_raw_response.get(
                "example-queue",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.queues.consumers.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
