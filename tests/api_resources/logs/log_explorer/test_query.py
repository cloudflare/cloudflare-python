# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.logs.log_explorer import QuerySqlResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_sql(self, client: Cloudflare) -> None:
        query = client.logs.log_explorer.query.sql(
            body=b"Example data",
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[QuerySqlResponse], query, path=["response"])

    @parametrize
    def test_method_sql_with_all_params(self, client: Cloudflare) -> None:
        query = client.logs.log_explorer.query.sql(
            body=b"Example data",
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[QuerySqlResponse], query, path=["response"])

    @parametrize
    def test_raw_response_sql(self, client: Cloudflare) -> None:
        response = client.logs.log_explorer.query.with_raw_response.sql(
            body=b"Example data",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(SyncSinglePage[QuerySqlResponse], query, path=["response"])

    @parametrize
    def test_streaming_response_sql(self, client: Cloudflare) -> None:
        with client.logs.log_explorer.query.with_streaming_response.sql(
            body=b"Example data",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(SyncSinglePage[QuerySqlResponse], query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_sql(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.logs.log_explorer.query.with_raw_response.sql(
                body=b"Example data",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.logs.log_explorer.query.with_raw_response.sql(
                body=b"Example data",
                account_id="account_id",
            )


class TestAsyncQuery:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_sql(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.logs.log_explorer.query.sql(
            body=b"Example data",
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[QuerySqlResponse], query, path=["response"])

    @parametrize
    async def test_method_sql_with_all_params(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.logs.log_explorer.query.sql(
            body=b"Example data",
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[QuerySqlResponse], query, path=["response"])

    @parametrize
    async def test_raw_response_sql(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logs.log_explorer.query.with_raw_response.sql(
            body=b"Example data",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(AsyncSinglePage[QuerySqlResponse], query, path=["response"])

    @parametrize
    async def test_streaming_response_sql(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logs.log_explorer.query.with_streaming_response.sql(
            body=b"Example data",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(AsyncSinglePage[QuerySqlResponse], query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_sql(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.logs.log_explorer.query.with_raw_response.sql(
                body=b"Example data",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.logs.log_explorer.query.with_raw_response.sql(
                body=b"Example data",
                account_id="account_id",
            )
