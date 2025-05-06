# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["OperationDeleteResponse"]


class OperationDeleteResponse(BaseModel):
    operation_id: Optional[str] = None
    """UUID."""
