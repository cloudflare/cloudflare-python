# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.queues import Queue, PurgeStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPurge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_start(self, client: Cloudflare) -> None:
        purge = client.queues.purge.start(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Queue], purge, path=["response"])

    @parametrize
    def test_method_start_with_all_params(self, client: Cloudflare) -> None:
        purge = client.queues.purge.start(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            delete_messages_permanently=True,
        )
        assert_matches_type(Optional[Queue], purge, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Cloudflare) -> None:
        response = client.queues.purge.with_raw_response.start(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge = response.parse()
        assert_matches_type(Optional[Queue], purge, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Cloudflare) -> None:
        with client.queues.purge.with_streaming_response.start(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge = response.parse()
            assert_matches_type(Optional[Queue], purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_start(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.purge.with_raw_response.start(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.queues.purge.with_raw_response.start(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_status(self, client: Cloudflare) -> None:
        purge = client.queues.purge.status(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PurgeStatusResponse], purge, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Cloudflare) -> None:
        response = client.queues.purge.with_raw_response.status(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge = response.parse()
        assert_matches_type(Optional[PurgeStatusResponse], purge, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Cloudflare) -> None:
        with client.queues.purge.with_streaming_response.status(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge = response.parse()
            assert_matches_type(Optional[PurgeStatusResponse], purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.purge.with_raw_response.status(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.queues.purge.with_raw_response.status(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPurge:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_start(self, async_client: AsyncCloudflare) -> None:
        purge = await async_client.queues.purge.start(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Queue], purge, path=["response"])

    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncCloudflare) -> None:
        purge = await async_client.queues.purge.start(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            delete_messages_permanently=True,
        )
        assert_matches_type(Optional[Queue], purge, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.purge.with_raw_response.start(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge = await response.parse()
        assert_matches_type(Optional[Queue], purge, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.purge.with_streaming_response.start(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge = await response.parse()
            assert_matches_type(Optional[Queue], purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_start(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.purge.with_raw_response.start(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.queues.purge.with_raw_response.start(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_status(self, async_client: AsyncCloudflare) -> None:
        purge = await async_client.queues.purge.status(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PurgeStatusResponse], purge, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.purge.with_raw_response.status(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge = await response.parse()
        assert_matches_type(Optional[PurgeStatusResponse], purge, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.purge.with_streaming_response.status(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge = await response.parse()
            assert_matches_type(Optional[PurgeStatusResponse], purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.purge.with_raw_response.status(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.queues.purge.with_raw_response.status(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
