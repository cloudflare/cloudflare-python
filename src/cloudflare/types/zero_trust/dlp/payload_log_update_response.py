# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from datetime import datetime

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PayloadLogUpdateResponse"]

class PayloadLogUpdateResponse(BaseModel):
    updated_at: datetime

    public_key: Optional[str] = None