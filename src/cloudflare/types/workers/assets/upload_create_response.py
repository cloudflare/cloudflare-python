# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["UploadCreateResponse"]


class UploadCreateResponse(BaseModel):
    jwt: Optional[str] = None
    """A "completion" JWT which can be redeemed when creating a Worker version."""
