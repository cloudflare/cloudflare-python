# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["IPProfile"]


class IPProfile(BaseModel):
    id: str
    """The ID of the Device IP profile."""

    created_at: str
    """The RFC3339Nano timestamp when the Device IP profile was created."""

    description: Optional[str] = None
    """An optional description of the Device IP profile."""

    enabled: bool
    """Whether the Device IP profile is enabled."""

    match: str
    """The wirefilter expression to match registrations.

    Available values: "identity.name", "identity.email", "identity.groups.id",
    "identity.groups.name", "identity.groups.email", "identity.saml_attributes".
    """

    name: str
    """A user-friendly name for the Device IP profile."""

    precedence: int
    """The precedence of the Device IP profile.

    Lower values indicate higher precedence. Device IP profile will be evaluated in
    ascending order of this field.
    """

    subnet_id: str
    """The ID of the Subnet."""

    updated_at: str
    """The RFC3339Nano timestamp when the Device IP profile was last updated."""
