# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "CrawlCreateParams",
    "Variant0",
    "Variant0AddScriptTag",
    "Variant0AddStyleTag",
    "Variant0Authenticate",
    "Variant0Cookie",
    "Variant0GotoOptions",
    "Variant0JsonOptions",
    "Variant0JsonOptionsCustomAI",
    "Variant0JsonOptionsResponseFormat",
    "Variant0Options",
    "Variant0Viewport",
    "Variant0WaitForSelector",
    "Variant1",
    "Variant1JsonOptions",
    "Variant1JsonOptionsCustomAI",
    "Variant1JsonOptionsResponseFormat",
    "Variant1Options",
]


class Variant0(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    url: Required[str]
    """URL to navigate to, eg. `https://example.com`."""

    cache_ttl: Annotated[float, PropertyInfo(alias="cacheTTL")]
    """Cache TTL default is 5s. Set to 0 to disable."""

    action_timeout: Annotated[float, PropertyInfo(alias="actionTimeout")]
    """
    The maximum duration allowed for the browser action to complete after the page
    has loaded (such as taking screenshots, extracting content, or generating PDFs).
    If this time limit is exceeded, the action stops and returns a timeout error.
    """

    add_script_tag: Annotated[Iterable[Variant0AddScriptTag], PropertyInfo(alias="addScriptTag")]
    """Adds a `<script>` tag into the page with the desired URL or content."""

    add_style_tag: Annotated[Iterable[Variant0AddStyleTag], PropertyInfo(alias="addStyleTag")]
    """
    Adds a `<link rel="stylesheet">` tag into the page with the desired URL or a
    `<style type="text/css">` tag with the content.
    """

    allow_request_pattern: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowRequestPattern")]
    """Only allow requests that match the provided regex patterns, eg. '/^.\\**\\..(css)'."""

    allow_resource_types: Annotated[
        List[
            Literal[
                "document",
                "stylesheet",
                "image",
                "media",
                "font",
                "script",
                "texttrack",
                "xhr",
                "fetch",
                "prefetch",
                "eventsource",
                "websocket",
                "manifest",
                "signedexchange",
                "ping",
                "cspviolationreport",
                "preflight",
                "other",
            ]
        ],
        PropertyInfo(alias="allowResourceTypes"),
    ]
    """Only allow requests that match the provided resource types, eg.

    'image' or 'script'.
    """

    authenticate: Variant0Authenticate
    """Provide credentials for HTTP authentication."""

    best_attempt: Annotated[bool, PropertyInfo(alias="bestAttempt")]
    """Attempt to proceed when 'awaited' events fail or timeout."""

    cookies: Iterable[Variant0Cookie]
    """Check [options](https://pptr.dev/api/puppeteer.page.setcookie)."""

    crawl_purposes: Annotated[List[Literal["search", "ai-input", "ai-train"]], PropertyInfo(alias="crawlPurposes")]
    """List of crawl purposes to respect Content-Signal directives in robots.txt.

    Allowed values: 'search', 'ai-input', 'ai-train'. Learn more:
    https://contentsignals.org/. Default: ['search', 'ai-input', 'ai-train'].
    """

    depth: float
    """Maximum number of levels deep the crawler will traverse from the starting URL."""

    emulate_media_type: Annotated[str, PropertyInfo(alias="emulateMediaType")]

    formats: List[Literal["html", "markdown", "json"]]
    """Formats to return. Default is `html`."""

    goto_options: Annotated[Variant0GotoOptions, PropertyInfo(alias="gotoOptions")]
    """Check [options](https://pptr.dev/api/puppeteer.gotooptions)."""

    json_options: Annotated[Variant0JsonOptions, PropertyInfo(alias="jsonOptions")]
    """Options for JSON extraction."""

    limit: float
    """Maximum number of URLs to crawl."""

    max_age: Annotated[float, PropertyInfo(alias="maxAge")]
    """Maximum age of a resource that can be returned from cache in seconds.

    Default is 1 day.
    """

    modified_since: Annotated[int, PropertyInfo(alias="modifiedSince")]
    """
    Unix timestamp (seconds since epoch) indicating to only crawl pages that were
    modified since this time. For sitemap URLs with a lastmod field, this is
    compared directly. For other URLs, the crawler will use If-Modified-Since header
    when fetching. URLs without modification information (no lastmod in sitemap and
    no Last-Modified header support) will be crawled. Note: This works in
    conjunction with maxAge - both filters must pass for a cached resource to be
    used. Must be within the last year and not in the future.
    """

    options: Variant0Options
    """Additional options for the crawler."""

    reject_request_pattern: Annotated[SequenceNotStr[str], PropertyInfo(alias="rejectRequestPattern")]
    """Block undesired requests that match the provided regex patterns, eg.

    '/^.\\**\\..(css)'.
    """

    reject_resource_types: Annotated[
        List[
            Literal[
                "document",
                "stylesheet",
                "image",
                "media",
                "font",
                "script",
                "texttrack",
                "xhr",
                "fetch",
                "prefetch",
                "eventsource",
                "websocket",
                "manifest",
                "signedexchange",
                "ping",
                "cspviolationreport",
                "preflight",
                "other",
            ]
        ],
        PropertyInfo(alias="rejectResourceTypes"),
    ]
    """Block undesired requests that match the provided resource types, eg.

    'image' or 'script'.
    """

    render: Literal[True]
    """Whether to render the page or fetch static content. True by default."""

    set_extra_http_headers: Annotated[Dict[str, str], PropertyInfo(alias="setExtraHTTPHeaders")]

    set_java_script_enabled: Annotated[bool, PropertyInfo(alias="setJavaScriptEnabled")]

    source: Literal["sitemaps", "links", "all"]
    """Source of links to crawl.

    'sitemaps' - only crawl URLs from sitemaps, 'links' - only crawl URLs scraped
    from pages, 'all' - crawl both sitemap and scraped links (default).
    """

    viewport: Variant0Viewport
    """Check [options](https://pptr.dev/api/puppeteer.page.setviewport)."""

    wait_for_selector: Annotated[Variant0WaitForSelector, PropertyInfo(alias="waitForSelector")]
    """Wait for the selector to appear in page.

    Check [options](https://pptr.dev/api/puppeteer.page.waitforselector).
    """

    wait_for_timeout: Annotated[float, PropertyInfo(alias="waitForTimeout")]
    """Waits for a specified timeout before continuing."""


class Variant0AddScriptTag(TypedDict, total=False):
    id: str

    content: str

    type: str

    url: str


class Variant0AddStyleTag(TypedDict, total=False):
    content: str

    url: str


class Variant0Authenticate(TypedDict, total=False):
    """Provide credentials for HTTP authentication."""

    password: Required[str]

    username: Required[str]


class Variant0Cookie(TypedDict, total=False):
    name: Required[str]
    """Cookie name."""

    value: Required[str]

    domain: str

    expires: float

    http_only: Annotated[bool, PropertyInfo(alias="httpOnly")]

    partition_key: Annotated[str, PropertyInfo(alias="partitionKey")]

    path: str

    priority: Literal["Low", "Medium", "High"]

    same_party: Annotated[bool, PropertyInfo(alias="sameParty")]

    same_site: Annotated[Literal["Strict", "Lax", "None"], PropertyInfo(alias="sameSite")]

    secure: bool

    source_port: Annotated[float, PropertyInfo(alias="sourcePort")]

    source_scheme: Annotated[Literal["Unset", "NonSecure", "Secure"], PropertyInfo(alias="sourceScheme")]

    url: str


class Variant0GotoOptions(TypedDict, total=False):
    """Check [options](https://pptr.dev/api/puppeteer.gotooptions)."""

    referer: str

    referrer_policy: Annotated[str, PropertyInfo(alias="referrerPolicy")]

    timeout: float

    wait_until: Annotated[
        Union[
            Literal["load", "domcontentloaded", "networkidle0", "networkidle2"],
            List[Literal["load", "domcontentloaded", "networkidle0", "networkidle2"]],
        ],
        PropertyInfo(alias="waitUntil"),
    ]


class Variant0JsonOptionsCustomAI(TypedDict, total=False):
    model: Required[str]
    """AI model to use for the request.

    Must be formed as `<provider>/<model_name>`, e.g.
    `workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast`.
    """

    authorization: str
    """Authorization token for the AI model: `Bearer <token>`.

    Not needed for workers-ai models.
    """


class Variant0JsonOptionsResponseFormat(TypedDict, total=False):
    type: Required[str]

    json_schema: Optional[Dict[str, Union[str, float, bool, SequenceNotStr[str], object]]]
    """Schema for the response format.

    More information here: https://developers.cloudflare.com/workers-ai/json-mode/
    """


class Variant0JsonOptions(TypedDict, total=False):
    """Options for JSON extraction."""

    custom_ai: Iterable[Variant0JsonOptionsCustomAI]
    """Optional list of custom AI models to use for the request.

    The models will be tried in the order provided, and in case a model returns an
    error, the next one will be used as fallback.
    """

    prompt: str

    response_format: Variant0JsonOptionsResponseFormat


class Variant0Options(TypedDict, total=False):
    """Additional options for the crawler."""

    exclude_patterns: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludePatterns")]
    """Exclude links matching the provided wildcard patterns in the crawl job.

    Example: 'https://example.com/privacy/**'.
    """

    include_external_links: Annotated[bool, PropertyInfo(alias="includeExternalLinks")]
    """Include external links in the crawl job.

    If set to true, includeSubdomains is ignored.
    """

    include_patterns: Annotated[SequenceNotStr[str], PropertyInfo(alias="includePatterns")]
    """Include only links matching the provided wildcard patterns in the crawl job.

    Include patterns are evaluated before exclude patterns. URLs that match any of
    the specified include patterns will be included in the crawl job. Example:
    'https://example.com/blog/**'.
    """

    include_subdomains: Annotated[bool, PropertyInfo(alias="includeSubdomains")]
    """Include links to subdomains in the crawl job.

    This option is ignored if includeExternalLinks is true.
    """


class Variant0Viewport(TypedDict, total=False):
    """Check [options](https://pptr.dev/api/puppeteer.page.setviewport)."""

    height: Required[float]

    width: Required[float]

    device_scale_factor: Annotated[float, PropertyInfo(alias="deviceScaleFactor")]

    has_touch: Annotated[bool, PropertyInfo(alias="hasTouch")]

    is_landscape: Annotated[bool, PropertyInfo(alias="isLandscape")]

    is_mobile: Annotated[bool, PropertyInfo(alias="isMobile")]


class Variant0WaitForSelector(TypedDict, total=False):
    """Wait for the selector to appear in page.

    Check [options](https://pptr.dev/api/puppeteer.page.waitforselector).
    """

    selector: Required[str]

    hidden: Literal[True]

    timeout: float

    visible: Literal[True]


class Variant1(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    render: Required[Literal[False]]
    """Whether to render the page or fetch static content. True by default."""

    url: Required[str]
    """URL to navigate to, eg. `https://example.com`."""

    cache_ttl: Annotated[float, PropertyInfo(alias="cacheTTL")]
    """Cache TTL default is 5s. Set to 0 to disable."""

    crawl_purposes: Annotated[List[Literal["search", "ai-input", "ai-train"]], PropertyInfo(alias="crawlPurposes")]
    """List of crawl purposes to respect Content-Signal directives in robots.txt.

    Allowed values: 'search', 'ai-input', 'ai-train'. Learn more:
    https://contentsignals.org/. Default: ['search', 'ai-input', 'ai-train'].
    """

    depth: float
    """Maximum number of levels deep the crawler will traverse from the starting URL."""

    formats: List[Literal["html", "markdown", "json"]]
    """Formats to return. Default is `html`."""

    json_options: Annotated[Variant1JsonOptions, PropertyInfo(alias="jsonOptions")]
    """Options for JSON extraction."""

    limit: float
    """Maximum number of URLs to crawl."""

    max_age: Annotated[float, PropertyInfo(alias="maxAge")]
    """Maximum age of a resource that can be returned from cache in seconds.

    Default is 1 day.
    """

    modified_since: Annotated[int, PropertyInfo(alias="modifiedSince")]
    """
    Unix timestamp (seconds since epoch) indicating to only crawl pages that were
    modified since this time. For sitemap URLs with a lastmod field, this is
    compared directly. For other URLs, the crawler will use If-Modified-Since header
    when fetching. URLs without modification information (no lastmod in sitemap and
    no Last-Modified header support) will be crawled. Note: This works in
    conjunction with maxAge - both filters must pass for a cached resource to be
    used. Must be within the last year and not in the future.
    """

    options: Variant1Options
    """Additional options for the crawler."""

    source: Literal["sitemaps", "links", "all"]
    """Source of links to crawl.

    'sitemaps' - only crawl URLs from sitemaps, 'links' - only crawl URLs scraped
    from pages, 'all' - crawl both sitemap and scraped links (default).
    """


class Variant1JsonOptionsCustomAI(TypedDict, total=False):
    model: Required[str]
    """AI model to use for the request.

    Must be formed as `<provider>/<model_name>`, e.g.
    `workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast`.
    """

    authorization: str
    """Authorization token for the AI model: `Bearer <token>`.

    Not needed for workers-ai models.
    """


class Variant1JsonOptionsResponseFormat(TypedDict, total=False):
    type: Required[str]

    json_schema: Optional[Dict[str, Union[str, float, bool, SequenceNotStr[str], object]]]
    """Schema for the response format.

    More information here: https://developers.cloudflare.com/workers-ai/json-mode/
    """


class Variant1JsonOptions(TypedDict, total=False):
    """Options for JSON extraction."""

    custom_ai: Iterable[Variant1JsonOptionsCustomAI]
    """Optional list of custom AI models to use for the request.

    The models will be tried in the order provided, and in case a model returns an
    error, the next one will be used as fallback.
    """

    prompt: str

    response_format: Variant1JsonOptionsResponseFormat


class Variant1Options(TypedDict, total=False):
    """Additional options for the crawler."""

    exclude_patterns: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludePatterns")]
    """Exclude links matching the provided wildcard patterns in the crawl job.

    Example: 'https://example.com/privacy/**'.
    """

    include_external_links: Annotated[bool, PropertyInfo(alias="includeExternalLinks")]
    """Include external links in the crawl job.

    If set to true, includeSubdomains is ignored.
    """

    include_patterns: Annotated[SequenceNotStr[str], PropertyInfo(alias="includePatterns")]
    """Include only links matching the provided wildcard patterns in the crawl job.

    Include patterns are evaluated before exclude patterns. URLs that match any of
    the specified include patterns will be included in the crawl job. Example:
    'https://example.com/blog/**'.
    """

    include_subdomains: Annotated[bool, PropertyInfo(alias="includeSubdomains")]
    """Include links to subdomains in the crawl job.

    This option is ignored if includeExternalLinks is true.
    """


CrawlCreateParams: TypeAlias = Union[Variant0, Variant1]
