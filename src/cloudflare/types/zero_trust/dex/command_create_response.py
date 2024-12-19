# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CommandCreateResponse", "Command"]


class Command(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the command"""

    args: Optional[Dict[str, str]] = None
    """Command arguments"""

    device_id: Optional[str] = None
    """Identifier for the device associated with the command"""

    status: Optional[Literal["PENDING_EXEC", "PENDING_UPLOAD", "SUCCESS", "FAILED"]] = None
    """Current status of the command"""

    type: Optional[str] = None
    """Type of the command (e.g., "pcap" or "warp-diag")"""


class CommandCreateResponse(BaseModel):
    commands: Optional[List[Command]] = None
    """List of created commands"""
