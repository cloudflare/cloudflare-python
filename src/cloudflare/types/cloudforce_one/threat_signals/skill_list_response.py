# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SkillListResponse", "Skill"]


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


class SkillListResponse(BaseModel):
    count: int
    """Number of skills on this page."""

    custom_skills_available: bool
    """
    Whether the authenticated account may access custom-skill capabilities under
    Stakeout's Threat Signals access-mode policy. This is a policy availability
    indicator, not a row-existence indicator. False for threat_signals_only mode;
    true for entitled, allowlisted, cfone_internal, and service modes.
    """

    page: int

    per_page: int

    skills: List[Skill]

    total_count: int
