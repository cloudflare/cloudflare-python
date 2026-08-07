# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RulesetDeleteParams"]


class RulesetDeleteParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    dry_run: bool
    """Validates the request without persisting changes when set to `true`.

    Responses that normally return 200 return `result: null`; endpoints that
    normally return 204 continue to return 204.
    """
