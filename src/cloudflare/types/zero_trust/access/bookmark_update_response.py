# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["BookmarkUpdateResponse"]


class BookmarkUpdateResponse(BaseModel):
    id: Optional[object] = None
    """The unique identifier for the Bookmark application."""

    app_launcher_visible: Optional[bool] = None
    """Displays the application in the App Launcher."""

    created_at: Optional[datetime] = None

    domain: Optional[str] = None
    """The domain of the Bookmark application."""

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: Optional[str] = None
    """The name of the Bookmark application."""

    updated_at: Optional[datetime] = None
