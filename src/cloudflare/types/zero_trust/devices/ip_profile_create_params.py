# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["IPProfileCreateParams"]


class IPProfileCreateParams(TypedDict, total=False):
    account_id: Required[str]

    match: Required[str]
    """The wirefilter expression to match registrations.

    Available values: "identity.name", "identity.email", "identity.groups.id",
    "identity.groups.name", "identity.groups.email", "identity.saml_attributes".
    """

    name: Required[str]
    """A user-friendly name for the Device IP profile."""

    precedence: Required[int]
    """The precedence of the Device IP profile.

    Lower values indicate higher precedence. Device IP profile will be evaluated in
    ascending order of this field.
    """

    subnet_id: Required[str]
    """The ID of the Subnet."""

    description: Optional[str]
    """An optional description of the Device IP profile."""

    enabled: bool
    """Whether the Device IP profile will be applied to matching devices."""
