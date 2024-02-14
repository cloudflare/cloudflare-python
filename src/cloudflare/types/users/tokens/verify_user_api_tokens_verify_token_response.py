# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["VerifyUserAPITokensVerifyTokenResponse"]


class VerifyUserAPITokensVerifyTokenResponse(BaseModel):
    id: str
    """Token identifier tag."""

    status: Literal["active", "disabled", "expired"]
    """Status of the token."""

    expires_on: Optional[datetime] = None
    """
    The expiration time on or after which the JWT MUST NOT be accepted for
    processing.
    """

    not_before: Optional[datetime] = None
    """The time before which the token MUST NOT be accepted for processing."""
