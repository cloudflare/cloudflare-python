# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["DeviceGetResponse", "LastSeenRegistration", "LastSeenRegistrationPolicy", "LastSeenUser"]


class LastSeenRegistrationPolicy(BaseModel):
    id: str
    """The ID of the device settings profile."""

    default: bool
    """Whether the device settings profile is the default profile for the account."""

    deleted: bool
    """Whether the device settings profile was deleted."""

    name: str
    """The name of the device settings profile."""

    updated_at: str
    """
    The RFC3339 timestamp of when the device settings profile last changed for the
    registration.
    """


class LastSeenRegistration(BaseModel):
    policy: Optional[LastSeenRegistrationPolicy] = None
    """A summary of the device profile evaluated for the registration."""


class LastSeenUser(BaseModel):
    id: Optional[str] = None
    """UUID."""

    email: Optional[str] = None
    """The contact email address of the user."""

    name: Optional[str] = None
    """The enrolled device user's name."""


class DeviceGetResponse(BaseModel):
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

    last_seen_registration: Optional[LastSeenRegistration] = None
    """The last seen registration for the device."""

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
    """
    **Deprecated**: IP information is provided by DEX - see
    https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/fleet_status/subresources/devices/methods/list/
    """

    serial_number: Optional[str] = None
    """The device serial number."""
