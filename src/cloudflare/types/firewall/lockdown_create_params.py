# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .waf.override_url import OverrideURL
from .configuration_param import ConfigurationParam

__all__ = ["LockdownCreateParams"]


class LockdownCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier."""

    configurations: Required[ConfigurationParam]
    """
    A list of IP addresses or CIDR ranges that will be allowed to access the URLs
    specified in the Zone Lockdown rule. You can include any number of `ip` or
    `ip_range` configurations.
    """

    urls: Required[List[OverrideURL]]
    """The URLs to include in the current WAF override.

    You can use wildcards. Each entered URL will be escaped before use, which means
    you can only use simple wildcard patterns.
    """

    description: str
    """An informative summary of the rate limit.

    This value is sanitized and any tags will be removed.
    """

    paused: bool
    """When true, indicates that the rule is currently paused."""

    priority: float
    """The priority of the rule to control the processing order.

    A lower number indicates higher priority. If not provided, any rules with a
    configured priority will be processed before rules without a priority.
    """
