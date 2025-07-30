# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["TraceCreateParams", "Body", "Context", "ContextGeoloc"]


class TraceCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    method: Required[str]
    """HTTP Method of tracing request"""

    url: Required[str]
    """URL to which perform tracing request"""

    body: Body

    context: Context
    """Additional request parameters"""

    cookies: Dict[str, str]
    """Cookies added to tracing request"""

    headers: Dict[str, str]
    """Headers added to tracing request"""

    protocol: str
    """HTTP Protocol of tracing request"""

    skip_response: bool
    """Skip sending the request to the Origin server after all rules evaluation"""


class Body(TypedDict, total=False):
    base64: str
    """Base64 encoded request body"""

    json: object
    """Arbitrary json as request body"""

    plain_text: str
    """Request body as plain text"""


class ContextGeoloc(TypedDict, total=False):
    city: str

    continent: str

    is_eu_country: bool

    iso_code: str

    latitude: float

    longitude: float

    postal_code: str

    region_code: str

    subdivision_2_iso_code: str

    timezone: str


class Context(TypedDict, total=False):
    bot_score: int
    """Bot score used for evaluating tracing request processing"""

    geoloc: ContextGeoloc
    """Geodata for tracing request"""

    skip_challenge: bool
    """Whether to skip any challenges for tracing request (e.g.: captcha)"""

    threat_score: int
    """Threat score used for evaluating tracing request processing"""
