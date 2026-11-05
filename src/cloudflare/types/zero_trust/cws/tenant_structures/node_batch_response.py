# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .tenant_structure_node import TenantStructureNode

__all__ = ["NodeBatchResponse", "Deleted"]


class Deleted(BaseModel):
    id: str


class NodeBatchResponse(BaseModel):
    created: List[TenantStructureNode]

    deleted: List[Deleted]

    updated: List[TenantStructureNode]
