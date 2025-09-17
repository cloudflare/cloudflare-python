# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BodyScanningSettingsParam"]


class BodyScanningSettingsParam(TypedDict, total=False):
    inspection_mode: Literal["deep", "shallow"]
    """Specify the inspection mode as either `deep` or `shallow`."""
