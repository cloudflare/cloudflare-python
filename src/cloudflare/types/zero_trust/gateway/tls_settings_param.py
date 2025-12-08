# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TLSSettingsParam"]


class TLSSettingsParam(TypedDict, total=False):
    """Specify whether to inspect encrypted HTTP traffic."""

    enabled: bool
    """Specify whether to inspect encrypted HTTP traffic."""
