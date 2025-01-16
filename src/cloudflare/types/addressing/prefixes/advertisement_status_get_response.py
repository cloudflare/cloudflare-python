# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AdvertisementStatusGetResponse"]


class AdvertisementStatusGetResponse(BaseModel):
    advertised: Optional[bool] = None
    """Advertisement status of the prefix.

    If `true`, the BGP route for the prefix is advertised to the Internet. If
    `false`, the BGP route is withdrawn.
    """

    advertised_modified_at: Optional[datetime] = None
    """Last time the advertisement status was changed.

    This field is only not 'null' if on demand is enabled.
    """
