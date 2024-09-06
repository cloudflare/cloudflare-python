# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["ConnectorEditParams"]


class ConnectorEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    activated: bool

    interrupt_window_duration_hours: float

    interrupt_window_hour_of_day: float

    notes: str

    timezone: str
