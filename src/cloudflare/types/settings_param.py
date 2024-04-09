# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SettingsParam"]


class SettingsParam(TypedDict, total=False):
    enabled: Literal[True, False]
    """State of the zone settings for Email Routing."""

    skip_wizard: Literal[True, False]
    """Flag to check if the user skipped the configuration wizard."""
