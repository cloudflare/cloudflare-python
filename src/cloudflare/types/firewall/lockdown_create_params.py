# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .waf.override_url import OverrideURL
from .configuration_param import ConfigurationParam

__all__ = ["LockdownCreateParams"]


class LockdownCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

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
