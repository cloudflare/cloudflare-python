# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RecipientCreateParams"]


class RecipientCreateParams(TypedDict, total=False):
    account_id_1: Required[Annotated[str, PropertyInfo(alias="account_id")]]
    """Account identifier."""

    account_id_2: Annotated[str, PropertyInfo(alias="account_id")]
    """Account identifier."""

    organization_id: str
    """Organization identifier."""
