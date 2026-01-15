# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TimeTravelRestoreResponse"]


class TimeTravelRestoreResponse(BaseModel):
    """Response from a time travel restore operation."""

    bookmark: Optional[str] = None
    """
    The new bookmark representing the state of the database after the restore
    operation.
    """

    message: Optional[str] = None
    """A message describing the result of the restore operation."""

    previous_bookmark: Optional[str] = None
    """The bookmark representing the state of the database before the restore
    operation.

    Can be used to undo the restore if needed.
    """
