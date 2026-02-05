# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BodyScanningSettings"]


class BodyScanningSettings(BaseModel):
    """Specify the DLP inspection mode."""

    inspection_mode: Optional[Literal["deep", "shallow"]] = None
    """Specify the inspection mode as either `deep` or `shallow`."""
