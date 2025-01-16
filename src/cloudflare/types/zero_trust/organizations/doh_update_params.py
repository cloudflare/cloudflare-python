# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DOHUpdateParams"]


class DOHUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    doh_jwt_duration: str
    """The duration the DoH JWT is valid for.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note that the maximum duration for this setting is the same as the
    key rotation period on the account. Default expiration is 24h
    """

    service_token_id: str
    """The uuid of the service token you want to use for DoH authentication"""
