# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..r2.buckets.provider import Provider

__all__ = [
    "InstanceCreateResponse",
    "CustomMetadata",
    "IndexMethod",
    "IndexingOptions",
    "Metadata",
    "MetadataSearchForAgents",
    "PublicEndpointParams",
    "PublicEndpointParamsChatCompletionsEndpoint",
    "PublicEndpointParamsMcp",
    "PublicEndpointParamsRateLimit",
    "PublicEndpointParamsSearchEndpoint",
    "RetrievalOptions",
    "RetrievalOptionsBoostBy",
    "SourceParams",
    "SourceParamsWebCrawler",
    "SourceParamsWebCrawlerCrawlOptions",
    "SourceParamsWebCrawlerParseOptions",
    "SourceParamsWebCrawlerParseOptionsContentSelector",
    "SourceParamsWebCrawlerStoreOptions",
]


class CustomMetadata(BaseModel):
    data_type: Literal["text", "number", "boolean", "datetime"]

    field_name: str


class IndexMethod(BaseModel):
    """Controls which storage backends are used during indexing.

    Defaults to vector-only.
    """

    keyword: bool
    """Enable keyword (BM25) storage backend."""

    vector: bool
    """Enable vector (embedding) storage backend."""


class IndexingOptions(BaseModel):
    keyword_tokenizer: Optional[Literal["porter", "trigram"]] = None
    """Tokenizer used for keyword search indexing.

    porter provides word-level tokenization with Porter stemming (good for natural
    language queries). trigram enables character-level substring matching (good for
    partial matches, code, identifiers). Changing this triggers a full re-index.
    Defaults to porter.
    """


class MetadataSearchForAgents(BaseModel):
    hostname: str

    zone_id: str

    zone_name: str


class Metadata(BaseModel):
    created_from_aisearch_wizard: Optional[bool] = None

    search_for_agents: Optional[MetadataSearchForAgents] = None

    worker_domain: Optional[str] = None


class PublicEndpointParamsChatCompletionsEndpoint(BaseModel):
    disabled: Optional[bool] = None
    """Disable chat completions endpoint for this public endpoint"""


class PublicEndpointParamsMcp(BaseModel):
    description: Optional[str] = None

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


class RetrievalOptionsBoostBy(BaseModel):
    field: str
    """Metadata field name to boost by.

    Use 'timestamp' for document freshness, or any custom_metadata field. Numeric
    and datetime fields support asc/desc directions; text/boolean fields support
    exists/not_exists.
    """

    direction: Optional[Literal["asc", "desc", "exists", "not_exists"]] = None
    """Boost direction.

    'desc' = higher values rank higher (e.g. newer timestamps). 'asc' = lower values
    rank higher. 'exists' = boost chunks that have the field. 'not_exists' = boost
    chunks that lack the field. Optional ��� defaults to 'asc' for numeric/datetime
    fields, 'exists' for text/boolean fields.
    """


class RetrievalOptions(BaseModel):
    boost_by: Optional[List[RetrievalOptionsBoostBy]] = None
    """Metadata fields to boost search results by.

    Each entry specifies a metadata field and an optional direction. Direction
    defaults to 'asc' for numeric fields and 'exists' for text/boolean fields.
    Fields must match 'timestamp' or a defined custom_metadata field.
    """

    keyword_match_mode: Optional[Literal["and", "or"]] = None
    """Controls which documents are candidates for BM25 scoring.

    'and' restricts candidates to documents containing all query terms; 'or'
    includes any document containing at least one term, ranked by BM25 relevance.
    Defaults to 'and'.
    """


class SourceParamsWebCrawlerCrawlOptions(BaseModel):
    depth: Optional[float] = None

    include_external_links: Optional[bool] = None

    include_subdomains: Optional[bool] = None

    max_age: Optional[float] = None

    source: Optional[Literal["all", "sitemaps", "links"]] = None


class SourceParamsWebCrawlerParseOptionsContentSelector(BaseModel):
    path: str
    """Glob pattern to match against the page URL path.

    Uses standard glob syntax: \\** matches within a segment, \\**\\** crosses
    directories.
    """

    selector: str
    """CSS selector to extract content from pages matching the path pattern.

    Supports standard CSS selectors including class, ID, element, and attribute
    selectors.
    """


class SourceParamsWebCrawlerParseOptions(BaseModel):
    content_selector: Optional[List[SourceParamsWebCrawlerParseOptionsContentSelector]] = None
    """
    List of path-to-selector mappings for extracting specific content from crawled
    pages. Each entry pairs a URL glob pattern with a CSS selector. The first
    matching path wins. Only the matched HTML fragment is stored and indexed.
    """

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
    crawl_options: Optional[SourceParamsWebCrawlerCrawlOptions] = None

    parse_options: Optional[SourceParamsWebCrawlerParseOptions] = None

    parse_type: Optional[Literal["sitemap", "feed-rss", "crawl"]] = None

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


class InstanceCreateResponse(BaseModel):
    id: str
    """AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores."""

    created_at: datetime

    modified_at: datetime

    ai_gateway_id: Optional[str] = None

    aisearch_model: Optional[
        Literal[
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
    ] = FieldInfo(alias="ai_search_model", default=None)

    cache: Optional[bool] = None

    cache_threshold: Optional[Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]] = None

    chunk_overlap: Optional[int] = None

    chunk_size: Optional[int] = None

    created_by: Optional[str] = None

    custom_metadata: Optional[List[CustomMetadata]] = None

    embedding_model: Optional[
        Literal[
            "@cf/qwen/qwen3-embedding-0.6b",
            "@cf/baai/bge-m3",
            "@cf/baai/bge-large-en-v1.5",
            "@cf/google/embeddinggemma-300m",
            "google-ai-studio/gemini-embedding-001",
            "google-ai-studio/gemini-embedding-2-preview",
            "openai/text-embedding-3-small",
            "openai/text-embedding-3-large",
            "",
        ]
    ] = None

    enable: Optional[bool] = None

    engine_version: Optional[float] = None

    fusion_method: Optional[Literal["max", "rrf"]] = None

    hybrid_search_enabled: Optional[bool] = None
    """Deprecated — use index_method instead."""

    index_method: Optional[IndexMethod] = None
    """Controls which storage backends are used during indexing.

    Defaults to vector-only.
    """

    indexing_options: Optional[IndexingOptions] = None

    last_activity: Optional[datetime] = None

    max_num_results: Optional[int] = None

    metadata: Optional[Metadata] = None

    modified_by: Optional[str] = None

    namespace: Optional[str] = None

    paused: Optional[bool] = None

    public_endpoint_id: Optional[str] = None

    public_endpoint_params: Optional[PublicEndpointParams] = None

    reranking: Optional[bool] = None

    reranking_model: Optional[Literal["@cf/baai/bge-reranker-base", ""]] = None

    retrieval_options: Optional[RetrievalOptions] = None

    rewrite_model: Optional[
        Literal[
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
    ] = None

    rewrite_query: Optional[bool] = None

    score_threshold: Optional[float] = None

    source: Optional[str] = None

    source_params: Optional[SourceParams] = None

    status: Optional[str] = None

    sync_interval: Optional[Literal[900, 1800, 3600, 7200, 14400, 21600, 43200, 86400]] = None
    """Interval between automatic syncs, in seconds.

    Allowed values: 900 (15min), 1800 (30min), 3600 (1h), 7200 (2h), 14400 (4h),
    21600 (6h), 43200 (12h), 86400 (24h).
    """

    token_id: Optional[str] = None

    type: Optional[Literal["r2", "web-crawler"]] = None
