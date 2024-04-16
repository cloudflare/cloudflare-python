# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .network_path import NetworkPath

__all__ = ["NetworkPathResponse"]


class NetworkPathResponse(BaseModel):
    id: str
    """API Resource UUID tag."""

    device_name: Optional[str] = FieldInfo(alias="deviceName", default=None)

    interval: Optional[str] = None
    """The interval at which the Traceroute synthetic application test is set to run."""

    kind: Optional[Literal["traceroute"]] = None

    name: Optional[str] = None

    network_path: Optional[NetworkPath] = FieldInfo(alias="networkPath", default=None)

    url: Optional[str] = None
    """The host of the Traceroute synthetic application test"""
