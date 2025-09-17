# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Category", "Subcategory"]


class Subcategory(BaseModel):
    id: Optional[int] = None
    """Identify this category. Only one category per ID."""

    beta: Optional[bool] = None
    """Indicate whether the category is in beta and subject to change."""

    class_: Optional[Literal["free", "premium", "blocked", "removalPending", "noBlock"]] = FieldInfo(
        alias="class", default=None
    )
    """Specify which account types can create policies for this category.

    `blocked` Blocks unconditionally for all accounts. `removalPending` Allows
    removal from policies but disables addition. `noBlock` Prevents blocking.
    """

    description: Optional[str] = None
    """Provide a short summary of domains in the category."""

    name: Optional[str] = None
    """Specify the category name."""


class Category(BaseModel):
    id: Optional[int] = None
    """Identify this category. Only one category per ID."""

    beta: Optional[bool] = None
    """Indicate whether the category is in beta and subject to change."""

    class_: Optional[Literal["free", "premium", "blocked", "removalPending", "noBlock"]] = FieldInfo(
        alias="class", default=None
    )
    """Specify which account types can create policies for this category.

    `blocked` Blocks unconditionally for all accounts. `removalPending` Allows
    removal from policies but disables addition. `noBlock` Prevents blocking.
    """

    description: Optional[str] = None
    """Provide a short summary of domains in the category."""

    name: Optional[str] = None
    """Specify the category name."""

    subcategories: Optional[List[Subcategory]] = None
    """Provide all subcategories for this category."""
