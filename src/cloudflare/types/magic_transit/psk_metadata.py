# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PSKMetadata"]

class PSKMetadata(BaseModel):
    last_generated_on: Optional[datetime] = None
    """The date and time the tunnel was last modified."""