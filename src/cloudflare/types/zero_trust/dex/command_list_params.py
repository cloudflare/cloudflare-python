# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CommandListParams"]


class CommandListParams(TypedDict, total=False):
    account_id: Required[str]

    page: Required[float]
    """Page number for pagination"""

    per_page: Required[float]
    """Number of results per page"""

    command_type: str
    """Optionally filter executed commands by command type"""

    device_id: str
    """Unique identifier for a device"""

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Start time for the query in ISO (RFC3339 - ISO 8601) format"""

    status: Literal["PENDING_EXEC", "PENDING_UPLOAD", "SUCCESS", "FAILED"]
    """Optionally filter executed commands by status"""

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End time for the query in ISO (RFC3339 - ISO 8601) format"""

    user_email: str
    """Email tied to the device"""
