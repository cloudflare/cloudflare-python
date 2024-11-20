# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BrowserCheck"]


class BrowserCheck(BaseModel):
    id: Optional[Literal["browser_check"]] = None
    """
    Inspect the visitor's browser for headers commonly associated with spammers and
    certain bots.
    """

    value: Optional[Literal["on", "off"]] = None
    """The status of Browser Integrity Check."""
