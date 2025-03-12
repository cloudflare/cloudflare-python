# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Stage"]


class Stage(BaseModel):
    ended_on: Optional[datetime] = None
    """When the stage ended."""

    name: Optional[Literal["queued", "initialize", "clone_repo", "build", "deploy"]] = None
    """The current build stage."""

    started_on: Optional[datetime] = None
    """When the stage started."""

    status: Optional[Literal["success", "idle", "active", "failure", "canceled"]] = None
    """State of the current stage."""
