# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "NamespaceChatCompletionsParams",
    "AISearchOptions",
    "AISearchOptionsCache",
    "AISearchOptionsQueryRewrite",
    "AISearchOptionsReranking",
    "AISearchOptionsRetrieval",
    "AISearchOptionsRetrievalBoostBy",
    "Message",
]


class NamespaceChatCompletionsParams(TypedDict, total=False):
    account_id: str

    aisearch_options: Required[Annotated[AISearchOptions, PropertyInfo(alias="ai_search_options")]]

    messages: Required[Iterable[Message]]

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

    stream: bool


class AISearchOptionsCache(TypedDict, total=False):
    cache_threshold: Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]

    enabled: bool


class AISearchOptionsQueryRewrite(TypedDict, total=False):
    enabled: bool

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

    rewrite_prompt: str


class AISearchOptionsReranking(TypedDict, total=False):
    enabled: bool

    match_threshold: float

    model: Literal["@cf/baai/bge-reranker-base", ""]


class AISearchOptionsRetrievalBoostBy(TypedDict, total=False):
    field: Required[str]
    """Metadata field name to boost by.

    Use 'timestamp' for document freshness, or any custom_metadata field. Numeric
    and datetime fields support asc/desc directions; text/boolean fields support
    exists/not_exists.
    """

    direction: Literal["asc", "desc", "exists", "not_exists"]
    """Boost direction.

    'desc' = higher values rank higher (e.g. newer timestamps). 'asc' = lower values
    rank higher. 'exists' = boost chunks that have the field. 'not_exists' = boost
    chunks that lack the field. Optional ��� defaults to 'asc' for numeric/datetime
    fields, 'exists' for text/boolean fields.
    """


class AISearchOptionsRetrieval(TypedDict, total=False):
    boost_by: Iterable[AISearchOptionsRetrievalBoostBy]
    """Metadata fields to boost search results by.

    Overrides the instance-level boost_by config. Direction defaults to 'asc' for
    numeric/datetime fields, 'exists' for text/boolean fields. Fields must match
    'timestamp' or a defined custom_metadata field.
    """

    context_expansion: int

    filters: Dict[str, object]

    fusion_method: Literal["max", "rrf"]

    keyword_match_mode: Literal["and", "or"]
    """Controls which documents are candidates for BM25 scoring.

    'and' restricts candidates to documents containing all query terms; 'or'
    includes any document containing at least one term, ranked by BM25 relevance.
    Defaults to 'and'.
    """

    match_threshold: float

    max_num_results: int

    retrieval_type: Literal["vector", "keyword", "hybrid"]

    return_on_failure: bool


class AISearchOptions(TypedDict, total=False):
    instance_ids: Required[SequenceNotStr[str]]

    cache: AISearchOptionsCache

    query_rewrite: AISearchOptionsQueryRewrite

    reranking: AISearchOptionsReranking

    retrieval: AISearchOptionsRetrieval


class Message(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    content: Required[Optional[str]]

    role: Required[Literal["system", "developer", "user", "assistant", "tool"]]
