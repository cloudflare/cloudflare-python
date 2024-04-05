# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Action", "Response"]


class Response(BaseModel):
    body: Optional[str] = None
    """The response body to return.

    The value must conform to the configured content type.
    """

    content_type: Optional[str] = None
    """The content type of the body.

    Must be one of the following: `text/plain`, `text/xml`, or `application/json`.
    """


class Action(BaseModel):
    mode: Optional[Literal["simulate", "ban", "challenge", "js_challenge", "managed_challenge"]] = None
    """The action to perform."""

    response: Optional[Response] = None
    """A custom content type and reponse to return when the threshold is exceeded.

    The custom response configured in this object will override the custom error for
    the zone. This object is optional. Notes: If you omit this object, Cloudflare
    will use the default HTML error page. If "mode" is "challenge",
    "managed_challenge", or "js_challenge", Cloudflare will use the zone challenge
    pages and you should not provide the "response" object.
    """

    timeout: Optional[float] = None
    """The time in seconds during which Cloudflare will perform the mitigation action.

    Must be an integer value greater than or equal to the period. Notes: If "mode"
    is "challenge", "managed_challenge", or "js_challenge", Cloudflare will use the
    zone's Challenge Passage time and you should not provide this value.
    """
