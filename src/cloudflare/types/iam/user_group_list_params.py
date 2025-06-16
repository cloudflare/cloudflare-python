# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserGroupListParams"]


class UserGroupListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    id: str
    """ID of the user group to be fetched."""

    direction: str
    """The sort order of returned user groups by name.

    Default sort order is ascending. To switch to descending, set this parameter to
    "desc"
    """

    fuzzy_name: Annotated[str, PropertyInfo(alias="fuzzyName")]
    """A string used for searching for user groups containing that substring."""

    name: str
    """Name of the user group to be fetched."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""
