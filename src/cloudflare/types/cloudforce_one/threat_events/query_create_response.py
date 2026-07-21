# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["QueryCreateResponse"]


class QueryCreateResponse(BaseModel):
    id: int
    """Unique identifier for the saved query"""

    account_id: int
    """Account ID"""

    alert_enabled: bool
    """Whether alerts are enabled"""

    alert_rollup_enabled: bool
    """Whether alert rollup is enabled"""

    created_at: str
    """Creation timestamp"""

    name: str
    """Name of the saved query"""

    query_json: str
    """JSON string containing the query parameters"""

    rule_enabled: bool
    """Whether rule is enabled"""

    updated_at: str
    """Last update timestamp"""

    user_email: str
    """Email of the user who created the query"""

    custom_threat_feed_id: Optional[int] = None
    """Intel Indicator Feed ID (numeric)"""

    rule_list_id: Optional[str] = None
    """WAF rules list ID for blocking"""

    rule_scope: Optional[str] = None
    """Scope for the rule"""
