# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["KeyCreateResponse"]


class KeyCreateResponse(BaseModel):
    created: Optional[datetime] = None
    """The date and time the item was created."""

    key: Optional[str] = None
    """Bearer token"""

    modified: Optional[datetime] = None
    """The date and time the item was last modified."""

    name: Optional[str] = None
    """A short description of a TURN key, not shown to end users."""

    uid: Optional[str] = None
    """A Cloudflare-generated unique identifier for a item."""
