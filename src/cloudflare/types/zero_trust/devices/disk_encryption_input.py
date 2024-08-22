# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from .carbonblack_input import CarbonblackInput

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DiskEncryptionInput"]

class DiskEncryptionInput(BaseModel):
    check_disks: Optional[List[CarbonblackInput]] = FieldInfo(alias = "checkDisks", default = None)
    """List of volume names to be checked for encryption."""

    require_all: Optional[bool] = FieldInfo(alias = "requireAll", default = None)
    """Whether to check all disks for encryption."""