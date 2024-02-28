# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["HhgJaXcvTrace", "HhgJaXcvTraceItem"]


class HhgJaXcvTraceItem(BaseModel):
    action: Optional[str] = None
    """If step type is rule, then action performed by this rule"""

    action_parameters: Optional[object] = None
    """If step type is rule, then action parameters of this rule as JSON"""

    description: Optional[str] = None
    """If step type is rule or ruleset, the description of this entity"""

    expression: Optional[str] = None
    """If step type is rule, then expression used to match for this rule"""

    kind: Optional[str] = None
    """If step type is ruleset, then kind of this ruleset"""

    matched: Optional[bool] = None
    """Whether tracing step affected tracing request/response"""

    name: Optional[str] = None
    """If step type is ruleset, then name of this ruleset"""

    step_name: Optional[str] = None
    """Tracing step identifying name"""

    trace: Optional[HhgJaXcvTrace] = None

    type: Optional[str] = None
    """Tracing step type"""


HhgJaXcvTrace = List[HhgJaXcvTraceItem]

if PYDANTIC_V2:
    HhgJaXcvTraceItem.model_rebuild()
else:
    HhgJaXcvTraceItem.update_forward_refs()  # type: ignore
