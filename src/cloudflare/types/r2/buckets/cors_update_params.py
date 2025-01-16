# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CORSUpdateParams", "Rule", "RuleAllowed"]


class CORSUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    rules: Iterable[Rule]

    jurisdiction: Annotated[Literal["default", "eu", "fedramp"], PropertyInfo(alias="cf-r2-jurisdiction")]
    """The bucket jurisdiction"""


class RuleAllowed(TypedDict, total=False):
    methods: Required[List[Literal["GET", "PUT", "POST", "DELETE", "HEAD"]]]
    """
    Specifies the value for the Access-Control-Allow-Methods header R2 sets when
    requesting objects in a bucket from a browser.
    """

    origins: Required[List[str]]
    """
    Specifies the value for the Access-Control-Allow-Origin header R2 sets when
    requesting objects in a bucket from a browser.
    """

    headers: List[str]
    """
    Specifies the value for the Access-Control-Allow-Headers header R2 sets when
    requesting objects in this bucket from a browser. Cross-origin requests that
    include custom headers (e.g. x-user-id) should specify these headers as
    AllowedHeaders.
    """


class Rule(TypedDict, total=False):
    allowed: Required[RuleAllowed]
    """Object specifying allowed origins, methods and headers for this CORS rule."""

    id: str
    """Identifier for this rule"""

    expose_headers: Annotated[List[str], PropertyInfo(alias="exposeHeaders")]
    """
    Specifies the headers that can be exposed back, and accessed by, the JavaScript
    making the cross-origin request. If you need to access headers beyond the
    safelisted response headers, such as Content-Encoding or cf-cache-status, you
    must specify it here.
    """

    max_age_seconds: Annotated[float, PropertyInfo(alias="maxAgeSeconds")]
    """
    Specifies the amount of time (in seconds) browsers are allowed to cache CORS
    preflight responses. Browsers may limit this to 2 hours or less, even if the
    maximum value (86400) is specified.
    """
