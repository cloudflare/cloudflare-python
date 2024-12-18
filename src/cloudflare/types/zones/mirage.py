# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Mirage"]


class Mirage(BaseModel):
    id: Optional[Literal["mirage"]] = None
    """
    Cloudflare Mirage reduces bandwidth used by images in mobile browsers. It can
    accelerate loading of image-heavy websites on very slow mobile connections and
    HTTP/1.
    """

    value: Optional[Literal["on", "off"]] = None
    """The status of Mirage."""
