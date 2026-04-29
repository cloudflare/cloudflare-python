# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImpersonationRegistryEditParams"]


class ImpersonationRegistryEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    comments: Optional[str]

    directory_id: Optional[int]

    directory_node_id: Optional[int]

    email: str

    external_directory_node_id: Optional[str]

    is_email_regex: bool

    name: str

    provenance: Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
