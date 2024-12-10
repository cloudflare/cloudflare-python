# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LeakedCredentialCheckCreateParams"]


class LeakedCredentialCheckCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    enabled: bool
    """Whether or not Leaked Credential Checks are enabled"""
