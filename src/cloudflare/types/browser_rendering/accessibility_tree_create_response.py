# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccessibilityTreeCreateResponse", "AccessibilityTree"]


class AccessibilityTree(BaseModel):
    """Accessibility tree node"""

    role: str

    autocomplete: Optional[str] = None

    checked: Union[bool, Literal["mixed"], None] = None

    children: Optional[List[object]] = None

    description: Optional[str] = None

    disabled: Optional[bool] = None

    expanded: Optional[bool] = None

    focused: Optional[bool] = None

    haspopup: Optional[str] = None

    invalid: Optional[str] = None

    keyshortcuts: Optional[str] = None

    level: Optional[float] = None

    modal: Optional[bool] = None

    multiline: Optional[bool] = None

    multiselectable: Optional[bool] = None

    name: Optional[str] = None

    orientation: Optional[str] = None

    pressed: Union[bool, Literal["mixed"], None] = None

    readonly: Optional[bool] = None

    required: Optional[bool] = None

    roledescription: Optional[str] = None

    selected: Optional[bool] = None

    value: Union[str, float, None] = None

    valuemax: Optional[float] = None

    valuemin: Optional[float] = None

    valuetext: Optional[str] = None


class AccessibilityTreeCreateResponse(BaseModel):
    accessibility_tree: Optional[AccessibilityTree] = FieldInfo(alias="accessibilityTree", default=None)
    """Accessibility tree node"""
