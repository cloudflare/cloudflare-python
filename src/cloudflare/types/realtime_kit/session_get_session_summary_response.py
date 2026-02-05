# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SessionGetSessionSummaryResponse", "Data"]


class Data(BaseModel):
    session_id: str = FieldInfo(alias="sessionId")

    summary_download_url: str = FieldInfo(alias="summaryDownloadUrl")
    """URL where the summary of transcripts can be downloaded"""

    summary_download_url_expiry: str = FieldInfo(alias="summaryDownloadUrlExpiry")
    """Time of Expiry before when you need to download the csv file."""


class SessionGetSessionSummaryResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
