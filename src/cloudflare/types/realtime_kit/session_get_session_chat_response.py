# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SessionGetSessionChatResponse", "Data"]


class Data(BaseModel):
    chat_download_url: str
    """URL where the chat logs can be downloaded"""

    chat_download_url_expiry: str
    """Time when the download URL will expire"""


class SessionGetSessionChatResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
