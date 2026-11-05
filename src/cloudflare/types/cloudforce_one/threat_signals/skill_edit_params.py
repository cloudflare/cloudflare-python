# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SkillEditParams"]


class SkillEditParams(TypedDict, total=False):
    account_id: Required[str]

    config: str
    """Optional skill configuration (stored but not currently interpreted)."""

    is_active: bool
    """Whether the skill is active and eligible for feed assignment."""

    name: str
    """Custom Skill name (1–100 characters)."""

    output_schema: str
    """JSON Schema serialized as a string (max 4096 characters)."""

    prompt: str
    """AI prompt (1–4000 characters) defining the skill's instructions."""
