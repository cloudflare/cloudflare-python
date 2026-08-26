# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["OperationBulkEditResponse", "OperationBulkEditResponseItem"]


class OperationBulkEditResponseItem(BaseModel):
    mitigation_action: Optional[Literal["log", "block", "none"]] = None
    """When set, this applies a mitigation action to this operation

    - `"log"` - log request when request does not conform to schema for this
      operation
    - `"block"` - deny access to the site when request does not conform to schema
      for this operation
    - `"none"` - will skip mitigation for this operation
    - `null` - clears any mitigation action
    """


OperationBulkEditResponse: TypeAlias = Dict[str, OperationBulkEditResponseItem]
