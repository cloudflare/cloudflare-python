# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["RuleGetParams"]


class RuleGetParams(TypedDict, total=False):
    path_id: Required[Annotated[str, PropertyInfo(alias="id")]]
    """The unique identifier of the firewall rule."""

    query_id: Annotated[str, PropertyInfo(alias="id")]
    """The unique identifier of the firewall rule."""
