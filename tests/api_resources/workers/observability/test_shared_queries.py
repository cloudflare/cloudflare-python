# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers.observability import (
    SharedQueryGetResponse,
    SharedQueryCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSharedQueries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        shared_query = client.workers.observability.shared_queries.create(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        )
        assert_matches_type(SharedQueryCreateResponse, shared_query, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        shared_query = client.workers.observability.shared_queries.create(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
            chart=True,
            compare=True,
            dry=True,
            granularity=0,
            ignore_series=True,
            limit=2000,
            offset="offset",
            offset_by=0,
            offset_direction="offsetDirection",
            parameters={
                "calculations": [
                    {
                        "operator": "uniq",
                        "alias": "alias",
                        "key": "key",
                        "key_type": "string",
                    }
                ],
                "datasets": ["string"],
                "filter_combination": "and",
                "filters": [
                    {
                        "filter_combination": "and",
                        "filters": [
                            {
                                "filter_combination": "and",
                                "filters": [],
                                "kind": "group",
                            }
                        ],
                        "kind": "group",
                    }
                ],
                "group_bys": [
                    {
                        "type": "string",
                        "value": "value",
                    }
                ],
                "havings": [
                    {
                        "key": "key",
                        "operation": "eq",
                        "value": 0,
                    }
                ],
                "limit": 0,
                "needle": {
                    "value": "string",
                    "is_regex": True,
                    "match_case": True,
                },
                "order_by": {
                    "value": "value",
                    "order": "asc",
                },
            },
            view="traces",
        )
        assert_matches_type(SharedQueryCreateResponse, shared_query, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.observability.shared_queries.with_raw_response.create(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shared_query = response.parse()
        assert_matches_type(SharedQueryCreateResponse, shared_query, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.observability.shared_queries.with_streaming_response.create(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shared_query = response.parse()
            assert_matches_type(SharedQueryCreateResponse, shared_query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.shared_queries.with_raw_response.create(
                account_id="",
                query_id="queryId",
                timeframe={
                    "from": 0,
                    "to": 0,
                },
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        shared_query = client.workers.observability.shared_queries.get(
            id="id",
            account_id="account_id",
        )
        assert_matches_type(SharedQueryGetResponse, shared_query, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        shared_query = client.workers.observability.shared_queries.get(
            id="id",
            account_id="account_id",
            view="events",
        )
        assert_matches_type(SharedQueryGetResponse, shared_query, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.observability.shared_queries.with_raw_response.get(
            id="id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shared_query = response.parse()
        assert_matches_type(SharedQueryGetResponse, shared_query, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.observability.shared_queries.with_streaming_response.get(
            id="id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shared_query = response.parse()
            assert_matches_type(SharedQueryGetResponse, shared_query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.shared_queries.with_raw_response.get(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workers.observability.shared_queries.with_raw_response.get(
                id="",
                account_id="account_id",
            )


class TestAsyncSharedQueries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        shared_query = await async_client.workers.observability.shared_queries.create(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        )
        assert_matches_type(SharedQueryCreateResponse, shared_query, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        shared_query = await async_client.workers.observability.shared_queries.create(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
            chart=True,
            compare=True,
            dry=True,
            granularity=0,
            ignore_series=True,
            limit=2000,
            offset="offset",
            offset_by=0,
            offset_direction="offsetDirection",
            parameters={
                "calculations": [
                    {
                        "operator": "uniq",
                        "alias": "alias",
                        "key": "key",
                        "key_type": "string",
                    }
                ],
                "datasets": ["string"],
                "filter_combination": "and",
                "filters": [
                    {
                        "filter_combination": "and",
                        "filters": [
                            {
                                "filter_combination": "and",
                                "filters": [],
                                "kind": "group",
                            }
                        ],
                        "kind": "group",
                    }
                ],
                "group_bys": [
                    {
                        "type": "string",
                        "value": "value",
                    }
                ],
                "havings": [
                    {
                        "key": "key",
                        "operation": "eq",
                        "value": 0,
                    }
                ],
                "limit": 0,
                "needle": {
                    "value": "string",
                    "is_regex": True,
                    "match_case": True,
                },
                "order_by": {
                    "value": "value",
                    "order": "asc",
                },
            },
            view="traces",
        )
        assert_matches_type(SharedQueryCreateResponse, shared_query, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.shared_queries.with_raw_response.create(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shared_query = await response.parse()
        assert_matches_type(SharedQueryCreateResponse, shared_query, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.shared_queries.with_streaming_response.create(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shared_query = await response.parse()
            assert_matches_type(SharedQueryCreateResponse, shared_query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.shared_queries.with_raw_response.create(
                account_id="",
                query_id="queryId",
                timeframe={
                    "from": 0,
                    "to": 0,
                },
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        shared_query = await async_client.workers.observability.shared_queries.get(
            id="id",
            account_id="account_id",
        )
        assert_matches_type(SharedQueryGetResponse, shared_query, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        shared_query = await async_client.workers.observability.shared_queries.get(
            id="id",
            account_id="account_id",
            view="events",
        )
        assert_matches_type(SharedQueryGetResponse, shared_query, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.shared_queries.with_raw_response.get(
            id="id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shared_query = await response.parse()
        assert_matches_type(SharedQueryGetResponse, shared_query, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.shared_queries.with_streaming_response.get(
            id="id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shared_query = await response.parse()
            assert_matches_type(SharedQueryGetResponse, shared_query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.shared_queries.with_raw_response.get(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workers.observability.shared_queries.with_raw_response.get(
                id="",
                account_id="account_id",
            )
