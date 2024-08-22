# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .carbonblack_input import CarbonblackInput

from typing_extensions import TypedDict, Annotated

from ...._utils import PropertyInfo

__all__ = ["DiskEncryptionInputParam"]

class DiskEncryptionInputParam(TypedDict, total=False):
    check_disks: Annotated[List[CarbonblackInput], PropertyInfo(alias="checkDisks")]
    """List of volume names to be checked for encryption."""

    require_all: Annotated[bool, PropertyInfo(alias="requireAll")]
    """Whether to check all disks for encryption."""