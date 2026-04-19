# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RegistrationEditParams"]


class RegistrationEditParams(TypedDict, total=False):
    account_id: str
    """Identifier"""

    auto_renew: bool
    """
    Enable or disable automatic renewal. Setting this field to `true` authorizes
    Cloudflare to charge the account's default payment method up to 30 days before
    domain expiry to renew the domain automatically. Renewal pricing may change over
    time based on registry pricing.
    """

    prefer: Annotated[Literal["respond-async"], PropertyInfo(alias="Prefer")]
