# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["SkillOutputGetResponse"]


class SkillOutputGetResponse(BaseModel):
    article_id: str

    custom_skill_version: Optional[str] = None

    output_schema: Optional[str] = None
    """JSON-encoded output schema of the skill. Null when the skill no longer exists."""

    skill_id: str

    custom_output: Optional[object] = None
    """Skill output.

    Parsed JSON when the stored output is valid JSON, otherwise the raw string.
    """
