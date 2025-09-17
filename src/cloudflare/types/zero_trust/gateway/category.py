# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Category", "Subcategory"]


class Subcategory(BaseModel):
    id: Optional[int] = None
    """The identifier for this category. There is only one category per ID."""

    beta: Optional[bool] = None
    """True if the category is in beta and subject to change."""

    class_: Optional[Literal["free", "premium", "blocked", "removalPending", "noBlock"]] = FieldInfo(
        alias="class", default=None
    )
    """Which account types are allowed to create policies based on this category.

    `blocked` categories are blocked unconditionally for all accounts.
    `removalPending` categories can be removed from policies but not added.
    `noBlock` categories cannot be blocked.
    """

    description: Optional[str] = None
    """A short summary of domains in the category."""

    name: Optional[str] = None
    """The name of the category."""


class Category(BaseModel):
    id: Optional[int] = None
    """The identifier for this category. There is only one category per ID."""

    beta: Optional[bool] = None
    """True if the category is in beta and subject to change."""

    class_: Optional[Literal["free", "premium", "blocked", "removalPending", "noBlock"]] = FieldInfo(
        alias="class", default=None
    )
    """Which account types are allowed to create policies based on this category.

    `blocked` categories are blocked unconditionally for all accounts.
    `removalPending` categories can be removed from policies but not added.
    `noBlock` categories cannot be blocked.
    """

    description: Optional[str] = None
    """A short summary of domains in the category."""

    name: Optional[str] = None
    """The name of the category."""

    subcategories: Optional[List[Subcategory]] = None
    """All subcategories for this category."""
