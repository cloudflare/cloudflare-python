# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..filters.firewall_filter_param import FirewallFilterParam

__all__ = ["RuleCreateParams", "Action", "ActionResponse"]


class RuleCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    action: Required[Action]
    """
    The action to perform when the threshold of matched traffic within the
    configured period is exceeded.
    """

    filter: Required[FirewallFilterParam]


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
