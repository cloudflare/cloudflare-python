# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["TargetCloseResponse"]


class TargetCloseResponse(BaseModel):
    message: str
    """Target is closing."""
