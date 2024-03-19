# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MobileRedirectEditParams", "Value"]


class MobileRedirectEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Value]
    """Value of the zone setting."""


class Value(TypedDict, total=False):
    mobile_subdomain: Optional[str]
    """
    Which subdomain prefix you wish to redirect visitors on mobile devices to
    (subdomain must already exist).
    """

    status: Literal["on", "off"]
    """Whether or not mobile redirect is enabled."""

    strip_uri: bool
    """
    Whether to drop the current page path and redirect to the mobile subdomain URL
    root, or keep the path and redirect to the same page on the mobile subdomain.
    """
