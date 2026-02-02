# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.aisearch import (
    instance_list_params,
    instance_create_params,
    instance_search_params,
    instance_update_params,
    instance_chat_completions_params,
)
from ....types.aisearch.instance_list_response import InstanceListResponse
from ....types.aisearch.instance_read_response import InstanceReadResponse
from ....types.aisearch.instance_stats_response import InstanceStatsResponse
from ....types.aisearch.instance_create_response import InstanceCreateResponse
from ....types.aisearch.instance_delete_response import InstanceDeleteResponse
from ....types.aisearch.instance_search_response import InstanceSearchResponse
from ....types.aisearch.instance_update_response import InstanceUpdateResponse
from ....types.aisearch.instance_chat_completions_response import InstanceChatCompletionsResponse

__all__ = ["InstancesResource", "AsyncInstancesResource"]


class InstancesResource(SyncAPIResource):
    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InstancesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        id: str,
        source: str,
        type: Literal["r2", "web-crawler"],
        ai_gateway_id: str | Omit = omit,
        aisearch_model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        chunk: bool | Omit = omit,
        chunk_overlap: int | Omit = omit,
        chunk_size: int | Omit = omit,
        custom_metadata: Iterable[instance_create_params.CustomMetadata] | Omit = omit,
        embedding_model: Literal[
            "@cf/qwen/qwen3-embedding-0.6b",
            "@cf/baai/bge-m3",
            "@cf/baai/bge-large-en-v1.5",
            "@cf/google/embeddinggemma-300m",
            "google-ai-studio/gemini-embedding-001",
            "openai/text-embedding-3-small",
            "openai/text-embedding-3-large",
            "",
        ]
        | Omit = omit,
        hybrid_search_enabled: bool | Omit = omit,
        max_num_results: int | Omit = omit,
        metadata: instance_create_params.Metadata | Omit = omit,
        public_endpoint_params: instance_create_params.PublicEndpointParams | Omit = omit,
        reranking: bool | Omit = omit,
        reranking_model: Literal["@cf/baai/bge-reranker-base", ""] | Omit = omit,
        rewrite_model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        rewrite_query: bool | Omit = omit,
        score_threshold: float | Omit = omit,
        source_params: instance_create_params.SourceParams | Omit = omit,
        token_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceCreateResponse:
        """
        Create new instances.

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/ai-search/instances",
            body=maybe_transform(
                {
                    "id": id,
                    "source": source,
                    "type": type,
                    "ai_gateway_id": ai_gateway_id,
                    "aisearch_model": aisearch_model,
                    "chunk": chunk,
                    "chunk_overlap": chunk_overlap,
                    "chunk_size": chunk_size,
                    "custom_metadata": custom_metadata,
                    "embedding_model": embedding_model,
                    "hybrid_search_enabled": hybrid_search_enabled,
                    "max_num_results": max_num_results,
                    "metadata": metadata,
                    "public_endpoint_params": public_endpoint_params,
                    "reranking": reranking,
                    "reranking_model": reranking_model,
                    "rewrite_model": rewrite_model,
                    "rewrite_query": rewrite_query,
                    "score_threshold": score_threshold,
                    "source_params": source_params,
                    "token_id": token_id,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceCreateResponse], ResultWrapper[InstanceCreateResponse]),
        )

    def update(
        self,
        id: str,
        *,
        account_id: str,
        ai_gateway_id: str | Omit = omit,
        aisearch_model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        cache: bool | Omit = omit,
        cache_threshold: Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]
        | Omit = omit,
        chunk: bool | Omit = omit,
        chunk_overlap: int | Omit = omit,
        chunk_size: int | Omit = omit,
        custom_metadata: Iterable[instance_update_params.CustomMetadata] | Omit = omit,
        embedding_model: Literal[
            "@cf/qwen/qwen3-embedding-0.6b",
            "@cf/baai/bge-m3",
            "@cf/baai/bge-large-en-v1.5",
            "@cf/google/embeddinggemma-300m",
            "google-ai-studio/gemini-embedding-001",
            "openai/text-embedding-3-small",
            "openai/text-embedding-3-large",
            "",
        ]
        | Omit = omit,
        hybrid_search_enabled: bool | Omit = omit,
        max_num_results: int | Omit = omit,
        metadata: instance_update_params.Metadata | Omit = omit,
        paused: bool | Omit = omit,
        public_endpoint_params: instance_update_params.PublicEndpointParams | Omit = omit,
        reranking: bool | Omit = omit,
        reranking_model: Literal["@cf/baai/bge-reranker-base", ""] | Omit = omit,
        rewrite_model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        rewrite_query: bool | Omit = omit,
        score_threshold: float | Omit = omit,
        source_params: instance_update_params.SourceParams | Omit = omit,
        summarization: bool | Omit = omit,
        summarization_model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        system_prompt_aisearch: str | Omit = omit,
        system_prompt_index_summarization: str | Omit = omit,
        system_prompt_rewrite_query: str | Omit = omit,
        token_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceUpdateResponse:
        """
        Update instances.

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/accounts/{account_id}/ai-search/instances/{id}",
            body=maybe_transform(
                {
                    "ai_gateway_id": ai_gateway_id,
                    "aisearch_model": aisearch_model,
                    "cache": cache,
                    "cache_threshold": cache_threshold,
                    "chunk": chunk,
                    "chunk_overlap": chunk_overlap,
                    "chunk_size": chunk_size,
                    "custom_metadata": custom_metadata,
                    "embedding_model": embedding_model,
                    "hybrid_search_enabled": hybrid_search_enabled,
                    "max_num_results": max_num_results,
                    "metadata": metadata,
                    "paused": paused,
                    "public_endpoint_params": public_endpoint_params,
                    "reranking": reranking,
                    "reranking_model": reranking_model,
                    "rewrite_model": rewrite_model,
                    "rewrite_query": rewrite_query,
                    "score_threshold": score_threshold,
                    "source_params": source_params,
                    "summarization": summarization,
                    "summarization_model": summarization_model,
                    "system_prompt_aisearch": system_prompt_aisearch,
                    "system_prompt_index_summarization": system_prompt_index_summarization,
                    "system_prompt_rewrite_query": system_prompt_rewrite_query,
                    "token_id": token_id,
                },
                instance_update_params.InstanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceUpdateResponse], ResultWrapper[InstanceUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[InstanceListResponse]:
        """
        List instances.

        Args:
          search: Search by id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai-search/instances",
            page=SyncV4PagePaginationArray[InstanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            model=InstanceListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceDeleteResponse:
        """
        Delete instances.

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/accounts/{account_id}/ai-search/instances/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceDeleteResponse], ResultWrapper[InstanceDeleteResponse]),
        )

    def chat_completions(
        self,
        id: str,
        *,
        account_id: str,
        messages: Iterable[instance_chat_completions_params.Message],
        aisearch_options: instance_chat_completions_params.AISearchOptions | Omit = omit,
        model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceChatCompletionsResponse:
        """
        Chat Completions

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/accounts/{account_id}/ai-search/instances/{id}/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "aisearch_options": aisearch_options,
                    "model": model,
                    "stream": stream,
                },
                instance_chat_completions_params.InstanceChatCompletionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceChatCompletionsResponse,
        )

    def read(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceReadResponse:
        """
        Read instances.

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-search/instances/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceReadResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceReadResponse], ResultWrapper[InstanceReadResponse]),
        )

    def search(
        self,
        id: str,
        *,
        account_id: str,
        messages: Iterable[instance_search_params.Message],
        aisearch_options: instance_search_params.AISearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceSearchResponse:
        """
        Search

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/accounts/{account_id}/ai-search/instances/{id}/search",
            body=maybe_transform(
                {
                    "messages": messages,
                    "aisearch_options": aisearch_options,
                },
                instance_search_params.InstanceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceSearchResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceSearchResponse], ResultWrapper[InstanceSearchResponse]),
        )

    def stats(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceStatsResponse:
        """
        Stats

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-search/instances/{id}/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceStatsResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceStatsResponse], ResultWrapper[InstanceStatsResponse]),
        )


class AsyncInstancesResource(AsyncAPIResource):
    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInstancesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        id: str,
        source: str,
        type: Literal["r2", "web-crawler"],
        ai_gateway_id: str | Omit = omit,
        aisearch_model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        chunk: bool | Omit = omit,
        chunk_overlap: int | Omit = omit,
        chunk_size: int | Omit = omit,
        custom_metadata: Iterable[instance_create_params.CustomMetadata] | Omit = omit,
        embedding_model: Literal[
            "@cf/qwen/qwen3-embedding-0.6b",
            "@cf/baai/bge-m3",
            "@cf/baai/bge-large-en-v1.5",
            "@cf/google/embeddinggemma-300m",
            "google-ai-studio/gemini-embedding-001",
            "openai/text-embedding-3-small",
            "openai/text-embedding-3-large",
            "",
        ]
        | Omit = omit,
        hybrid_search_enabled: bool | Omit = omit,
        max_num_results: int | Omit = omit,
        metadata: instance_create_params.Metadata | Omit = omit,
        public_endpoint_params: instance_create_params.PublicEndpointParams | Omit = omit,
        reranking: bool | Omit = omit,
        reranking_model: Literal["@cf/baai/bge-reranker-base", ""] | Omit = omit,
        rewrite_model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        rewrite_query: bool | Omit = omit,
        score_threshold: float | Omit = omit,
        source_params: instance_create_params.SourceParams | Omit = omit,
        token_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceCreateResponse:
        """
        Create new instances.

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/ai-search/instances",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "source": source,
                    "type": type,
                    "ai_gateway_id": ai_gateway_id,
                    "aisearch_model": aisearch_model,
                    "chunk": chunk,
                    "chunk_overlap": chunk_overlap,
                    "chunk_size": chunk_size,
                    "custom_metadata": custom_metadata,
                    "embedding_model": embedding_model,
                    "hybrid_search_enabled": hybrid_search_enabled,
                    "max_num_results": max_num_results,
                    "metadata": metadata,
                    "public_endpoint_params": public_endpoint_params,
                    "reranking": reranking,
                    "reranking_model": reranking_model,
                    "rewrite_model": rewrite_model,
                    "rewrite_query": rewrite_query,
                    "score_threshold": score_threshold,
                    "source_params": source_params,
                    "token_id": token_id,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceCreateResponse], ResultWrapper[InstanceCreateResponse]),
        )

    async def update(
        self,
        id: str,
        *,
        account_id: str,
        ai_gateway_id: str | Omit = omit,
        aisearch_model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        cache: bool | Omit = omit,
        cache_threshold: Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]
        | Omit = omit,
        chunk: bool | Omit = omit,
        chunk_overlap: int | Omit = omit,
        chunk_size: int | Omit = omit,
        custom_metadata: Iterable[instance_update_params.CustomMetadata] | Omit = omit,
        embedding_model: Literal[
            "@cf/qwen/qwen3-embedding-0.6b",
            "@cf/baai/bge-m3",
            "@cf/baai/bge-large-en-v1.5",
            "@cf/google/embeddinggemma-300m",
            "google-ai-studio/gemini-embedding-001",
            "openai/text-embedding-3-small",
            "openai/text-embedding-3-large",
            "",
        ]
        | Omit = omit,
        hybrid_search_enabled: bool | Omit = omit,
        max_num_results: int | Omit = omit,
        metadata: instance_update_params.Metadata | Omit = omit,
        paused: bool | Omit = omit,
        public_endpoint_params: instance_update_params.PublicEndpointParams | Omit = omit,
        reranking: bool | Omit = omit,
        reranking_model: Literal["@cf/baai/bge-reranker-base", ""] | Omit = omit,
        rewrite_model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        rewrite_query: bool | Omit = omit,
        score_threshold: float | Omit = omit,
        source_params: instance_update_params.SourceParams | Omit = omit,
        summarization: bool | Omit = omit,
        summarization_model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        system_prompt_aisearch: str | Omit = omit,
        system_prompt_index_summarization: str | Omit = omit,
        system_prompt_rewrite_query: str | Omit = omit,
        token_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceUpdateResponse:
        """
        Update instances.

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/accounts/{account_id}/ai-search/instances/{id}",
            body=await async_maybe_transform(
                {
                    "ai_gateway_id": ai_gateway_id,
                    "aisearch_model": aisearch_model,
                    "cache": cache,
                    "cache_threshold": cache_threshold,
                    "chunk": chunk,
                    "chunk_overlap": chunk_overlap,
                    "chunk_size": chunk_size,
                    "custom_metadata": custom_metadata,
                    "embedding_model": embedding_model,
                    "hybrid_search_enabled": hybrid_search_enabled,
                    "max_num_results": max_num_results,
                    "metadata": metadata,
                    "paused": paused,
                    "public_endpoint_params": public_endpoint_params,
                    "reranking": reranking,
                    "reranking_model": reranking_model,
                    "rewrite_model": rewrite_model,
                    "rewrite_query": rewrite_query,
                    "score_threshold": score_threshold,
                    "source_params": source_params,
                    "summarization": summarization,
                    "summarization_model": summarization_model,
                    "system_prompt_aisearch": system_prompt_aisearch,
                    "system_prompt_index_summarization": system_prompt_index_summarization,
                    "system_prompt_rewrite_query": system_prompt_rewrite_query,
                    "token_id": token_id,
                },
                instance_update_params.InstanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceUpdateResponse], ResultWrapper[InstanceUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InstanceListResponse, AsyncV4PagePaginationArray[InstanceListResponse]]:
        """
        List instances.

        Args:
          search: Search by id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai-search/instances",
            page=AsyncV4PagePaginationArray[InstanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            model=InstanceListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceDeleteResponse:
        """
        Delete instances.

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/accounts/{account_id}/ai-search/instances/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceDeleteResponse], ResultWrapper[InstanceDeleteResponse]),
        )

    async def chat_completions(
        self,
        id: str,
        *,
        account_id: str,
        messages: Iterable[instance_chat_completions_params.Message],
        aisearch_options: instance_chat_completions_params.AISearchOptions | Omit = omit,
        model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "anthropic/claude-3-7-sonnet",
            "anthropic/claude-sonnet-4",
            "anthropic/claude-opus-4",
            "anthropic/claude-3-5-haiku",
            "cerebras/qwen-3-235b-a22b-instruct",
            "cerebras/qwen-3-235b-a22b-thinking",
            "cerebras/llama-3.3-70b",
            "cerebras/llama-4-maverick-17b-128e-instruct",
            "cerebras/llama-4-scout-17b-16e-instruct",
            "cerebras/gpt-oss-120b",
            "google-ai-studio/gemini-2.5-flash",
            "google-ai-studio/gemini-2.5-pro",
            "grok/grok-4",
            "groq/llama-3.3-70b-versatile",
            "groq/llama-3.1-8b-instant",
            "openai/gpt-5",
            "openai/gpt-5-mini",
            "openai/gpt-5-nano",
            "",
        ]
        | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceChatCompletionsResponse:
        """
        Chat Completions

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/accounts/{account_id}/ai-search/instances/{id}/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "aisearch_options": aisearch_options,
                    "model": model,
                    "stream": stream,
                },
                instance_chat_completions_params.InstanceChatCompletionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceChatCompletionsResponse,
        )

    async def read(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceReadResponse:
        """
        Read instances.

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-search/instances/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceReadResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceReadResponse], ResultWrapper[InstanceReadResponse]),
        )

    async def search(
        self,
        id: str,
        *,
        account_id: str,
        messages: Iterable[instance_search_params.Message],
        aisearch_options: instance_search_params.AISearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceSearchResponse:
        """
        Search

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/accounts/{account_id}/ai-search/instances/{id}/search",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "aisearch_options": aisearch_options,
                },
                instance_search_params.InstanceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceSearchResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceSearchResponse], ResultWrapper[InstanceSearchResponse]),
        )

    async def stats(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceStatsResponse:
        """
        Stats

        Args:
          id: Use your AI Search ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-search/instances/{id}/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceStatsResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceStatsResponse], ResultWrapper[InstanceStatsResponse]),
        )


class InstancesResourceWithRawResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.create = to_raw_response_wrapper(
            instances.create,
        )
        self.update = to_raw_response_wrapper(
            instances.update,
        )
        self.list = to_raw_response_wrapper(
            instances.list,
        )
        self.delete = to_raw_response_wrapper(
            instances.delete,
        )
        self.chat_completions = to_raw_response_wrapper(
            instances.chat_completions,
        )
        self.read = to_raw_response_wrapper(
            instances.read,
        )
        self.search = to_raw_response_wrapper(
            instances.search,
        )
        self.stats = to_raw_response_wrapper(
            instances.stats,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._instances.items)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._instances.jobs)


class AsyncInstancesResourceWithRawResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = async_to_raw_response_wrapper(
            instances.create,
        )
        self.update = async_to_raw_response_wrapper(
            instances.update,
        )
        self.list = async_to_raw_response_wrapper(
            instances.list,
        )
        self.delete = async_to_raw_response_wrapper(
            instances.delete,
        )
        self.chat_completions = async_to_raw_response_wrapper(
            instances.chat_completions,
        )
        self.read = async_to_raw_response_wrapper(
            instances.read,
        )
        self.search = async_to_raw_response_wrapper(
            instances.search,
        )
        self.stats = async_to_raw_response_wrapper(
            instances.stats,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._instances.items)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._instances.jobs)


class InstancesResourceWithStreamingResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.create = to_streamed_response_wrapper(
            instances.create,
        )
        self.update = to_streamed_response_wrapper(
            instances.update,
        )
        self.list = to_streamed_response_wrapper(
            instances.list,
        )
        self.delete = to_streamed_response_wrapper(
            instances.delete,
        )
        self.chat_completions = to_streamed_response_wrapper(
            instances.chat_completions,
        )
        self.read = to_streamed_response_wrapper(
            instances.read,
        )
        self.search = to_streamed_response_wrapper(
            instances.search,
        )
        self.stats = to_streamed_response_wrapper(
            instances.stats,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._instances.items)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._instances.jobs)


class AsyncInstancesResourceWithStreamingResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = async_to_streamed_response_wrapper(
            instances.create,
        )
        self.update = async_to_streamed_response_wrapper(
            instances.update,
        )
        self.list = async_to_streamed_response_wrapper(
            instances.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            instances.delete,
        )
        self.chat_completions = async_to_streamed_response_wrapper(
            instances.chat_completions,
        )
        self.read = async_to_streamed_response_wrapper(
            instances.read,
        )
        self.search = async_to_streamed_response_wrapper(
            instances.search,
        )
        self.stats = async_to_streamed_response_wrapper(
            instances.stats,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._instances.items)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._instances.jobs)
