# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

__all__ = ["FirewallInputParam"]


class FirewallInputParam(TypedDict, total=False):
    enabled: Required[bool]
    """Enabled"""

    operating_system: Required[Literal["windows", "mac"]]
    """Operating System"""
