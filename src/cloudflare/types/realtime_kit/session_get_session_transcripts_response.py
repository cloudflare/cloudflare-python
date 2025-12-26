# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SessionGetSessionTranscriptsResponse", "Data"]


class Data(BaseModel):
    session_id: str = FieldInfo(alias="sessionId")

    transcript_download_url: str
    """URL where the transcript can be downloaded"""

    transcript_download_url_expiry: str
    """Time when the download URL will expire"""


class SessionGetSessionTranscriptsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
