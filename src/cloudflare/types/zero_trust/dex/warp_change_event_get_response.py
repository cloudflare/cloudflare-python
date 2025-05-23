# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "WARPChangeEventGetResponse",
    "WARPChangeEventGetResponseItem",
    "WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPToggleChangeEvent",
    "WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEvent",
    "WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEventFrom",
    "WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEventTo",
]


class WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPToggleChangeEvent(BaseModel):
    account_name: Optional[str] = None
    """The account name."""

    account_tag: Optional[str] = None
    """The public account identifier."""

    device_id: Optional[str] = None
    """API Resource UUID tag."""

    device_registration: Optional[str] = None
    """API Resource UUID tag."""

    hostname: Optional[str] = None
    """The hostname of the machine the event is from"""

    serial_number: Optional[str] = None
    """The serial number of the machine the event is from"""

    timestamp: Optional[str] = None
    """Timestamp in ISO format"""

    toggle: Optional[Literal["on", "off"]] = None
    """The state of the WARP toggle."""

    user_email: Optional[str] = None
    """Email tied to the device"""


class WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEventFrom(BaseModel):
    account_name: Optional[str] = None
    """The account name."""

    account_tag: Optional[str] = None
    """API Resource UUID tag."""

    config_name: Optional[str] = None
    """The name of the WARP configuration."""


class WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEventTo(BaseModel):
    account_name: Optional[str] = None
    """The account name."""

    account_tag: Optional[str] = None
    """API Resource UUID tag."""

    config_name: Optional[str] = None
    """The name of the WARP configuration."""


class WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEvent(BaseModel):
    device_id: Optional[str] = None
    """API Resource UUID tag."""

    device_registration: Optional[str] = None
    """API Resource UUID tag."""

    from_: Optional[WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEventFrom] = FieldInfo(
        alias="from", default=None
    )

    hostname: Optional[str] = None
    """The hostname of the machine the event is from"""

    serial_number: Optional[str] = None
    """The serial number of the machine the event is from"""

    timestamp: Optional[str] = None
    """Timestamp in ISO format"""

    to: Optional[WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEventTo] = None

    user_email: Optional[str] = None
    """Email tied to the device"""


WARPChangeEventGetResponseItem: TypeAlias = Union[
    WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPToggleChangeEvent,
    WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEvent,
]

WARPChangeEventGetResponse: TypeAlias = List[WARPChangeEventGetResponseItem]
