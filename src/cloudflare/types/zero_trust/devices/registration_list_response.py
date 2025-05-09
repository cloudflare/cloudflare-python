# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["RegistrationListResponse", "Device", "User"]


class Device(BaseModel):
    id: str
    """The ID of the device."""

    name: str
    """The name of the device."""

    client_version: Optional[str] = None
    """Version of the WARP client."""


class User(BaseModel):
    id: Optional[str] = None
    """UUID."""

    email: Optional[str] = None
    """The contact email address of the user."""

    name: Optional[str] = None
    """The enrolled device user's name."""


class RegistrationListResponse(BaseModel):
    id: str
    """The ID of the registration."""

    created_at: str
    """The RFC3339 timestamp when the registration was created."""

    device: Device
    """Device details embedded inside of a registration."""

    key: str
    """The public key used to connect to the Cloudflare network."""

    last_seen_at: str
    """The RFC3339 timestamp when the registration was last seen."""

    updated_at: str
    """The RFC3339 timestamp when the registration was last updated."""

    deleted_at: Optional[str] = None
    """The RFC3339 timestamp when the registration was deleted."""

    key_type: Optional[str] = None
    """The type of encryption key used by the WARP client for the active key.

    Currently 'curve25519' for WireGuard and 'secp256r1' for MASQUE.
    """

    revoked_at: Optional[str] = None
    """The RFC3339 timestamp when the registration was revoked."""

    tunnel_type: Optional[str] = None
    """Type of the tunnel - wireguard or masque."""

    user: Optional[User] = None
