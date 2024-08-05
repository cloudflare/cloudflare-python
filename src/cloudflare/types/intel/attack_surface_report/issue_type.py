# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["IssueType"]

IssueType: TypeAlias = Literal[
    "compliance_violation", "email_security", "exposed_infrastructure", "insecure_configuration", "weak_authentication"
]
