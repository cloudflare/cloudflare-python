# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RecordImportResponse"]

class RecordImportResponse(BaseModel):
    recs_added: Optional[float] = None
    """Number of DNS records added."""

    total_records_parsed: Optional[float] = None
    """Total number of DNS records parsed."""