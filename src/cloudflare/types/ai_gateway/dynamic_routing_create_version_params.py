# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "DynamicRoutingCreateVersionParams",
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
]


class DynamicRoutingCreateVersionParams(TypedDict, total=False):
    account_id: Required[str]

    gateway_id: Required[str]

    comment: Required[str]

    elements: Required[Iterable[Element]]


class ElementUnionMember0OutputsNext(TypedDict, total=False):
    element_id: Required[Annotated[str, PropertyInfo(alias="elementId")]]


class ElementUnionMember0Outputs(TypedDict, total=False):
    next: Required[ElementUnionMember0OutputsNext]


class ElementUnionMember0(TypedDict, total=False):
    id: Required[str]

    outputs: Required[ElementUnionMember0Outputs]

    type: Required[Literal["start"]]


class ElementUnionMember1OutputsFalse_(TypedDict, total=False):
    element_id: Required[Annotated[str, PropertyInfo(alias="elementId")]]


class ElementUnionMember1OutputsTrue_(TypedDict, total=False):
    element_id: Required[Annotated[str, PropertyInfo(alias="elementId")]]


class ElementUnionMember1Outputs(TypedDict, total=False):
    false: Required[ElementUnionMember1OutputsFalse_]

    true: Required[ElementUnionMember1OutputsTrue_]


class ElementUnionMember1Properties(TypedDict, total=False):
    conditions: object


class ElementUnionMember1(TypedDict, total=False):
    id: Required[str]

    outputs: Required[ElementUnionMember1Outputs]

    properties: Required[ElementUnionMember1Properties]

    type: Required[Literal["conditional"]]


class ElementUnionMember2Outputs(TypedDict, total=False):
    element_id: Required[Annotated[str, PropertyInfo(alias="elementId")]]


class ElementUnionMember2(TypedDict, total=False):
    id: Required[str]

    outputs: Required[Dict[str, ElementUnionMember2Outputs]]

    type: Required[Literal["percentage"]]


class ElementUnionMember3OutputsFallback(TypedDict, total=False):
    element_id: Required[Annotated[str, PropertyInfo(alias="elementId")]]


class ElementUnionMember3OutputsSuccess(TypedDict, total=False):
    element_id: Required[Annotated[str, PropertyInfo(alias="elementId")]]


class ElementUnionMember3Outputs(TypedDict, total=False):
    fallback: Required[ElementUnionMember3OutputsFallback]

    success: Required[ElementUnionMember3OutputsSuccess]


class ElementUnionMember3Properties(TypedDict, total=False):
    key: Required[str]

    limit: Required[float]

    limit_type: Required[Annotated[Literal["count", "cost"], PropertyInfo(alias="limitType")]]

    window: Required[float]


class ElementUnionMember3(TypedDict, total=False):
    id: Required[str]

    outputs: Required[ElementUnionMember3Outputs]

    properties: Required[ElementUnionMember3Properties]

    type: Required[Literal["rate"]]


class ElementUnionMember4OutputsFallback(TypedDict, total=False):
    element_id: Required[Annotated[str, PropertyInfo(alias="elementId")]]


class ElementUnionMember4OutputsSuccess(TypedDict, total=False):
    element_id: Required[Annotated[str, PropertyInfo(alias="elementId")]]


class ElementUnionMember4Outputs(TypedDict, total=False):
    fallback: Required[ElementUnionMember4OutputsFallback]

    success: Required[ElementUnionMember4OutputsSuccess]


class ElementUnionMember4Properties(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    retries: Required[float]

    timeout: Required[float]


class ElementUnionMember4(TypedDict, total=False):
    id: Required[str]

    outputs: Required[ElementUnionMember4Outputs]

    properties: Required[ElementUnionMember4Properties]

    type: Required[Literal["model"]]


class ElementUnionMember5Outputs(TypedDict, total=False):
    element_id: Required[Annotated[str, PropertyInfo(alias="elementId")]]


class ElementUnionMember5(TypedDict, total=False):
    id: Required[str]

    outputs: Required[Dict[str, ElementUnionMember5Outputs]]

    type: Required[Literal["end"]]


Element: TypeAlias = Union[
    ElementUnionMember0,
    ElementUnionMember1,
    ElementUnionMember2,
    ElementUnionMember3,
    ElementUnionMember4,
    ElementUnionMember5,
]
