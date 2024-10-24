# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ASNConfiguration"]


class ASNConfiguration(BaseModel):
    target: Optional[Literal["asn"]] = None
    """The configuration target.

    You must set the target to `asn` when specifying an Autonomous System Number
    (ASN) in the rule.
    """

    value: Optional[str] = None
    """The AS number to match."""
