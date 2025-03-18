# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RuleUpdateResponse", "Parameters"]


class Parameters(BaseModel):
    host: Optional[str] = None
    """Host to perform Cloud Connection to"""


class RuleUpdateResponse(BaseModel):
    id: Optional[str] = None

    description: Optional[str] = None

    enabled: Optional[bool] = None

    expression: Optional[str] = None

    parameters: Optional[Parameters] = None
    """Parameters of Cloud Connector Rule"""

    provider: Optional[Literal["aws_s3", "r2", "gcp_storage", "azure_storage"]] = None
    """Cloud Provider type"""
