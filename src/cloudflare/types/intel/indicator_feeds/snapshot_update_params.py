# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SnapshotUpdateParams"]


class SnapshotUpdateParams(TypedDict, total=False):
    account_id: str
    """Identifier"""

    source: str
    """The file to upload"""
