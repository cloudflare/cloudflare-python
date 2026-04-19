# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

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
    namespace_list_params,
    namespace_create_params,
    namespace_search_params,
    namespace_update_params,
    namespace_chat_completions_params,
)
from .instances.instances import (
    InstancesResource,
    AsyncInstancesResource,
    InstancesResourceWithRawResponse,
    AsyncInstancesResourceWithRawResponse,
    InstancesResourceWithStreamingResponse,
    AsyncInstancesResourceWithStreamingResponse,
)
from ....types.aisearch.namespace_list_response import NamespaceListResponse
from ....types.aisearch.namespace_read_response import NamespaceReadResponse
from ....types.aisearch.namespace_create_response import NamespaceCreateResponse
from ....types.aisearch.namespace_search_response import NamespaceSearchResponse
from ....types.aisearch.namespace_update_response import NamespaceUpdateResponse
from ....types.aisearch.namespace_chat_completions_response import NamespaceChatCompletionsResponse

__all__ = ["NamespacesResource", "AsyncNamespacesResource"]


class NamespacesResource(SyncAPIResource):
    @cached_property
    def instances(self) -> InstancesResource:
        return InstancesResource(self._client)

    @cached_property
    def with_raw_response(self) -> NamespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return NamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return NamespacesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str | None = None,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceCreateResponse:
        """
        Create a new namespace.

        Args:
          description: Optional description for the namespace. Max 256 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/ai-search/namespaces", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                namespace_create_params.NamespaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NamespaceCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[NamespaceCreateResponse], ResultWrapper[NamespaceCreateResponse]),
        )

    def update(
        self,
        name: str,
        *,
        account_id: str | None = None,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceUpdateResponse:
        """Update namespace.

        Args:
          description: Optional description for the namespace.

        Max 256 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._put(
            path_template("/accounts/{account_id}/ai-search/namespaces/{name}", account_id=account_id, name=name),
            body=maybe_transform({"description": description}, namespace_update_params.NamespaceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NamespaceUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[NamespaceUpdateResponse], ResultWrapper[NamespaceUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | None = None,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[NamespaceListResponse]:
        """
        List namespaces.

        Args:
          page: Page number (1-indexed).

          per_page: Number of results per page.

          search: Filter namespaces whose name or description contains this string
              (case-insensitive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/ai-search/namespaces", account_id=account_id),
            page=SyncV4PagePaginationArray[NamespaceListResponse],
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
                    namespace_list_params.NamespaceListParams,
                ),
            ),
            model=NamespaceListResponse,
        )

    def delete(
        self,
        name: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete namespace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._delete(
            path_template("/accounts/{account_id}/ai-search/namespaces/{name}", account_id=account_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def chat_completions(
        self,
        name: str,
        *,
        account_id: str | None = None,
        aisearch_options: namespace_chat_completions_params.AISearchOptions,
        messages: Iterable[namespace_chat_completions_params.Message],
        model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/zai-org/glm-4.7-flash",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "@cf/google/gemma-3-12b-it",
            "@cf/google/gemma-4-26b-a4b-it",
            "@cf/moonshotai/kimi-k2.5",
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
    ) -> NamespaceChatCompletionsResponse:
        """
        Performs a chat completion request against multiple AI Search instances in
        parallel, merging retrieved content as context for generating a response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/chat/completions", account_id=account_id, name=name
            ),
            body=maybe_transform(
                {
                    "aisearch_options": aisearch_options,
                    "messages": messages,
                    "model": model,
                    "stream": stream,
                },
                namespace_chat_completions_params.NamespaceChatCompletionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceChatCompletionsResponse,
        )

    def read(
        self,
        name: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceReadResponse:
        """
        Read namespace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/accounts/{account_id}/ai-search/namespaces/{name}", account_id=account_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NamespaceReadResponse]._unwrapper,
            ),
            cast_to=cast(Type[NamespaceReadResponse], ResultWrapper[NamespaceReadResponse]),
        )

    def search(
        self,
        name: str,
        *,
        account_id: str | None = None,
        aisearch_options: namespace_search_params.AISearchOptions,
        messages: Iterable[namespace_search_params.Message] | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceSearchResponse:
        """Multi-Instance Search

        Args:
          query: A simple text query string.

        Alternative to 'messages' — provide either this or
              'messages', not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/search", account_id=account_id, name=name
            ),
            body=maybe_transform(
                {
                    "aisearch_options": aisearch_options,
                    "messages": messages,
                    "query": query,
                },
                namespace_search_params.NamespaceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NamespaceSearchResponse]._unwrapper,
            ),
            cast_to=cast(Type[NamespaceSearchResponse], ResultWrapper[NamespaceSearchResponse]),
        )


class AsyncNamespacesResource(AsyncAPIResource):
    @cached_property
    def instances(self) -> AsyncInstancesResource:
        return AsyncInstancesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncNamespacesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str | None = None,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceCreateResponse:
        """
        Create a new namespace.

        Args:
          description: Optional description for the namespace. Max 256 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/ai-search/namespaces", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                namespace_create_params.NamespaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NamespaceCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[NamespaceCreateResponse], ResultWrapper[NamespaceCreateResponse]),
        )

    async def update(
        self,
        name: str,
        *,
        account_id: str | None = None,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceUpdateResponse:
        """Update namespace.

        Args:
          description: Optional description for the namespace.

        Max 256 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._put(
            path_template("/accounts/{account_id}/ai-search/namespaces/{name}", account_id=account_id, name=name),
            body=await async_maybe_transform(
                {"description": description}, namespace_update_params.NamespaceUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NamespaceUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[NamespaceUpdateResponse], ResultWrapper[NamespaceUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | None = None,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NamespaceListResponse, AsyncV4PagePaginationArray[NamespaceListResponse]]:
        """
        List namespaces.

        Args:
          page: Page number (1-indexed).

          per_page: Number of results per page.

          search: Filter namespaces whose name or description contains this string
              (case-insensitive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/ai-search/namespaces", account_id=account_id),
            page=AsyncV4PagePaginationArray[NamespaceListResponse],
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
                    namespace_list_params.NamespaceListParams,
                ),
            ),
            model=NamespaceListResponse,
        )

    async def delete(
        self,
        name: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete namespace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._delete(
            path_template("/accounts/{account_id}/ai-search/namespaces/{name}", account_id=account_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def chat_completions(
        self,
        name: str,
        *,
        account_id: str | None = None,
        aisearch_options: namespace_chat_completions_params.AISearchOptions,
        messages: Iterable[namespace_chat_completions_params.Message],
        model: Literal[
            "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "@cf/zai-org/glm-4.7-flash",
            "@cf/meta/llama-3.1-8b-instruct-fast",
            "@cf/meta/llama-3.1-8b-instruct-fp8",
            "@cf/meta/llama-4-scout-17b-16e-instruct",
            "@cf/qwen/qwen3-30b-a3b-fp8",
            "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "@cf/moonshotai/kimi-k2-instruct",
            "@cf/google/gemma-3-12b-it",
            "@cf/google/gemma-4-26b-a4b-it",
            "@cf/moonshotai/kimi-k2.5",
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
    ) -> NamespaceChatCompletionsResponse:
        """
        Performs a chat completion request against multiple AI Search instances in
        parallel, merging retrieved content as context for generating a response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/chat/completions", account_id=account_id, name=name
            ),
            body=await async_maybe_transform(
                {
                    "aisearch_options": aisearch_options,
                    "messages": messages,
                    "model": model,
                    "stream": stream,
                },
                namespace_chat_completions_params.NamespaceChatCompletionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceChatCompletionsResponse,
        )

    async def read(
        self,
        name: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceReadResponse:
        """
        Read namespace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/accounts/{account_id}/ai-search/namespaces/{name}", account_id=account_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NamespaceReadResponse]._unwrapper,
            ),
            cast_to=cast(Type[NamespaceReadResponse], ResultWrapper[NamespaceReadResponse]),
        )

    async def search(
        self,
        name: str,
        *,
        account_id: str | None = None,
        aisearch_options: namespace_search_params.AISearchOptions,
        messages: Iterable[namespace_search_params.Message] | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceSearchResponse:
        """Multi-Instance Search

        Args:
          query: A simple text query string.

        Alternative to 'messages' — provide either this or
              'messages', not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/search", account_id=account_id, name=name
            ),
            body=await async_maybe_transform(
                {
                    "aisearch_options": aisearch_options,
                    "messages": messages,
                    "query": query,
                },
                namespace_search_params.NamespaceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NamespaceSearchResponse]._unwrapper,
            ),
            cast_to=cast(Type[NamespaceSearchResponse], ResultWrapper[NamespaceSearchResponse]),
        )


class NamespacesResourceWithRawResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = to_raw_response_wrapper(
            namespaces.create,
        )
        self.update = to_raw_response_wrapper(
            namespaces.update,
        )
        self.list = to_raw_response_wrapper(
            namespaces.list,
        )
        self.delete = to_raw_response_wrapper(
            namespaces.delete,
        )
        self.chat_completions = to_raw_response_wrapper(
            namespaces.chat_completions,
        )
        self.read = to_raw_response_wrapper(
            namespaces.read,
        )
        self.search = to_raw_response_wrapper(
            namespaces.search,
        )

    @cached_property
    def instances(self) -> InstancesResourceWithRawResponse:
        return InstancesResourceWithRawResponse(self._namespaces.instances)


class AsyncNamespacesResourceWithRawResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = async_to_raw_response_wrapper(
            namespaces.create,
        )
        self.update = async_to_raw_response_wrapper(
            namespaces.update,
        )
        self.list = async_to_raw_response_wrapper(
            namespaces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            namespaces.delete,
        )
        self.chat_completions = async_to_raw_response_wrapper(
            namespaces.chat_completions,
        )
        self.read = async_to_raw_response_wrapper(
            namespaces.read,
        )
        self.search = async_to_raw_response_wrapper(
            namespaces.search,
        )

    @cached_property
    def instances(self) -> AsyncInstancesResourceWithRawResponse:
        return AsyncInstancesResourceWithRawResponse(self._namespaces.instances)


class NamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = to_streamed_response_wrapper(
            namespaces.create,
        )
        self.update = to_streamed_response_wrapper(
            namespaces.update,
        )
        self.list = to_streamed_response_wrapper(
            namespaces.list,
        )
        self.delete = to_streamed_response_wrapper(
            namespaces.delete,
        )
        self.chat_completions = to_streamed_response_wrapper(
            namespaces.chat_completions,
        )
        self.read = to_streamed_response_wrapper(
            namespaces.read,
        )
        self.search = to_streamed_response_wrapper(
            namespaces.search,
        )

    @cached_property
    def instances(self) -> InstancesResourceWithStreamingResponse:
        return InstancesResourceWithStreamingResponse(self._namespaces.instances)


class AsyncNamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = async_to_streamed_response_wrapper(
            namespaces.create,
        )
        self.update = async_to_streamed_response_wrapper(
            namespaces.update,
        )
        self.list = async_to_streamed_response_wrapper(
            namespaces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            namespaces.delete,
        )
        self.chat_completions = async_to_streamed_response_wrapper(
            namespaces.chat_completions,
        )
        self.read = async_to_streamed_response_wrapper(
            namespaces.read,
        )
        self.search = async_to_streamed_response_wrapper(
            namespaces.search,
        )

    @cached_property
    def instances(self) -> AsyncInstancesResourceWithStreamingResponse:
        return AsyncInstancesResourceWithStreamingResponse(self._namespaces.instances)
