# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ModelListParams"]


class ModelListParams(TypedDict, total=False):
    account_id: Required[str]

    author: str
    """Filter by Author"""

    format: Literal["openrouter"]
    """
    If set, return models in the requested marketplace format instead of the default
    response.
    """

    hide_experimental: bool
    """Filter to hide experimental models"""

    page: int

    per_page: int

    search: str
    """Search"""

    source: float
    """Filter by Source Id"""

    task: str
    """Filter by Task Name"""
