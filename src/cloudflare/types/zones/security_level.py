# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SecurityLevel"]


class SecurityLevel(BaseModel):
    id: Optional[Literal["security_level"]] = None
    """Control options for the **Security Level** feature from the **Security** app."""

    value: Optional[Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]] = None
