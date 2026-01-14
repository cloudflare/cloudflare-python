# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DownloadCreateResponse"]


class DownloadCreateResponse(BaseModel):
    percent_complete: Optional[float] = FieldInfo(alias="percentComplete", default=None)
    """Indicates the progress as a percentage between 0 and 100."""

    status: Optional[Literal["ready", "inprogress", "error"]] = None
    """The status of a generated download."""

    url: Optional[str] = None
    """The URL to access the generated download."""
