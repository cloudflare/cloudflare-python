# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable

from .route_param import RouteParam

from .target_param import TargetParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["PageruleUpdateParams"]


class PageruleUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    actions: Required[Iterable[RouteParam]]
    """The set of actions to perform if the targets of this rule match the request.

    Actions can redirect to another URL or override settings, but not both.
    """

    targets: Required[Iterable[TargetParam]]
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
