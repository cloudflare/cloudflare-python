# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TargetListResponse", "TargetListResponseItem"]


class TargetListResponseItem(BaseModel):
    id: str
    """Target ID."""

    type: str
    """Target type (page, background_page, worker, etc.)."""

    url: str
    """URL of the target."""

    description: Optional[str] = None
    """Target description."""

    devtools_frontend_url: Optional[str] = FieldInfo(alias="devtoolsFrontendUrl", default=None)
    """DevTools frontend URL."""

    title: Optional[str] = None
    """Title of the target."""

    web_socket_debugger_url: Optional[str] = FieldInfo(alias="webSocketDebuggerUrl", default=None)
    """WebSocket URL for debugging this target."""


TargetListResponse: TypeAlias = List[TargetListResponseItem]
