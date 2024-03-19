# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["DLPDatasetNewVersion"]


class DLPDatasetNewVersion(BaseModel):
    max_cells: int

    version: int

    secret: Optional[str] = None
