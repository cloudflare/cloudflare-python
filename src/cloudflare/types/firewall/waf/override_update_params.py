# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from ...._utils import PropertyInfo

from .rewrite_action_param import RewriteActionParam

from .waf_rule_param import WAFRuleParam

from typing import List

from .override_url import OverrideURL

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["OverrideUpdateParams"]

class OverrideUpdateParams(TypedDict, total=False):
    path_id: Required[Annotated[str, PropertyInfo(alias="id")]]
    """The unique identifier of the WAF override."""

    body_id: Required[Annotated[str, PropertyInfo(alias="id")]]
    """Identifier"""

    rewrite_action: Required[RewriteActionParam]
    """
    Specifies that, when a WAF rule matches, its configured action will be replaced
    by the action configured in this object.
    """

    rules: Required[WAFRuleParam]
    """An object that allows you to override the action of specific WAF rules.

    Each key of this object must be the ID of a WAF rule, and each value must be a
    valid WAF action. Unless you are disabling a rule, ensure that you also enable
    the rule group that this WAF rule belongs to. When creating a new URI-based WAF
    override, you must provide a `groups` object or a `rules` object.
    """

    urls: Required[List[OverrideURL]]
    """The URLs to include in the current WAF override.

    You can use wildcards. Each entered URL will be escaped before use, which means
    you can only use simple wildcard patterns.
    """