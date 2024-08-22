# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from .kind import Kind

from datetime import datetime

from .phase import Phase

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["VersionListResponse"]

class VersionListResponse(BaseModel):
    id: str
    """The unique ID of the ruleset."""

    kind: Kind
    """The kind of the ruleset."""

    last_updated: datetime
    """The timestamp of when the ruleset was last modified."""

    name: str
    """The human-readable name of the ruleset."""

    phase: Phase
    """The phase of the ruleset."""

    version: str
    """The version of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""