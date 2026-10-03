# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["SkillGetResponse", "Skill"]


class Skill(BaseModel):
    id: str

    config: Optional[str] = None
    """JSON-encoded skill configuration. Always null for default skills."""

    created_at: str

    is_active: int
    """1 when active, 0 when inactive."""

    name: str

    output_schema: Optional[str] = None
    """JSON-encoded JSON Schema the skill output must satisfy."""

    prompt: str

    source: Literal["default", "custom"]
    """
    `default` for Cloudforce One managed skills (read-only), `custom` for account
    skills.
    """

    type: str

    updated_at: str


class SkillGetResponse(BaseModel):
    feed_id: str

    skills: List[Skill]
