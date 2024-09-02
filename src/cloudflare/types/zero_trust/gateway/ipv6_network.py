# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IPV6Network"]


class IPV6Network(BaseModel):
    network: str
    """The IPv6 address or IPv6 CIDR."""
