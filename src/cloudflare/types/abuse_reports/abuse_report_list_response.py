# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AbuseReportListResponse", "Report", "ReportMitigationSummary"]


class ReportMitigationSummary(BaseModel):
    accepted_url_count: int
    """How many of the reported URLs were confirmed as abusive."""

    active_count: int
    """How many mitigations are active."""

    external_host_notified: bool
    """Whether the report has been forwarded to an external hosting provider."""

    in_review_count: int
    """How many mitigations are under review."""

    pending_count: int
    """How many mitigations are pending their effective date."""


class Report(BaseModel):
    id: str
    """Public facing ID of abuse report, aka abuse_rand."""

    cdate: str
    """Creation date of report.

    Time in RFC 3339 format (https://www.rfc-editor.org/rfc/rfc3339.html)
    """

    domain: str
    """Domain that relates to the report."""

    mitigation_summary: ReportMitigationSummary
    """A summary of the mitigations related to this report."""

    status: Literal["accepted", "in_review"]
    """An enum value that represents the status of an abuse record"""

    type: Literal["PHISH", "GEN", "THREAT", "DMCA", "EMER", "TM", "REG_WHO", "NCSEI", "NETWORK"]
    """The abuse report type"""


class AbuseReportListResponse(BaseModel):
    reports: List[Report]
