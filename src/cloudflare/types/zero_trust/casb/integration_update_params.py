# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["IntegrationUpdateParams"]


class IntegrationUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    credentials: Dict[str, object]
    """Partial credential fields to merge with existing."""

    dlp_profiles: SequenceNotStr[str]
    """List of DLP profile IDs to associate with the integration."""

    name: str
    """Name of the integration."""

    permissions: SequenceNotStr[str]
    """List of permission scopes granted to the integration."""

    use_cases: List[Literal["casb", "ces", "auto_remediation"]]
    """
    List of use case or feature slugs to enroll (e.g., ['casb', 'ces',
    'auto_remediation']).
    """
