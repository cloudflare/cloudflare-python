# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.workers.observability import (
    QueryListResponse,
    QueryCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        query = client.workers.observability.queries.create(
            account_id="account_id",
            description="Query description",
            name="x",
            parameters={},
        )
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        query = client.workers.observability.queries.create(
            account_id="account_id",
            description="Query description",
            name="x",
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
                        "filters": [{}],
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
        )
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.observability.queries.with_raw_response.create(
            account_id="account_id",
            description="Query description",
            name="x",
            parameters={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.observability.queries.with_streaming_response.create(
            account_id="account_id",
            description="Query description",
            name="x",
            parameters={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryCreateResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.queries.with_raw_response.create(
                account_id="",
                description="Query description",
                name="x",
                parameters={},
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        query = client.workers.observability.queries.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[QueryListResponse], query, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        query = client.workers.observability.queries.list(
            account_id="account_id",
            order="asc",
            order_by="created",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncSinglePage[QueryListResponse], query, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workers.observability.queries.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(SyncSinglePage[QueryListResponse], query, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers.observability.queries.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(SyncSinglePage[QueryListResponse], query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.queries.with_raw_response.list(
                account_id="",
            )


class TestAsyncQueries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.workers.observability.queries.create(
            account_id="account_id",
            description="Query description",
            name="x",
            parameters={},
        )
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.workers.observability.queries.create(
            account_id="account_id",
            description="Query description",
            name="x",
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
                        "filters": [{}],
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
        )
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.queries.with_raw_response.create(
            account_id="account_id",
            description="Query description",
            name="x",
            parameters={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryCreateResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.queries.with_streaming_response.create(
            account_id="account_id",
            description="Query description",
            name="x",
            parameters={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryCreateResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.queries.with_raw_response.create(
                account_id="",
                description="Query description",
                name="x",
                parameters={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.workers.observability.queries.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[QueryListResponse], query, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.workers.observability.queries.list(
            account_id="account_id",
            order="asc",
            order_by="created",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncSinglePage[QueryListResponse], query, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.queries.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(AsyncSinglePage[QueryListResponse], query, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.queries.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(AsyncSinglePage[QueryListResponse], query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.queries.with_raw_response.list(
                account_id="",
            )
