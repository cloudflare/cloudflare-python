# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MonetizationRuleInputOriginControlled"]


class MonetizationRuleInputOriginControlled(BaseModel):
    """Payment rule whose price the origin server sets dynamically.

    The rule carries no price and the price field must be omitted — any provided value, including "0", is rejected because it would not be enforced.
    """

    address: str
    """0x-prefixed 20-byte hexadecimal Ethereum address.

    Mixed-case addresses must carry a valid EIP-55 checksum; all-lowercase or
    all-uppercase addresses are also accepted. The address must pass wallet
    screening whenever its rule is deployed or patched.
    """

    expression: str
    """Wirefilter expression identifying the requests that require payment.

    Forwarded verbatim to the Rulesets API, which validates its syntax.
    """

    scheme: Literal["origin_controlled"]
    """X402 payment scheme.

    "origin_controlled" lets the origin server set pricing dynamically; the rule
    carries no price and the price field must be omitted.
    """

    id: Optional[str] = None
    """Optional on input.

    Include the ID of an existing payment rule to update it in place, preserving its
    stable identity across the full-ruleset replacement; omit it to create a new
    rule. An ID that does not match an existing payment rule in the zone is
    rejected. Rules omitted from the request are deleted.
    """

    description: Optional[str] = None

    enabled: Optional[bool] = None
