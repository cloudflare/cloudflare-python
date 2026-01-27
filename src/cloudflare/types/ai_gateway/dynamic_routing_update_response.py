# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DynamicRoutingUpdateResponse",
    "Route",
    "RouteDeployment",
    "RouteElement",
    "RouteElementUnionMember0",
    "RouteElementUnionMember0Outputs",
    "RouteElementUnionMember0OutputsNext",
    "RouteElementUnionMember1",
    "RouteElementUnionMember1Outputs",
    "RouteElementUnionMember1OutputsFalse_",
    "RouteElementUnionMember1OutputsTrue_",
    "RouteElementUnionMember1Properties",
    "RouteElementUnionMember2",
    "RouteElementUnionMember2Outputs",
    "RouteElementUnionMember3",
    "RouteElementUnionMember3Outputs",
    "RouteElementUnionMember3OutputsFallback",
    "RouteElementUnionMember3OutputsSuccess",
    "RouteElementUnionMember3Properties",
    "RouteElementUnionMember4",
    "RouteElementUnionMember4Outputs",
    "RouteElementUnionMember4OutputsFallback",
    "RouteElementUnionMember4OutputsSuccess",
    "RouteElementUnionMember4Properties",
    "RouteElementUnionMember5",
    "RouteElementUnionMember5Outputs",
    "RouteVersion",
]


class RouteDeployment(BaseModel):
    created_at: str

    deployment_id: str

    version_id: str

    comment: Optional[str] = None


class RouteElementUnionMember0OutputsNext(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class RouteElementUnionMember0Outputs(BaseModel):
    next: RouteElementUnionMember0OutputsNext


class RouteElementUnionMember0(BaseModel):
    id: str

    outputs: RouteElementUnionMember0Outputs

    type: Literal["start"]


class RouteElementUnionMember1OutputsFalse_(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class RouteElementUnionMember1OutputsTrue_(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class RouteElementUnionMember1Outputs(BaseModel):
    false: RouteElementUnionMember1OutputsFalse_

    true: RouteElementUnionMember1OutputsTrue_


class RouteElementUnionMember1Properties(BaseModel):
    conditions: Optional[object] = None


class RouteElementUnionMember1(BaseModel):
    id: str

    outputs: RouteElementUnionMember1Outputs

    properties: RouteElementUnionMember1Properties

    type: Literal["conditional"]


class RouteElementUnionMember2Outputs(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class RouteElementUnionMember2(BaseModel):
    id: str

    outputs: Dict[str, RouteElementUnionMember2Outputs]

    type: Literal["percentage"]


class RouteElementUnionMember3OutputsFallback(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class RouteElementUnionMember3OutputsSuccess(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class RouteElementUnionMember3Outputs(BaseModel):
    fallback: RouteElementUnionMember3OutputsFallback

    success: RouteElementUnionMember3OutputsSuccess


class RouteElementUnionMember3Properties(BaseModel):
    key: str

    limit: float

    limit_type: Literal["count", "cost"] = FieldInfo(alias="limitType")

    window: float


class RouteElementUnionMember3(BaseModel):
    id: str

    outputs: RouteElementUnionMember3Outputs

    properties: RouteElementUnionMember3Properties

    type: Literal["rate"]


class RouteElementUnionMember4OutputsFallback(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class RouteElementUnionMember4OutputsSuccess(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class RouteElementUnionMember4Outputs(BaseModel):
    fallback: RouteElementUnionMember4OutputsFallback

    success: RouteElementUnionMember4OutputsSuccess


class RouteElementUnionMember4Properties(BaseModel):
    model: str

    provider: str

    retries: float

    timeout: float


class RouteElementUnionMember4(BaseModel):
    id: str

    outputs: RouteElementUnionMember4Outputs

    properties: RouteElementUnionMember4Properties

    type: Literal["model"]


class RouteElementUnionMember5Outputs(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class RouteElementUnionMember5(BaseModel):
    id: str

    outputs: Dict[str, RouteElementUnionMember5Outputs]

    type: Literal["end"]


RouteElement: TypeAlias = Union[
    RouteElementUnionMember0,
    RouteElementUnionMember1,
    RouteElementUnionMember2,
    RouteElementUnionMember3,
    RouteElementUnionMember4,
    RouteElementUnionMember5,
]


class RouteVersion(BaseModel):
    active: Literal["true", "false"]

    created_at: str

    data: str

    version_id: str

    comment: Optional[str] = None


class Route(BaseModel):
    id: str

    account_tag: str

    created_at: datetime

    deployment: RouteDeployment

    elements: List[RouteElement]

    gateway_id: str

    modified_at: datetime

    name: str

    version: RouteVersion


class DynamicRoutingUpdateResponse(BaseModel):
    route: Route

    success: bool
