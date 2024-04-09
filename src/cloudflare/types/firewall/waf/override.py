# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .waf_rule import WAFRule
from ...._models import BaseModel
from .override_url import OverrideURL
from .rewrite_action import RewriteAction

__all__ = ["Override"]


class Override(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the WAF override."""

    description: Optional[str] = None
    """An informative summary of the current URI-based WAF override."""

    groups: Optional[Dict[str, object]] = None
    """
    An object that allows you to enable or disable WAF rule groups for the current
    WAF override. Each key of this object must be the ID of a WAF rule group, and
    each value must be a valid WAF action (usually `default` or `disable`). When
    creating a new URI-based WAF override, you must provide a `groups` object or a
    `rules` object.
    """

    paused: Optional[bool] = None
    """When true, indicates that the WAF package is currently paused."""

    priority: Optional[float] = None
    """
    The relative priority of the current URI-based WAF override when multiple
    overrides match a single URL. A lower number indicates higher priority. Higher
    priority overrides may overwrite values set by lower priority overrides.
    """

    rewrite_action: Optional[RewriteAction] = None
    """
    Specifies that, when a WAF rule matches, its configured action will be replaced
    by the action configured in this object.
    """

    rules: Optional[WAFRule] = None
    """An object that allows you to override the action of specific WAF rules.

    Each key of this object must be the ID of a WAF rule, and each value must be a
    valid WAF action. Unless you are disabling a rule, ensure that you also enable
    the rule group that this WAF rule belongs to. When creating a new URI-based WAF
    override, you must provide a `groups` object or a `rules` object.
    """

    urls: Optional[List[OverrideURL]] = None
    """The URLs to include in the current WAF override.

    You can use wildcards. Each entered URL will be escaped before use, which means
    you can only use simple wildcard patterns.
    """
