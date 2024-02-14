# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["DNSRecordScanResponse"]


class DNSRecordScanResponse(BaseModel):
    recs_added: Optional[float] = None
    """Number of DNS records added."""

    total_records_parsed: Optional[float] = None
    """Total number of DNS records parsed."""
