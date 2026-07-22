# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AppCreateResponse"]


class AppCreateResponse(BaseModel):
    id: str

    created_at: str

    name: str

    updated_at: str

    updated_by: str
    """Email of the actor who last modified the app, or `unknown` when unavailable."""
