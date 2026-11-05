# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MonetizationRuleInputFixedPrice"]


class MonetizationRuleInputFixedPrice(BaseModel):
    """Payment rule with a fixed price set at configuration time."""

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

    price: str
    """
    Price in the smallest indivisible unit of the configured payment token, encoded
    as a decimal string. Must be a canonical decimal integer in [1000, 100000000]:
    no leading zeros, and a bare JSON number is rejected. The price is required for
    the fixed-price schemes ("exact" and "upto") and must be at least 1000, the
    smallest amount the payment facilitator can settle ($0.001 for a 6-decimal token
    such as USDC), and at most 100000000 ($100 for a 6-decimal token). When the
    scheme is "origin_controlled" the origin server sets pricing dynamically and the
    rule carries no price: the field must be omitted — any provided value, including
    "0", is rejected because it would not be enforced. Responses always encode this
    as a string and omit it for "origin_controlled" rules; the pattern matches
    exactly the set of values the server accepts.
    """

    scheme: Literal["exact", "upto"]
    """X402 payment scheme.

    "exact" requires the specified payment amount; "upto" permits a payment up to
    the specified amount. Both fixed-price schemes require the price field.
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
