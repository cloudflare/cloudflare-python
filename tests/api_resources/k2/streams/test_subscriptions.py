# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.k2.streams import SubscriptionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        subscription = client.k2.streams.subscriptions.list(
            stream_id="053e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[SubscriptionListResponse], subscription, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.k2.streams.subscriptions.with_raw_response.list(
            stream_id="053e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncSinglePage[SubscriptionListResponse], subscription, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.k2.streams.subscriptions.with_streaming_response.list(
            stream_id="053e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SyncSinglePage[SubscriptionListResponse], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.k2.streams.subscriptions.with_raw_response.list(
                stream_id="053e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stream_id` but received ''"):
            client.k2.streams.subscriptions.with_raw_response.list(
                stream_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.k2.streams.subscriptions.list(
            stream_id="053e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[SubscriptionListResponse], subscription, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.k2.streams.subscriptions.with_raw_response.list(
            stream_id="053e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(AsyncSinglePage[SubscriptionListResponse], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.k2.streams.subscriptions.with_streaming_response.list(
            stream_id="053e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncSinglePage[SubscriptionListResponse], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.k2.streams.subscriptions.with_raw_response.list(
                stream_id="053e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stream_id` but received ''"):
            await async_client.k2.streams.subscriptions.with_raw_response.list(
                stream_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )
