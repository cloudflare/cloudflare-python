# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["LogcontrolCmbConfig"]


class LogcontrolCmbConfig(BaseModel):
    regions: Optional[str] = None
    """Comma-separated list of regions."""
