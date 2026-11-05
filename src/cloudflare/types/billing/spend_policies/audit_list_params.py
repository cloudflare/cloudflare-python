# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AuditListParams"]


class AuditListParams(TypedDict, total=False):
    account_id: Required[str]
    """Represents a Cloudflare resource identifier tag."""

    limit: int
    """Maximum number of audit entries to return.

    Defaults to 50. Values above 100 are capped at 100 rather than rejected.
    """

    period: Literal["current_billing_cycle", "all"]
    """Select current subscription billing-cycle history or history across all cycles."""
