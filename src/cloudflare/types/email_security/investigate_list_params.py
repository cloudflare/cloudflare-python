# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InvestigateListParams"]


class InvestigateListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    action_log: bool
    """Determines if the message action log is included in the response."""

    alert_id: str

    detections_only: bool
    """Determines if the search results will include detections or not."""

    domain: str
    """The sender domains the search filters by."""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end of the search date range. Defaults to `now`."""

    final_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]
    """The dispositions the search filters by."""

    message_action: Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"]
    """The message actions the search filters by."""

    message_id: str

    metric: str

    page: int
    """The page number of paginated results."""

    per_page: int
    """The number of results per page."""

    query: str
    """The space-delimited term used in the query. The search is case-insensitive.

    The content of the following email metadata fields are searched:

    - alert_id
    - CC
    - From (envelope_from)
    - From Name
    - final_disposition
    - md5 hash (of any attachment)
    - sha1 hash (of any attachment)
    - sha256 hash (of any attachment)
    - name (of any attachment)
    - Reason
    - Received DateTime (yyyy-mm-ddThh:mm:ss)
    - Sent DateTime (yyyy-mm-ddThh:mm:ss)
    - ReplyTo
    - To (envelope_to)
    - To Name
    - Message-ID
    - smtp_helo_server_ip
    - smtp_previous_hop_ip
    - x_originating_ip
    - Subject
    """

    recipient: str

    sender: str

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The beginning of the search date range. Defaults to `now - 30 days`."""
