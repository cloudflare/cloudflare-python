# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AuditHistoryParams"]


class AuditHistoryParams(TypedDict, total=False):
    organization_id: Required[str]
    """The unique ID that identifies the organization."""

    action_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC3339 timestamp of the source audit log entry's action time.

    Used to narrow the source-entry lookup window. Provide the `action.time` value
    from the audit log identified by `id`.
    """

    before: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Limits the returned results to logs older than the specified date.

    This can be a date string 2019-04-30 (interpreted in UTC) or an absolute
    timestamp that conforms to RFC3339.
    """

    since: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Limits the returned results to logs newer than the specified date.

    This can be a date string 2019-04-30 (interpreted in UTC) or an absolute
    timestamp that conforms to RFC3339.
    """

    cursor: str
    """The cursor is an opaque token used to paginate through large sets of records.

    It indicates the position from which to continue when requesting the next set of
    records. A valid cursor value can be obtained from the cursor object in the
    result_info structure of a previous response.
    """

    direction: Literal["desc", "asc"]
    """Sets sorting order."""

    limit: float
    """The number limits the objects to return.

    The cursor attribute may be used to iterate over the next batch of objects if
    there are more than the limit.
    """
