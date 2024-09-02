# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Percentiles"]


class Percentiles(BaseModel):
    p50: Optional[float] = None
    """p50 observed in the time period"""

    p90: Optional[float] = None
    """p90 observed in the time period"""

    p95: Optional[float] = None
    """p95 observed in the time period"""

    p99: Optional[float] = None
    """p99 observed in the time period"""
