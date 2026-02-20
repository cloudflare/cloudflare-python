# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DynamicRoutingListResponse",
    "Data",
    "DataRoute",
    "DataRouteDeployment",
    "DataRouteElement",
    "DataRouteElementUnionMember0",
    "DataRouteElementUnionMember0Outputs",
    "DataRouteElementUnionMember0OutputsNext",
    "DataRouteElementUnionMember1",
    "DataRouteElementUnionMember1Outputs",
    "DataRouteElementUnionMember1OutputsFalse_",
    "DataRouteElementUnionMember1OutputsTrue_",
    "DataRouteElementUnionMember1Properties",
    "DataRouteElementUnionMember2",
    "DataRouteElementUnionMember2Outputs",
    "DataRouteElementUnionMember3",
    "DataRouteElementUnionMember3Outputs",
    "DataRouteElementUnionMember3OutputsFallback",
    "DataRouteElementUnionMember3OutputsSuccess",
    "DataRouteElementUnionMember3Properties",
    "DataRouteElementUnionMember4",
    "DataRouteElementUnionMember4Outputs",
    "DataRouteElementUnionMember4OutputsFallback",
    "DataRouteElementUnionMember4OutputsSuccess",
    "DataRouteElementUnionMember4Properties",
    "DataRouteElementUnionMember5",
    "DataRouteElementUnionMember5Outputs",
    "DataRouteVersion",
]


class DataRouteDeployment(BaseModel):
    created_at: str

    deployment_id: str

    version_id: str

    comment: Optional[str] = None


class DataRouteElementUnionMember0OutputsNext(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class DataRouteElementUnionMember0Outputs(BaseModel):
    next: DataRouteElementUnionMember0OutputsNext


class DataRouteElementUnionMember0(BaseModel):
    id: str

    outputs: DataRouteElementUnionMember0Outputs

    type: Literal["start"]


class DataRouteElementUnionMember1OutputsFalse_(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class DataRouteElementUnionMember1OutputsTrue_(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class DataRouteElementUnionMember1Outputs(BaseModel):
    false: DataRouteElementUnionMember1OutputsFalse_

    true: DataRouteElementUnionMember1OutputsTrue_


class DataRouteElementUnionMember1Properties(BaseModel):
    conditions: Optional[object] = None


class DataRouteElementUnionMember1(BaseModel):
    id: str

    outputs: DataRouteElementUnionMember1Outputs

    properties: DataRouteElementUnionMember1Properties

    type: Literal["conditional"]


class DataRouteElementUnionMember2Outputs(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class DataRouteElementUnionMember2(BaseModel):
    id: str

    outputs: Dict[str, DataRouteElementUnionMember2Outputs]

    type: Literal["percentage"]


class DataRouteElementUnionMember3OutputsFallback(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class DataRouteElementUnionMember3OutputsSuccess(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class DataRouteElementUnionMember3Outputs(BaseModel):
    fallback: DataRouteElementUnionMember3OutputsFallback

    success: DataRouteElementUnionMember3OutputsSuccess


class DataRouteElementUnionMember3Properties(BaseModel):
    key: str

    limit: float

    limit_type: Literal["count", "cost"] = FieldInfo(alias="limitType")

    window: float


class DataRouteElementUnionMember3(BaseModel):
    id: str

    outputs: DataRouteElementUnionMember3Outputs

    properties: DataRouteElementUnionMember3Properties

    type: Literal["rate"]


class DataRouteElementUnionMember4OutputsFallback(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class DataRouteElementUnionMember4OutputsSuccess(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class DataRouteElementUnionMember4Outputs(BaseModel):
    fallback: DataRouteElementUnionMember4OutputsFallback

    success: DataRouteElementUnionMember4OutputsSuccess


class DataRouteElementUnionMember4Properties(BaseModel):
    model: str

    provider: str

    retries: float

    timeout: float


class DataRouteElementUnionMember4(BaseModel):
    id: str

    outputs: DataRouteElementUnionMember4Outputs

    properties: DataRouteElementUnionMember4Properties

    type: Literal["model"]


class DataRouteElementUnionMember5Outputs(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class DataRouteElementUnionMember5(BaseModel):
    id: str

    outputs: Dict[str, DataRouteElementUnionMember5Outputs]

    type: Literal["end"]


DataRouteElement: TypeAlias = Union[
    DataRouteElementUnionMember0,
    DataRouteElementUnionMember1,
    DataRouteElementUnionMember2,
    DataRouteElementUnionMember3,
    DataRouteElementUnionMember4,
    DataRouteElementUnionMember5,
]


class DataRouteVersion(BaseModel):
    active: Literal["true", "false"]

    created_at: str

    data: str

    version_id: str

    comment: Optional[str] = None


class DataRoute(BaseModel):
    id: str

    account_tag: str

    created_at: datetime

    deployment: DataRouteDeployment

    elements: List[DataRouteElement]

    gateway_id: str

    modified_at: datetime

    name: str

    version: DataRouteVersion


class Data(BaseModel):
    order_by: str

    order_by_direction: str

    page: float

    per_page: float

    routes: List[DataRoute]


class DynamicRoutingListResponse(BaseModel):
    data: Data

    success: bool
