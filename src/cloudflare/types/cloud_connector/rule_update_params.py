# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleUpdateParams", "Body", "BodyParameters"]


class RuleUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    body: Required[Iterable[Body]]
    """List of Cloud Connector rules"""


class BodyParameters(TypedDict, total=False):
    host: str
    """Host to perform Cloud Connection to"""


class Body(TypedDict, total=False):
    id: str

    description: str

    enabled: bool

    expression: str

    parameters: BodyParameters
    """Parameters of Cloud Connector Rule"""

    provider: Literal["aws_s3", "r2", "gcp_storage", "azure_storage"]
    """Cloud Provider type"""
