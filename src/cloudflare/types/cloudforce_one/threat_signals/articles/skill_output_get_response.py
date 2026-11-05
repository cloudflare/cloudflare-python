# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["SkillOutputGetResponse"]


class SkillOutputGetResponse(BaseModel):
    article_id: str
    """Article UUID that received the skill output."""

    custom_output: Union[str, float, bool, Dict[str, object], List[Union[str, float, bool, Dict[str, object]]]]
    """
    Untrusted model output: parsed JSON when the stored completion text is valid
    JSON, otherwise raw text. Consumers must safely render or escape it.
    """

    custom_output_parse_status: Literal["parsed", "invalid_json"]
    """Whether custom_output was parsed from the stored completion text."""

    custom_output_validation_status: Literal["valid", "invalid_json", "schema_invalid", "unknown"]
    """Non-blocking validation classification for untrusted model output.

    `unknown` is retained only for historical rows.
    """

    custom_skill_version: Optional[str] = None
    """Custom Skill version that produced the output.

    Null when historical metadata is unavailable.
    """

    output_schema: Optional[str] = None
    """JSON-encoded output schema. Null when historical skill metadata is unavailable."""

    skill_id: str
    """Custom Skill UUID that produced the output."""
