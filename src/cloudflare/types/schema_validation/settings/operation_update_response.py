# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["OperationUpdateResponse"]


class OperationUpdateResponse(BaseModel):
    mitigation_action: Literal["log", "block", "none"]
    """
    When set, this applies a mitigation action to this operation which supersedes a
    global schema validation setting just for this operation

    - `"log"` - log request when request does not conform to schema for this
      operation
    - `"block"` - deny access to the site when request does not conform to schema
      for this operation
    - `"none"` - will skip mitigation for this operation
    """

    operation_id: str
    """UUID."""
