# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..r2.buckets.provider import Provider

__all__ = [
    "InstanceCreateParams",
    "Metadata",
    "SourceParams",
    "SourceParamsWebCrawler",
    "SourceParamsWebCrawlerParseOptions",
    "SourceParamsWebCrawlerStoreOptions",
]


class InstanceCreateParams(TypedDict, total=False):
    account_id: Required[str]

    id: Required[str]
    """Use your AI Search ID."""

    source: Required[str]

    token_id: Required[str]

    type: Required[Literal["r2", "web-crawler"]]

    ai_gateway_id: str

    aisearch_model: Annotated[
        Literal[
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
        ],
        PropertyInfo(alias="ai_search_model"),
    ]

    chunk: bool

    chunk_overlap: int

    chunk_size: int

    embedding_model: Literal[
        "@cf/baai/bge-m3",
        "@cf/baai/bge-large-en-v1.5",
        "@cf/google/embeddinggemma-300m",
        "@cf/qwen/qwen3-embedding-0.6b",
        "google-ai-studio/gemini-embedding-001",
        "openai/text-embedding-3-small",
        "openai/text-embedding-3-large",
        "",
    ]

    max_num_results: int

    metadata: Metadata

    reranking: bool

    reranking_model: Literal["@cf/baai/bge-reranker-base", ""]

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

    rewrite_query: bool

    score_threshold: float

    source_params: SourceParams


class Metadata(TypedDict, total=False):
    created_from_aisearch_wizard: bool

    worker_domain: str


class SourceParamsWebCrawlerParseOptions(TypedDict, total=False):
    include_headers: Dict[str, str]

    include_images: bool

    use_browser_rendering: bool


class SourceParamsWebCrawlerStoreOptions(TypedDict, total=False):
    storage_id: Required[str]

    r2_jurisdiction: str

    storage_type: Provider


class SourceParamsWebCrawler(TypedDict, total=False):
    parse_options: SourceParamsWebCrawlerParseOptions

    parse_type: Literal["sitemap", "feed-rss"]

    store_options: SourceParamsWebCrawlerStoreOptions


class SourceParams(TypedDict, total=False):
    exclude_items: SequenceNotStr[str]
    """List of path patterns to exclude.

    Supports wildcards (e.g., _/admin/_, /private/\\**_, _\\pprivate\\**)
    """

    include_items: SequenceNotStr[str]
    """List of path patterns to include.

    Supports wildcards (e.g., _/blog/_.html, /docs/\\**_, _\blog\\**.html)
    """

    prefix: str

    r2_jurisdiction: str

    web_crawler: SourceParamsWebCrawler
