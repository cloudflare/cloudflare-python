# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TLSSupportParams"]


class TLSSupportParams(TypedDict, total=False):
    host: Required[str]
    """
    Hostname or IP address to test for Post-Quantum TLS support, optionally with
    port (defaults to 443).
    """
