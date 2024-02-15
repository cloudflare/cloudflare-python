# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.d1 import (
    DatabaseGetResponse,
    DatabaseQueryResponse,
    DatabaseDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatabase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        database = client.d1.database.delete(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DatabaseDeleteResponse], database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.delete(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(Optional[DatabaseDeleteResponse], database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.delete(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(Optional[DatabaseDeleteResponse], database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.d1.database.with_raw_response.delete(
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_identifier` but received ''"):
            client.d1.database.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        database = client.d1.database.get(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DatabaseGetResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.get(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseGetResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.get(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseGetResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.d1.database.with_raw_response.get(
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_identifier` but received ''"):
            client.d1.database.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_query(self, client: Cloudflare) -> None:
        database = client.d1.database.query(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_query_with_all_params(self, client: Cloudflare) -> None:
        database = client.d1.database.query(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            params=["firstParam", "secondParam"],
        )
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_query(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.query(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_query(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.query(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseQueryResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_query(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.d1.database.with_raw_response.query(
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_identifier="",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_identifier` but received ''"):
            client.d1.database.with_raw_response.query(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )


class TestAsyncDatabase:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.delete(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DatabaseDeleteResponse], database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.delete(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(Optional[DatabaseDeleteResponse], database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.delete(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(Optional[DatabaseDeleteResponse], database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.d1.database.with_raw_response.delete(
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_identifier` but received ''"):
            await async_client.d1.database.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.get(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DatabaseGetResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.get(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseGetResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.get(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseGetResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.d1.database.with_raw_response.get(
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_identifier` but received ''"):
            await async_client.d1.database.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_query(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.query(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.query(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            params=["firstParam", "secondParam"],
        )
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.query(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.query(
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseQueryResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_query(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.d1.database.with_raw_response.query(
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_identifier="",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_identifier` but received ''"):
            await async_client.d1.database.with_raw_response.query(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )
