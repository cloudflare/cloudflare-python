# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DatabaseExportResponse", "Result"]


class Result(BaseModel):
    filename: Optional[str] = None
    """The generated SQL filename."""

    signed_url: Optional[str] = None
    """The URL to download the exported SQL. Available for one hour."""


class DatabaseExportResponse(BaseModel):
    at_bookmark: Optional[str] = None
    """The current time-travel bookmark for your D1, used to poll for updates.

    Will not change for the duration of the export task.
    """

    error: Optional[str] = None
    """Only present when status = 'error'. Contains the error message."""

    messages: Optional[List[str]] = None
    """Logs since the last time you polled"""

    result: Optional[Result] = None
    """Only present when status = 'complete'"""

    status: Optional[Literal["complete", "error"]] = None

    success: Optional[bool] = None

    type: Optional[Literal["export"]] = None
