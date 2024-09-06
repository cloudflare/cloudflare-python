# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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
