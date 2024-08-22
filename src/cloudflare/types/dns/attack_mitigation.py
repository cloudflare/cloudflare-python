# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AttackMitigation"]

class AttackMitigation(BaseModel):
    enabled: Optional[bool] = None
    """
    When enabled, random-prefix attacks are automatically mitigated and the upstream
    DNS servers protected.
    """

    only_when_upstream_unhealthy: Optional[bool] = None
    """Only mitigate attacks when upstream servers seem unhealthy."""