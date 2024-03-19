# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RuleDeleteParams"]


class RuleDeleteParams(TypedDict, total=False):
    zone_identifier: Required[str]
    """Identifier"""

    delete_filter_if_unused: bool
    """
    When true, indicates that Cloudflare should also delete the associated filter if
    there are no other firewall rules referencing the filter.
    """
