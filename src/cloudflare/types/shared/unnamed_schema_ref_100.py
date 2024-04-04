# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef100"]


class UnnamedSchemaRef100(BaseModel):
    operation_id: Optional[str] = None
    """The unique operation ID of the asynchronous action."""
