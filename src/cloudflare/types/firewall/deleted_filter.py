# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DeletedFilter"]


class DeletedFilter(BaseModel):
    id: str
    """The unique identifier of the filter."""

    deleted: bool
    """When true, indicates that the firewall rule was deleted."""
