# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OriginErrorPagePassThru"]


class OriginErrorPagePassThru(BaseModel):
    id: Optional[Literal["origin_error_page_pass_thru"]] = None
    """
    Turn on or off Cloudflare error pages generated from issues sent from the origin
    server. If enabled, this setting triggers error pages issued by the origin.
    """

    value: Optional[Literal["on", "off"]] = None
    """The status of Origin Error Page Passthru."""
