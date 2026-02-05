# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ScriptSearchResponse", "ScriptSearchResponseItem"]


class ScriptSearchResponseItem(BaseModel):
    created_on: datetime
    """When the script was created."""

    modified_on: datetime
    """When the script was last modified."""

    script_name: str
    """Name of the script, used in URLs and route configuration."""

    script_tag: str
    """Identifier."""

    environment_is_default: Optional[bool] = None
    """Whether the environment is the default environment."""

    environment_name: Optional[str] = None
    """Name of the environment."""

    service_name: Optional[str] = None
    """Name of the service."""


ScriptSearchResponse: TypeAlias = List[ScriptSearchResponseItem]
