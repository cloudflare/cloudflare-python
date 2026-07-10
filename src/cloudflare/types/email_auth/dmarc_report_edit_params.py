# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DMARCReportEditParams"]


class DMARCReportEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    enabled: Optional[bool]
    """Enable or disable DMARC reports for this zone"""

    skip_wizard: Optional[bool]
    """Skip the DMARC setup wizard"""
