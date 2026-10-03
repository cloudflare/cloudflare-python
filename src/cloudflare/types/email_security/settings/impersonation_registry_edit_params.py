# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImpersonationRegistryEditParams"]


class ImpersonationRegistryEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    comments: Optional[str]
    """Optional note describing the entry."""

    directory_id: Optional[int]
    """Identifier of the directory the entry was synced from, when directory-synced."""

    directory_node_id: Optional[int]
    """
    Identifier of the directory node the entry was synced from, when
    directory-synced.
    """

    email: str
    """Email address (or pattern) of the protected identity."""

    external_directory_node_id: Optional[str]
    """Deprecated. External identifier of the directory node."""

    is_email_regex: bool
    """Whether `email` is a regular expression instead of a literal address."""

    name: str
    """Display name of the protected identity."""

    provenance: Optional[
        Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
    ]
    """Source the entry was created from."""
