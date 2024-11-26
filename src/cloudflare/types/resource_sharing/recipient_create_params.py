# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RecipientCreateParams"]


class RecipientCreateParams(TypedDict, total=False):
    path_account_id: Required[Annotated[str, PropertyInfo(alias="account_id")]]
    """Account identifier."""

    body_account_id: Annotated[str, PropertyInfo(alias="account_id")]
    """Account identifier."""

    organization_id: str
    """Organization identifier."""
