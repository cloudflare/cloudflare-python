# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FipsSettingsParam"]


class FipsSettingsParam(TypedDict, total=False):
    tls: bool
    """Enable only cipher suites and TLS versions compliant with FIPS 140-2."""
