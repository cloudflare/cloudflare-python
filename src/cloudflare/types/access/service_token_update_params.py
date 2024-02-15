# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServiceTokenUpdateParams"]


class ServiceTokenUpdateParams(TypedDict, total=False):
    account_or_zone: Required[str]

    account_or_zone_id: Required[str]
    """Identifier"""

    duration: str
    """The duration for how long the service token will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. The default is 1 year in hours (8760h).
    """

    name: str
    """The name of the service token."""
