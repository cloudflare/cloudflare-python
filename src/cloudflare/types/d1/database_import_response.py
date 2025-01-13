# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DatabaseImportResponse", "Result", "ResultMeta"]


class ResultMeta(BaseModel):
    changed_db: Optional[bool] = None

    changes: Optional[float] = None

    duration: Optional[float] = None

    last_row_id: Optional[float] = None

    rows_read: Optional[float] = None

    rows_written: Optional[float] = None

    size_after: Optional[float] = None


class Result(BaseModel):
    final_bookmark: Optional[str] = None
    """
    The time-travel bookmark if you need restore your D1 to directly after the
    import succeeded.
    """

    meta: Optional[ResultMeta] = None

    num_queries: Optional[float] = None
    """The total number of queries that were executed during the import."""


class DatabaseImportResponse(BaseModel):
    at_bookmark: Optional[str] = None
    """The current time-travel bookmark for your D1, used to poll for updates.

    Will not change for the duration of the import. Only returned if an import
    process is currently running or recently finished.
    """

    error: Optional[str] = None
    """Only present when status = 'error'.

    Contains the error message that prevented the import from succeeding.
    """

    filename: Optional[str] = None
    """Derived from the database ID and etag, to use in avoiding repeated uploads.

    Only returned when for the 'init' action.
    """

    messages: Optional[List[str]] = None
    """Logs since the last time you polled"""

    result: Optional[Result] = None
    """Only present when status = 'complete'"""

    status: Optional[Literal["complete", "error"]] = None

    success: Optional[bool] = None

    type: Optional[Literal["import"]] = None

    upload_url: Optional[str] = None
    """The R2 presigned URL to use for uploading.

    Only returned when for the 'init' action.
    """
