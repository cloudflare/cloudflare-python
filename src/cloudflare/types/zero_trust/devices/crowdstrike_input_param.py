# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CrowdstrikeInputParam"]


class CrowdstrikeInputParam(TypedDict, total=False):
    connection_id: Required[str]
    """Posture Integration ID."""

    last_seen: str
    """For more details on last seen, please refer to the Crowdstrike documentation."""

    operator: Literal["<", "<=", ">", ">=", "=="]
    """operator"""

    os: str
    """Os Version"""

    overall: str
    """overall"""

    sensor_config: str
    """SensorConfig"""

    state: Literal["online", "offline", "unknown"]
    """For more details on state, please refer to the Crowdstrike documentation."""

    version: str
    """Version"""

    version_operator: Annotated[Literal["<", "<=", ">", ">=", "=="], PropertyInfo(alias="versionOperator")]
    """Version Operator"""
