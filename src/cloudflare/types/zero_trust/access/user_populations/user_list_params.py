# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    attributes: str
    """Comma-separated SCIM attributes to return."""

    count: int
    """The maximum number of results to return."""

    excluded_attributes: Annotated[str, PropertyInfo(alias="excludedAttributes")]
    """Comma-separated SCIM attributes to exclude from the response."""

    filter: str
    """A SCIM filter expression."""

    start_index: Annotated[int, PropertyInfo(alias="startIndex")]
    """The 1-based index of the first result to return."""
