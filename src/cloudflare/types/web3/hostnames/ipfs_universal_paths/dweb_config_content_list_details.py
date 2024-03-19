# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["DwebConfigContentListDetails"]


class DwebConfigContentListDetails(BaseModel):
    action: Optional[Literal["block"]] = None
    """Behavior of the content list."""
