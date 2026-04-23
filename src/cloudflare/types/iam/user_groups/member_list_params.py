# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MemberListParams"]


class MemberListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    direction: Literal["asc", "desc"]
    """The sort order of returned user group members by email."""

    fuzzy_email: Annotated[str, PropertyInfo(alias="fuzzyEmail")]
    """A string used for filtering members by partial email match."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""
