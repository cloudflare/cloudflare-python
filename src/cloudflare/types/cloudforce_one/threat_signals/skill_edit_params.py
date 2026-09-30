# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SkillEditParams"]


class SkillEditParams(TypedDict, total=False):
    account_id: Required[str]

    config: str

    is_active: bool

    name: str

    output_schema: str

    prompt: str
