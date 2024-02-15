# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SchemaUpdateResponse"]


class SchemaUpdateResponse(BaseModel):
    mitigation_action: Optional[Literal["log", "block", "none"]] = None
    """When set, this applies a mitigation action to this operation

    - `log` log request when request does not conform to schema for this operation
    - `block` deny access to the site when request does not conform to schema for
      this operation
    - `none` will skip mitigation for this operation
    - `null` indicates that no operation level mitigation is in place, see Zone
      Level Schema Validation Settings for mitigation action that will be applied
    """
