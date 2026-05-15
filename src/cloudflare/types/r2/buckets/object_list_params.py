# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ObjectListParams"]


class ObjectListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    cursor: str
    """Pagination cursor received from a previous List Objects call.

    Used to retrieve the next page of results.
    """

    delimiter: str
    """A single character used to group keys.

    All keys that contain the delimiter between the prefix and the first occurrence
    of the delimiter after the prefix are grouped under a single result element.
    """

    per_page: int
    """Maximum number of objects to return per page."""

    prefix: str
    """
    Restricts results to only those objects whose keys begin with the specified
    prefix.
    """

    start_after: str
    """
    Returns objects with keys that come after the specified key in lexicographic
    order.
    """

    jurisdiction: Annotated[Literal["default", "eu", "fedramp"], PropertyInfo(alias="cf-r2-jurisdiction")]
    """Jurisdiction where objects in this bucket are guaranteed to be stored."""
