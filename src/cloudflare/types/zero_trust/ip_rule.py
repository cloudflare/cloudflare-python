# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IPRule", "IP"]

class IP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""

class IPRule(BaseModel):
    ip: IP