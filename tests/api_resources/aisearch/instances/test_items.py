# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.aisearch.instances import ItemGetResponse, ItemListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        item = client.aisearch.instances.items.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(SyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        item = client.aisearch.instances.items.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            page=1,
            per_page=0,
            search="search",
            status="queued",
        )
        assert_matches_type(SyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.aisearch.instances.items.with_raw_response.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.aisearch.instances.items.with_streaming_response.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.instances.items.with_raw_response.list(
                id="my-ai-search",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.instances.items.with_raw_response.list(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        item = client.aisearch.instances.items.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
        )
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.aisearch.instances.items.with_raw_response.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.aisearch.instances.items.with_streaming_response.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemGetResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.instances.items.with_raw_response.get(
                item_id="item_id",
                account_id="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.instances.items.with_raw_response.get(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.aisearch.instances.items.with_raw_response.get(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                id="my-ai-search",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.instances.items.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.instances.items.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            page=1,
            per_page=0,
            search="search",
            status="queued",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.instances.items.with_raw_response.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.instances.items.with_streaming_response.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.instances.items.with_raw_response.list(
                id="my-ai-search",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.instances.items.with_raw_response.list(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.instances.items.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
        )
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.instances.items.with_raw_response.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.instances.items.with_streaming_response.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemGetResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.instances.items.with_raw_response.get(
                item_id="item_id",
                account_id="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.instances.items.with_raw_response.get(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.aisearch.instances.items.with_raw_response.get(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                id="my-ai-search",
            )
