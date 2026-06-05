# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "VersionGraphResponse",
    "Graph",
    "GraphWorkflow",
    "GraphWorkflowFunctions",
    "GraphWorkflowNode",
    "GraphWorkflowNodeUnionMember0",
    "GraphWorkflowNodeUnionMember1",
    "GraphWorkflowNodeUnionMember1Config",
    "GraphWorkflowNodeUnionMember1ConfigRetries",
    "GraphWorkflowNodeUnionMember2",
    "GraphWorkflowNodeUnionMember2Options",
    "GraphWorkflowNodeUnionMember2Payload",
    "GraphWorkflowNodeUnionMember2PayloadType",
    "GraphWorkflowNodeUnionMember2PayloadUnionMember1",
    "GraphWorkflowNodeUnionMember3",
    "GraphWorkflowNodeUnionMember4",
    "GraphWorkflowNodeUnionMember5",
    "GraphWorkflowNodeUnionMember6",
    "GraphWorkflowNodeUnionMember6CatchBlock",
    "GraphWorkflowNodeUnionMember6FinallyBlock",
    "GraphWorkflowNodeUnionMember6TryBlock",
    "GraphWorkflowNodeUnionMember7",
    "GraphWorkflowNodeUnionMember8",
    "GraphWorkflowNodeUnionMember8Branch",
    "GraphWorkflowNodeUnionMember9",
    "GraphWorkflowNodeUnionMember9Branch",
    "GraphWorkflowNodeUnionMember10",
    "GraphWorkflowNodeUnionMember10Functions",
    "GraphWorkflowNodeUnionMember10Payload",
    "GraphWorkflowNodeUnionMember10PayloadType",
    "GraphWorkflowNodeUnionMember10PayloadUnionMember1",
    "GraphWorkflowNodeUnionMember11",
    "GraphWorkflowNodeUnionMember12",
    "GraphWorkflowNodeUnionMember13",
    "GraphWorkflowPayload",
    "GraphWorkflowPayloadType",
    "GraphWorkflowPayloadUnionMember1",
]


class GraphWorkflowFunctions(BaseModel):
    name: str

    nodes: List[object]
    """Child nodes (recursive)."""

    type: Literal["function_def"]


class GraphWorkflowNodeUnionMember0(BaseModel):
    duration: Union[float, str]
    """Duration as milliseconds (number) or human-readable string."""

    name: str

    type: Literal["step_sleep"]

    resolves: Optional[float] = None

    starts: Optional[float] = None


class GraphWorkflowNodeUnionMember1ConfigRetries(BaseModel):
    """Retry policy for a step."""

    backoff: Literal["constant", "linear", "exponential"]
    """Backoff strategy for step retries."""

    delay: Union[float, str]
    """Duration as milliseconds (number) or human-readable string."""

    limit: float


class GraphWorkflowNodeUnionMember1Config(BaseModel):
    """Configuration for a step (retries and timeout)."""

    retries: GraphWorkflowNodeUnionMember1ConfigRetries
    """Retry policy for a step."""

    timeout: Union[float, str]
    """Duration as milliseconds (number) or human-readable string."""


class GraphWorkflowNodeUnionMember1(BaseModel):
    config: GraphWorkflowNodeUnionMember1Config
    """Configuration for a step (retries and timeout)."""

    name: str

    nodes: List[object]
    """Child nodes (recursive)."""

    type: Literal["step_do"]

    resolves: Optional[float] = None

    starts: Optional[float] = None


class GraphWorkflowNodeUnionMember2Options(BaseModel):
    """Options for a waitForEvent step."""

    event_type: str

    timeout: Union[float, str]
    """Duration as milliseconds (number) or human-readable string."""


class GraphWorkflowNodeUnionMember2PayloadType(BaseModel):
    type: Literal["unknown"]


class GraphWorkflowNodeUnionMember2PayloadUnionMember1(BaseModel):
    fields: Dict[str, object]
    """Nested JsonShape fields (recursive structure)."""

    type: Literal["object"]


GraphWorkflowNodeUnionMember2Payload: TypeAlias = Union[
    GraphWorkflowNodeUnionMember2PayloadType, GraphWorkflowNodeUnionMember2PayloadUnionMember1
]


class GraphWorkflowNodeUnionMember2(BaseModel):
    name: str

    options: Optional[GraphWorkflowNodeUnionMember2Options] = None
    """Options for a waitForEvent step."""

    type: Literal["step_wait_for_event"]

    payload: Optional[GraphWorkflowNodeUnionMember2Payload] = None
    """Shape descriptor for JSON payloads."""

    resolves: Optional[float] = None

    starts: Optional[float] = None


class GraphWorkflowNodeUnionMember3(BaseModel):
    name: str

    timestamp: str

    type: Literal["step_sleep_until"]

    resolves: Optional[float] = None

    starts: Optional[float] = None


class GraphWorkflowNodeUnionMember4(BaseModel):
    nodes: List[object]
    """Child nodes (recursive)."""

    type: Literal["loop"]


class GraphWorkflowNodeUnionMember5(BaseModel):
    kind: Literal["all", "any", "all_settled", "race"]
    """Parallel execution strategy."""

    nodes: List[object]
    """Child nodes (recursive)."""

    type: Literal["parallel"]


class GraphWorkflowNodeUnionMember6CatchBlock(BaseModel):
    nodes: List[object]
    """Child nodes (recursive)."""

    type: Literal["block"]


class GraphWorkflowNodeUnionMember6FinallyBlock(BaseModel):
    nodes: List[object]
    """Child nodes (recursive)."""

    type: Literal["block"]


class GraphWorkflowNodeUnionMember6TryBlock(BaseModel):
    nodes: List[object]
    """Child nodes (recursive)."""

    type: Literal["block"]


class GraphWorkflowNodeUnionMember6(BaseModel):
    catch_block: Optional[GraphWorkflowNodeUnionMember6CatchBlock] = None

    finally_block: Optional[GraphWorkflowNodeUnionMember6FinallyBlock] = None

    try_block: Optional[GraphWorkflowNodeUnionMember6TryBlock] = None

    type: Literal["try"]


class GraphWorkflowNodeUnionMember7(BaseModel):
    nodes: List[object]
    """Child nodes (recursive)."""

    type: Literal["block"]


class GraphWorkflowNodeUnionMember8Branch(BaseModel):
    condition: Optional[str] = None

    nodes: List[object]
    """Child nodes (recursive)."""


class GraphWorkflowNodeUnionMember8(BaseModel):
    branches: List[GraphWorkflowNodeUnionMember8Branch]

    type: Literal["if"]


class GraphWorkflowNodeUnionMember9Branch(BaseModel):
    condition: Optional[str] = None

    nodes: List[object]
    """Child nodes (recursive)."""


class GraphWorkflowNodeUnionMember9(BaseModel):
    branches: List[GraphWorkflowNodeUnionMember9Branch]

    discriminant: str

    type: Literal["switch"]


class GraphWorkflowNodeUnionMember10Functions(BaseModel):
    name: str

    nodes: List[object]
    """Child nodes (recursive)."""

    type: Literal["function_def"]


class GraphWorkflowNodeUnionMember10PayloadType(BaseModel):
    type: Literal["unknown"]


class GraphWorkflowNodeUnionMember10PayloadUnionMember1(BaseModel):
    fields: Dict[str, object]
    """Nested JsonShape fields (recursive structure)."""

    type: Literal["object"]


GraphWorkflowNodeUnionMember10Payload: TypeAlias = Union[
    GraphWorkflowNodeUnionMember10PayloadType, GraphWorkflowNodeUnionMember10PayloadUnionMember1
]


class GraphWorkflowNodeUnionMember10(BaseModel):
    class_name: str

    functions: Dict[str, GraphWorkflowNodeUnionMember10Functions]

    nodes: List[object]
    """Child nodes (recursive)."""

    type: Literal["start"]

    payload: Optional[GraphWorkflowNodeUnionMember10Payload] = None
    """Shape descriptor for JSON payloads."""


class GraphWorkflowNodeUnionMember11(BaseModel):
    name: str

    type: Literal["function_call"]

    resolves: Optional[float] = None

    starts: Optional[float] = None


class GraphWorkflowNodeUnionMember12(BaseModel):
    name: str

    nodes: List[object]
    """Child nodes (recursive)."""

    type: Literal["function_def"]


class GraphWorkflowNodeUnionMember13(BaseModel):
    kind: Literal["break", "return"]
    """Break or return from a loop."""

    type: Literal["break"]


GraphWorkflowNode: TypeAlias = Union[
    GraphWorkflowNodeUnionMember0,
    GraphWorkflowNodeUnionMember1,
    GraphWorkflowNodeUnionMember2,
    GraphWorkflowNodeUnionMember3,
    GraphWorkflowNodeUnionMember4,
    GraphWorkflowNodeUnionMember5,
    GraphWorkflowNodeUnionMember6,
    GraphWorkflowNodeUnionMember7,
    GraphWorkflowNodeUnionMember8,
    GraphWorkflowNodeUnionMember9,
    GraphWorkflowNodeUnionMember10,
    GraphWorkflowNodeUnionMember11,
    GraphWorkflowNodeUnionMember12,
    GraphWorkflowNodeUnionMember13,
]


class GraphWorkflowPayloadType(BaseModel):
    type: Literal["unknown"]


class GraphWorkflowPayloadUnionMember1(BaseModel):
    fields: Dict[str, object]
    """Nested JsonShape fields (recursive structure)."""

    type: Literal["object"]


GraphWorkflowPayload: TypeAlias = Union[GraphWorkflowPayloadType, GraphWorkflowPayloadUnionMember1]


class GraphWorkflow(BaseModel):
    """A parsed workflow entrypoint with its step graph."""

    class_name: str

    functions: Dict[str, GraphWorkflowFunctions]

    nodes: List[GraphWorkflowNode]

    payload: Optional[GraphWorkflowPayload] = None
    """Shape descriptor for JSON payloads."""


class Graph(BaseModel):
    """Versioned workflow graph payload."""

    version: float

    workflow: GraphWorkflow
    """A parsed workflow entrypoint with its step graph."""


class VersionGraphResponse(BaseModel):
    id: str

    class_name: str

    created_on: datetime

    graph: Optional[Graph] = None
    """Versioned workflow graph payload."""

    modified_on: datetime

    workflow_id: str
