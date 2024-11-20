# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .target import Target
from ..._models import BaseModel

__all__ = ["PageRule", "Action", "ActionValue"]


class ActionValue(BaseModel):
    status_code: Optional[Literal[301, 302]] = None
    """The status code to use for the URL redirect.

    301 is a permanent redirect. 302 is a temporary redirect.
    """

    url: Optional[str] = None
    """
    The URL to redirect the request to. Notes: ${num} refers to the position of '\\**'
    in the constraint value.
    """


class Action(BaseModel):
    id: Optional[Literal["forwarding_url"]] = None
    """Redirects one URL to another using an `HTTP 301/302` redirect.

    Refer to
    [Wildcard matching and referencing](https://developers.cloudflare.com/rules/page-rules/reference/wildcard-matching/).
    """

    value: Optional[ActionValue] = None


class PageRule(BaseModel):
    id: str
    """Identifier"""

    actions: List[Action]
    """The set of actions to perform if the targets of this rule match the request.

    Actions can redirect to another URL or override settings, but not both.
    """

    created_on: datetime
    """The timestamp of when the Page Rule was created."""

    modified_on: datetime
    """The timestamp of when the Page Rule was last modified."""

    priority: int
    """
    The priority of the rule, used to define which Page Rule is processed over
    another. A higher number indicates a higher priority. For example, if you have a
    catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to
    take precedence (rule B: `/images/special/*`), specify a higher priority for
    rule B so it overrides rule A.
    """

    status: Literal["active", "disabled"]
    """The status of the Page Rule."""

    targets: List[Target]
    """The rule targets to evaluate on each request."""
