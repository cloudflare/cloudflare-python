# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "InstanceUpdateResponse",
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


class Metadata(BaseModel):
    created_from_aisearch_wizard: Optional[bool] = None

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

    custom_domains: Optional[List[str]] = None
    """Custom domain hostnames that alias this public endpoint.

    GET and create responses return the current set; on update (PUT) this field is
    only echoed back when supplied in the request body, otherwise it is null (omit
    it to leave domains unchanged).
    """

    default_domain_enabled: Optional[bool] = None
    """
    When false, the instance is reachable only via a registered custom domain and
    the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404.
    Requires at least one custom domain. Defaults to true. public_endpoint_params is
    replaced wholesale on update, so resend default_domain_enabled on every update
    to keep the default host off — omitting it resets to true.
    """

    enabled: Optional[bool] = None

    mcp: Optional[PublicEndpointParamsMcp] = None

    rate_limit: Optional[PublicEndpointParamsRateLimit] = None

    search_endpoint: Optional[PublicEndpointParamsSearchEndpoint] = None


class RetrievalOptionsBoostBy(BaseModel):
    field: str
    """Metadata field name to boost by.

    Use 'timestamp' for document freshness, or any custom_metadata field. Numeric
    and datetime fields support all four directions (asc, desc, exists, not_exists);
    text/boolean fields only support exists/not_exists.
    """

    direction: Optional[Literal["asc", "desc", "exists", "not_exists"]] = None
    """Boost direction.

    'desc' = higher values rank higher (e.g. newer timestamps). 'asc' = lower values
    rank higher. 'exists' = boost chunks that have the field. 'not_exists' = boost
    chunks that lack the field. Optional — defaults to 'asc' for numeric/datetime
    fields, 'exists' for text/boolean fields.
    """


class RetrievalOptions(BaseModel):
    boost_by: Optional[List[RetrievalOptionsBoostBy]] = None
    """Metadata fields to boost search results by.

    Each entry specifies a metadata field and an optional direction. Direction
    defaults to 'asc' for numeric/datetime fields and 'exists' for text/boolean
    fields. Fields must match 'timestamp' or a defined custom_metadata field.
    """

    keyword_match_mode: Optional[Literal["and", "or"]] = None
    """Controls which documents are candidates for BM25 scoring.

    'and' restricts candidates to documents containing all query terms; 'or'
    includes any document containing at least one term, ranked by BM25 relevance.
    When omitted on an update, the existing stored value is preserved; when never
    set, search falls back to 'and'.
    """


class SourceParamsWebCrawlerDiscoverOptions(BaseModel):
    """
    Options for parse_type 'discover', where Browser Run discovers URLs by link following and sitemaps. Ignored for 'sitemap'.
    """

    depth: Optional[float] = None
    """Maximum link-follow depth from the seed URL."""

    include_external_links: Optional[bool] = None
    """Follow links that point outside the source domain.

    Must stay `false` — discover crawls are restricted to the zone you own.
    """

    include_subdomains: Optional[bool] = None
    """Follow links to subdomains of the source host."""

    limit: Optional[float] = None
    """Maximum number of pages to crawl (1-100000)."""

    max_age: Optional[float] = None
    """Maximum content age in seconds to accept (0–604800)."""

    source: Optional[Literal["all", "sitemaps", "links"]] = None
    """
    Where the crawler looks for URLs: 'sitemaps' reads sitemap XML only, 'links'
    follows page links only, 'all' does both.
    """


class SourceParamsWebCrawlerParseOptionsContentSelector(BaseModel):
    path: str
    """Glob pattern to match against the page URL path.

    Uses standard glob syntax: \\** matches within a segment, \\**\\** crosses
    directories.
    """

    selector: str
    """CSS selector to extract content from pages matching the path pattern.

    Must not contain disallowed characters (;, `, $, {, }, \\)). Must target a single
    element; if multiple elements match, the selector is ignored and the full page
    is used.
    """


class SourceParamsWebCrawlerParseOptions(BaseModel):
    content_selector: Optional[List[SourceParamsWebCrawlerParseOptionsContentSelector]] = None
    """
    List of path-to-selector mappings for extracting specific content from crawled
    pages. Each entry pairs a URL glob pattern with a CSS selector. The first
    matching path wins. Only the matched HTML fragment is stored and indexed. Omit
    the field to disable content selection — empty arrays are rejected.
    """

    include_headers: Optional[Dict[str, str]] = None
    """Up to 5 custom HTTP headers sent with each crawl request.

    Names must be RFC-7230 token characters (no spaces, colons, or control
    characters); values must be HTAB + printable ASCII (no CR/LF).
    """

    include_images: Optional[bool] = None

    specific_sitemaps: Optional[List[str]] = None
    """List of specific sitemap URLs to use for crawling.

    Only valid when parse_type is 'sitemap'.
    """

    use_browser_rendering: Optional[bool] = None


class SourceParamsWebCrawler(BaseModel):
    discover_options: Optional[SourceParamsWebCrawlerDiscoverOptions] = None
    """
    Options for parse_type 'discover', where Browser Run discovers URLs by link
    following and sitemaps. Ignored for 'sitemap'.
    """

    parse_options: Optional[SourceParamsWebCrawlerParseOptions] = None

    parse_type: Optional[Literal["sitemap", "discover"]] = None
    """How URLs are discovered.

    'sitemap' reads XML sitemaps; 'discover' follows links recursively and requires
    the source to be a Verified zone on this account.
    """


class SourceParams(BaseModel):
    exclude_items: Optional[List[str]] = None
    """List of path patterns to exclude.

    Uses micromatch glob syntax: \\** matches within a path segment, ** matches across
    path segments (e.g., /admin/** matches /admin/users and
    /admin/settings/advanced). Most accounts are limited to 10 rules; contact
    support to raise it.
    """

    include_items: Optional[List[str]] = None
    """List of path patterns to include.

    Uses micromatch glob syntax: \\** matches within a path segment, ** matches across
    path segments (e.g., /blog/** matches /blog/post and /blog/2024/post). Most
    accounts are limited to 10 rules; contact support to raise it.
    """

    prefix: Optional[str] = None

    r2_jurisdiction: Optional[str] = None

    web_crawler: Optional[SourceParamsWebCrawler] = None


class InstanceUpdateResponse(BaseModel):
    id: str
    """AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores."""

    created_at: datetime

    modified_at: datetime

    ai_gateway_id: Optional[str] = None

    aisearch_model: Optional[str] = FieldInfo(alias="ai_search_model", default=None)

    cache: Optional[bool] = None

    cache_threshold: Optional[Literal["super_strict_match", "close_enough", "flexible_friend", "anything_goes"]] = None

    cache_ttl: Optional[Literal[600, 1800, 3600, 7200, 21600, 43200, 86400, 172800, 259200, 518400]] = None
    """Cache entry TTL in seconds.

    Allowed values: 600 (10min), 1800 (30min), 3600 (1h), 7200 (2h), 21600 (6h),
    43200 (12h), 86400 (24h), 172800 (48h), 259200 (72h), 518400 (6d).
    """

    chunk_overlap: Optional[int] = None

    chunk_size: Optional[int] = None

    created_by: Optional[str] = None

    custom_metadata: Optional[List[CustomMetadata]] = None

    embedding_model: Optional[str] = None

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

    reranking_model: Optional[str] = None

    retrieval_options: Optional[RetrievalOptions] = None

    rewrite_model: Optional[str] = None

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
