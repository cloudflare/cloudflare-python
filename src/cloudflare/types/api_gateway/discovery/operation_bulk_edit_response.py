# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["OperationBulkEditResponse", "OperationBulkEditResponseItem"]


class OperationBulkEditResponseItem(BaseModel):
    state: Optional[Literal["review", "ignored"]] = None
    """Mark state of operation in API Discovery

    - `review` - Mark operation as for review
    - `ignored` - Mark operation as ignored
    """


OperationBulkEditResponse: TypeAlias = Dict[str, OperationBulkEditResponseItem]
