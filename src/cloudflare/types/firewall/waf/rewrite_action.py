# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["RewriteAction"]


class RewriteAction(BaseModel):
    block: Optional[Literal["challenge", "block", "simulate", "disable", "default"]] = None
    """The WAF rule action to apply."""

    challenge: Optional[str] = None

    default: Optional[str] = None

    disable: Optional[Literal["challenge", "block", "simulate", "disable", "default"]] = None
    """The WAF rule action to apply."""

    simulate: Optional[str] = None
