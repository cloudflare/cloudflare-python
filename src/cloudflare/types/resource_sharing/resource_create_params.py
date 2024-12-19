# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResourceCreateParams"]


class ResourceCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier."""

    meta: Required[object]
    """Resource Metadata."""

    resource_account_id: Required[str]
    """Account identifier."""

    resource_id: Required[str]
    """Share Resource identifier."""

    resource_type: Required[Literal["custom-ruleset", "widget"]]
    """Resource Type."""
