# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IssueTypeParams"]


class IssueTypeParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dismissed: bool

    issue_class: List[str]

    issue_class_neq: Annotated[List[str], PropertyInfo(alias="issue_class~neq")]

    issue_type: List[
        Literal[
            "compliance_violation",
            "email_security",
            "exposed_infrastructure",
            "insecure_configuration",
            "weak_authentication",
        ]
    ]

    issue_type_neq: Annotated[
        List[
            Literal[
                "compliance_violation",
                "email_security",
                "exposed_infrastructure",
                "insecure_configuration",
                "weak_authentication",
            ]
        ],
        PropertyInfo(alias="issue_type~neq"),
    ]

    product: List[str]

    product_neq: Annotated[List[str], PropertyInfo(alias="product~neq")]

    severity: List[Literal["low", "moderate", "critical"]]

    severity_neq: Annotated[List[Literal["low", "moderate", "critical"]], PropertyInfo(alias="severity~neq")]

    subject: List[str]

    subject_neq: Annotated[List[str], PropertyInfo(alias="subject~neq")]
