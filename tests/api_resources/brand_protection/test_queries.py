# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        query = client.brand_protection.queries.create(
            account_id="x",
        )
        assert query is None

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        query = client.brand_protection.queries.create(
            account_id="x",
            id="id",
            query_scan=True,
            query_tag="tag",
            max_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            body_scan=True,
            string_matches={},
            body_tag="tag",
        )
        assert query is None

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.brand_protection.queries.with_raw_response.create(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert query is None

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.brand_protection.queries.with_streaming_response.create(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert query is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.brand_protection.queries.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        query = client.brand_protection.queries.delete(
            account_id="x",
        )
        assert query is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        query = client.brand_protection.queries.delete(
            account_id="x",
            id="id",
            scan=True,
            tag="tag",
        )
        assert query is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.brand_protection.queries.with_raw_response.delete(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert query is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.brand_protection.queries.with_streaming_response.delete(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert query is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.brand_protection.queries.with_raw_response.delete(
                account_id="",
            )


class TestAsyncQueries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.brand_protection.queries.create(
            account_id="x",
        )
        assert query is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.brand_protection.queries.create(
            account_id="x",
            id="id",
            query_scan=True,
            query_tag="tag",
            max_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            body_scan=True,
            string_matches={},
            body_tag="tag",
        )
        assert query is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.brand_protection.queries.with_raw_response.create(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert query is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.brand_protection.queries.with_streaming_response.create(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert query is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.brand_protection.queries.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.brand_protection.queries.delete(
            account_id="x",
        )
        assert query is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        query = await async_client.brand_protection.queries.delete(
            account_id="x",
            id="id",
            scan=True,
            tag="tag",
        )
        assert query is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.brand_protection.queries.with_raw_response.delete(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert query is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.brand_protection.queries.with_streaming_response.delete(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert query is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.brand_protection.queries.with_raw_response.delete(
                account_id="",
            )
