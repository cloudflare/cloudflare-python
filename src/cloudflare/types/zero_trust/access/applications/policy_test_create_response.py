# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["PolicyTestCreateResponse"]


class PolicyTestCreateResponse(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy test."""

    status: Optional[Literal["success"]] = None
    """The status of the policy test request."""
