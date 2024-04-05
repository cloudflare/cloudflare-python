# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NatParam"]


class NatParam(TypedDict, total=False):
    static_prefix: str
    """A valid CIDR notation representing an IP range."""
