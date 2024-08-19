# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .migration_step import MigrationStep

__all__ = ["SteppedMigration"]


class SteppedMigration(BaseModel):
    new_tag: Optional[str] = None
    """Tag to set as the latest migration tag."""

    old_tag: Optional[str] = None
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Optional[List[MigrationStep]] = None
    """Migrations to apply in order."""
