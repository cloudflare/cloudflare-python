# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.aisearch import (
    InstanceListResponse,
    InstanceReadResponse,
    InstanceStatsResponse,
    InstanceCreateResponse,
    InstanceDeleteResponse,
    InstanceSearchResponse,
    InstanceUpdateResponse,
    InstanceChatCompletionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
            source="source",
            type="r2",
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
            source="source",
            type="r2",
            ai_gateway_id="ai_gateway_id",
            aisearch_model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            chunk=True,
            chunk_overlap=0,
            chunk_size=64,
            custom_metadata=[
                {
                    "data_type": "text",
                    "field_name": "x",
                }
            ],
            embedding_model="@cf/qwen/qwen3-embedding-0.6b",
            hybrid_search_enabled=True,
            max_num_results=1,
            metadata={
                "created_from_aisearch_wizard": True,
                "worker_domain": "worker_domain",
            },
            public_endpoint_params={
                "authorized_hosts": ["string"],
                "chat_completions_endpoint": {"disabled": True},
                "enabled": True,
                "mcp": {"disabled": True},
                "rate_limit": {
                    "period_ms": 60000,
                    "requests": 1,
                    "technique": "fixed",
                },
                "search_endpoint": {"disabled": True},
            },
            reranking=True,
            reranking_model="@cf/baai/bge-reranker-base",
            rewrite_model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            rewrite_query=True,
            score_threshold=0,
            source_params={
                "exclude_items": ["/admin/**", "/private/**", "**\\temp\\**"],
                "include_items": ["/blog/**", "/docs/**/*.html", "**\\blog\\**.html"],
                "prefix": "prefix",
                "r2_jurisdiction": "r2_jurisdiction",
                "web_crawler": {
                    "parse_options": {
                        "include_headers": {"foo": "string"},
                        "include_images": True,
                        "specific_sitemaps": [
                            "https://example.com/sitemap.xml",
                            "https://example.com/blog-sitemap.xml",
                        ],
                        "use_browser_rendering": True,
                    },
                    "parse_type": "sitemap",
                    "store_options": {
                        "storage_id": "storage_id",
                        "r2_jurisdiction": "r2_jurisdiction",
                        "storage_type": "r2",
                    },
                },
            },
            token_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.aisearch.instances.with_raw_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
            source="source",
            type="r2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.aisearch.instances.with_streaming_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
            source="source",
            type="r2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceCreateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.instances.with_raw_response.create(
                account_id="",
                id="my-ai-search",
                source="source",
                type="r2",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            ai_gateway_id="ai_gateway_id",
            aisearch_model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            cache=True,
            cache_threshold="super_strict_match",
            chunk=True,
            chunk_overlap=0,
            chunk_size=64,
            custom_metadata=[
                {
                    "data_type": "text",
                    "field_name": "x",
                }
            ],
            embedding_model="@cf/qwen/qwen3-embedding-0.6b",
            hybrid_search_enabled=True,
            max_num_results=1,
            metadata={
                "created_from_aisearch_wizard": True,
                "worker_domain": "worker_domain",
            },
            paused=True,
            public_endpoint_params={
                "authorized_hosts": ["string"],
                "chat_completions_endpoint": {"disabled": True},
                "enabled": True,
                "mcp": {"disabled": True},
                "rate_limit": {
                    "period_ms": 60000,
                    "requests": 1,
                    "technique": "fixed",
                },
                "search_endpoint": {"disabled": True},
            },
            reranking=True,
            reranking_model="@cf/baai/bge-reranker-base",
            rewrite_model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            rewrite_query=True,
            score_threshold=0,
            source_params={
                "exclude_items": ["/admin/**", "/private/**", "**\\temp\\**"],
                "include_items": ["/blog/**", "/docs/**/*.html", "**\\blog\\**.html"],
                "prefix": "prefix",
                "r2_jurisdiction": "r2_jurisdiction",
                "web_crawler": {
                    "parse_options": {
                        "include_headers": {"foo": "string"},
                        "include_images": True,
                        "specific_sitemaps": [
                            "https://example.com/sitemap.xml",
                            "https://example.com/blog-sitemap.xml",
                        ],
                        "use_browser_rendering": True,
                    },
                    "parse_type": "sitemap",
                    "store_options": {
                        "storage_id": "storage_id",
                        "r2_jurisdiction": "r2_jurisdiction",
                        "storage_type": "r2",
                    },
                },
            },
            summarization=True,
            summarization_model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            system_prompt_aisearch="system_prompt_ai_search",
            system_prompt_index_summarization="system_prompt_index_summarization",
            system_prompt_rewrite_query="system_prompt_rewrite_query",
            token_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.aisearch.instances.with_raw_response.update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.aisearch.instances.with_streaming_response.update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.instances.with_raw_response.update(
                id="my-ai-search",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.instances.with_raw_response.update(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            page=1,
            per_page=1,
            search="search",
        )
        assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.aisearch.instances.with_raw_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.aisearch.instances.with_streaming_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.instances.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.delete(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.aisearch.instances.with_raw_response.delete(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.aisearch.instances.with_streaming_response.delete(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.instances.with_raw_response.delete(
                id="my-ai-search",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.instances.with_raw_response.delete(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    def test_method_chat_completions(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.chat_completions(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )
        assert_matches_type(InstanceChatCompletionsResponse, instance, path=["response"])

    @parametrize
    def test_method_chat_completions_with_all_params(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.chat_completions(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            aisearch_options={
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
                    "context_expansion": 0,
                    "filters": {
                        "key": "key",
                        "type": "eq",
                        "value": "string",
                    },
                    "match_threshold": 0,
                    "max_num_results": 1,
                    "retrieval_type": "vector",
                },
            },
            model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            stream=True,
        )
        assert_matches_type(InstanceChatCompletionsResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_chat_completions(self, client: Cloudflare) -> None:
        response = client.aisearch.instances.with_raw_response.chat_completions(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceChatCompletionsResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_chat_completions(self, client: Cloudflare) -> None:
        with client.aisearch.instances.with_streaming_response.chat_completions(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceChatCompletionsResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_chat_completions(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.instances.with_raw_response.chat_completions(
                id="my-ai-search",
                account_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.instances.with_raw_response.chat_completions(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

    @parametrize
    def test_method_read(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.read(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(InstanceReadResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: Cloudflare) -> None:
        response = client.aisearch.instances.with_raw_response.read(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceReadResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_read(self, client: Cloudflare) -> None:
        with client.aisearch.instances.with_streaming_response.read(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceReadResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_read(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.instances.with_raw_response.read(
                id="my-ai-search",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.instances.with_raw_response.read(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    def test_method_search(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.search(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )
        assert_matches_type(InstanceSearchResponse, instance, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.search(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            aisearch_options={
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
                    "context_expansion": 0,
                    "filters": {
                        "key": "key",
                        "type": "eq",
                        "value": "string",
                    },
                    "match_threshold": 0,
                    "max_num_results": 1,
                    "retrieval_type": "vector",
                },
            },
        )
        assert_matches_type(InstanceSearchResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Cloudflare) -> None:
        response = client.aisearch.instances.with_raw_response.search(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceSearchResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Cloudflare) -> None:
        with client.aisearch.instances.with_streaming_response.search(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceSearchResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.instances.with_raw_response.search(
                id="my-ai-search",
                account_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.instances.with_raw_response.search(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

    @parametrize
    def test_method_stats(self, client: Cloudflare) -> None:
        instance = client.aisearch.instances.stats(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(InstanceStatsResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_stats(self, client: Cloudflare) -> None:
        response = client.aisearch.instances.with_raw_response.stats(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceStatsResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_stats(self, client: Cloudflare) -> None:
        with client.aisearch.instances.with_streaming_response.stats(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceStatsResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stats(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.instances.with_raw_response.stats(
                id="my-ai-search",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.instances.with_raw_response.stats(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )


class TestAsyncInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
            source="source",
            type="r2",
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
            source="source",
            type="r2",
            ai_gateway_id="ai_gateway_id",
            aisearch_model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            chunk=True,
            chunk_overlap=0,
            chunk_size=64,
            custom_metadata=[
                {
                    "data_type": "text",
                    "field_name": "x",
                }
            ],
            embedding_model="@cf/qwen/qwen3-embedding-0.6b",
            hybrid_search_enabled=True,
            max_num_results=1,
            metadata={
                "created_from_aisearch_wizard": True,
                "worker_domain": "worker_domain",
            },
            public_endpoint_params={
                "authorized_hosts": ["string"],
                "chat_completions_endpoint": {"disabled": True},
                "enabled": True,
                "mcp": {"disabled": True},
                "rate_limit": {
                    "period_ms": 60000,
                    "requests": 1,
                    "technique": "fixed",
                },
                "search_endpoint": {"disabled": True},
            },
            reranking=True,
            reranking_model="@cf/baai/bge-reranker-base",
            rewrite_model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            rewrite_query=True,
            score_threshold=0,
            source_params={
                "exclude_items": ["/admin/**", "/private/**", "**\\temp\\**"],
                "include_items": ["/blog/**", "/docs/**/*.html", "**\\blog\\**.html"],
                "prefix": "prefix",
                "r2_jurisdiction": "r2_jurisdiction",
                "web_crawler": {
                    "parse_options": {
                        "include_headers": {"foo": "string"},
                        "include_images": True,
                        "specific_sitemaps": [
                            "https://example.com/sitemap.xml",
                            "https://example.com/blog-sitemap.xml",
                        ],
                        "use_browser_rendering": True,
                    },
                    "parse_type": "sitemap",
                    "store_options": {
                        "storage_id": "storage_id",
                        "r2_jurisdiction": "r2_jurisdiction",
                        "storage_type": "r2",
                    },
                },
            },
            token_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.instances.with_raw_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
            source="source",
            type="r2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.instances.with_streaming_response.create(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            id="my-ai-search",
            source="source",
            type="r2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceCreateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.create(
                account_id="",
                id="my-ai-search",
                source="source",
                type="r2",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            ai_gateway_id="ai_gateway_id",
            aisearch_model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            cache=True,
            cache_threshold="super_strict_match",
            chunk=True,
            chunk_overlap=0,
            chunk_size=64,
            custom_metadata=[
                {
                    "data_type": "text",
                    "field_name": "x",
                }
            ],
            embedding_model="@cf/qwen/qwen3-embedding-0.6b",
            hybrid_search_enabled=True,
            max_num_results=1,
            metadata={
                "created_from_aisearch_wizard": True,
                "worker_domain": "worker_domain",
            },
            paused=True,
            public_endpoint_params={
                "authorized_hosts": ["string"],
                "chat_completions_endpoint": {"disabled": True},
                "enabled": True,
                "mcp": {"disabled": True},
                "rate_limit": {
                    "period_ms": 60000,
                    "requests": 1,
                    "technique": "fixed",
                },
                "search_endpoint": {"disabled": True},
            },
            reranking=True,
            reranking_model="@cf/baai/bge-reranker-base",
            rewrite_model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            rewrite_query=True,
            score_threshold=0,
            source_params={
                "exclude_items": ["/admin/**", "/private/**", "**\\temp\\**"],
                "include_items": ["/blog/**", "/docs/**/*.html", "**\\blog\\**.html"],
                "prefix": "prefix",
                "r2_jurisdiction": "r2_jurisdiction",
                "web_crawler": {
                    "parse_options": {
                        "include_headers": {"foo": "string"},
                        "include_images": True,
                        "specific_sitemaps": [
                            "https://example.com/sitemap.xml",
                            "https://example.com/blog-sitemap.xml",
                        ],
                        "use_browser_rendering": True,
                    },
                    "parse_type": "sitemap",
                    "store_options": {
                        "storage_id": "storage_id",
                        "r2_jurisdiction": "r2_jurisdiction",
                        "storage_type": "r2",
                    },
                },
            },
            summarization=True,
            summarization_model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            system_prompt_aisearch="system_prompt_ai_search",
            system_prompt_index_summarization="system_prompt_index_summarization",
            system_prompt_rewrite_query="system_prompt_rewrite_query",
            token_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.instances.with_raw_response.update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.instances.with_streaming_response.update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.update(
                id="my-ai-search",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.update(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            page=1,
            per_page=1,
            search="search",
        )
        assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.instances.with_raw_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.instances.with_streaming_response.list(
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.delete(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.instances.with_raw_response.delete(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.instances.with_streaming_response.delete(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.delete(
                id="my-ai-search",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.delete(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    async def test_method_chat_completions(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.chat_completions(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )
        assert_matches_type(InstanceChatCompletionsResponse, instance, path=["response"])

    @parametrize
    async def test_method_chat_completions_with_all_params(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.chat_completions(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            aisearch_options={
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
                    "context_expansion": 0,
                    "filters": {
                        "key": "key",
                        "type": "eq",
                        "value": "string",
                    },
                    "match_threshold": 0,
                    "max_num_results": 1,
                    "retrieval_type": "vector",
                },
            },
            model="@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            stream=True,
        )
        assert_matches_type(InstanceChatCompletionsResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_chat_completions(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.instances.with_raw_response.chat_completions(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceChatCompletionsResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_chat_completions(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.instances.with_streaming_response.chat_completions(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceChatCompletionsResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_chat_completions(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.chat_completions(
                id="my-ai-search",
                account_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.chat_completions(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

    @parametrize
    async def test_method_read(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.read(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(InstanceReadResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.instances.with_raw_response.read(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceReadResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.instances.with_streaming_response.read(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceReadResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_read(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.read(
                id="my-ai-search",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.read(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.search(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )
        assert_matches_type(InstanceSearchResponse, instance, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.search(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            aisearch_options={
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
                    "context_expansion": 0,
                    "filters": {
                        "key": "key",
                        "type": "eq",
                        "value": "string",
                    },
                    "match_threshold": 0,
                    "max_num_results": 1,
                    "retrieval_type": "vector",
                },
            },
        )
        assert_matches_type(InstanceSearchResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.instances.with_raw_response.search(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceSearchResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.instances.with_streaming_response.search(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceSearchResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.search(
                id="my-ai-search",
                account_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.search(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                messages=[
                    {
                        "content": "content",
                        "role": "system",
                    }
                ],
            )

    @parametrize
    async def test_method_stats(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.aisearch.instances.stats(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )
        assert_matches_type(InstanceStatsResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_stats(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.instances.with_raw_response.stats(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceStatsResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_stats(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.instances.with_streaming_response.stats(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceStatsResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stats(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.stats(
                id="my-ai-search",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.instances.with_raw_response.stats(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            )
