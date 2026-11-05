# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["NEL", "Value", "ValueEnabled"]


class ValueEnabled(BaseModel):
    enabled: Optional[bool] = None


Value: TypeAlias = Union[ValueEnabled, ValueEnabled, ValueEnabled, ValueEnabled, ValueEnabled]


class NEL(BaseModel):
    """Enable Network Error Logging reporting on your zone. (Beta)"""

    id: Literal["nel"]
    """Zone setting identifier."""

    value: Value
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""
