# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef117"]


class UnnamedSchemaRef117(BaseModel):
    encrypted: Optional[int] = None
    """The number of bytes served over HTTPS."""

    unencrypted: Optional[int] = None
    """The number of bytes served over HTTP."""
