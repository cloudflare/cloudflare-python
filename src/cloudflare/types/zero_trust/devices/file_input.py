# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["FileInput"]


class FileInput(BaseModel):
    operating_system: Literal["windows", "linux", "mac"]
    """Operating system"""

    path: str
    """File path."""

    exists: Optional[bool] = None
    """Whether or not file exists"""

    sha256: Optional[str] = None
    """SHA-256."""

    thumbprint: Optional[str] = None
    """Signing certificate thumbprint."""
