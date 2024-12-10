# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WAF"]


class WAF(BaseModel):
    id: Optional[Literal["waf"]] = None
    """
    Turn on or off
    [WAF managed rules (previous version, deprecated)](https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/).
    You cannot enable or disable individual WAF managed rules via Page Rules.
    """

    value: Optional[Literal["on", "off"]] = None
    """The status of WAF managed rules (previous version)."""
