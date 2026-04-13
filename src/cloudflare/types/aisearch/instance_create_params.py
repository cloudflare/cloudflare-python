# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..r2.buckets.provider import Provider

__all__ = [
    "InstanceCreateParams",
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


class InstanceCreateParams(TypedDict, total=False):
    account_id: Required[str]

    id: Required[str]
    """AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores."""

    ai_gateway_id: Optional[str]

    aisearch_model: Annotated[
        Optional[
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
        ],
        PropertyInfo(alias="ai_search_model"),
    ]

    cache: bool

    cache_threshold: Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]

    chunk: bool

    chunk_overlap: int

    chunk_size: int

    custom_metadata: Iterable[CustomMetadata]

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
    ]

    fusion_method: Literal["max", "rrf"]

    hybrid_search_enabled: bool
    """Deprecated — use index_method instead."""

    index_method: IndexMethod
    """Controls which storage backends are used during indexing.

    Defaults to vector-only.
    """

    indexing_options: Optional[IndexingOptions]

    max_num_results: int

    metadata: Metadata

    public_endpoint_params: PublicEndpointParams

    reranking: bool

    reranking_model: Optional[Literal["@cf/baai/bge-reranker-base", ""]]

    retrieval_options: Optional[RetrievalOptions]

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
    ]

    rewrite_query: bool

    score_threshold: float

    source: Optional[str]

    source_params: Optional[SourceParams]

    sync_interval: Literal[3600, 7200, 14400, 21600, 43200, 86400]
    """Interval between automatic syncs, in seconds.

    Allowed values: 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400
    (24h).
    """

    token_id: str

    type: Optional[Literal["r2", "web-crawler"]]


class CustomMetadata(TypedDict, total=False):
    data_type: Required[Literal["text", "number", "boolean", "datetime"]]

    field_name: Required[str]


class IndexMethod(TypedDict, total=False):
    """Controls which storage backends are used during indexing.

    Defaults to vector-only.
    """

    keyword: Required[bool]
    """Enable keyword (BM25) storage backend."""

    vector: Required[bool]
    """Enable vector (embedding) storage backend."""


class IndexingOptions(TypedDict, total=False):
    keyword_tokenizer: Literal["porter", "trigram"]
    """Tokenizer used for keyword search indexing.

    porter provides word-level tokenization with Porter stemming (good for natural
    language queries). trigram enables character-level substring matching (good for
    partial matches, code, identifiers). Changing this triggers a full re-index.
    Defaults to porter.
    """


class MetadataSearchForAgents(TypedDict, total=False):
    hostname: Required[str]

    zone_id: Required[str]

    zone_name: Required[str]


class Metadata(TypedDict, total=False):
    created_from_aisearch_wizard: bool

    search_for_agents: MetadataSearchForAgents

    worker_domain: str


class PublicEndpointParamsChatCompletionsEndpoint(TypedDict, total=False):
    disabled: bool
    """Disable chat completions endpoint for this public endpoint"""


class PublicEndpointParamsMcp(TypedDict, total=False):
    description: str

    disabled: bool
    """Disable MCP endpoint for this public endpoint"""


class PublicEndpointParamsRateLimit(TypedDict, total=False):
    period_ms: int

    requests: int

    technique: Literal["fixed", "sliding"]


class PublicEndpointParamsSearchEndpoint(TypedDict, total=False):
    disabled: bool
    """Disable search endpoint for this public endpoint"""


class PublicEndpointParams(TypedDict, total=False):
    authorized_hosts: SequenceNotStr[str]

    chat_completions_endpoint: PublicEndpointParamsChatCompletionsEndpoint

    enabled: bool

    mcp: PublicEndpointParamsMcp

    rate_limit: PublicEndpointParamsRateLimit

    search_endpoint: PublicEndpointParamsSearchEndpoint


class RetrievalOptionsBoostBy(TypedDict, total=False):
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


class RetrievalOptions(TypedDict, total=False):
    boost_by: Iterable[RetrievalOptionsBoostBy]
    """Metadata fields to boost search results by.

    Each entry specifies a metadata field and an optional direction. Direction
    defaults to 'asc' for numeric fields and 'exists' for text/boolean fields.
    Fields must match 'timestamp' or a defined custom_metadata field.
    """

    keyword_match_mode: Literal["and", "or"]
    """Controls which documents are candidates for BM25 scoring.

    'and' restricts candidates to documents containing all query terms; 'or'
    includes any document containing at least one term, ranked by BM25 relevance.
    Defaults to 'and'.
    """


class SourceParamsWebCrawlerCrawlOptions(TypedDict, total=False):
    depth: float

    include_external_links: bool

    include_subdomains: bool

    max_age: float

    source: Literal["all", "sitemaps", "links"]


class SourceParamsWebCrawlerParseOptionsContentSelector(TypedDict, total=False):
    path: Required[str]
    """Glob pattern to match against the page URL path.

    Uses standard glob syntax: \\** matches within a segment, \\**\\** crosses
    directories.
    """

    selector: Required[str]
    """CSS selector to extract content from pages matching the path pattern.

    Supports standard CSS selectors including class, ID, element, and attribute
    selectors.
    """


class SourceParamsWebCrawlerParseOptions(TypedDict, total=False):
    content_selector: Iterable[SourceParamsWebCrawlerParseOptionsContentSelector]
    """
    List of path-to-selector mappings for extracting specific content from crawled
    pages. Each entry pairs a URL glob pattern with a CSS selector. The first
    matching path wins. Only the matched HTML fragment is stored and indexed.
    """

    include_headers: Dict[str, str]

    include_images: bool

    specific_sitemaps: SequenceNotStr[str]
    """List of specific sitemap URLs to use for crawling.

    Only valid when parse_type is 'sitemap'.
    """

    use_browser_rendering: bool


class SourceParamsWebCrawlerStoreOptions(TypedDict, total=False):
    storage_id: Required[str]

    r2_jurisdiction: str

    storage_type: Provider


class SourceParamsWebCrawler(TypedDict, total=False):
    crawl_options: SourceParamsWebCrawlerCrawlOptions

    parse_options: SourceParamsWebCrawlerParseOptions

    parse_type: Literal["sitemap", "feed-rss", "crawl"]

    store_options: SourceParamsWebCrawlerStoreOptions


class SourceParams(TypedDict, total=False):
    exclude_items: SequenceNotStr[str]
    """List of path patterns to exclude.

    Uses micromatch glob syntax: \\** matches within a path segment, ** matches across
    path segments (e.g., /admin/** matches /admin/users and
    /admin/settings/advanced)
    """

    include_items: SequenceNotStr[str]
    """List of path patterns to include.

    Uses micromatch glob syntax: \\** matches within a path segment, ** matches across
    path segments (e.g., /blog/** matches /blog/post and /blog/2024/post)
    """

    prefix: str

    r2_jurisdiction: str

    web_crawler: SourceParamsWebCrawler
