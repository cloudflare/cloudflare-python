# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .product import Product
from .subject import Subject
from ...._utils import PropertyInfo
from .issue_type import IssueType
from .issue_class import IssueClass
from .severity_query_param import SeverityQueryParam

__all__ = ["IssueListParams"]


class IssueListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dismissed: bool

    issue_class: List[IssueClass]

    issue_class_neq: Annotated[List[IssueClass], PropertyInfo(alias="issue_class~neq")]

    issue_type: List[IssueType]

    issue_type_neq: Annotated[List[IssueType], PropertyInfo(alias="issue_type~neq")]

    page: int
    """Current page within paginated list of results"""

    per_page: int
    """Number of results per page of results"""

    product: List[Product]

    product_neq: Annotated[List[Product], PropertyInfo(alias="product~neq")]

    severity: List[SeverityQueryParam]

    severity_neq: Annotated[List[SeverityQueryParam], PropertyInfo(alias="severity~neq")]

    subject: List[Subject]

    subject_neq: Annotated[List[Subject], PropertyInfo(alias="subject~neq")]
