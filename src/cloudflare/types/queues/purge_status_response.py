# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PurgeStatusResponse"]


class PurgeStatusResponse(BaseModel):
    completed: Optional[str] = None
    """Indicates if the last purge operation completed successfully."""

    started_at: Optional[str] = None
    """Timestamp when the last purge operation started."""
