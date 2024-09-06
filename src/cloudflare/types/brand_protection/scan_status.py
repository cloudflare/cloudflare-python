# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ScanStatus"]


class ScanStatus(BaseModel):
    last_processed: Optional[str] = None
    """Timestamp of when the submission was processed."""

    scan_complete: Optional[bool] = None
    """For internal use."""

    status_code: Optional[int] = None
    """Status code that the crawler received when loading the submitted URL."""

    submission_id: Optional[int] = None
    """ID of the most recent submission."""
