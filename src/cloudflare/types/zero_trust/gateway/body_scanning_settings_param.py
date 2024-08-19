# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BodyScanningSettingsParam"]


class BodyScanningSettingsParam(TypedDict, total=False):
    inspection_mode: str
    """Set the inspection mode to either `deep` or `shallow`."""
