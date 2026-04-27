# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InvestigateListParams"]


class InvestigateListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    action_log: bool
    """Whether to include the message action log in the response."""

    alert_id: str

    cursor: str

    detections_only: bool
    """Whether to include only detections in search results."""

    domain: str
    """Sender domains to filter by."""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end of the search date range. Defaults to `now`."""

    final_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]
    """Dispositions to filter by."""

    message_action: Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"]
    """Message actions to filter by."""

    message_id: str

    metric: str

    page: Optional[int]
    """Deprecated: Use cursor pagination instead. End of life: November 1, 2026."""

    per_page: int
    """The number of results per page. Maximum value is 1000."""

    query: str
    """Space-delimited search term. Case-insensitive."""

    recipient: str

    sender: str

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The beginning of the search date range. Defaults to `now - 30 days`."""

    subject: str
