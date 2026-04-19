# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IPProfileUpdateParams"]


class IPProfileUpdateParams(TypedDict, total=False):
    account_id: str

    description: str
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
