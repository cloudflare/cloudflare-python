# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["StatusGetResponse"]


class StatusGetResponse(BaseModel):
    advertised: Optional[bool] = None
    """Enablement of prefix advertisement to the Internet."""

    advertised_modified_at: Optional[datetime] = None
    """Last time the advertisement status was changed.

    This field is only not 'null' if on demand is enabled.
    """
