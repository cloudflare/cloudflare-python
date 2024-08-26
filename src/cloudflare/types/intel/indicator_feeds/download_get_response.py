# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DownloadGetResponse"]

class DownloadGetResponse(BaseModel):
    file_id: Optional[int] = None
    """Feed id"""

    filename: Optional[str] = None
    """Name of the file unified in our system"""

    status: Optional[str] = None
    """Current status of upload, should be unified"""