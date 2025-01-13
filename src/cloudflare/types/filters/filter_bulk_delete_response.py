# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .firewall_filter import FirewallFilter

__all__ = ["FilterBulkDeleteResponse"]

FilterBulkDeleteResponse: TypeAlias = List[FirewallFilter]
