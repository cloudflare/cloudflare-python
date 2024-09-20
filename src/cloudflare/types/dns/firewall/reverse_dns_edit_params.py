# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ReverseDNSEditParams"]


class ReverseDNSEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    ptr: Dict[str, str]
    """Map of cluster IP addresses to PTR record contents"""
