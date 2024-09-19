# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AttackMitigation"]


class AttackMitigation(BaseModel):
    enabled: Optional[bool] = None
    """
    When enabled, automatically mitigate random-prefix attacks to protect upstream
    DNS servers
    """

    only_when_upstream_unhealthy: Optional[bool] = None
    """Only mitigate attacks when upstream servers seem unhealthy"""
