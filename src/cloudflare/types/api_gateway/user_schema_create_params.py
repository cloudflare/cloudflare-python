# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from ..._types import FileTypes

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["UserSchemaCreateParams"]


class UserSchemaCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    file: Required[FileTypes]
    """Schema file bytes"""

    kind: Required[Literal["openapi_v3"]]
    """Kind of schema"""

    name: str
    """Name of the schema"""

    validation_enabled: Literal["true", "false"]
    """Flag whether schema is enabled for validation."""
