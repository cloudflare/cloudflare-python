# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleEditRuleParams"]


class RuleEditRuleParams(TypedDict, total=False):
    zone_id: Required[str]
    """The unique ID of the zone."""

    address: str
    """0x-prefixed 20-byte hexadecimal Ethereum address.

    Mixed-case addresses must carry a valid EIP-55 checksum; all-lowercase or
    all-uppercase addresses are also accepted. The effective address must pass
    wallet screening whenever the rule is patched.
    """

    description: str

    enabled: bool

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

    scheme: Literal["exact", "upto", "origin_controlled"]
    """X402 payment scheme.

    "exact" requires the specified payment amount; "upto" permits a payment up to
    the specified amount; "origin_controlled" lets the origin server set pricing
    dynamically, in which case the rule carries no price and the price field must be
    omitted.
    """
