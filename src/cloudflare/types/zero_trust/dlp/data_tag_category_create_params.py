# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DataTagCategoryCreateParams", "Tag"]


class DataTagCategoryCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    description: Optional[str]

    tags: Iterable[Tag]
    """Tags to create with the category. Mutually exclusive with `template_id`."""

    template_id: Optional[str]


class Tag(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]
