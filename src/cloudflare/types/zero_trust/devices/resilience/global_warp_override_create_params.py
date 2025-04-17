# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GlobalWARPOverrideCreateParams"]


class GlobalWARPOverrideCreateParams(TypedDict, total=False):
    account_id: Required[str]

    disconnect: Required[bool]
    """Disconnects all devices on the account using Global WARP override."""

    justification: str
    """Reasoning for setting the Global WARP override state.

    This will be surfaced in the audit log.
    """
