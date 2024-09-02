# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IssueType"]

IssueType: TypeAlias = Literal[
    "compliance_violation", "email_security", "exposed_infrastructure", "insecure_configuration", "weak_authentication"
]
