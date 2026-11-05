# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr

__all__ = ["SkillUpdateParams"]


class SkillUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    skill_ids: Required[SequenceNotStr[str]]
    """Ordered array of Custom Skill UUIDs (max 20).

    Replaces the feed's custom skill assignments. Free accounts cannot assign custom
    skills. Managed default skills are unaffected.
    """
