# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["FirewallInput"]


class FirewallInput(BaseModel):
    enabled: bool
    """Enabled"""

    operating_system: Literal["windows", "mac"]
    """Operating System"""
