# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef3e10ea08deb8102a27500f986488c1e8"]


class UnnamedSchemaRef3e10ea08deb8102a27500f986488c1e8(BaseModel):
    banning: Optional[bool] = None
    """For internal use."""

    blocking: Optional[bool] = None
    """For internal use."""

    description: Optional[str] = None
    """Description of the signature that matched."""

    name: Optional[str] = None
    """Name of the signature that matched."""
