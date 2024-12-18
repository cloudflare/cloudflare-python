# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DeviceGetResponse", "Account", "User"]


class Account(BaseModel):
    id: Optional[str] = None

    account_type: Optional[str] = None

    name: Optional[str] = None
    """The name of the enrolled account."""


class User(BaseModel):
    id: Optional[str] = None
    """UUID"""

    email: Optional[str] = None
    """The contact email address of the user."""

    name: Optional[str] = None
    """The enrolled device user's name."""


class DeviceGetResponse(BaseModel):
    id: Optional[str] = None
    """Device ID."""

    account: Optional[Account] = None

    created: Optional[datetime] = None
    """When the device was created."""

    deleted: Optional[bool] = None
    """True if the device was deleted."""

    device_type: Optional[str] = None

    gateway_device_id: Optional[str] = None

    ip: Optional[str] = None
    """IPv4 or IPv6 address."""

    key: Optional[str] = None
    """The device's public key."""

    key_type: Optional[str] = None
    """Type of the key."""

    last_seen: Optional[datetime] = None
    """When the device last connected to Cloudflare services."""

    mac_address: Optional[str] = None
    """The device mac address."""

    model: Optional[str] = None
    """The device model name."""

    name: Optional[str] = None
    """The device name."""

    os_version: Optional[str] = None
    """The operating system version."""

    serial_number: Optional[str] = None
    """The device serial number."""

    tunnel_type: Optional[str] = None
    """Type of the tunnel connection used."""

    updated: Optional[datetime] = None
    """When the device was updated."""

    user: Optional[User] = None

    version: Optional[str] = None
    """The WARP client version."""
