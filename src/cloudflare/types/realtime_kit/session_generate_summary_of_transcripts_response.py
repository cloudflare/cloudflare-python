# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SessionGenerateSummaryOfTranscriptsResponse", "Data"]


class Data(BaseModel):
    session_id: Optional[str] = None

    status: Optional[str] = None


class SessionGenerateSummaryOfTranscriptsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
