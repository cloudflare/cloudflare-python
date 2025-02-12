# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Settings"]


class Settings(BaseModel):
    id: str
    """Email Routing settings identifier."""

    enabled: Literal[True, False]
    """State of the zone settings for Email Routing."""

    name: str
    """Domain of your zone."""

    created: Optional[datetime] = None
    """The date and time the settings have been created."""

    modified: Optional[datetime] = None
    """The date and time the settings have been modified."""

    skip_wizard: Optional[Literal[True, False]] = None
    """Flag to check if the user skipped the configuration wizard."""

    status: Optional[Literal["ready", "unconfigured", "misconfigured", "misconfigured/locked", "unlocked"]] = None
    """Show the state of your account, and the type or configuration error."""

    tag: Optional[str] = None
    """Email Routing settings tag.

    (Deprecated, replaced by Email Routing settings identifier)
    """
