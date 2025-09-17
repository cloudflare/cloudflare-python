# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProtocolDetectionParam"]


class ProtocolDetectionParam(TypedDict, total=False):
    enabled: Optional[bool]
    """Enable detecting protocol on initial bytes of client traffic."""
