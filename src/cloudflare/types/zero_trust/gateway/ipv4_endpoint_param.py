# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IPV4EndpointParam"]


class IPV4EndpointParam(TypedDict, total=False):
    enabled: bool
    """True if the endpoint is enabled for this location."""
