# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["QueryResult", "Meta", "MetaTimings"]


class MetaTimings(BaseModel):
    sql_duration_ms: Optional[float] = None
    """The duration of the SQL query execution inside the database.

    Does not include any network communication.
    """


class Meta(BaseModel):
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

    timings: Optional[MetaTimings] = None
    """Various durations for the query."""


class QueryResult(BaseModel):
    meta: Optional[Meta] = None

    results: Optional[List[object]] = None

    success: Optional[bool] = None
