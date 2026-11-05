# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ResourceSharingUpdateParams"]


class ResourceSharingUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier."""

    name: Required[str]
    """The name of the share."""

    tags: Dict[str, str]
    """Tags associated with the share."""
