# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["AppConfigurationCreateResponse"]


class AppConfigurationCreateResponse(BaseModel):
    id: str
    """Identifier"""

    site_id: str
    """Identifier"""

    breakout: Optional[bool] = None
    """Whether to breakout traffic to the app's endpoints directly.

    Null preserves default behavior.
    """

    priority: Optional[int] = None
    """Priority of traffic.

    0 is default, anything greater is prioritized. (Currently only 0 and 1 are
    supported)
    """
