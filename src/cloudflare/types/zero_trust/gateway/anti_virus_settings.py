# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from .notification_settings import NotificationSettings

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AntiVirusSettings"]

class AntiVirusSettings(BaseModel):
    enabled_download_phase: Optional[bool] = None
    """Enable anti-virus scanning on downloads."""

    enabled_upload_phase: Optional[bool] = None
    """Enable anti-virus scanning on uploads."""

    fail_closed: Optional[bool] = None
    """Block requests for files that cannot be scanned."""

    notification_settings: Optional[NotificationSettings] = None
    """
    Configure a message to display on the user's device when an antivirus search is
    performed.
    """