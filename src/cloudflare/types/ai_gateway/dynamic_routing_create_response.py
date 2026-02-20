# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DynamicRoutingCreateResponse",
    "Deployment",
    "Element",
    "ElementUnionMember0",
    "ElementUnionMember0Outputs",
    "ElementUnionMember0OutputsNext",
    "ElementUnionMember1",
    "ElementUnionMember1Outputs",
    "ElementUnionMember1OutputsFalse_",
    "ElementUnionMember1OutputsTrue_",
    "ElementUnionMember1Properties",
    "ElementUnionMember2",
    "ElementUnionMember2Outputs",
    "ElementUnionMember3",
    "ElementUnionMember3Outputs",
    "ElementUnionMember3OutputsFallback",
    "ElementUnionMember3OutputsSuccess",
    "ElementUnionMember3Properties",
    "ElementUnionMember4",
    "ElementUnionMember4Outputs",
    "ElementUnionMember4OutputsFallback",
    "ElementUnionMember4OutputsSuccess",
    "ElementUnionMember4Properties",
    "ElementUnionMember5",
    "ElementUnionMember5Outputs",
    "Version",
]


class Deployment(BaseModel):
    created_at: str

    deployment_id: str

    version_id: str

    comment: Optional[str] = None


class ElementUnionMember0OutputsNext(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class ElementUnionMember0Outputs(BaseModel):
    next: ElementUnionMember0OutputsNext


class ElementUnionMember0(BaseModel):
    id: str

    outputs: ElementUnionMember0Outputs

    type: Literal["start"]


class ElementUnionMember1OutputsFalse_(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class ElementUnionMember1OutputsTrue_(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class ElementUnionMember1Outputs(BaseModel):
    false: ElementUnionMember1OutputsFalse_

    true: ElementUnionMember1OutputsTrue_


class ElementUnionMember1Properties(BaseModel):
    conditions: Optional[object] = None


class ElementUnionMember1(BaseModel):
    id: str

    outputs: ElementUnionMember1Outputs

    properties: ElementUnionMember1Properties

    type: Literal["conditional"]


class ElementUnionMember2Outputs(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class ElementUnionMember2(BaseModel):
    id: str

    outputs: Dict[str, ElementUnionMember2Outputs]

    type: Literal["percentage"]


class ElementUnionMember3OutputsFallback(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class ElementUnionMember3OutputsSuccess(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class ElementUnionMember3Outputs(BaseModel):
    fallback: ElementUnionMember3OutputsFallback

    success: ElementUnionMember3OutputsSuccess


class ElementUnionMember3Properties(BaseModel):
    key: str

    limit: float

    limit_type: Literal["count", "cost"] = FieldInfo(alias="limitType")

    window: float


class ElementUnionMember3(BaseModel):
    id: str

    outputs: ElementUnionMember3Outputs

    properties: ElementUnionMember3Properties

    type: Literal["rate"]


class ElementUnionMember4OutputsFallback(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class ElementUnionMember4OutputsSuccess(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class ElementUnionMember4Outputs(BaseModel):
    fallback: ElementUnionMember4OutputsFallback

    success: ElementUnionMember4OutputsSuccess


class ElementUnionMember4Properties(BaseModel):
    model: str

    provider: str

    retries: float

    timeout: float


class ElementUnionMember4(BaseModel):
    id: str

    outputs: ElementUnionMember4Outputs

    properties: ElementUnionMember4Properties

    type: Literal["model"]


class ElementUnionMember5Outputs(BaseModel):
    element_id: str = FieldInfo(alias="elementId")


class ElementUnionMember5(BaseModel):
    id: str

    outputs: Dict[str, ElementUnionMember5Outputs]

    type: Literal["end"]


Element: TypeAlias = Union[
    ElementUnionMember0,
    ElementUnionMember1,
    ElementUnionMember2,
    ElementUnionMember3,
    ElementUnionMember4,
    ElementUnionMember5,
]


class Version(BaseModel):
    active: Literal["true", "false"]

    created_at: str

    data: str

    version_id: str

    comment: Optional[str] = None


class DynamicRoutingCreateResponse(BaseModel):
    id: str

    account_tag: str

    created_at: datetime

    deployment: Deployment

    elements: List[Element]

    gateway_id: str

    modified_at: datetime

    name: str

    version: Version
