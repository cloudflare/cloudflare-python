# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtendedEmailMatchingParam"]


class ExtendedEmailMatchingParam(TypedDict, total=False):
    enabled: bool
    """Enable matching all variants of user emails (with + or .

    modifiers) used as criteria in Firewall policies.
    """
