# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["DeviceListResponse", "LastSeenUser"]


class LastSeenUser(BaseModel):
    id: Optional[str] = None
    """UUID."""

    email: Optional[str] = None
    """The contact email address of the user."""

    name: Optional[str] = None
    """The enrolled device user's name."""


class DeviceListResponse(BaseModel):
    id: str
    """The unique ID of the device."""

    active_registrations: int
    """The number of active registrations for the device.

    Active registrations are those which haven't been revoked or deleted.
    """

    created_at: str
    """The RFC3339 timestamp when the device was created."""

    last_seen_at: Optional[str] = None
    """The RFC3339 timestamp when the device was last seen."""

    name: str
    """The name of the device."""

    updated_at: str
    """The RFC3339 timestamp when the device was last updated."""

    client_version: Optional[str] = None
    """Version of the WARP client."""

    deleted_at: Optional[str] = None
    """The RFC3339 timestamp when the device was deleted."""

    device_type: Optional[str] = None
    """The device operating system."""

    hardware_id: Optional[str] = None
    """A string that uniquely identifies the hardware or virtual machine (VM)."""

    last_seen_user: Optional[LastSeenUser] = None
    """The last user to use the WARP device."""

    mac_address: Optional[str] = None
    """The device MAC address."""

    manufacturer: Optional[str] = None
    """The device manufacturer."""

    model: Optional[str] = None
    """The model name of the device."""

    os_version: Optional[str] = None
    """The device operating system version number."""

    os_version_extra: Optional[str] = None
    """Additional operating system version data.

    For macOS or iOS, the Product Version Extra. For Linux, the kernel release
    version.
    """

    public_ip: Optional[str] = None
    """The public IP address of the WARP client."""

    serial_number: Optional[str] = None
    """The device serial number."""
