# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

__all__ = ["IssueTypeParamItem"]

IssueTypeParamItem = Literal[
    "compliance_violation", "email_security", "exposed_infrastructure", "insecure_configuration", "weak_authentication"
]

IssueTypeParam = List[
    Literal[
        "compliance_violation",
        "email_security",
        "exposed_infrastructure",
        "insecure_configuration",
        "weak_authentication",
    ]
]
