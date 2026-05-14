# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ItemEditParams"]


class ItemEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    burst_sensitivity: str
    """The new burst sensitivity. Optional. Must be one of 'low', 'medium', 'high'."""

    mitigation_type: str
    """The new mitigation type. Optional. Must be one of 'challenge' or 'retransmit'."""

    mode: str
    """The new mode for SYN Protection.

    Optional. Must be one of 'enabled', 'disabled', 'monitoring'.
    """

    rate_sensitivity: str
    """The new rate sensitivity. Optional. Must be one of 'low', 'medium', 'high'."""
