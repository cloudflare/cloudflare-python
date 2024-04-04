# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UnnamedSchemaRef28"]


class UnnamedSchemaRef28(TypedDict, total=False):
    dns: object
    """Logging settings for DNS firewall."""

    http: object
    """Logging settings for HTTP/HTTPS firewall."""

    l4: object
    """Logging settings for Network firewall."""
