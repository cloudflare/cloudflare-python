# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubdomainCreateParams"]


class SubdomainCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """The domain name within the zone.

    A wildcard is allowed only as the complete leftmost label (`*.example.com`) and
    requires the account wildcard Email Sending entitlement.
    """
