# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["NewVersion"]


class NewVersion(BaseModel):
    max_cells: int

    version: int

    secret: Optional[str] = None
