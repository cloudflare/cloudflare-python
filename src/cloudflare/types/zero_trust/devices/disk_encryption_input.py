# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .carbonblack_input import CarbonblackInput

__all__ = ["DiskEncryptionInput"]


class DiskEncryptionInput(BaseModel):
    check_disks: Optional[List[CarbonblackInput]] = FieldInfo(alias="checkDisks", default=None)
    """List of volume names to be checked for encryption."""

    require_all: Optional[bool] = FieldInfo(alias="requireAll", default=None)
    """Whether to check all disks for encryption."""
