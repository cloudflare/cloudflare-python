# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PolicyTestCreateResponse"]


class PolicyTestCreateResponse(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy test."""

    status: Optional[Literal["success"]] = None
    """The status of the policy test request."""
