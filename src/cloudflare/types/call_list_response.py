# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["CallListResponse", "CallListResponseItem"]


class CallListResponseItem(BaseModel):
    created: Optional[datetime] = None
    """The date and time the item was created."""

    modified: Optional[datetime] = None
    """The date and time the item was last modified."""

    name: Optional[str] = None
    """A short description of Calls app, not shown to end users."""

    uid: Optional[str] = None
    """A Cloudflare-generated unique identifier for a item."""


CallListResponse = List[CallListResponseItem]
