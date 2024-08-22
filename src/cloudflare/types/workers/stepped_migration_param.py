# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

from .migration_step_param import MigrationStepParam

from typing_extensions import TypedDict

__all__ = ["SteppedMigrationParam"]

class SteppedMigrationParam(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[MigrationStepParam]
    """Migrations to apply in order."""