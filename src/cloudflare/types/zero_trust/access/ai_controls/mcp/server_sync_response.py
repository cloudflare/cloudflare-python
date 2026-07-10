# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["ServerSyncResponse", "ErrorDetails"]


class ErrorDetails(BaseModel):
    cause: Optional[str] = None
    """Underlying error message"""

    is_upstream: Optional[bool] = None
    """True = MCP server returned an error. False = couldn't reach the server"""

    mcp_code: Optional[float] = None
    """MCP protocol error code"""

    retryable: Optional[bool] = None
    """Whether the error is transient and worth retrying"""

    status_code: Optional[float] = None
    """HTTP status code from the server"""


class ServerSyncResponse(BaseModel):
    error: Optional[str] = None

    error_details: Optional[ErrorDetails] = None

    status: Optional[Literal["waiting", "ready", "stale", "error"]] = None
