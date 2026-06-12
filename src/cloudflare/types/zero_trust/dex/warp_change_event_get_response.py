# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
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
    """The device ID."""

    device_registration: Optional[str] = None
    """Deprecated: use registration_id. The device registration ID."""

    hostname: Optional[str] = None
    """The hostname of the machine the event is from."""

    registration_id: Optional[str] = None
    """The device registration ID."""

    serial_number: Optional[str] = None
    """The serial number of the machine the event is from."""

    timestamp: Optional[datetime] = None
    """The event time."""

    toggle: Optional[Literal["on", "off"]] = None
    """The state of the WARP toggle."""

    user_email: Optional[str] = None
    """Email tied to the device."""


class WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEventFrom(BaseModel):
    """The details for the WARP configuration that was switched from."""

    account_name: Optional[str] = None
    """The account name."""

    account_tag: Optional[str] = None
    """The public account identifier."""

    config_name: Optional[str] = None
    """The name of the WARP configuration."""


class WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEventTo(BaseModel):
    """The details for the WARP configuration that was switched to."""

    account_name: Optional[str] = None
    """The account name."""

    account_tag: Optional[str] = None
    """The public account identifier."""

    config_name: Optional[str] = None
    """The name of the WARP configuration."""


class WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEvent(BaseModel):
    device_id: Optional[str] = None
    """The device ID."""

    device_registration: Optional[str] = None
    """Deprecated: use registration_id. The device registration ID."""

    from_: Optional[WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEventFrom] = FieldInfo(
        alias="from", default=None
    )
    """The details for the WARP configuration that was switched from."""

    hostname: Optional[str] = None
    """The hostname of the machine the event is from."""

    registration_id: Optional[str] = None
    """The device registration ID."""

    serial_number: Optional[str] = None
    """The serial number of the machine the event is from."""

    timestamp: Optional[datetime] = None
    """The event time."""

    to: Optional[WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEventTo] = None
    """The details for the WARP configuration that was switched to."""

    user_email: Optional[str] = None
    """Email tied to the device."""


WARPChangeEventGetResponseItem: TypeAlias = Union[
    WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPToggleChangeEvent,
    WARPChangeEventGetResponseItemDigitalExperienceMonitoringWARPConfigChangeEvent,
]

WARPChangeEventGetResponse: TypeAlias = List[WARPChangeEventGetResponseItem]
