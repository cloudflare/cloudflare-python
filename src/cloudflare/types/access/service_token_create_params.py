# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServiceTokenCreateParams"]


class ServiceTokenCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: Required[str]
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    name: Required[str]
    """The name of the service token."""

    duration: str
    """The duration for how long the service token will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. The default is 1 year in hours (8760h).
    """
