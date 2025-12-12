# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.aisearch import (
    TokenListResponse,
    TokenReadResponse,
    TokenCreateResponse,
    TokenDeleteResponse,
    TokenUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        token = client.aisearch.tokens.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            cf_api_id="cf_api_id",
            cf_api_key="cf_api_key",
            name="name",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        token = client.aisearch.tokens.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            cf_api_id="cf_api_id",
            cf_api_key="cf_api_key",
            name="name",
            legacy=True,
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.aisearch.tokens.with_raw_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            cf_api_id="cf_api_id",
            cf_api_key="cf_api_key",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.aisearch.tokens.with_streaming_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            cf_api_id="cf_api_id",
            cf_api_key="cf_api_key",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenCreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.tokens.with_raw_response.create(
                account_id="",
                cf_api_id="cf_api_id",
                cf_api_key="cf_api_key",
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        token = client.aisearch.tokens.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(TokenUpdateResponse, token, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.aisearch.tokens.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenUpdateResponse, token, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.aisearch.tokens.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenUpdateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.tokens.with_raw_response.update(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.tokens.with_raw_response.update(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        token = client.aisearch.tokens.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(SyncV4PagePaginationArray[TokenListResponse], token, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        token = client.aisearch.tokens.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[TokenListResponse], token, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.aisearch.tokens.with_raw_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[TokenListResponse], token, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.aisearch.tokens.with_streaming_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[TokenListResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.tokens.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        token = client.aisearch.tokens.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(TokenDeleteResponse, token, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.aisearch.tokens.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenDeleteResponse, token, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.aisearch.tokens.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenDeleteResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.tokens.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.tokens.with_raw_response.delete(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    def test_method_read(self, client: Cloudflare) -> None:
        token = client.aisearch.tokens.read(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(TokenReadResponse, token, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: Cloudflare) -> None:
        response = client.aisearch.tokens.with_raw_response.read(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenReadResponse, token, path=["response"])

    @parametrize
    def test_streaming_response_read(self, client: Cloudflare) -> None:
        with client.aisearch.tokens.with_streaming_response.read(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenReadResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_read(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.tokens.with_raw_response.read(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.tokens.with_raw_response.read(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.aisearch.tokens.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            cf_api_id="cf_api_id",
            cf_api_key="cf_api_key",
            name="name",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.aisearch.tokens.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            cf_api_id="cf_api_id",
            cf_api_key="cf_api_key",
            name="name",
            legacy=True,
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.tokens.with_raw_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            cf_api_id="cf_api_id",
            cf_api_key="cf_api_key",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.tokens.with_streaming_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            cf_api_id="cf_api_id",
            cf_api_key="cf_api_key",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenCreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.tokens.with_raw_response.create(
                account_id="",
                cf_api_id="cf_api_id",
                cf_api_key="cf_api_key",
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.aisearch.tokens.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(TokenUpdateResponse, token, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.tokens.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenUpdateResponse, token, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.tokens.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenUpdateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.tokens.with_raw_response.update(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.tokens.with_raw_response.update(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.aisearch.tokens.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(AsyncV4PagePaginationArray[TokenListResponse], token, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.aisearch.tokens.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[TokenListResponse], token, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.tokens.with_raw_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[TokenListResponse], token, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.tokens.with_streaming_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[TokenListResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.tokens.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.aisearch.tokens.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(TokenDeleteResponse, token, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.tokens.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenDeleteResponse, token, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.tokens.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenDeleteResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.tokens.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.tokens.with_raw_response.delete(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    async def test_method_read(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.aisearch.tokens.read(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(TokenReadResponse, token, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.tokens.with_raw_response.read(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenReadResponse, token, path=["response"])

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.tokens.with_streaming_response.read(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenReadResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_read(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.tokens.with_raw_response.read(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.tokens.with_raw_response.read(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )
