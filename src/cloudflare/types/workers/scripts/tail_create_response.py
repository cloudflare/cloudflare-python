# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["TailCreateResponse"]


class TailCreateResponse(BaseModel):
    id: str
    """Identifier."""

    expires_at: str

    url: str
