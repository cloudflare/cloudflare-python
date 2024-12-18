# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["DomainBulkDeleteResponse", "DomainBulkDeleteResponseItem"]


class DomainBulkDeleteResponseItem(BaseModel):
    id: int
    """The unique identifier for the domain."""


DomainBulkDeleteResponse: TypeAlias = List[DomainBulkDeleteResponseItem]
