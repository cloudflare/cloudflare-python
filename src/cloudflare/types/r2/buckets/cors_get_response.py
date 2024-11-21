# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CORSGetResponse", "Rule", "RuleAllowed"]


class RuleAllowed(BaseModel):
    methods: List[Literal["GET", "PUT", "POST", "DELETE", "HEAD"]]
    """
    Specifies the value for the Access-Control-Allow-Methods header R2 sets when
    requesting objects in a bucket from a browser.
    """

    origins: List[str]
    """
    Specifies the value for the Access-Control-Allow-Origin header R2 sets when
    requesting objects in a bucket from a browser.
    """

    headers: Optional[List[str]] = None
    """
    Specifies the value for the Access-Control-Allow-Headers header R2 sets when
    requesting objects in this bucket from a browser. Cross-origin requests that
    include custom headers (e.g. x-user-id) should specify these headers as
    AllowedHeaders.
    """


class Rule(BaseModel):
    allowed: RuleAllowed
    """Object specifying allowed origins, methods and headers for this CORS rule."""

    id: Optional[str] = None
    """Identifier for this rule"""

    expose_headers: Optional[List[str]] = FieldInfo(alias="exposeHeaders", default=None)
    """
    Specifies the headers that can be exposed back, and accessed by, the JavaScript
    making the cross-origin request. If you need to access headers beyond the
    safelisted response headers, such as Content-Encoding or cf-cache-status, you
    must specify it here.
    """

    max_age_seconds: Optional[float] = FieldInfo(alias="maxAgeSeconds", default=None)
    """
    Specifies the amount of time (in seconds) browsers are allowed to cache CORS
    preflight responses. Browsers may limit this to 2 hours or less, even if the
    maximum value (86400) is specified.
    """


class CORSGetResponse(BaseModel):
    rules: Optional[List[Rule]] = None
