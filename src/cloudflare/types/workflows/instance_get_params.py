# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceGetParams"]


class InstanceGetParams(TypedDict, total=False):
    account_id: str

    workflow_name: Required[str]

    order: Literal["asc", "desc"]
    """Step ordering: "asc" (default, oldest first) or "desc" (newest first)."""

    simple: Literal["true", "false"]
    """When true, omits step details and returns only metadata with step_count."""
