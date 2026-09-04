# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["TailCreateParams"]


class TailCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    project_name: Required[str]
    """Name of the project."""

    filters: Iterable[Dict[str, object]]
    """Filters to apply to the tail session."""
