# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .action_item_param import ActionItemParam
from .targes_item_param import TargesItemParam

__all__ = ["PageruleCreateParams"]


class PageruleCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    actions: Required[Iterable[ActionItemParam]]
    """The set of actions to perform if the targets of this rule match the request.

    Actions can redirect to another URL or override settings, but not both.
    """

    targets: Required[Iterable[TargesItemParam]]
    """The rule targets to evaluate on each request."""

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
