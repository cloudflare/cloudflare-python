# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatabaseCreateParams"]


class DatabaseCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    name: Required[str]
    """D1 database name."""

    primary_location_hint: Literal["wnam", "enam", "weur", "eeur", "apac", "oc"]
    """Specify the region to create the D1 primary, if available.

    If this option is omitted, the D1 will be created as close as possible to the
    current user.
    """
