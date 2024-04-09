# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Device", "User"]


class User(BaseModel):
    id: Optional[str] = None
    """UUID"""

    email: Optional[str] = None
    """The contact email address of the user."""

    name: Optional[str] = None
    """The enrolled device user's name."""


class Device(BaseModel):
    id: Optional[str] = None
    """Device ID."""

    created: Optional[datetime] = None
    """When the device was created."""

    deleted: Optional[bool] = None
    """True if the device was deleted."""

    device_type: Optional[Literal["windows", "mac", "linux", "android", "ios"]] = None

    ip: Optional[str] = None
    """IPv4 or IPv6 address."""

    key: Optional[str] = None
    """The device's public key."""

    last_seen: Optional[datetime] = None
    """When the device last connected to Cloudflare services."""

    mac_address: Optional[str] = None
    """The device mac address."""

    manufacturer: Optional[str] = None
    """The device manufacturer name."""

    model: Optional[str] = None
    """The device model name."""

    name: Optional[str] = None
    """The device name."""

    os_distro_name: Optional[str] = None
    """The Linux distro name."""

    os_distro_revision: Optional[str] = None
    """The Linux distro revision."""

    os_version: Optional[str] = None
    """The operating system version."""

    os_version_extra: Optional[str] = None
    """The operating system version extra parameter."""

    revoked_at: Optional[datetime] = None
    """When the device was revoked."""

    serial_number: Optional[str] = None
    """The device serial number."""

    updated: Optional[datetime] = None
    """When the device was updated."""

    user: Optional[User] = None

    version: Optional[str] = None
    """The WARP client version."""
