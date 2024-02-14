# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["KeyCloudflareImagesKeysListSigningKeysResponse", "Key"]


class Key(BaseModel):
    name: Optional[str] = None
    """Key name."""

    value: Optional[str] = None
    """Key value."""


class KeyCloudflareImagesKeysListSigningKeysResponse(BaseModel):
    keys: Optional[List[Key]] = None
