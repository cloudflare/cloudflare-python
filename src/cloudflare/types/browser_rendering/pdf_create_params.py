# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "PDFCreateParams",
    "Variant0",
    "Variant0AddScriptTag",
    "Variant0AddStyleTag",
    "Variant0Authenticate",
    "Variant0Cookie",
    "Variant0GotoOptions",
    "Variant0PDFOptions",
    "Variant0PDFOptionsMargin",
    "Variant0Viewport",
    "Variant0WaitForSelector",
    "Variant1",
    "Variant1AddScriptTag",
    "Variant1AddStyleTag",
    "Variant1Authenticate",
    "Variant1Cookie",
    "Variant1GotoOptions",
    "Variant1PDFOptions",
    "Variant1PDFOptionsMargin",
    "Variant1Viewport",
    "Variant1WaitForSelector",
]


class Variant0(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    html: Required[str]
    """Set the content of the page, eg: `<h1>Hello World!!</h1>`.

    Either `html` or `url` must be set.
    """

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

    emulate_media_type: Annotated[str, PropertyInfo(alias="emulateMediaType")]

    goto_options: Annotated[Variant0GotoOptions, PropertyInfo(alias="gotoOptions")]
    """Check [options](https://pptr.dev/api/puppeteer.gotooptions)."""

    pdf_options: Annotated[Variant0PDFOptions, PropertyInfo(alias="pdfOptions")]
    """Check [options](https://pptr.dev/api/puppeteer.pdfoptions)."""

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

    set_extra_http_headers: Annotated[Dict[str, str], PropertyInfo(alias="setExtraHTTPHeaders")]

    set_java_script_enabled: Annotated[bool, PropertyInfo(alias="setJavaScriptEnabled")]

    user_agent: Annotated[str, PropertyInfo(alias="userAgent")]

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


class Variant0PDFOptionsMargin(TypedDict, total=False):
    """Set the PDF margins. Useful when setting header and footer."""

    bottom: Union[str, float]

    left: Union[str, float]

    right: Union[str, float]

    top: Union[str, float]


class Variant0PDFOptions(TypedDict, total=False):
    """Check [options](https://pptr.dev/api/puppeteer.pdfoptions)."""

    display_header_footer: Annotated[bool, PropertyInfo(alias="displayHeaderFooter")]
    """Whether to show the header and footer."""

    footer_template: Annotated[str, PropertyInfo(alias="footerTemplate")]
    """HTML template for the print footer."""

    format: Literal["letter", "legal", "tabloid", "ledger", "a0", "a1", "a2", "a3", "a4", "a5", "a6"]
    """Paper format. Takes priority over width and height if set."""

    header_template: Annotated[str, PropertyInfo(alias="headerTemplate")]
    """HTML template for the print header."""

    height: Union[str, float]
    """Sets the height of paper. Can be a number or string with unit."""

    landscape: bool
    """Whether to print in landscape orientation."""

    margin: Variant0PDFOptionsMargin
    """Set the PDF margins. Useful when setting header and footer."""

    omit_background: Annotated[bool, PropertyInfo(alias="omitBackground")]
    """Hides default white background and allows generating pdfs with transparency."""

    outline: bool
    """Generate document outline."""

    page_ranges: Annotated[str, PropertyInfo(alias="pageRanges")]
    """Paper ranges to print, e.g. '1-5, 8, 11-13'."""

    prefer_css_page_size: Annotated[bool, PropertyInfo(alias="preferCSSPageSize")]
    """Give CSS @page size priority over other size declarations."""

    print_background: Annotated[bool, PropertyInfo(alias="printBackground")]
    """Set to true to print background graphics."""

    scale: float
    """Scales the rendering of the web page. Amount must be between 0.1 and 2."""

    tagged: bool
    """Generate tagged (accessible) PDF."""

    timeout: float
    """Timeout in milliseconds."""

    width: Union[str, float]
    """Sets the width of paper. Can be a number or string with unit."""


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

    add_script_tag: Annotated[Iterable[Variant1AddScriptTag], PropertyInfo(alias="addScriptTag")]
    """Adds a `<script>` tag into the page with the desired URL or content."""

    add_style_tag: Annotated[Iterable[Variant1AddStyleTag], PropertyInfo(alias="addStyleTag")]
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

    authenticate: Variant1Authenticate
    """Provide credentials for HTTP authentication."""

    best_attempt: Annotated[bool, PropertyInfo(alias="bestAttempt")]
    """Attempt to proceed when 'awaited' events fail or timeout."""

    cookies: Iterable[Variant1Cookie]
    """Check [options](https://pptr.dev/api/puppeteer.page.setcookie)."""

    emulate_media_type: Annotated[str, PropertyInfo(alias="emulateMediaType")]

    goto_options: Annotated[Variant1GotoOptions, PropertyInfo(alias="gotoOptions")]
    """Check [options](https://pptr.dev/api/puppeteer.gotooptions)."""

    pdf_options: Annotated[Variant1PDFOptions, PropertyInfo(alias="pdfOptions")]
    """Check [options](https://pptr.dev/api/puppeteer.pdfoptions)."""

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

    set_extra_http_headers: Annotated[Dict[str, str], PropertyInfo(alias="setExtraHTTPHeaders")]

    set_java_script_enabled: Annotated[bool, PropertyInfo(alias="setJavaScriptEnabled")]

    user_agent: Annotated[str, PropertyInfo(alias="userAgent")]

    viewport: Variant1Viewport
    """Check [options](https://pptr.dev/api/puppeteer.page.setviewport)."""

    wait_for_selector: Annotated[Variant1WaitForSelector, PropertyInfo(alias="waitForSelector")]
    """Wait for the selector to appear in page.

    Check [options](https://pptr.dev/api/puppeteer.page.waitforselector).
    """

    wait_for_timeout: Annotated[float, PropertyInfo(alias="waitForTimeout")]
    """Waits for a specified timeout before continuing."""


class Variant1AddScriptTag(TypedDict, total=False):
    id: str

    content: str

    type: str

    url: str


class Variant1AddStyleTag(TypedDict, total=False):
    content: str

    url: str


class Variant1Authenticate(TypedDict, total=False):
    """Provide credentials for HTTP authentication."""

    password: Required[str]

    username: Required[str]


class Variant1Cookie(TypedDict, total=False):
    name: Required[str]

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


class Variant1GotoOptions(TypedDict, total=False):
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


class Variant1PDFOptionsMargin(TypedDict, total=False):
    """Set the PDF margins. Useful when setting header and footer."""

    bottom: Union[str, float]

    left: Union[str, float]

    right: Union[str, float]

    top: Union[str, float]


class Variant1PDFOptions(TypedDict, total=False):
    """Check [options](https://pptr.dev/api/puppeteer.pdfoptions)."""

    display_header_footer: Annotated[bool, PropertyInfo(alias="displayHeaderFooter")]
    """Whether to show the header and footer."""

    footer_template: Annotated[str, PropertyInfo(alias="footerTemplate")]
    """HTML template for the print footer."""

    format: Literal["letter", "legal", "tabloid", "ledger", "a0", "a1", "a2", "a3", "a4", "a5", "a6"]
    """Paper format. Takes priority over width and height if set."""

    header_template: Annotated[str, PropertyInfo(alias="headerTemplate")]
    """HTML template for the print header."""

    height: Union[str, float]
    """Sets the height of paper. Can be a number or string with unit."""

    landscape: bool
    """Whether to print in landscape orientation."""

    margin: Variant1PDFOptionsMargin
    """Set the PDF margins. Useful when setting header and footer."""

    omit_background: Annotated[bool, PropertyInfo(alias="omitBackground")]
    """Hides default white background and allows generating pdfs with transparency."""

    outline: bool
    """Generate document outline."""

    page_ranges: Annotated[str, PropertyInfo(alias="pageRanges")]
    """Paper ranges to print, e.g. '1-5, 8, 11-13'."""

    prefer_css_page_size: Annotated[bool, PropertyInfo(alias="preferCSSPageSize")]
    """Give CSS @page size priority over other size declarations."""

    print_background: Annotated[bool, PropertyInfo(alias="printBackground")]
    """Set to true to print background graphics."""

    scale: float
    """Scales the rendering of the web page. Amount must be between 0.1 and 2."""

    tagged: bool
    """Generate tagged (accessible) PDF."""

    timeout: float
    """Timeout in milliseconds."""

    width: Union[str, float]
    """Sets the width of paper. Can be a number or string with unit."""


class Variant1Viewport(TypedDict, total=False):
    """Check [options](https://pptr.dev/api/puppeteer.page.setviewport)."""

    height: Required[float]

    width: Required[float]

    device_scale_factor: Annotated[float, PropertyInfo(alias="deviceScaleFactor")]

    has_touch: Annotated[bool, PropertyInfo(alias="hasTouch")]

    is_landscape: Annotated[bool, PropertyInfo(alias="isLandscape")]

    is_mobile: Annotated[bool, PropertyInfo(alias="isMobile")]


class Variant1WaitForSelector(TypedDict, total=False):
    """Wait for the selector to appear in page.

    Check [options](https://pptr.dev/api/puppeteer.page.waitforselector).
    """

    selector: Required[str]

    hidden: Literal[True]

    timeout: float

    visible: Literal[True]


PDFCreateParams: TypeAlias = Union[Variant0, Variant1]
