# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ScreenshotCreateParams",
    "AddScriptTag",
    "AddStyleTag",
    "Authenticate",
    "Cookie",
    "GotoOptions",
    "ScreenshotOptions",
    "ScreenshotOptionsClip",
    "Viewport",
    "WaitForSelector",
]


class ScreenshotCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    cache_ttl: Annotated[float, PropertyInfo(alias="cacheTTL")]
    """Cache TTL default is 5s. Set to 0 to disable."""

    add_script_tag: Annotated[Iterable[AddScriptTag], PropertyInfo(alias="addScriptTag")]
    """Adds a `<script>` tag into the page with the desired URL or content."""

    add_style_tag: Annotated[Iterable[AddStyleTag], PropertyInfo(alias="addStyleTag")]
    """
    Adds a `<link rel="stylesheet">` tag into the page with the desired URL or a
    `<style type="text/css">` tag with the content.
    """

    allow_request_pattern: Annotated[List[str], PropertyInfo(alias="allowRequestPattern")]
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

    authenticate: Authenticate
    """Provide credentials for HTTP authentication."""

    best_attempt: Annotated[bool, PropertyInfo(alias="bestAttempt")]
    """Attempt to proceed when 'awaited' events fail or timeout."""

    cookies: Iterable[Cookie]
    """Check [options](https://pptr.dev/api/puppeteer.page.setcookie)."""

    emulate_media_type: Annotated[str, PropertyInfo(alias="emulateMediaType")]

    goto_options: Annotated[GotoOptions, PropertyInfo(alias="gotoOptions")]
    """Check [options](https://pptr.dev/api/puppeteer.gotooptions)."""

    html: str
    """Set the content of the page, eg: `<h1>Hello World!!</h1>`.

    Either `html` or `url` must be set.
    """

    reject_request_pattern: Annotated[List[str], PropertyInfo(alias="rejectRequestPattern")]
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

    screenshot_options: Annotated[ScreenshotOptions, PropertyInfo(alias="screenshotOptions")]
    """Check [options](https://pptr.dev/api/puppeteer.screenshotoptions)."""

    scroll_page: Annotated[bool, PropertyInfo(alias="scrollPage")]

    selector: str

    set_extra_http_headers: Annotated[Dict[str, str], PropertyInfo(alias="setExtraHTTPHeaders")]

    set_java_script_enabled: Annotated[bool, PropertyInfo(alias="setJavaScriptEnabled")]

    url: str
    """URL to navigate to, eg. `https://example.com`."""

    user_agent: Annotated[str, PropertyInfo(alias="userAgent")]

    viewport: Viewport
    """Check [options](https://pptr.dev/api/puppeteer.page.setviewport)."""

    wait_for_selector: Annotated[WaitForSelector, PropertyInfo(alias="waitForSelector")]
    """Wait for the selector to appear in page.

    Check [options](https://pptr.dev/api/puppeteer.page.waitforselector).
    """

    wait_for_timeout: Annotated[float, PropertyInfo(alias="waitForTimeout")]
    """Waits for a specified timeout before continuing."""


class AddScriptTag(TypedDict, total=False):
    id: str

    content: str

    type: str

    url: str


class AddStyleTag(TypedDict, total=False):
    content: str

    url: str


class Authenticate(TypedDict, total=False):
    password: Required[str]

    username: Required[str]


class Cookie(TypedDict, total=False):
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


class GotoOptions(TypedDict, total=False):
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


class ScreenshotOptionsClip(TypedDict, total=False):
    height: Required[float]

    width: Required[float]

    x: Required[float]

    y: Required[float]

    scale: float


class ScreenshotOptions(TypedDict, total=False):
    capture_beyond_viewport: Annotated[bool, PropertyInfo(alias="captureBeyondViewport")]

    clip: ScreenshotOptionsClip

    encoding: Literal["binary", "base64"]

    from_surface: Annotated[bool, PropertyInfo(alias="fromSurface")]

    full_page: Annotated[bool, PropertyInfo(alias="fullPage")]

    omit_background: Annotated[bool, PropertyInfo(alias="omitBackground")]

    optimize_for_speed: Annotated[bool, PropertyInfo(alias="optimizeForSpeed")]

    quality: float

    type: Literal["png", "jpeg", "webp"]


class Viewport(TypedDict, total=False):
    height: Required[float]

    width: Required[float]

    device_scale_factor: Annotated[float, PropertyInfo(alias="deviceScaleFactor")]

    has_touch: Annotated[bool, PropertyInfo(alias="hasTouch")]

    is_landscape: Annotated[bool, PropertyInfo(alias="isLandscape")]

    is_mobile: Annotated[bool, PropertyInfo(alias="isMobile")]


class WaitForSelector(TypedDict, total=False):
    selector: Required[str]

    hidden: Literal[True]

    timeout: float

    visible: Literal[True]
