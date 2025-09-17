# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BodyScanningSettings"]


class BodyScanningSettings(BaseModel):
    inspection_mode: Optional[Literal["deep", "shallow"]] = None
    """Set the inspection mode to either `deep` or `shallow`."""
