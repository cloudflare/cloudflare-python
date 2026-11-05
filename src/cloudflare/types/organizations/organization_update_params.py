# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OrganizationUpdateParams"]


class OrganizationUpdateParams(TypedDict, total=False):
    name: str
    """The Organization's display name, limited to 65 UTF-8 bytes.

    An omitted, empty, or unchanged value is a no-op.
    """

    parent_id: str
    """The current parent Organization ID.

    A different value is rejected; this endpoint cannot move an Organization.
    """
