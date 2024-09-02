# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SchemaData"]


class SchemaData(BaseModel):
    host: Optional[str] = None
    """The desired endpoint to test."""

    kind: Optional[str] = None
    """The type of test."""

    method: Optional[str] = None
    """The HTTP request method type."""
