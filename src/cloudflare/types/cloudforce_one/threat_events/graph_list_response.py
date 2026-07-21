# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["GraphListResponse", "Edge"]


class Edge(BaseModel):
    id: str
    """Deterministic composite edge id (source→target:relationshipType)"""

    relationship_type: str = FieldInfo(alias="relationshipType")

    source: str
    """Compact id of the source node (type:uuid)"""

    source_id: str = FieldInfo(alias="sourceId")

    source_type: str = FieldInfo(alias="sourceType")

    target: str
    """Compact id of the target node (type:uuid)"""

    target_id: str = FieldInfo(alias="targetId")

    target_type: str = FieldInfo(alias="targetType")


class GraphListResponse(BaseModel):
    edges: List[Edge]

    node: Optional[Dict[str, object]] = None
    """Focal node object (legacy single-seed). Null when unavailable."""

    nodes: List[Dict[str, object]]
