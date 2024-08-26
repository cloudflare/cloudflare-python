# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated, Literal

from typing import Union

from datetime import datetime

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["InvestigateListParams"]

class InvestigateListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    action_log: bool
    """Controls whether the message action log in included in the response."""

    alert_id: str

    detections_only: bool
    """If `false`, the search includes non-detections."""

    domain: str
    """Filter by the sender domain"""

    end: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """The end of the search date range. Defaults to `now`."""

    final_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK"]
    """Filter messages by the provided disposition."""

    message_action: Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"]
    """Filter messages by actions applied to them"""

    message_id: str

    metric: str

    page: int
    """Page number of paginated results."""

    per_page: int
    """Number of results to display."""

    query: str
    """Space delimited query term(s). The search is case-insensitive.

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

    start: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """The beginning of the search date range. Defaults to `now - 30 days`."""