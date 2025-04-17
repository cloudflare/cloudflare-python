# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DatabaseImportResponse", "Result", "ResultMeta", "ResultMetaTimings"]


class ResultMetaTimings(BaseModel):
    sql_duration_ms: Optional[float] = None
    """The duration of the SQL query execution inside the database.

    Does not include any network communication.
    """


class ResultMeta(BaseModel):
    changed_db: Optional[bool] = None
    """Denotes if the database has been altered in some way, like deleting rows."""

    changes: Optional[float] = None
    """
    Rough indication of how many rows were modified by the query, as provided by
    SQLite's `sqlite3_total_changes()`.
    """

    duration: Optional[float] = None
    """The duration of the SQL query execution inside the database.

    Does not include any network communication.
    """

    last_row_id: Optional[float] = None
    """
    The row ID of the last inserted row in a table with an `INTEGER PRIMARY KEY` as
    provided by SQLite. Tables created with `WITHOUT ROWID` do not populate this.
    """

    rows_read: Optional[float] = None
    """
    Number of rows read during the SQL query execution, including indices (not all
    rows are necessarily returned).
    """

    rows_written: Optional[float] = None
    """Number of rows written during the SQL query execution, including indices."""

    served_by_primary: Optional[bool] = None
    """Denotes if the query has been handled by the database primary instance."""

    served_by_region: Optional[Literal["WNAM", "ENAM", "WEUR", "EEUR", "APAC", "OC"]] = None
    """Region location hint of the database instance that handled the query."""

    size_after: Optional[float] = None
    """Size of the database after the query committed, in bytes."""

    timings: Optional[ResultMetaTimings] = None
    """Various durations for the query."""


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
