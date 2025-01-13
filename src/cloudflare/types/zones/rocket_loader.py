# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RocketLoader"]


class RocketLoader(BaseModel):
    id: Optional[Literal["rocket_loader"]] = None
    """Turn on or off Rocket Loader in the Cloudflare Speed app."""

    value: Optional[Literal["on", "off"]] = None
    """The status of Rocket Loader"""
