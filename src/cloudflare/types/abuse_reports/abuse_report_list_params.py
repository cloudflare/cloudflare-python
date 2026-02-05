# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AbuseReportListParams"]


class AbuseReportListParams(TypedDict, total=False):
    account_id: Required[str]

    created_after: str
    """Returns reports created after the specified date"""

    created_before: str
    """Returns reports created before the specified date"""

    domain: str
    """Filter by domain name related to the abuse report"""

    mitigation_status: Literal["pending", "active", "in_review", "cancelled", "removed"]
    """Filter reports that have any mitigations in the given status."""

    page: int
    """Where in pagination to start listing abuse reports"""

    per_page: int
    """How many abuse reports per page to list"""

    sort: str
    """A property to sort by, followed by the order (id, cdate, domain, type, status)"""

    status: Literal["accepted", "in_review"]
    """Filter by the status of the report."""

    type: Literal["PHISH", "GEN", "THREAT", "DMCA", "EMER", "TM", "REG_WHO", "NCSEI", "NETWORK"]
    """Filter by the type of the report."""
