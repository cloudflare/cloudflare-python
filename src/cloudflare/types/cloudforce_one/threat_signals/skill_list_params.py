# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SkillListParams"]


class SkillListParams(TypedDict, total=False):
    account_id: Required[str]

    page: int
    """Page number (≥ 1, default 1)."""

    per_page: int
    """Results per page (1–100, default 20)."""
