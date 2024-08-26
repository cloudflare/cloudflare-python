# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from datetime import datetime

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ImpersonationRegistryEditResponse"]

class ImpersonationRegistryEditResponse(BaseModel):
    id: int

    created_at: datetime

    is_email_regex: bool

    last_modified: datetime

    name: str

    comments: Optional[str] = None

    directory_id: Optional[int] = None

    directory_node_id: Optional[str] = None

    email: Optional[str] = None

    provenance: Optional[str] = None