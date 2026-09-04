# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["MessagePurgeResponse", "Error"]


class Error(BaseModel):
    message: Optional[str] = None


class MessagePurgeResponse(BaseModel):
    errors: Optional[List[Error]] = None
    """Errors encountered while purging messages."""

    warnings: Optional[Dict[str, str]] = None
    """Map of refs to warning messages encountered during purge."""
