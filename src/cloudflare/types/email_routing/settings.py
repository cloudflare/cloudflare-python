# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Settings"]


class Settings(BaseModel):
    id: Optional[str] = None
    """Email Routing settings identifier."""

    created: Optional[datetime] = None
    """The date and time the settings have been created."""

    enabled: Optional[Literal[True, False]] = None
    """State of the zone settings for Email Routing."""

    modified: Optional[datetime] = None
    """The date and time the settings have been modified."""

    name: Optional[str] = None
    """Domain of your zone."""

    skip_wizard: Optional[Literal[True, False]] = None
    """Flag to check if the user skipped the configuration wizard."""

    status: Optional[Literal["ready", "unconfigured", "misconfigured", "misconfigured/locked", "unlocked"]] = None
    """Show the state of your account, and the type or configuration error."""

    tag: Optional[str] = None
    """Email Routing settings tag.

    (Deprecated, replaced by Email Routing settings identifier)
    """
