# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .methods import Methods

__all__ = ["RateLimitEditParams", "Action", "ActionResponse", "Match", "MatchHeader", "MatchRequest", "MatchResponse"]


class RateLimitEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    action: Required[Action]
    """
    The action to perform when the threshold of matched traffic within the
    configured period is exceeded.
    """

    match: Required[Match]
    """Determines which traffic the rate limit counts towards the threshold."""

    period: Required[float]
    """The time in seconds (an integer value) to count matching traffic.

    If the count exceeds the configured threshold within this period, Cloudflare
    will perform the configured action.
    """

    threshold: Required[float]
    """The threshold that will trigger the configured mitigation action.

    Configure this value along with the `period` property to establish a threshold
    per period.
    """


class ActionResponse(TypedDict, total=False):
    body: str
    """The response body to return.

    The value must conform to the configured content type.
    """

    content_type: str
    """The content type of the body.

    Must be one of the following: `text/plain`, `text/xml`, or `application/json`.
    """


class Action(TypedDict, total=False):
    mode: Literal["simulate", "ban", "challenge", "js_challenge", "managed_challenge"]
    """The action to perform."""

    response: ActionResponse
    """A custom content type and reponse to return when the threshold is exceeded.

    The custom response configured in this object will override the custom error for
    the zone. This object is optional. Notes: If you omit this object, Cloudflare
    will use the default HTML error page. If "mode" is "challenge",
    "managed_challenge", or "js_challenge", Cloudflare will use the zone challenge
    pages and you should not provide the "response" object.
    """

    timeout: float
    """The time in seconds during which Cloudflare will perform the mitigation action.

    Must be an integer value greater than or equal to the period. Notes: If "mode"
    is "challenge", "managed_challenge", or "js_challenge", Cloudflare will use the
    zone's Challenge Passage time and you should not provide this value.
    """


class MatchHeader(TypedDict, total=False):
    name: str
    """The name of the response header to match."""

    op: Literal["eq", "ne"]
    """The operator used when matching: `eq` means "equal" and `ne` means "not equal"."""

    value: str
    """The value of the response header, which must match exactly."""


class MatchRequest(TypedDict, total=False):
    methods: List[Methods]
    """The HTTP methods to match.

    You can specify a subset (for example, `['POST','PUT']`) or all methods
    (`['_ALL_']`). This field is optional when creating a rate limit.
    """

    schemes: List[str]
    """The HTTP schemes to match.

    You can specify one scheme (`['HTTPS']`), both schemes (`['HTTP','HTTPS']`), or
    all schemes (`['_ALL_']`). This field is optional.
    """

    url: str
    """
    The URL pattern to match, composed of a host and a path such as
    `example.org/path*`. Normalization is applied before the pattern is matched. `*`
    wildcards are expanded to match applicable traffic. Query strings are not
    matched. Set the value to `*` to match all traffic to your zone.
    """


class MatchResponse(TypedDict, total=False):
    origin_traffic: bool
    """
    When true, only the uncached traffic served from your origin servers will count
    towards rate limiting. In this case, any cached traffic served by Cloudflare
    will not count towards rate limiting. This field is optional. Notes: This field
    is deprecated. Instead, use response headers and set "origin_traffic" to "false"
    to avoid legacy behaviour interacting with the "response_headers" property.
    """


class Match(TypedDict, total=False):
    headers: Iterable[MatchHeader]

    request: MatchRequest

    response: MatchResponse
