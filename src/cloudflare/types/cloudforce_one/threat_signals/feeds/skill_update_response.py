# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["SkillUpdateResponse", "Skill"]


class Skill(BaseModel):
    position: int
    """Zero-based pipeline position."""

    skill_id: str


class SkillUpdateResponse(BaseModel):
    feed_id: str

    skills: List[Skill]
