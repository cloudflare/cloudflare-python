# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ASNConfigurationParam"]


class ASNConfigurationParam(TypedDict, total=False):
    target: Literal["asn"]
    """The configuration target.

    You must set the target to `asn` when specifying an Autonomous System Number
    (ASN) in the rule.
    """

    value: str
    """The AS number to match."""
