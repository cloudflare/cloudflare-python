# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
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
    "MetadataCreatedFromEmdashPlugin",
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
    """Controls which storage backends indexing uses.

    Defaults to vector and keyword indexing for new instances. When set, both vector and keyword are required.
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

    use_ocr: Optional[bool] = None
    """Enables OCR ingestion for PDFs and images.

    Changing this triggers a full re-index. Defaults to false.
    """


class MetadataCreatedFromEmdashPlugin(BaseModel):
    type: Literal["native", "rest"]

    version: str

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Metadata(BaseModel):
    created_from_aisearch_wizard: Optional[bool] = None

    created_from_emdash_plugin: Optional[MetadataCreatedFromEmdashPlugin] = None

    worker_domain: Optional[str] = None


class PublicEndpointParamsChatCompletionsEndpoint(BaseModel):
    disabled: Optional[bool] = None
    """Disable chat completions endpoint for this public endpoint."""


class PublicEndpointParamsMcp(BaseModel):
    description: Optional[str] = None

    disabled: Optional[bool] = None
    """Disable MCP endpoint for this public endpoint."""


class PublicEndpointParamsRateLimit(BaseModel):
    period_ms: Optional[int] = None

    requests: Optional[int] = None

    technique: Optional[Literal["fixed", "sliding"]] = None


class PublicEndpointParamsSearchEndpoint(BaseModel):
    disabled: Optional[bool] = None
    """Disable search endpoint for this public endpoint."""


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
    """Controls which documents become candidates for BM25 scoring.

    'and' restricts candidates to documents containing all query terms; 'or'
    includes any document containing at least one term and ranks results according
    to BM25 relevance. When omitted on an update, the existing stored value stays
    unchanged; when never set, search falls back to 'and'.
    """


class SourceParamsWebCrawlerDiscoverOptions(BaseModel):
    """
    Options for parse_type 'discover', where Browser Run discovers URLs through link following and sitemaps. Ignored for 'sitemap'.
    """

    depth: Optional[float] = None
    """Maximum link-follow depth from the seed URL."""

    include_external_links: Optional[bool] = None
    """Follow links that point outside the source domain.

    Must stay `false` because discover crawls only cover the zone you own.
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

    Disallowed characters: ;, `, $, {, }, \\.. Must target a single element; if
    multiple elements match, the crawler ignores the selector and uses the full
    page.
    """


class SourceParamsWebCrawlerParseOptions(BaseModel):
    content_selector: Optional[List[SourceParamsWebCrawlerParseOptionsContentSelector]] = None
    """
    List of path-to-selector mappings for extracting specific content from crawled
    pages. Each entry pairs a URL glob pattern with a CSS selector. The first
    matching path wins. The crawler stores and indexes only the matched HTML
    fragment. Omit the field to disable content selection; the API rejects empty
    arrays.
    """

    include_headers: Optional[Dict[str, str]] = None
    """Up to 5 custom HTTP headers sent with each crawl request.

    Names must use RFC-7230 token characters, excluding spaces, colons, and control
    characters. Values must use HTAB and printable ASCII only, excluding CR and LF.
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
    Options for parse_type 'discover', where Browser Run discovers URLs through link
    following and sitemaps. Ignored for 'sitemap'.
    """

    parse_options: Optional[SourceParamsWebCrawlerParseOptions] = None

    parse_type: Optional[Literal["sitemap", "discover"]] = None
    """How the crawler finds URLs.

    'sitemap' reads XML sitemaps; 'discover' follows links recursively and requires
    the source to belong to a Verified zone on this account.
    """


class SourceParams(BaseModel):
    exclude_items: Optional[List[str]] = None
    """List of path patterns to exclude.

    Uses micromatch glob syntax: \\** matches within a path segment, ** matches across
    path segments (e.g., /admin/** matches /admin/users and
    /admin/settings/advanced). Most accounts have a limit of 10 rules; contact
    support to raise it.
    """

    include_items: Optional[List[str]] = None
    """List of path patterns to include.

    Uses micromatch glob syntax: \\** matches within a path segment, ** matches across
    path segments (e.g., /blog/** matches /blog/post and /blog/2024/post). Most
    accounts have a limit of 10 rules; contact support to raise it.
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
    """
    A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
    Completions API. An empty string uses the configured or default model.
    """

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
    """Deprecated — use index_method instead.

    Defaults to true for new instances; set false to create a vector-only instance.
    """

    index_method: Optional[IndexMethod] = None
    """Controls which storage backends indexing uses.

    Defaults to vector and keyword indexing for new instances. When set, both vector
    and keyword are required.
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
    """
    A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat
    Completions API. An empty string uses the configured or default model.
    """

    rewrite_query: Optional[bool] = None

    score_threshold: Optional[float] = None
    """Minimum similarity score a chunk must reach to be returned. Defaults to 0.4."""

    source: Optional[str] = None

    source_params: Optional[SourceParams] = None

    status: Optional[str] = None

    sync_interval: Optional[Literal[900, 1800, 3600, 7200, 14400, 21600, 43200, 86400]] = None
    """Interval between automatic syncs, in seconds.

    Allowed values: 900 (15min), 1800 (30min), 3600 (1h), 7200 (2h), 14400 (4h),
    21600 (6h), 43200 (12h), 86400 (24h). Defaults to 86400 (24h).
    """

    token_id: Optional[str] = None

    type: Optional[Literal["r2", "web-crawler"]] = None
    """Source type.

    When omitted or null with a non-blank source, HTTP(S) URLs infer web-crawler and
    existing R2 bucket names infer r2. A missing or blank source without a type uses
    managed upload-only storage.
    """
