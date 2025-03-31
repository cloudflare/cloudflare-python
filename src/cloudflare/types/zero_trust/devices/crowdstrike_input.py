# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CrowdstrikeInput"]


class CrowdstrikeInput(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    last_seen: Optional[str] = None
    """For more details on last seen, please refer to the Crowdstrike documentation."""

    operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = None
    """operator"""

    os: Optional[str] = None
    """Os Version"""

    overall: Optional[str] = None
    """overall"""

    sensor_config: Optional[str] = None
    """SensorConfig"""

    state: Optional[Literal["online", "offline", "unknown"]] = None
    """For more details on state, please refer to the Crowdstrike documentation."""

    version: Optional[str] = None
    """Version"""

    version_operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = FieldInfo(alias="versionOperator", default=None)
    """Version Operator"""
