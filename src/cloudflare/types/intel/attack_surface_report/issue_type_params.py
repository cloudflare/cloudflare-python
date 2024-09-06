# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import List

from ...._utils import PropertyInfo

from .issue_type import IssueType

from .severity_query_param import SeverityQueryParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["IssueTypeParams"]


class IssueTypeParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dismissed: bool

    issue_class: List[str]

    issue_class_neq: Annotated[List[str], PropertyInfo(alias="issue_class~neq")]

    issue_type: List[IssueType]

    issue_type_neq: Annotated[List[IssueType], PropertyInfo(alias="issue_type~neq")]

    product: List[str]

    product_neq: Annotated[List[str], PropertyInfo(alias="product~neq")]

    severity: List[SeverityQueryParam]

    severity_neq: Annotated[List[SeverityQueryParam], PropertyInfo(alias="severity~neq")]

    subject: List[str]

    subject_neq: Annotated[List[str], PropertyInfo(alias="subject~neq")]
