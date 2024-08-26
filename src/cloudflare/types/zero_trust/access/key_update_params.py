# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KeyUpdateParams"]


class KeyUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    key_rotation_interval_days: Required[float]
    """The number of days between key rotations."""
