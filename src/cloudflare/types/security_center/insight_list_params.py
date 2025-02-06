# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..intel.attack_surface_report.issue_type import IssueType
from ..intel.attack_surface_report.severity_query_param import SeverityQueryParam

__all__ = ["InsightListParams"]


class InsightListParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    dismissed: bool

    issue_class: List[str]

    issue_class_neq: Annotated[List[str], PropertyInfo(alias="issue_class~neq")]

    issue_type: List[IssueType]

    issue_type_neq: Annotated[List[IssueType], PropertyInfo(alias="issue_type~neq")]

    page: int
    """Current page within paginated list of results"""

    per_page: int
    """Number of results per page of results"""

    product: List[str]

    product_neq: Annotated[List[str], PropertyInfo(alias="product~neq")]

    severity: List[SeverityQueryParam]

    severity_neq: Annotated[List[SeverityQueryParam], PropertyInfo(alias="severity~neq")]

    subject: List[str]

    subject_neq: Annotated[List[str], PropertyInfo(alias="subject~neq")]
