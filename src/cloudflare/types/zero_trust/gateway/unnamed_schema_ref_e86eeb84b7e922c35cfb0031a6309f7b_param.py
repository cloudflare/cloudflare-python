# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UnnamedSchemaRefE86eeb84b7e922c35cfb0031a6309f7bParam"]


class UnnamedSchemaRefE86eeb84b7e922c35cfb0031a6309f7bParam(TypedDict, total=False):
    dns: object
    """Logging settings for DNS firewall."""

    http: object
    """Logging settings for HTTP/HTTPS firewall."""

    l4: object
    """Logging settings for Network firewall."""
