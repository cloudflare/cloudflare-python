# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["UserGetParams"]


class UserGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    user_population_id: Required[str]
    """UUID."""

    attributes: str
    """Comma-separated SCIM attributes to return."""

    excluded_attributes: Annotated[str, PropertyInfo(alias="excludedAttributes")]
    """Comma-separated SCIM attributes to exclude from the response."""
