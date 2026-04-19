# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ScriptListParams"]


class ScriptListParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    tags: str
    """Filter scripts by tags.

    Format: comma-separated list of tag:allowed pairs where allowed is 'yes' or
    'no'.
    """
