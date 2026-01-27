# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "InstanceChatCompletionsParams",
    "Message",
    "AISearchOptions",
    "AISearchOptionsQueryRewrite",
    "AISearchOptionsReranking",
    "AISearchOptionsRetrieval",
    "AISearchOptionsRetrievalFilters",
    "AISearchOptionsRetrievalFiltersUnionMember0",
    "AISearchOptionsRetrievalFiltersUnionMember1",
    "AISearchOptionsRetrievalFiltersUnionMember1Filter",
]


class InstanceChatCompletionsParams(TypedDict, total=False):
    account_id: Required[str]

    messages: Required[Iterable[Message]]

    aisearch_options: Annotated[AISearchOptions, PropertyInfo(alias="ai_search_options")]

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

    stream: bool


class MessageTyped(TypedDict, total=False):
    content: Required[Optional[str]]

    role: Required[Literal["system", "developer", "user", "assistant", "tool"]]


Message: TypeAlias = Union[MessageTyped, Dict[str, object]]


class AISearchOptionsQueryRewrite(TypedDict, total=False):
    enabled: bool

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

    rewrite_prompt: str


class AISearchOptionsReranking(TypedDict, total=False):
    enabled: bool

    match_threshold: float

    model: Literal["@cf/baai/bge-reranker-base", ""]


class AISearchOptionsRetrievalFiltersUnionMember0(TypedDict, total=False):
    key: Required[str]

    type: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte"]]

    value: Required[Union[str, float, bool]]


class AISearchOptionsRetrievalFiltersUnionMember1Filter(TypedDict, total=False):
    key: Required[str]

    type: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte"]]

    value: Required[Union[str, float, bool]]


class AISearchOptionsRetrievalFiltersUnionMember1(TypedDict, total=False):
    filters: Required[Iterable[AISearchOptionsRetrievalFiltersUnionMember1Filter]]

    type: Required[Literal["and", "or"]]


AISearchOptionsRetrievalFilters: TypeAlias = Union[
    AISearchOptionsRetrievalFiltersUnionMember0, AISearchOptionsRetrievalFiltersUnionMember1
]


class AISearchOptionsRetrieval(TypedDict, total=False):
    context_expansion: int

    filters: AISearchOptionsRetrievalFilters

    match_threshold: float

    max_num_results: int

    retrieval_type: Literal["vector", "keyword", "hybrid"]


class AISearchOptions(TypedDict, total=False):
    query_rewrite: AISearchOptionsQueryRewrite

    reranking: AISearchOptionsReranking

    retrieval: AISearchOptionsRetrieval
