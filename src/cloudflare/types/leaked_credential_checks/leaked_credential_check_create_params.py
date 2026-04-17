# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LeakedCredentialCheckCreateParams"]


class LeakedCredentialCheckCreateParams(TypedDict, total=False):
    zone_id: str
    """Defines an identifier."""

    enabled: bool
    """Determines whether or not Leaked Credential Checks are enabled."""
