# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.workers.observability.telemetry import KeyCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        key = client.workers.observability.telemetry.keys.create(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[KeyCreateResponse], key, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        key = client.workers.observability.telemetry.keys.create(
            account_id="account_id",
            datasets=["string"],
            filters=[
                {
                    "key": "key",
                    "operation": "includes",
                    "type": "string",
                    "value": "string",
                }
            ],
            key_needle={
                "value": "string",
                "is_regex": True,
                "match_case": True,
            },
            limit=0,
            needle={
                "value": "string",
                "is_regex": True,
                "match_case": True,
            },
            timeframe={
                "from": 0,
                "to": 0,
            },
        )
        assert_matches_type(SyncSinglePage[KeyCreateResponse], key, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.observability.telemetry.keys.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(SyncSinglePage[KeyCreateResponse], key, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.observability.telemetry.keys.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(SyncSinglePage[KeyCreateResponse], key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.telemetry.keys.with_raw_response.create(
                account_id="",
            )


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        key = await async_client.workers.observability.telemetry.keys.create(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[KeyCreateResponse], key, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        key = await async_client.workers.observability.telemetry.keys.create(
            account_id="account_id",
            datasets=["string"],
            filters=[
                {
                    "key": "key",
                    "operation": "includes",
                    "type": "string",
                    "value": "string",
                }
            ],
            key_needle={
                "value": "string",
                "is_regex": True,
                "match_case": True,
            },
            limit=0,
            needle={
                "value": "string",
                "is_regex": True,
                "match_case": True,
            },
            timeframe={
                "from": 0,
                "to": 0,
            },
        )
        assert_matches_type(AsyncSinglePage[KeyCreateResponse], key, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.telemetry.keys.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(AsyncSinglePage[KeyCreateResponse], key, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.telemetry.keys.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(AsyncSinglePage[KeyCreateResponse], key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.telemetry.keys.with_raw_response.create(
                account_id="",
            )
