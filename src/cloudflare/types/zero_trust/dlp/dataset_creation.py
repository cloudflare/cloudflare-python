# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .dataset import Dataset
from ...._models import BaseModel

__all__ = ["DatasetCreation"]


class DatasetCreation(BaseModel):
    dataset: Dataset

    encoding_version: int
    """Encoding version to use for dataset"""

    max_cells: int

    version: int
    """The version to use when uploading the dataset."""

    secret: Optional[str] = None
    """The secret to use for Exact Data Match datasets.

    This is not present in Custom Wordlists.
    """
