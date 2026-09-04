# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "InstanceCreateParams",
    "CustomMetadata",
    "IndexMethod",
    "IndexingOptions",
    "Metadata",
    "PublicEndpointParams",
    "PublicEndpointParamsChatCompletionsEndpoint",
    "PublicEndpointParamsMcp",
    "PublicEndpointParamsRateLimit",
    "PublicEndpointParamsSearchEndpoint",
    "RetrievalOptions",
    "RetrievalOptionsBoostBy",
    "SourceParams",
    "SourceParamsWebCrawler",
    "SourceParamsWebCrawlerDiscoverOptions",
    "SourceParamsWebCrawlerParseOptions",
    "SourceParamsWebCrawlerParseOptionsContentSelector",
]


class InstanceCreateParams(TypedDict, total=False):
    account_id: Required[str]

    id: Required[str]
    """AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores."""

    ai_gateway_id: Optional[str]

    aisearch_model: Annotated[Optional[str], PropertyInfo(alias="ai_search_model")]
    """
    A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
    Completions API. An empty string uses the configured or default model.
    """

    cache: bool

    cache_threshold: Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]

    cache_ttl: Literal[600, 1800, 3600, 7200, 21600, 43200, 86400, 172800, 259200, 518400]
    """Cache entry TTL in seconds.

    Allowed values: 600 (10min), 1800 (30min), 3600 (1h), 7200 (2h), 21600 (6h),
    43200 (12h), 86400 (24h), 172800 (48h), 259200 (72h), 518400 (6d).
    """

    chunk: bool

    chunk_overlap: int

    chunk_size: int

    custom_metadata: Iterable[CustomMetadata]

    embedding_model: Optional[str]

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

    reranking_model: Optional[str]

    retrieval_options: Optional[RetrievalOptions]

    rewrite_model: Optional[str]
    """
    A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
    Completions API. An empty string uses the configured or default model.
    """

    rewrite_query: bool

    score_threshold: float

    source: Optional[str]

    source_params: Optional[SourceParams]

    sync_interval: Literal[900, 1800, 3600, 7200, 14400, 21600, 43200, 86400]
    """Interval between automatic syncs, in seconds.

    Allowed values: 900 (15min), 1800 (30min), 3600 (1h), 7200 (2h), 14400 (4h),
    21600 (6h), 43200 (12h), 86400 (24h).
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


class Metadata(TypedDict, total=False):
    created_from_aisearch_wizard: bool

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

    custom_domains: Optional[SequenceNotStr[str]]
    """Custom domain hostnames that alias this public endpoint.

    GET and create responses return the current set; on update (PUT) this field is
    only echoed back when supplied in the request body, otherwise it is null (omit
    it to leave domains unchanged).
    """

    default_domain_enabled: bool
    """
    When false, the instance is reachable only via a registered custom domain and
    the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404.
    Requires at least one custom domain. Defaults to true. public_endpoint_params is
    replaced wholesale on update, so resend default_domain_enabled on every update
    to keep the default host off — omitting it resets to true.
    """

    enabled: bool

    mcp: PublicEndpointParamsMcp

    rate_limit: PublicEndpointParamsRateLimit

    search_endpoint: PublicEndpointParamsSearchEndpoint


class RetrievalOptionsBoostBy(TypedDict, total=False):
    field: Required[str]
    """Metadata field name to boost by.

    Use 'timestamp' for document freshness, or any custom_metadata field. Numeric
    and datetime fields support all four directions (asc, desc, exists, not_exists);
    text/boolean fields only support exists/not_exists.
    """

    direction: Literal["asc", "desc", "exists", "not_exists"]
    """Boost direction.

    'desc' = higher values rank higher (e.g. newer timestamps). 'asc' = lower values
    rank higher. 'exists' = boost chunks that have the field. 'not_exists' = boost
    chunks that lack the field. Optional — defaults to 'asc' for numeric/datetime
    fields, 'exists' for text/boolean fields.
    """


class RetrievalOptions(TypedDict, total=False):
    boost_by: Iterable[RetrievalOptionsBoostBy]
    """Metadata fields to boost search results by.

    Each entry specifies a metadata field and an optional direction. Direction
    defaults to 'asc' for numeric/datetime fields and 'exists' for text/boolean
    fields. Fields must match 'timestamp' or a defined custom_metadata field.
    """

    keyword_match_mode: Literal["and", "or"]
    """Controls which documents are candidates for BM25 scoring.

    'and' restricts candidates to documents containing all query terms; 'or'
    includes any document containing at least one term, ranked by BM25 relevance.
    When omitted on an update, the existing stored value is preserved; when never
    set, search falls back to 'and'.
    """


class SourceParamsWebCrawlerDiscoverOptions(TypedDict, total=False):
    """
    Options for parse_type 'discover', where Browser Run discovers URLs by link following and sitemaps. Ignored for 'sitemap'.
    """

    depth: float
    """Maximum link-follow depth from the seed URL."""

    include_external_links: bool
    """Follow links that point outside the source domain.

    Must stay `false` — discover crawls are restricted to the zone you own.
    """

    include_subdomains: bool
    """Follow links to subdomains of the source host."""

    limit: float
    """Maximum number of pages to crawl (1-100000)."""

    max_age: float
    """Maximum content age in seconds to accept (0–604800)."""

    source: Literal["all", "sitemaps", "links"]
    """
    Where the crawler looks for URLs: 'sitemaps' reads sitemap XML only, 'links'
    follows page links only, 'all' does both.
    """


class SourceParamsWebCrawlerParseOptionsContentSelector(TypedDict, total=False):
    path: Required[str]
    """Glob pattern to match against the page URL path.

    Uses standard glob syntax: \\** matches within a segment, \\**\\** crosses
    directories.
    """

    selector: Required[str]
    """CSS selector to extract content from pages matching the path pattern.

    Must not contain disallowed characters (;, `, $, {, }, \\)). Must target a single
    element; if multiple elements match, the selector is ignored and the full page
    is used.
    """


class SourceParamsWebCrawlerParseOptions(TypedDict, total=False):
    content_selector: Iterable[SourceParamsWebCrawlerParseOptionsContentSelector]
    """
    List of path-to-selector mappings for extracting specific content from crawled
    pages. Each entry pairs a URL glob pattern with a CSS selector. The first
    matching path wins. Only the matched HTML fragment is stored and indexed. Omit
    the field to disable content selection — empty arrays are rejected.
    """

    include_headers: Dict[str, str]
    """Up to 5 custom HTTP headers sent with each crawl request.

    Names must be RFC-7230 token characters (no spaces, colons, or control
    characters); values must be HTAB + printable ASCII (no CR/LF).
    """

    include_images: bool

    specific_sitemaps: SequenceNotStr[str]
    """List of specific sitemap URLs to use for crawling.

    Only valid when parse_type is 'sitemap'.
    """

    use_browser_rendering: bool


class SourceParamsWebCrawler(TypedDict, total=False):
    discover_options: SourceParamsWebCrawlerDiscoverOptions
    """
    Options for parse_type 'discover', where Browser Run discovers URLs by link
    following and sitemaps. Ignored for 'sitemap'.
    """

    parse_options: SourceParamsWebCrawlerParseOptions

    parse_type: Literal["sitemap", "discover"]
    """How URLs are discovered.

    'sitemap' reads XML sitemaps; 'discover' follows links recursively and requires
    the source to be a Verified zone on this account.
    """


class SourceParams(TypedDict, total=False):
    exclude_items: SequenceNotStr[str]
    """List of path patterns to exclude.

    Uses micromatch glob syntax: \\** matches within a path segment, ** matches across
    path segments (e.g., /admin/** matches /admin/users and
    /admin/settings/advanced). Most accounts are limited to 10 rules; contact
    support to raise it.
    """

    include_items: SequenceNotStr[str]
    """List of path patterns to include.

    Uses micromatch glob syntax: \\** matches within a path segment, ** matches across
    path segments (e.g., /blog/** matches /blog/post and /blog/2024/post). Most
    accounts are limited to 10 rules; contact support to raise it.
    """

    prefix: str

    r2_jurisdiction: str

    web_crawler: SourceParamsWebCrawler
