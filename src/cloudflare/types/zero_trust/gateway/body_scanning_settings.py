# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BodyScanningSettings"]


class BodyScanningSettings(BaseModel):
    inspection_mode: Optional[str] = None
    """Set the inspection mode to either `deep` or `shallow`."""
