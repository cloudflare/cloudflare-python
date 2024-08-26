# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AttackMitigationParam"]

class AttackMitigationParam(TypedDict, total=False):
    enabled: bool
    """
    When enabled, random-prefix attacks are automatically mitigated and the upstream
    DNS servers protected.
    """

    only_when_upstream_unhealthy: bool
    """Only mitigate attacks when upstream servers seem unhealthy."""