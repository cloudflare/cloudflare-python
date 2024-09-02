# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.event_notifications.r2.configuration import QueueUpdateResponse, QueueDeleteResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.event_notifications.r2.configuration import queue_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        queue = client.event_notifications.r2.configuration.queues.update(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        queue = client.event_notifications.r2.configuration.queues.update(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
            rules=[
                {
                    "actions": ["PutObject", "CopyObject"],
                    "prefix": "img/",
                    "suffix": ".jpeg",
                },
                {
                    "actions": ["PutObject", "CopyObject"],
                    "prefix": "img/",
                    "suffix": ".jpeg",
                },
                {
                    "actions": ["PutObject", "CopyObject"],
                    "prefix": "img/",
                    "suffix": ".jpeg",
                },
            ],
        )
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.event_notifications.r2.configuration.queues.with_raw_response.update(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.event_notifications.r2.configuration.queues.with_streaming_response.update(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(QueueUpdateResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.event_notifications.r2.configuration.queues.with_raw_response.update(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.event_notifications.r2.configuration.queues.with_raw_response.update(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.event_notifications.r2.configuration.queues.with_raw_response.update(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        queue = client.event_notifications.r2.configuration.queues.delete(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(QueueDeleteResponse, queue, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.event_notifications.r2.configuration.queues.with_raw_response.delete(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(QueueDeleteResponse, queue, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.event_notifications.r2.configuration.queues.with_streaming_response.delete(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(QueueDeleteResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.event_notifications.r2.configuration.queues.with_raw_response.delete(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.event_notifications.r2.configuration.queues.with_raw_response.delete(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.event_notifications.r2.configuration.queues.with_raw_response.delete(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncQueues:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        queue = await async_client.event_notifications.r2.configuration.queues.update(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        queue = await async_client.event_notifications.r2.configuration.queues.update(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
            rules=[
                {
                    "actions": ["PutObject", "CopyObject"],
                    "prefix": "img/",
                    "suffix": ".jpeg",
                },
                {
                    "actions": ["PutObject", "CopyObject"],
                    "prefix": "img/",
                    "suffix": ".jpeg",
                },
                {
                    "actions": ["PutObject", "CopyObject"],
                    "prefix": "img/",
                    "suffix": ".jpeg",
                },
            ],
        )
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.event_notifications.r2.configuration.queues.with_raw_response.update(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.event_notifications.r2.configuration.queues.with_streaming_response.update(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(QueueUpdateResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.event_notifications.r2.configuration.queues.with_raw_response.update(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.event_notifications.r2.configuration.queues.with_raw_response.update(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.event_notifications.r2.configuration.queues.with_raw_response.update(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        queue = await async_client.event_notifications.r2.configuration.queues.delete(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(QueueDeleteResponse, queue, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.event_notifications.r2.configuration.queues.with_raw_response.delete(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(QueueDeleteResponse, queue, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.event_notifications.r2.configuration.queues.with_streaming_response.delete(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(QueueDeleteResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.event_notifications.r2.configuration.queues.with_raw_response.delete(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.event_notifications.r2.configuration.queues.with_raw_response.delete(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.event_notifications.r2.configuration.queues.with_raw_response.delete(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="023e105f4ecef8ad9ca31a8372d0c353",
            )
