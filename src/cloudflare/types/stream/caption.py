# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Caption"]


class Caption(BaseModel):
    generated: Optional[bool] = None
    """Whether the caption was generated via AI."""

    label: Optional[str] = None
    """The language label displayed in the native language to users."""

    language: Optional[str] = None
    """The language tag in BCP 47 format."""

    status: Optional[Literal["ready", "inprogress", "error"]] = None
    """The status of a generated caption."""
