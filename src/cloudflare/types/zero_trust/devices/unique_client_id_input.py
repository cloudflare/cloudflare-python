# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["UniqueClientIDInput"]


class UniqueClientIDInput(BaseModel):
    id: str
    """List ID."""

    operating_system: Literal["android", "ios", "chromeos"]
    """Operating System"""
