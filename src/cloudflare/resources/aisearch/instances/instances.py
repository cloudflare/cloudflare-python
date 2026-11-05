# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Type, Iterable, Optional, cast
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
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        *,
        account_id: str,
        id: str,
        ai_gateway_id: Optional[str] | Omit = omit,
        aisearch_model: Optional[str] | Omit = omit,
        cache: bool | Omit = omit,
        cache_threshold: Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]
        | Omit = omit,
        cache_ttl: Literal[600, 1800, 3600, 7200, 21600, 43200, 86400, 172800, 259200, 518400] | Omit = omit,
        chunk: bool | Omit = omit,
        chunk_overlap: int | Omit = omit,
        chunk_size: int | Omit = omit,
        custom_metadata: Iterable[instance_create_params.CustomMetadata] | Omit = omit,
        embedding_model: Optional[str] | Omit = omit,
        fusion_method: Literal["max", "rrf"] | Omit = omit,
        hybrid_search_enabled: bool | Omit = omit,
        index_method: instance_create_params.IndexMethod | Omit = omit,
        indexing_options: Optional[instance_create_params.IndexingOptions] | Omit = omit,
        max_num_results: int | Omit = omit,
        metadata: instance_create_params.Metadata | Omit = omit,
        public_endpoint_params: instance_create_params.PublicEndpointParams | Omit = omit,
        reranking: bool | Omit = omit,
        reranking_model: Optional[str] | Omit = omit,
        retrieval_options: Optional[instance_create_params.RetrievalOptions] | Omit = omit,
        rewrite_model: Optional[str] | Omit = omit,
        rewrite_query: bool | Omit = omit,
        score_threshold: float | Omit = omit,
        source: Optional[str] | Omit = omit,
        source_params: Optional[instance_create_params.SourceParams] | Omit = omit,
        sync_interval: Literal[900, 1800, 3600, 7200, 14400, 21600, 43200, 86400] | Omit = omit,
        token_id: str | Omit = omit,
        type: Optional[Literal["r2", "web-crawler"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceCreateResponse:
        """Create a new AI Search instance with the given configuration.

        If type is omitted
        or null, a non-blank HTTP(S) source infers web-crawler and any other source
        infers r2; r2 sources must name an existing bucket. A missing or blank source
        without a type creates a managed upload-only instance.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          aisearch_model: A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
              Completions API. An empty string uses the configured or default model.

          cache_ttl: Cache entry TTL in seconds. Allowed values: 600 (10min), 1800 (30min), 3600
              (1h), 7200 (2h), 21600 (6h), 43200 (12h), 86400 (24h), 172800 (48h), 259200
              (72h), 518400 (6d).

          hybrid_search_enabled: Deprecated — use index_method instead. Defaults to true for new instances; set
              false to create a vector-only instance.

          index_method: Controls which storage backends indexing uses. Defaults to vector and keyword
              indexing for new instances. When set, both vector and keyword are required.

          rewrite_model: A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
              Completions API. An empty string uses the configured or default model.

          score_threshold: Minimum similarity score a chunk must reach to be returned. Defaults to 0.4.

          sync_interval: Interval between automatic syncs, in seconds. Allowed values: 900 (15min), 1800
              (30min), 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400 (24h).
              Defaults to 86400 (24h).

          type: Source type. When omitted or null with a non-blank source, HTTP(S) URLs infer
              web-crawler and existing R2 bucket names infer r2. A missing or blank source
              without a type uses managed upload-only storage.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/ai-search/instances", account_id=account_id),
            body=maybe_transform(
                {
                    "id": id,
                    "ai_gateway_id": ai_gateway_id,
                    "aisearch_model": aisearch_model,
                    "cache": cache,
                    "cache_threshold": cache_threshold,
                    "cache_ttl": cache_ttl,
                    "chunk": chunk,
                    "chunk_overlap": chunk_overlap,
                    "chunk_size": chunk_size,
                    "custom_metadata": custom_metadata,
                    "embedding_model": embedding_model,
                    "fusion_method": fusion_method,
                    "hybrid_search_enabled": hybrid_search_enabled,
                    "index_method": index_method,
                    "indexing_options": indexing_options,
                    "max_num_results": max_num_results,
                    "metadata": metadata,
                    "public_endpoint_params": public_endpoint_params,
                    "reranking": reranking,
                    "reranking_model": reranking_model,
                    "retrieval_options": retrieval_options,
                    "rewrite_model": rewrite_model,
                    "rewrite_query": rewrite_query,
                    "score_threshold": score_threshold,
                    "source": source,
                    "source_params": source_params,
                    "sync_interval": sync_interval,
                    "token_id": token_id,
                    "type": type,
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

    @typing_extensions.deprecated("deprecated")
    def update(
        self,
        id: str,
        *,
        account_id: str,
        ai_gateway_id: Optional[str] | Omit = omit,
        aisearch_model: Optional[str] | Omit = omit,
        cache: bool | Omit = omit,
        cache_threshold: Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]
        | Omit = omit,
        cache_ttl: Literal[600, 1800, 3600, 7200, 21600, 43200, 86400, 172800, 259200, 518400] | Omit = omit,
        chunk: bool | Omit = omit,
        chunk_overlap: int | Omit = omit,
        chunk_size: int | Omit = omit,
        custom_metadata: Iterable[instance_update_params.CustomMetadata] | Omit = omit,
        embedding_model: Optional[str] | Omit = omit,
        fusion_method: Literal["max", "rrf"] | Omit = omit,
        index_method: instance_update_params.IndexMethod | Omit = omit,
        indexing_options: Optional[instance_update_params.IndexingOptions] | Omit = omit,
        max_num_results: int | Omit = omit,
        metadata: instance_update_params.Metadata | Omit = omit,
        paused: bool | Omit = omit,
        public_endpoint_params: instance_update_params.PublicEndpointParams | Omit = omit,
        reranking: bool | Omit = omit,
        reranking_model: Optional[str] | Omit = omit,
        retrieval_options: Optional[instance_update_params.RetrievalOptions] | Omit = omit,
        rewrite_model: Optional[str] | Omit = omit,
        rewrite_query: bool | Omit = omit,
        score_threshold: float | Omit = omit,
        source: Optional[str] | Omit = omit,
        source_params: Optional[instance_update_params.SourceParams] | Omit = omit,
        summarization: bool | Omit = omit,
        summarization_model: Optional[str] | Omit = omit,
        sync_interval: Literal[900, 1800, 3600, 7200, 14400, 21600, 43200, 86400] | Omit = omit,
        system_prompt_aisearch: Optional[str] | Omit = omit,
        system_prompt_index_summarization: Optional[str] | Omit = omit,
        system_prompt_rewrite_query: Optional[str] | Omit = omit,
        token_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceUpdateResponse:
        """
        Updates the configuration of an AI Search instance.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          aisearch_model: A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
              Completions API. An empty string uses the configured or default model.

          cache_ttl: Cache entry TTL in seconds. Allowed values: 600 (10min), 1800 (30min), 3600
              (1h), 7200 (2h), 21600 (6h), 43200 (12h), 86400 (24h), 172800 (48h), 259200
              (72h), 518400 (6d).

          index_method: Controls which storage backends indexing uses. Defaults to vector and keyword
              indexing for new instances. When set, both vector and keyword are required.

          rewrite_model: A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
              Completions API. An empty string uses the configured or default model.

          score_threshold: Minimum similarity score a chunk must reach to be returned. Defaults to 0.4.

          sync_interval: Interval between automatic syncs, in seconds. Allowed values: 900 (15min), 1800
              (30min), 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400 (24h).
              Defaults to 86400 (24h).

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
            path_template("/accounts/{account_id}/ai-search/instances/{id}", account_id=account_id, id=id),
            body=maybe_transform(
                {
                    "ai_gateway_id": ai_gateway_id,
                    "aisearch_model": aisearch_model,
                    "cache": cache,
                    "cache_threshold": cache_threshold,
                    "cache_ttl": cache_ttl,
                    "chunk": chunk,
                    "chunk_overlap": chunk_overlap,
                    "chunk_size": chunk_size,
                    "custom_metadata": custom_metadata,
                    "embedding_model": embedding_model,
                    "fusion_method": fusion_method,
                    "index_method": index_method,
                    "indexing_options": indexing_options,
                    "max_num_results": max_num_results,
                    "metadata": metadata,
                    "paused": paused,
                    "public_endpoint_params": public_endpoint_params,
                    "reranking": reranking,
                    "reranking_model": reranking_model,
                    "retrieval_options": retrieval_options,
                    "rewrite_model": rewrite_model,
                    "rewrite_query": rewrite_query,
                    "score_threshold": score_threshold,
                    "source": source,
                    "source_params": source_params,
                    "summarization": summarization,
                    "summarization_model": summarization_model,
                    "sync_interval": sync_interval,
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

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        *,
        account_id: str,
        hostname: str | Omit = omit,
        namespace: str | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
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
        Lists all AI Search instances in the account.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          hostname: Return only instances with this exact Search for Agents hostname
              (case-insensitive).

          namespace: Return only instances in this namespace.

          order_by: Field to order results by.

          order_by_direction: Order direction.

          page: Page number (1-indexed).

          per_page: Number of results per page.

          search: Filter instances whose id contains this string (case-insensitive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/ai-search/instances", account_id=account_id),
            page=SyncV4PagePaginationArray[InstanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "hostname": hostname,
                        "namespace": namespace,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            model=InstanceListResponse,
        )

    @typing_extensions.deprecated("deprecated")
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
        Deletes an AI Search instance and all its indexed data permanently.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
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
            path_template("/accounts/{account_id}/ai-search/instances/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceDeleteResponse], ResultWrapper[InstanceDeleteResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def chat_completions(
        self,
        id: str,
        *,
        account_id: str,
        messages: Iterable[instance_chat_completions_params.Message],
        aisearch_options: instance_chat_completions_params.AISearchOptions | Omit = omit,
        model: str | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceChatCompletionsResponse:
        """
        Performs a chat completion request against an AI Search instance, using indexed
        content as context for generating responses.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          model: A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
              Completions API. An empty string uses the configured or default model.

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
            path_template(
                "/accounts/{account_id}/ai-search/instances/{id}/chat/completions", account_id=account_id, id=id
            ),
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

    @typing_extensions.deprecated("deprecated")
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
        Retrieve the configuration and status of an AI Search instance.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
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
            path_template("/accounts/{account_id}/ai-search/instances/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceReadResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceReadResponse], ResultWrapper[InstanceReadResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def search(
        self,
        id: str,
        *,
        account_id: str,
        aisearch_options: instance_search_params.AISearchOptions | Omit = omit,
        messages: Iterable[instance_search_params.Message] | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceSearchResponse:
        """
        Executes a semantic search query against an AI Search instance to find relevant
        indexed content.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          messages: OpenAI-compatible message array. For multimodal queries, set the last user
              message's `content` to an array of typed parts:
              `[{type:'text', text:'…'}, {type:'image_url', image_url:{url:'…'}}]`. Image
              inputs require the RAG's embedding_model to declare 'image' in
              supported_modalities.

          query: A simple text query string. Alternative to 'messages' — provide either this or
              'messages', not both.

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
            path_template("/accounts/{account_id}/ai-search/instances/{id}/search", account_id=account_id, id=id),
            body=maybe_transform(
                {
                    "aisearch_options": aisearch_options,
                    "messages": messages,
                    "query": query,
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

    @typing_extensions.deprecated("deprecated")
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
        Retrieve usage and indexing statistics for an AI Search instance.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

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
            path_template("/accounts/{account_id}/ai-search/instances/{id}/stats", account_id=account_id, id=id),
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

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        *,
        account_id: str,
        id: str,
        ai_gateway_id: Optional[str] | Omit = omit,
        aisearch_model: Optional[str] | Omit = omit,
        cache: bool | Omit = omit,
        cache_threshold: Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]
        | Omit = omit,
        cache_ttl: Literal[600, 1800, 3600, 7200, 21600, 43200, 86400, 172800, 259200, 518400] | Omit = omit,
        chunk: bool | Omit = omit,
        chunk_overlap: int | Omit = omit,
        chunk_size: int | Omit = omit,
        custom_metadata: Iterable[instance_create_params.CustomMetadata] | Omit = omit,
        embedding_model: Optional[str] | Omit = omit,
        fusion_method: Literal["max", "rrf"] | Omit = omit,
        hybrid_search_enabled: bool | Omit = omit,
        index_method: instance_create_params.IndexMethod | Omit = omit,
        indexing_options: Optional[instance_create_params.IndexingOptions] | Omit = omit,
        max_num_results: int | Omit = omit,
        metadata: instance_create_params.Metadata | Omit = omit,
        public_endpoint_params: instance_create_params.PublicEndpointParams | Omit = omit,
        reranking: bool | Omit = omit,
        reranking_model: Optional[str] | Omit = omit,
        retrieval_options: Optional[instance_create_params.RetrievalOptions] | Omit = omit,
        rewrite_model: Optional[str] | Omit = omit,
        rewrite_query: bool | Omit = omit,
        score_threshold: float | Omit = omit,
        source: Optional[str] | Omit = omit,
        source_params: Optional[instance_create_params.SourceParams] | Omit = omit,
        sync_interval: Literal[900, 1800, 3600, 7200, 14400, 21600, 43200, 86400] | Omit = omit,
        token_id: str | Omit = omit,
        type: Optional[Literal["r2", "web-crawler"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceCreateResponse:
        """Create a new AI Search instance with the given configuration.

        If type is omitted
        or null, a non-blank HTTP(S) source infers web-crawler and any other source
        infers r2; r2 sources must name an existing bucket. A missing or blank source
        without a type creates a managed upload-only instance.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          aisearch_model: A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
              Completions API. An empty string uses the configured or default model.

          cache_ttl: Cache entry TTL in seconds. Allowed values: 600 (10min), 1800 (30min), 3600
              (1h), 7200 (2h), 21600 (6h), 43200 (12h), 86400 (24h), 172800 (48h), 259200
              (72h), 518400 (6d).

          hybrid_search_enabled: Deprecated — use index_method instead. Defaults to true for new instances; set
              false to create a vector-only instance.

          index_method: Controls which storage backends indexing uses. Defaults to vector and keyword
              indexing for new instances. When set, both vector and keyword are required.

          rewrite_model: A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
              Completions API. An empty string uses the configured or default model.

          score_threshold: Minimum similarity score a chunk must reach to be returned. Defaults to 0.4.

          sync_interval: Interval between automatic syncs, in seconds. Allowed values: 900 (15min), 1800
              (30min), 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400 (24h).
              Defaults to 86400 (24h).

          type: Source type. When omitted or null with a non-blank source, HTTP(S) URLs infer
              web-crawler and existing R2 bucket names infer r2. A missing or blank source
              without a type uses managed upload-only storage.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/ai-search/instances", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "ai_gateway_id": ai_gateway_id,
                    "aisearch_model": aisearch_model,
                    "cache": cache,
                    "cache_threshold": cache_threshold,
                    "cache_ttl": cache_ttl,
                    "chunk": chunk,
                    "chunk_overlap": chunk_overlap,
                    "chunk_size": chunk_size,
                    "custom_metadata": custom_metadata,
                    "embedding_model": embedding_model,
                    "fusion_method": fusion_method,
                    "hybrid_search_enabled": hybrid_search_enabled,
                    "index_method": index_method,
                    "indexing_options": indexing_options,
                    "max_num_results": max_num_results,
                    "metadata": metadata,
                    "public_endpoint_params": public_endpoint_params,
                    "reranking": reranking,
                    "reranking_model": reranking_model,
                    "retrieval_options": retrieval_options,
                    "rewrite_model": rewrite_model,
                    "rewrite_query": rewrite_query,
                    "score_threshold": score_threshold,
                    "source": source,
                    "source_params": source_params,
                    "sync_interval": sync_interval,
                    "token_id": token_id,
                    "type": type,
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

    @typing_extensions.deprecated("deprecated")
    async def update(
        self,
        id: str,
        *,
        account_id: str,
        ai_gateway_id: Optional[str] | Omit = omit,
        aisearch_model: Optional[str] | Omit = omit,
        cache: bool | Omit = omit,
        cache_threshold: Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]
        | Omit = omit,
        cache_ttl: Literal[600, 1800, 3600, 7200, 21600, 43200, 86400, 172800, 259200, 518400] | Omit = omit,
        chunk: bool | Omit = omit,
        chunk_overlap: int | Omit = omit,
        chunk_size: int | Omit = omit,
        custom_metadata: Iterable[instance_update_params.CustomMetadata] | Omit = omit,
        embedding_model: Optional[str] | Omit = omit,
        fusion_method: Literal["max", "rrf"] | Omit = omit,
        index_method: instance_update_params.IndexMethod | Omit = omit,
        indexing_options: Optional[instance_update_params.IndexingOptions] | Omit = omit,
        max_num_results: int | Omit = omit,
        metadata: instance_update_params.Metadata | Omit = omit,
        paused: bool | Omit = omit,
        public_endpoint_params: instance_update_params.PublicEndpointParams | Omit = omit,
        reranking: bool | Omit = omit,
        reranking_model: Optional[str] | Omit = omit,
        retrieval_options: Optional[instance_update_params.RetrievalOptions] | Omit = omit,
        rewrite_model: Optional[str] | Omit = omit,
        rewrite_query: bool | Omit = omit,
        score_threshold: float | Omit = omit,
        source: Optional[str] | Omit = omit,
        source_params: Optional[instance_update_params.SourceParams] | Omit = omit,
        summarization: bool | Omit = omit,
        summarization_model: Optional[str] | Omit = omit,
        sync_interval: Literal[900, 1800, 3600, 7200, 14400, 21600, 43200, 86400] | Omit = omit,
        system_prompt_aisearch: Optional[str] | Omit = omit,
        system_prompt_index_summarization: Optional[str] | Omit = omit,
        system_prompt_rewrite_query: Optional[str] | Omit = omit,
        token_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceUpdateResponse:
        """
        Updates the configuration of an AI Search instance.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          aisearch_model: A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
              Completions API. An empty string uses the configured or default model.

          cache_ttl: Cache entry TTL in seconds. Allowed values: 600 (10min), 1800 (30min), 3600
              (1h), 7200 (2h), 21600 (6h), 43200 (12h), 86400 (24h), 172800 (48h), 259200
              (72h), 518400 (6d).

          index_method: Controls which storage backends indexing uses. Defaults to vector and keyword
              indexing for new instances. When set, both vector and keyword are required.

          rewrite_model: A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
              Completions API. An empty string uses the configured or default model.

          score_threshold: Minimum similarity score a chunk must reach to be returned. Defaults to 0.4.

          sync_interval: Interval between automatic syncs, in seconds. Allowed values: 900 (15min), 1800
              (30min), 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400 (24h).
              Defaults to 86400 (24h).

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
            path_template("/accounts/{account_id}/ai-search/instances/{id}", account_id=account_id, id=id),
            body=await async_maybe_transform(
                {
                    "ai_gateway_id": ai_gateway_id,
                    "aisearch_model": aisearch_model,
                    "cache": cache,
                    "cache_threshold": cache_threshold,
                    "cache_ttl": cache_ttl,
                    "chunk": chunk,
                    "chunk_overlap": chunk_overlap,
                    "chunk_size": chunk_size,
                    "custom_metadata": custom_metadata,
                    "embedding_model": embedding_model,
                    "fusion_method": fusion_method,
                    "index_method": index_method,
                    "indexing_options": indexing_options,
                    "max_num_results": max_num_results,
                    "metadata": metadata,
                    "paused": paused,
                    "public_endpoint_params": public_endpoint_params,
                    "reranking": reranking,
                    "reranking_model": reranking_model,
                    "retrieval_options": retrieval_options,
                    "rewrite_model": rewrite_model,
                    "rewrite_query": rewrite_query,
                    "score_threshold": score_threshold,
                    "source": source,
                    "source_params": source_params,
                    "summarization": summarization,
                    "summarization_model": summarization_model,
                    "sync_interval": sync_interval,
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

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        *,
        account_id: str,
        hostname: str | Omit = omit,
        namespace: str | Omit = omit,
        order_by: Literal["created_at"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
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
        Lists all AI Search instances in the account.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          hostname: Return only instances with this exact Search for Agents hostname
              (case-insensitive).

          namespace: Return only instances in this namespace.

          order_by: Field to order results by.

          order_by_direction: Order direction.

          page: Page number (1-indexed).

          per_page: Number of results per page.

          search: Filter instances whose id contains this string (case-insensitive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/ai-search/instances", account_id=account_id),
            page=AsyncV4PagePaginationArray[InstanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "hostname": hostname,
                        "namespace": namespace,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            model=InstanceListResponse,
        )

    @typing_extensions.deprecated("deprecated")
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
        Deletes an AI Search instance and all its indexed data permanently.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
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
            path_template("/accounts/{account_id}/ai-search/instances/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceDeleteResponse], ResultWrapper[InstanceDeleteResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def chat_completions(
        self,
        id: str,
        *,
        account_id: str,
        messages: Iterable[instance_chat_completions_params.Message],
        aisearch_options: instance_chat_completions_params.AISearchOptions | Omit = omit,
        model: str | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceChatCompletionsResponse:
        """
        Performs a chat completion request against an AI Search instance, using indexed
        content as context for generating responses.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          model: A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
              Completions API. An empty string uses the configured or default model.

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
            path_template(
                "/accounts/{account_id}/ai-search/instances/{id}/chat/completions", account_id=account_id, id=id
            ),
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

    @typing_extensions.deprecated("deprecated")
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
        Retrieve the configuration and status of an AI Search instance.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
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
            path_template("/accounts/{account_id}/ai-search/instances/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InstanceReadResponse]._unwrapper,
            ),
            cast_to=cast(Type[InstanceReadResponse], ResultWrapper[InstanceReadResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def search(
        self,
        id: str,
        *,
        account_id: str,
        aisearch_options: instance_search_params.AISearchOptions | Omit = omit,
        messages: Iterable[instance_search_params.Message] | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceSearchResponse:
        """
        Executes a semantic search query against an AI Search instance to find relevant
        indexed content.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          messages: OpenAI-compatible message array. For multimodal queries, set the last user
              message's `content` to an array of typed parts:
              `[{type:'text', text:'…'}, {type:'image_url', image_url:{url:'…'}}]`. Image
              inputs require the RAG's embedding_model to declare 'image' in
              supported_modalities.

          query: A simple text query string. Alternative to 'messages' — provide either this or
              'messages', not both.

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
            path_template("/accounts/{account_id}/ai-search/instances/{id}/search", account_id=account_id, id=id),
            body=await async_maybe_transform(
                {
                    "aisearch_options": aisearch_options,
                    "messages": messages,
                    "query": query,
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

    @typing_extensions.deprecated("deprecated")
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
        Retrieve usage and indexing statistics for an AI Search instance.

        Deprecated: use
        /accounts/{account_id}/ai-search/namespaces/{namespace}/instances (and
        descendant paths) instead.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

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
            path_template("/accounts/{account_id}/ai-search/instances/{id}/stats", account_id=account_id, id=id),
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

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                instances.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                instances.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                instances.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                instances.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.chat_completions = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                instances.chat_completions,  # pyright: ignore[reportDeprecated],
            )
        )
        self.read = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                instances.read,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                instances.search,  # pyright: ignore[reportDeprecated],
            )
        )
        self.stats = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                instances.stats,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._instances.jobs)


class AsyncInstancesResourceWithRawResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                instances.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                instances.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                instances.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                instances.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.chat_completions = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                instances.chat_completions,  # pyright: ignore[reportDeprecated],
            )
        )
        self.read = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                instances.read,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                instances.search,  # pyright: ignore[reportDeprecated],
            )
        )
        self.stats = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                instances.stats,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._instances.jobs)


class InstancesResourceWithStreamingResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                instances.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                instances.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                instances.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                instances.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.chat_completions = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                instances.chat_completions,  # pyright: ignore[reportDeprecated],
            )
        )
        self.read = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                instances.read,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                instances.search,  # pyright: ignore[reportDeprecated],
            )
        )
        self.stats = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                instances.stats,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._instances.jobs)


class AsyncInstancesResourceWithStreamingResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                instances.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                instances.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                instances.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                instances.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.chat_completions = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                instances.chat_completions,  # pyright: ignore[reportDeprecated],
            )
        )
        self.read = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                instances.read,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                instances.search,  # pyright: ignore[reportDeprecated],
            )
        )
        self.stats = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                instances.stats,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._instances.jobs)
