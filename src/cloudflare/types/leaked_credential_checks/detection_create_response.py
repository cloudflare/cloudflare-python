# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DetectionCreateResponse"]


class DetectionCreateResponse(BaseModel):
    id: Optional[str] = None
    """Defines the unique ID for this custom detection."""

    password: Optional[str] = None
    """Defines ehe ruleset expression to use in matching the password in a request."""

    username: Optional[str] = None
    """Defines the ruleset expression to use in matching the username in a request."""
