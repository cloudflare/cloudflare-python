# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["InstantLogpushJob"]

class InstantLogpushJob(BaseModel):
    destination_conf: Optional[str] = None
    """Unique WebSocket address that will receive messages from Cloudflare’s edge."""

    fields: Optional[str] = None
    """Comma-separated list of fields."""

    filter: Optional[str] = None
    """Filters to drill down into specific events."""

    sample: Optional[int] = None
    """
    The sample parameter is the sample rate of the records set by the client:
    "sample": 1 is 100% of records "sample": 10 is 10% and so on.
    """

    session_id: Optional[str] = None
    """Unique session id of the job."""