# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.r2_data_catalog.namespaces import TableListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTables:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        table = client.r2_data_catalog.namespaces.tables.list(
            namespace="bronze",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
        )
        assert_matches_type(Optional[TableListResponse], table, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        table = client.r2_data_catalog.namespaces.tables.list(
            namespace="bronze",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            page_size=1,
            page_token="page_token",
            return_details=True,
            return_uuids=True,
        )
        assert_matches_type(Optional[TableListResponse], table, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.r2_data_catalog.namespaces.tables.with_raw_response.list(
            namespace="bronze",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(Optional[TableListResponse], table, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.r2_data_catalog.namespaces.tables.with_streaming_response.list(
            namespace="bronze",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(Optional[TableListResponse], table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2_data_catalog.namespaces.tables.with_raw_response.list(
                namespace="bronze",
                account_id="",
                bucket_name="my-data-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2_data_catalog.namespaces.tables.with_raw_response.list(
                namespace="bronze",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.r2_data_catalog.namespaces.tables.with_raw_response.list(
                namespace="",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="my-data-bucket",
            )


class TestAsyncTables:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        table = await async_client.r2_data_catalog.namespaces.tables.list(
            namespace="bronze",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
        )
        assert_matches_type(Optional[TableListResponse], table, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        table = await async_client.r2_data_catalog.namespaces.tables.list(
            namespace="bronze",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            page_size=1,
            page_token="page_token",
            return_details=True,
            return_uuids=True,
        )
        assert_matches_type(Optional[TableListResponse], table, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2_data_catalog.namespaces.tables.with_raw_response.list(
            namespace="bronze",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(Optional[TableListResponse], table, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2_data_catalog.namespaces.tables.with_streaming_response.list(
            namespace="bronze",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(Optional[TableListResponse], table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2_data_catalog.namespaces.tables.with_raw_response.list(
                namespace="bronze",
                account_id="",
                bucket_name="my-data-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2_data_catalog.namespaces.tables.with_raw_response.list(
                namespace="bronze",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.r2_data_catalog.namespaces.tables.with_raw_response.list(
                namespace="",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="my-data-bucket",
            )
