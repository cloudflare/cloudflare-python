# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QueryCreateParams"]


class QueryCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    name: Required[str]
    """Unique name for the saved query"""

    query_json: Required[str]
    """JSON string containing the query parameters"""

    alert_enabled: bool
    """Deprecated and ignored: saved-query alerting and rules were removed."""

    alert_rollup_enabled: bool
    """Deprecated and ignored: saved-query alerting and rules were removed."""

    rule_enabled: bool
    """Deprecated and ignored: saved-query alerting and rules were removed."""

    rule_scope: str
    """Deprecated and ignored: saved-query alerting and rules were removed."""
