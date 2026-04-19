# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["PipelineValidateSqlResponse", "Tables", "Graph", "GraphEdge", "GraphNode"]


class Tables(BaseModel):
    id: str

    name: str

    type: str

    version: float


class GraphEdge(BaseModel):
    dest_id: int

    edge_type: str

    key_type: str

    src_id: int

    value_type: str


class GraphNode(BaseModel):
    description: str

    node_id: int

    operator: str

    parallelism: int


class Graph(BaseModel):
    edges: List[GraphEdge]

    nodes: List[GraphNode]


class PipelineValidateSqlResponse(BaseModel):
    tables: Dict[str, Tables]
    """Indicates tables involved in the processing."""

    graph: Optional[Graph] = None
