# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .action import Action
from .._models import BaseModel
from .methods_item import MethodsItem

__all__ = ["RateLimitListResponse", "Bypass", "Match", "MatchHeader", "MatchRequest", "MatchResponse"]


class Bypass(BaseModel):
    name: Optional[Literal["url"]] = None

    value: Optional[str] = None
    """The URL to bypass."""


class MatchHeader(BaseModel):
    name: Optional[str] = None
    """The name of the response header to match."""

    op: Optional[Literal["eq", "ne"]] = None
    """The operator used when matching: `eq` means "equal" and `ne` means "not equal"."""

    value: Optional[str] = None
    """The value of the response header, which must match exactly."""


class MatchRequest(BaseModel):
    methods: Optional[List[MethodsItem]] = None
    """The HTTP methods to match.

    You can specify a subset (for example, `['POST','PUT']`) or all methods
    (`['_ALL_']`). This field is optional when creating a rate limit.
    """

    schemes: Optional[List[str]] = None
    """The HTTP schemes to match.

    You can specify one scheme (`['HTTPS']`), both schemes (`['HTTP','HTTPS']`), or
    all schemes (`['_ALL_']`). This field is optional.
    """

    url: Optional[str] = None
    """
    The URL pattern to match, composed of a host and a path such as
    `example.org/path*`. Normalization is applied before the pattern is matched. `*`
    wildcards are expanded to match applicable traffic. Query strings are not
    matched. Set the value to `*` to match all traffic to your zone.
    """


class MatchResponse(BaseModel):
    origin_traffic: Optional[bool] = None
    """
    When true, only the uncached traffic served from your origin servers will count
    towards rate limiting. In this case, any cached traffic served by Cloudflare
    will not count towards rate limiting. This field is optional. Notes: This field
    is deprecated. Instead, use response headers and set "origin_traffic" to "false"
    to avoid legacy behaviour interacting with the "response_headers" property.
    """


class Match(BaseModel):
    headers: Optional[List[MatchHeader]] = None

    request: Optional[MatchRequest] = None

    response: Optional[MatchResponse] = None


class RateLimitListResponse(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the rate limit."""

    action: Optional[Action] = None
    """
    The action to perform when the threshold of matched traffic within the
    configured period is exceeded.
    """

    bypass: Optional[List[Bypass]] = None
    """Criteria specifying when the current rate limit should be bypassed.

    You can specify that the rate limit should not apply to one or more URLs.
    """

    description: Optional[str] = None
    """An informative summary of the rate limit.

    This value is sanitized and any tags will be removed.
    """

    disabled: Optional[bool] = None
    """When true, indicates that the rate limit is currently disabled."""

    match: Optional[Match] = None
    """Determines which traffic the rate limit counts towards the threshold."""

    period: Optional[float] = None
    """The time in seconds (an integer value) to count matching traffic.

    If the count exceeds the configured threshold within this period, Cloudflare
    will perform the configured action.
    """

    threshold: Optional[float] = None
    """The threshold that will trigger the configured mitigation action.

    Configure this value along with the `period` property to establish a threshold
    per period.
    """
