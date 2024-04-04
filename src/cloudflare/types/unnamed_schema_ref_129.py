# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef129"]


class UnnamedSchemaRef129(BaseModel):
    timestamps: List[datetime]

    values: List[str]
