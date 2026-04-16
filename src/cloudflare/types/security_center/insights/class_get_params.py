# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ...intel.attack_surface_report.issue_type import IssueType
from ...intel.attack_surface_report.severity_query_param import SeverityQueryParam

__all__ = ["ClassGetParams"]


class ClassGetParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    dismissed: bool

    issue_class: SequenceNotStr[str]

    issue_class_neq: Annotated[SequenceNotStr[str], PropertyInfo(alias="issue_class~neq")]

    issue_type: List[IssueType]

    issue_type_neq: Annotated[List[IssueType], PropertyInfo(alias="issue_type~neq")]

    product: SequenceNotStr[str]

    product_neq: Annotated[SequenceNotStr[str], PropertyInfo(alias="product~neq")]

    severity: List[SeverityQueryParam]

    severity_neq: Annotated[List[SeverityQueryParam], PropertyInfo(alias="severity~neq")]

    subject: SequenceNotStr[str]

    subject_neq: Annotated[SequenceNotStr[str], PropertyInfo(alias="subject~neq")]
