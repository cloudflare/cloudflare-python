# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .nat_param import NatParam

from typing_extensions import TypedDict, Required

__all__ = ["RoutedSubnetParam"]

class RoutedSubnetParam(TypedDict, total=False):
    next_hop: Required[str]
    """A valid IPv4 address."""

    prefix: Required[str]
    """A valid CIDR notation representing an IP range."""

    nat: NatParam