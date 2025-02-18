# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.queues import MessageAckResponse, MessagePullResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_ack(self, client: Cloudflare) -> None:
        message = client.queues.messages.ack(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[MessageAckResponse], message, path=["response"])

    @parametrize
    def test_method_ack_with_all_params(self, client: Cloudflare) -> None:
        message = client.queues.messages.ack(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            acks=[
                {
                    "lease_id": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..Q8p21d7dceR6vUfwftONdQ.JVqZgAS-Zk7MqmqccYtTHeeMElNHaOMigeWdb8LyMOg.T2_HV99CYzGaQuhTyW8RsgbnpTRZHRM6N7UoSaAKeK0"
                }
            ],
            retries=[
                {
                    "delay_seconds": 10,
                    "lease_id": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..Q8p21d7dceR6vUfwftONdQ.JVqZgAS-Zk7MqmqccYtTHeeMElNHaOMigeWdb8LyMOg.T2_HV99CYzGaQuhTyW8RsgbnpTRZHRM6N7UoSaAKeK0",
                }
            ],
        )
        assert_matches_type(Optional[MessageAckResponse], message, path=["response"])

    @parametrize
    def test_raw_response_ack(self, client: Cloudflare) -> None:
        response = client.queues.messages.with_raw_response.ack(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Optional[MessageAckResponse], message, path=["response"])

    @parametrize
    def test_streaming_response_ack(self, client: Cloudflare) -> None:
        with client.queues.messages.with_streaming_response.ack(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Optional[MessageAckResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_ack(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.messages.with_raw_response.ack(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.queues.messages.with_raw_response.ack(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_pull(self, client: Cloudflare) -> None:
        message = client.queues.messages.pull(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[MessagePullResponse], message, path=["response"])

    @parametrize
    def test_method_pull_with_all_params(self, client: Cloudflare) -> None:
        message = client.queues.messages.pull(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            batch_size=50,
            visibility_timeout_ms=6000,
        )
        assert_matches_type(SyncSinglePage[MessagePullResponse], message, path=["response"])

    @parametrize
    def test_raw_response_pull(self, client: Cloudflare) -> None:
        response = client.queues.messages.with_raw_response.pull(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncSinglePage[MessagePullResponse], message, path=["response"])

    @parametrize
    def test_streaming_response_pull(self, client: Cloudflare) -> None:
        with client.queues.messages.with_streaming_response.pull(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncSinglePage[MessagePullResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_pull(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.queues.messages.with_raw_response.pull(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.queues.messages.with_raw_response.pull(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_ack(self, async_client: AsyncCloudflare) -> None:
        message = await async_client.queues.messages.ack(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[MessageAckResponse], message, path=["response"])

    @parametrize
    async def test_method_ack_with_all_params(self, async_client: AsyncCloudflare) -> None:
        message = await async_client.queues.messages.ack(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            acks=[
                {
                    "lease_id": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..Q8p21d7dceR6vUfwftONdQ.JVqZgAS-Zk7MqmqccYtTHeeMElNHaOMigeWdb8LyMOg.T2_HV99CYzGaQuhTyW8RsgbnpTRZHRM6N7UoSaAKeK0"
                }
            ],
            retries=[
                {
                    "delay_seconds": 10,
                    "lease_id": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..Q8p21d7dceR6vUfwftONdQ.JVqZgAS-Zk7MqmqccYtTHeeMElNHaOMigeWdb8LyMOg.T2_HV99CYzGaQuhTyW8RsgbnpTRZHRM6N7UoSaAKeK0",
                }
            ],
        )
        assert_matches_type(Optional[MessageAckResponse], message, path=["response"])

    @parametrize
    async def test_raw_response_ack(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.messages.with_raw_response.ack(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Optional[MessageAckResponse], message, path=["response"])

    @parametrize
    async def test_streaming_response_ack(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.messages.with_streaming_response.ack(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Optional[MessageAckResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_ack(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.messages.with_raw_response.ack(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.queues.messages.with_raw_response.ack(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_pull(self, async_client: AsyncCloudflare) -> None:
        message = await async_client.queues.messages.pull(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[MessagePullResponse], message, path=["response"])

    @parametrize
    async def test_method_pull_with_all_params(self, async_client: AsyncCloudflare) -> None:
        message = await async_client.queues.messages.pull(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            batch_size=50,
            visibility_timeout_ms=6000,
        )
        assert_matches_type(AsyncSinglePage[MessagePullResponse], message, path=["response"])

    @parametrize
    async def test_raw_response_pull(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.queues.messages.with_raw_response.pull(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncSinglePage[MessagePullResponse], message, path=["response"])

    @parametrize
    async def test_streaming_response_pull(self, async_client: AsyncCloudflare) -> None:
        async with async_client.queues.messages.with_streaming_response.pull(
            queue_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncSinglePage[MessagePullResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_pull(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.queues.messages.with_raw_response.pull(
                queue_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.queues.messages.with_raw_response.pull(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
