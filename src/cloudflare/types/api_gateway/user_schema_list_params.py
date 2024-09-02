# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["UserSchemaListParams"]


class UserSchemaListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    omit_source: bool
    """Omit the source-files of schemas and only retrieve their meta-data."""

    page: int
    """Page number of paginated results."""

    per_page: int
    """Maximum number of results per page."""

    validation_enabled: bool
    """Flag whether schema is enabled for validation."""
