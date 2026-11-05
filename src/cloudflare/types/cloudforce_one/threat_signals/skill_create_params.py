# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SkillCreateParams"]


class SkillCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """Custom Skill name (1–100 characters)."""

    output_schema: Required[str]
    """JSON Schema serialized as a string (max 4096 characters)."""

    prompt: Required[str]
    """AI prompt (1–4000 characters) defining the skill's instructions."""

    type: Literal["summary", "tags"]
    """Optional label; does not affect execution. Defaults to "summary"."""
