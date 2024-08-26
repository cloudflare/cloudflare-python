# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RuleUpdateResponse", "RuleUpdateResponseItem", "RuleUpdateResponseItemParameters"]

class RuleUpdateResponseItemParameters(BaseModel):
    host: Optional[str] = None
    """Host to perform Cloud Connection to"""

class RuleUpdateResponseItem(BaseModel):
    id: Optional[str] = None

    description: Optional[str] = None

    enabled: Optional[bool] = None

    expression: Optional[str] = None

    parameters: Optional[RuleUpdateResponseItemParameters] = None
    """Parameters of Cloud Connector Rule"""

    provider: Optional[Literal["aws_s3", "r2", "gcp_storage", "azure_storage"]] = None
    """Cloud Provider type"""

RuleUpdateResponse: TypeAlias = List[RuleUpdateResponseItem]