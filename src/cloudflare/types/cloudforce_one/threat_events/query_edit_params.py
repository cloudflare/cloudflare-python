# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QueryEditParams"]


class QueryEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    alert_enabled: bool
    """Enable alerts for this query"""

    alert_rollup_enabled: bool
    """Enable alert rollup for this query"""

    name: str
    """Unique name for the saved query"""

    query_json: str
    """JSON string containing the query parameters"""

    rule_enabled: bool
    """Enable rule for this query"""

    rule_scope: str
    """Scope for the rule"""
