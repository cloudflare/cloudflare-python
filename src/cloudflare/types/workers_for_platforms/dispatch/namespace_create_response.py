# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["NamespaceCreateResponse"]

class NamespaceCreateResponse(BaseModel):
    created_by: Optional[str] = None
    """Identifier"""

    created_on: Optional[datetime] = None
    """When the script was created."""

    modified_by: Optional[str] = None
    """Identifier"""

    modified_on: Optional[datetime] = None
    """When the script was last modified."""

    namespace_id: Optional[str] = None
    """API Resource UUID tag."""

    namespace_name: Optional[str] = None
    """Name of the Workers for Platforms dispatch namespace."""

    script_count: Optional[int] = None
    """The current number of scripts in this Dispatch Namespace"""