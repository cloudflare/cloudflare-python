# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .firewall_rule import FirewallRule

__all__ = ["RuleBulkDeleteResponse"]

RuleBulkDeleteResponse: TypeAlias = List[FirewallRule]
