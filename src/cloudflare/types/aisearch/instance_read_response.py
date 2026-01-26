# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..r2.buckets.provider import Provider

__all__ = [
    "InstanceReadResponse",
    "Metadata",
    "PublicEndpointParams",
    "PublicEndpointParamsChatCompletionsEndpoint",
    "PublicEndpointParamsMcp",
    "PublicEndpointParamsRateLimit",
    "PublicEndpointParamsSearchEndpoint",
    "SourceParams",
    "SourceParamsWebCrawler",
    "SourceParamsWebCrawlerParseOptions",
    "SourceParamsWebCrawlerStoreOptions",
]


class Metadata(BaseModel):
    created_from_aisearch_wizard: Optional[bool] = None

    worker_domain: Optional[str] = None


class PublicEndpointParamsChatCompletionsEndpoint(BaseModel):
    disabled: Optional[bool] = None
    """Disable chat completions endpoint for this public endpoint"""


class PublicEndpointParamsMcp(BaseModel):
    disabled: Optional[bool] = None
    """Disable MCP endpoint for this public endpoint"""


class PublicEndpointParamsRateLimit(BaseModel):
    period_ms: Optional[int] = None

    requests: Optional[int] = None

    technique: Optional[Literal["fixed", "sliding"]] = None


class PublicEndpointParamsSearchEndpoint(BaseModel):
    disabled: Optional[bool] = None
    """Disable search endpoint for this public endpoint"""


class PublicEndpointParams(BaseModel):
    authorized_hosts: Optional[List[str]] = None

    chat_completions_endpoint: Optional[PublicEndpointParamsChatCompletionsEndpoint] = None

    enabled: Optional[bool] = None

    mcp: Optional[PublicEndpointParamsMcp] = None

    rate_limit: Optional[PublicEndpointParamsRateLimit] = None

    search_endpoint: Optional[PublicEndpointParamsSearchEndpoint] = None


class SourceParamsWebCrawlerParseOptions(BaseModel):
    include_headers: Optional[Dict[str, str]] = None

    include_images: Optional[bool] = None

    specific_sitemaps: Optional[List[str]] = None
    """List of specific sitemap URLs to use for crawling.

    Only valid when parse_type is 'sitemap'.
    """

    use_browser_rendering: Optional[bool] = None


class SourceParamsWebCrawlerStoreOptions(BaseModel):
    storage_id: str

    r2_jurisdiction: Optional[str] = None

    storage_type: Optional[Provider] = None


class SourceParamsWebCrawler(BaseModel):
    parse_options: Optional[SourceParamsWebCrawlerParseOptions] = None

    parse_type: Optional[Literal["sitemap", "feed-rss"]] = None

    store_options: Optional[SourceParamsWebCrawlerStoreOptions] = None


class SourceParams(BaseModel):
    exclude_items: Optional[List[str]] = None
    """List of path patterns to exclude.

    Uses micromatch glob syntax: \\** matches within a path segment, ** matches across
    path segments (e.g., /admin/** matches /admin/users and
    /admin/settings/advanced)
    """

    include_items: Optional[List[str]] = None
    """List of path patterns to include.

    Uses micromatch glob syntax: \\** matches within a path segment, ** matches across
    path segments (e.g., /blog/** matches /blog/post and /blog/2024/post)
    """

    prefix: Optional[str] = None

    r2_jurisdiction: Optional[str] = None

    web_crawler: Optional[SourceParamsWebCrawler] = None


class InstanceReadResponse(BaseModel):
    id: str
    """Use your AI Search ID."""

    account_id: str

    account_tag: str

    created_at: datetime

    internal_id: str

    modified_at: datetime

    source: str

    type: Literal["r2", "web-crawler"]

    vectorize_name: str

    ai_gateway_id: Optional[str] = None

    aisearch_model: Optional[
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
        ]
    ] = FieldInfo(alias="ai_search_model", default=None)

    cache: Optional[bool] = None

    cache_threshold: Optional[Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]] = None

    chunk: Optional[bool] = None

    chunk_overlap: Optional[int] = None

    chunk_size: Optional[int] = None

    created_by: Optional[str] = None

    embedding_model: Optional[
        Literal[
            "@cf/qwen/qwen3-embedding-0.6b",
            "@cf/baai/bge-m3",
            "@cf/baai/bge-large-en-v1.5",
            "@cf/google/embeddinggemma-300m",
            "google-ai-studio/gemini-embedding-001",
            "openai/text-embedding-3-small",
            "openai/text-embedding-3-large",
            "",
        ]
    ] = None

    enable: Optional[bool] = None

    engine_version: Optional[float] = None

    hybrid_search_enabled: Optional[bool] = None

    last_activity: Optional[datetime] = None

    max_num_results: Optional[int] = None

    metadata: Optional[Metadata] = None

    modified_by: Optional[str] = None

    paused: Optional[bool] = None

    public_endpoint_id: Optional[str] = None

    public_endpoint_params: Optional[PublicEndpointParams] = None

    reranking: Optional[bool] = None

    reranking_model: Optional[Literal["@cf/baai/bge-reranker-base", ""]] = None

    rewrite_model: Optional[
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
        ]
    ] = None

    rewrite_query: Optional[bool] = None

    score_threshold: Optional[float] = None

    source_params: Optional[SourceParams] = None

    status: Optional[str] = None

    summarization: Optional[bool] = None

    summarization_model: Optional[
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
        ]
    ] = None

    system_prompt_aisearch: Optional[str] = FieldInfo(alias="system_prompt_ai_search", default=None)

    system_prompt_index_summarization: Optional[str] = None

    system_prompt_rewrite_query: Optional[str] = None

    token_id: Optional[str] = None

    vectorize_active_namespace: Optional[str] = None
