# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.d1 import (
    D1,
    QueryResult,
    DatabaseRawResponse,
    DatabaseListResponse,
    DatabaseExportResponse,
    DatabaseImportResponse,
)
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatabase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        database = client.d1.database.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        )
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        database = client.d1.database.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
            primary_location_hint="wnam",
        )
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(D1, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.create(
                account_id="",
                name="my-database",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        database = client.d1.database.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        database = client.d1.database.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            page=1,
            per_page=10,
        )
        assert_matches_type(SyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        database = client.d1.database.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, database, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(object, database, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(object, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.delete(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.delete(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_export(self, client: Cloudflare) -> None:
        database = client.d1.database.export(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            output_format="polling",
        )
        assert_matches_type(DatabaseExportResponse, database, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: Cloudflare) -> None:
        database = client.d1.database.export(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            output_format="polling",
            current_bookmark="current_bookmark",
            dump_options={
                "no_data": True,
                "no_schema": True,
                "tables": ["string"],
            },
        )
        assert_matches_type(DatabaseExportResponse, database, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.export(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            output_format="polling",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseExportResponse, database, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.export(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            output_format="polling",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseExportResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_export(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.export(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                output_format="polling",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.export(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                output_format="polling",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        database = client.d1.database.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(D1, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.get(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.get(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_import_overload_1(self, client: Cloudflare) -> None:
        database = client.d1.database.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="init",
            etag="etag",
        )
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    def test_raw_response_import_overload_1(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="init",
            etag="etag",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    def test_streaming_response_import_overload_1(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="init",
            etag="etag",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseImportResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_import_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.import_(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                action="init",
                etag="etag",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.import_(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="init",
                etag="etag",
            )

    @parametrize
    def test_method_import_overload_2(self, client: Cloudflare) -> None:
        database = client.d1.database.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="ingest",
            etag="etag",
            filename="filename",
        )
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    def test_raw_response_import_overload_2(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="ingest",
            etag="etag",
            filename="filename",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    def test_streaming_response_import_overload_2(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="ingest",
            etag="etag",
            filename="filename",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseImportResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_import_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.import_(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                action="ingest",
                etag="etag",
                filename="filename",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.import_(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="ingest",
                etag="etag",
                filename="filename",
            )

    @parametrize
    def test_method_import_overload_3(self, client: Cloudflare) -> None:
        database = client.d1.database.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="poll",
            current_bookmark="current_bookmark",
        )
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    def test_raw_response_import_overload_3(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="poll",
            current_bookmark="current_bookmark",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    def test_streaming_response_import_overload_3(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="poll",
            current_bookmark="current_bookmark",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseImportResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_import_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.import_(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                action="poll",
                current_bookmark="current_bookmark",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.import_(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="poll",
                current_bookmark="current_bookmark",
            )

    @parametrize
    def test_method_query(self, client: Cloudflare) -> None:
        database = client.d1.database.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )
        assert_matches_type(SyncSinglePage[QueryResult], database, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Cloudflare) -> None:
        database = client.d1.database.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            params=["firstParam", "secondParam"],
        )
        assert_matches_type(SyncSinglePage[QueryResult], database, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(SyncSinglePage[QueryResult], database, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(SyncSinglePage[QueryResult], database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_query(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.query(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.query(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

    @parametrize
    def test_method_raw(self, client: Cloudflare) -> None:
        database = client.d1.database.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )
        assert_matches_type(SyncSinglePage[DatabaseRawResponse], database, path=["response"])

    @parametrize
    def test_method_raw_with_all_params(self, client: Cloudflare) -> None:
        database = client.d1.database.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            params=["firstParam", "secondParam"],
        )
        assert_matches_type(SyncSinglePage[DatabaseRawResponse], database, path=["response"])

    @parametrize
    def test_raw_response_raw(self, client: Cloudflare) -> None:
        response = client.d1.database.with_raw_response.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(SyncSinglePage[DatabaseRawResponse], database, path=["response"])

    @parametrize
    def test_streaming_response_raw(self, client: Cloudflare) -> None:
        with client.d1.database.with_streaming_response.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(SyncSinglePage[DatabaseRawResponse], database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_raw(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.raw(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.raw(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )


class TestAsyncDatabase:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        )
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
            primary_location_hint="wnam",
        )
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(D1, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.create(
                account_id="",
                name="my-database",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            page=1,
            per_page=10,
        )
        assert_matches_type(AsyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, database, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(object, database, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(object, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.delete(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.delete(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_export(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.export(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            output_format="polling",
        )
        assert_matches_type(DatabaseExportResponse, database, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.export(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            output_format="polling",
            current_bookmark="current_bookmark",
            dump_options={
                "no_data": True,
                "no_schema": True,
                "tables": ["string"],
            },
        )
        assert_matches_type(DatabaseExportResponse, database, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.export(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            output_format="polling",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseExportResponse, database, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.export(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            output_format="polling",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseExportResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_export(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.export(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                output_format="polling",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.export(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                output_format="polling",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(D1, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.get(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.get(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_import_overload_1(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="init",
            etag="etag",
        )
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    async def test_raw_response_import_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="init",
            etag="etag",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    async def test_streaming_response_import_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="init",
            etag="etag",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseImportResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_import_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.import_(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                action="init",
                etag="etag",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.import_(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="init",
                etag="etag",
            )

    @parametrize
    async def test_method_import_overload_2(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="ingest",
            etag="etag",
            filename="filename",
        )
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    async def test_raw_response_import_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="ingest",
            etag="etag",
            filename="filename",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    async def test_streaming_response_import_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="ingest",
            etag="etag",
            filename="filename",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseImportResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_import_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.import_(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                action="ingest",
                etag="etag",
                filename="filename",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.import_(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="ingest",
                etag="etag",
                filename="filename",
            )

    @parametrize
    async def test_method_import_overload_3(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="poll",
            current_bookmark="current_bookmark",
        )
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    async def test_raw_response_import_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="poll",
            current_bookmark="current_bookmark",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseImportResponse, database, path=["response"])

    @parametrize
    async def test_streaming_response_import_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.import_(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="poll",
            current_bookmark="current_bookmark",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseImportResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_import_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.import_(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                action="poll",
                current_bookmark="current_bookmark",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.import_(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="poll",
                current_bookmark="current_bookmark",
            )

    @parametrize
    async def test_method_query(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )
        assert_matches_type(AsyncSinglePage[QueryResult], database, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            params=["firstParam", "secondParam"],
        )
        assert_matches_type(AsyncSinglePage[QueryResult], database, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(AsyncSinglePage[QueryResult], database, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(AsyncSinglePage[QueryResult], database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_query(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.query(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.query(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

    @parametrize
    async def test_method_raw(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )
        assert_matches_type(AsyncSinglePage[DatabaseRawResponse], database, path=["response"])

    @parametrize
    async def test_method_raw_with_all_params(self, async_client: AsyncCloudflare) -> None:
        database = await async_client.d1.database.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            params=["firstParam", "secondParam"],
        )
        assert_matches_type(AsyncSinglePage[DatabaseRawResponse], database, path=["response"])

    @parametrize
    async def test_raw_response_raw(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.with_raw_response.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(AsyncSinglePage[DatabaseRawResponse], database, path=["response"])

    @parametrize
    async def test_streaming_response_raw(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.with_streaming_response.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(AsyncSinglePage[DatabaseRawResponse], database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_raw(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.raw(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.raw(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )
