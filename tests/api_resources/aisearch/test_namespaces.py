# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.aisearch import (
    NamespaceListResponse,
    NamespaceReadResponse,
    NamespaceCreateResponse,
    NamespaceSearchResponse,
    NamespaceUpdateResponse,
    NamespaceChatCompletionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNamespaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="name",
        )
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="name",
            description="Production environment",
        )
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.with_raw_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.with_streaming_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.with_raw_response.create(
                account_id="",
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.update(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.update(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            description="Production environment",
        )
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.with_raw_response.update(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.with_streaming_response.update(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.with_raw_response.update(
                name="production",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.with_raw_response.update(
                name="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(SyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            page=1,
            per_page=20,
            search="prod",
        )
        assert_matches_type(SyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.with_raw_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.with_streaming_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.delete(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(object, namespace, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.with_raw_response.delete(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(object, namespace, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.with_streaming_response.delete(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(object, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.with_raw_response.delete(
                name="production",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.with_raw_response.delete(
                name="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    def test_method_chat_completions(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.chat_completions(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )
        assert_matches_type(NamespaceChatCompletionsResponse, namespace, path=["response"])

    @parametrize
    def test_method_chat_completions_with_all_params(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.chat_completions(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={
                "instance_ids": ["my-ai-search"],
                "cache": {
                    "cache_threshold": "super_strict_match",
                    "enabled": True,
                },
                "query_rewrite": {
                    "enabled": True,
                    "model": "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
                    "rewrite_prompt": "rewrite_prompt",
                },
                "reranking": {
                    "enabled": True,
                    "match_threshold": 0,
                    "model": "@cf/baai/bge-reranker-base",
                },
                "retrieval": {
                    "boost_by": [
                        {
                            "field": "timestamp",
                            "direction": "desc",
                        }
                    ],
                    "context_expansion": 0,
                    "filters": {"foo": "bar"},
                    "fusion_method": "max",
                    "keyword_match_mode": "and",
                    "match_threshold": 0,
                    "max_num_results": 1,
                    "retrieval_type": "vector",
                    "return_on_failure": True,
                },
            },
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            stream=True,
        )
        assert_matches_type(NamespaceChatCompletionsResponse, namespace, path=["response"])

    @parametrize
    def test_raw_response_chat_completions(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.with_raw_response.chat_completions(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceChatCompletionsResponse, namespace, path=["response"])

    @parametrize
    def test_streaming_response_chat_completions(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.with_streaming_response.chat_completions(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceChatCompletionsResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_chat_completions(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.with_raw_response.chat_completions(
                name="my-namespace",
                account_id="",
                aisearch_options={"instance_ids": ["my-ai-search"]},
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.with_raw_response.chat_completions(
                name="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                aisearch_options={"instance_ids": ["my-ai-search"]},
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

    @parametrize
    def test_method_read(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.read(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(NamespaceReadResponse, namespace, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.with_raw_response.read(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceReadResponse, namespace, path=["response"])

    @parametrize
    def test_streaming_response_read(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.with_streaming_response.read(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceReadResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_read(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.with_raw_response.read(
                name="production",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.with_raw_response.read(
                name="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    def test_method_search(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.search(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
        )
        assert_matches_type(NamespaceSearchResponse, namespace, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Cloudflare) -> None:
        namespace = client.aisearch.namespaces.search(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={
                "instance_ids": ["my-ai-search"],
                "cache": {
                    "cache_threshold": "super_strict_match",
                    "enabled": True,
                },
                "query_rewrite": {
                    "enabled": True,
                    "model": "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
                    "rewrite_prompt": "rewrite_prompt",
                },
                "reranking": {
                    "enabled": True,
                    "match_threshold": 0,
                    "model": "@cf/baai/bge-reranker-base",
                },
                "retrieval": {
                    "boost_by": [
                        {
                            "field": "timestamp",
                            "direction": "desc",
                        }
                    ],
                    "context_expansion": 0,
                    "filters": {"foo": "bar"},
                    "fusion_method": "max",
                    "keyword_match_mode": "and",
                    "match_threshold": 0,
                    "max_num_results": 1,
                    "retrieval_type": "vector",
                    "return_on_failure": True,
                },
            },
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            query="x",
        )
        assert_matches_type(NamespaceSearchResponse, namespace, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.with_raw_response.search(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceSearchResponse, namespace, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.with_streaming_response.search(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceSearchResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.with_raw_response.search(
                name="my-namespace",
                account_id="",
                aisearch_options={"instance_ids": ["my-ai-search"]},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.with_raw_response.search(
                name="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                aisearch_options={"instance_ids": ["my-ai-search"]},
            )


class TestAsyncNamespaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="name",
        )
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="name",
            description="Production environment",
        )
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.with_raw_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.with_streaming_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.create(
                account_id="",
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.update(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.update(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            description="Production environment",
        )
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.with_raw_response.update(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.with_streaming_response.update(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.update(
                name="production",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.update(
                name="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(AsyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            page=1,
            per_page=20,
            search="prod",
        )
        assert_matches_type(AsyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.with_raw_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.with_streaming_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.delete(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(object, namespace, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.with_raw_response.delete(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(object, namespace, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.with_streaming_response.delete(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(object, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.delete(
                name="production",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.delete(
                name="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    async def test_method_chat_completions(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.chat_completions(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )
        assert_matches_type(NamespaceChatCompletionsResponse, namespace, path=["response"])

    @parametrize
    async def test_method_chat_completions_with_all_params(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.chat_completions(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={
                "instance_ids": ["my-ai-search"],
                "cache": {
                    "cache_threshold": "super_strict_match",
                    "enabled": True,
                },
                "query_rewrite": {
                    "enabled": True,
                    "model": "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
                    "rewrite_prompt": "rewrite_prompt",
                },
                "reranking": {
                    "enabled": True,
                    "match_threshold": 0,
                    "model": "@cf/baai/bge-reranker-base",
                },
                "retrieval": {
                    "boost_by": [
                        {
                            "field": "timestamp",
                            "direction": "desc",
                        }
                    ],
                    "context_expansion": 0,
                    "filters": {"foo": "bar"},
                    "fusion_method": "max",
                    "keyword_match_mode": "and",
                    "match_threshold": 0,
                    "max_num_results": 1,
                    "retrieval_type": "vector",
                    "return_on_failure": True,
                },
            },
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            stream=True,
        )
        assert_matches_type(NamespaceChatCompletionsResponse, namespace, path=["response"])

    @parametrize
    async def test_raw_response_chat_completions(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.with_raw_response.chat_completions(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceChatCompletionsResponse, namespace, path=["response"])

    @parametrize
    async def test_streaming_response_chat_completions(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.with_streaming_response.chat_completions(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceChatCompletionsResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_chat_completions(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.chat_completions(
                name="my-namespace",
                account_id="",
                aisearch_options={"instance_ids": ["my-ai-search"]},
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.chat_completions(
                name="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                aisearch_options={"instance_ids": ["my-ai-search"]},
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

    @parametrize
    async def test_method_read(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.read(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(NamespaceReadResponse, namespace, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.with_raw_response.read(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceReadResponse, namespace, path=["response"])

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.with_streaming_response.read(
            name="production",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceReadResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_read(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.read(
                name="production",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.read(
                name="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.search(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
        )
        assert_matches_type(NamespaceSearchResponse, namespace, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.aisearch.namespaces.search(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={
                "instance_ids": ["my-ai-search"],
                "cache": {
                    "cache_threshold": "super_strict_match",
                    "enabled": True,
                },
                "query_rewrite": {
                    "enabled": True,
                    "model": "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
                    "rewrite_prompt": "rewrite_prompt",
                },
                "reranking": {
                    "enabled": True,
                    "match_threshold": 0,
                    "model": "@cf/baai/bge-reranker-base",
                },
                "retrieval": {
                    "boost_by": [
                        {
                            "field": "timestamp",
                            "direction": "desc",
                        }
                    ],
                    "context_expansion": 0,
                    "filters": {"foo": "bar"},
                    "fusion_method": "max",
                    "keyword_match_mode": "and",
                    "match_threshold": 0,
                    "max_num_results": 1,
                    "retrieval_type": "vector",
                    "return_on_failure": True,
                },
            },
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            query="x",
        )
        assert_matches_type(NamespaceSearchResponse, namespace, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.with_raw_response.search(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceSearchResponse, namespace, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.with_streaming_response.search(
            name="my-namespace",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            aisearch_options={"instance_ids": ["my-ai-search"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceSearchResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.search(
                name="my-namespace",
                account_id="",
                aisearch_options={"instance_ids": ["my-ai-search"]},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.with_raw_response.search(
                name="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                aisearch_options={"instance_ids": ["my-ai-search"]},
            )
