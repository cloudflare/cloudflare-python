# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["QueryEditResponse"]


class QueryEditResponse(BaseModel):
    id: int
    """Unique identifier for the saved query"""

    account_id: int
    """Account ID"""

    alert_enabled: bool
    """Deprecated: saved-query alerting and rules were removed. Always false."""

    alert_rollup_enabled: bool
    """Deprecated: saved-query alerting and rules were removed. Always false."""

    created_at: str
    """Creation timestamp"""

    name: str
    """Name of the saved query"""

    query_json: str
    """JSON string containing the query parameters"""

    rule_enabled: bool
    """Deprecated: saved-query alerting and rules were removed. Always false."""

    updated_at: str
    """Last update timestamp"""

    user_email: str
    """Email of the user who created the query"""

    custom_threat_feed_id: Optional[int] = None
    """Deprecated: saved-query alerting and rules were removed. Always null."""

    rule_list_id: Optional[str] = None
    """Deprecated: saved-query alerting and rules were removed. Always null."""

    rule_scope: Optional[str] = None
    """Deprecated: saved-query alerting and rules were removed. Always null."""
