# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Dict, Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["SchemaUpdateMultipleParams", "Body"]


class SchemaUpdateMultipleParams(TypedDict, total=False):
    body: Required[Dict[str, Body]]


class Body(TypedDict, total=False):
    mitigation_action: Optional[Literal["log", "block", "none"]]
    """When set, this applies a mitigation action to this operation

    - `log` log request when request does not conform to schema for this operation
    - `block` deny access to the site when request does not conform to schema for
      this operation
    - `none` will skip mitigation for this operation
    - `null` indicates that no operation level mitigation is in place, see Zone
      Level Schema Validation Settings for mitigation action that will be applied
    """
