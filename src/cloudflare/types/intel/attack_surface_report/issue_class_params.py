# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .product_param import ProductParam
from .subject_param import SubjectParam
from .issue_type_param import IssueTypeParam
from .issue_class_param import IssueClassParam
from .severity_query_param import SeverityQueryParam

__all__ = ["IssueClassParams"]


class IssueClassParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dismissed: bool

    issue_class: IssueClassParam

    issue_class_neq: Annotated[IssueClassParam, PropertyInfo(alias="issue_class~neq")]

    issue_type: IssueTypeParam

    issue_type_neq: Annotated[IssueTypeParam, PropertyInfo(alias="issue_type~neq")]

    product: ProductParam

    product_neq: Annotated[ProductParam, PropertyInfo(alias="product~neq")]

    severity: List[SeverityQueryParam]

    severity_neq: Annotated[List[SeverityQueryParam], PropertyInfo(alias="severity~neq")]

    subject: SubjectParam

    subject_neq: Annotated[SubjectParam, PropertyInfo(alias="subject~neq")]
