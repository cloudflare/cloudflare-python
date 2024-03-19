# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .dlp_dataset import DLPDataset

__all__ = ["DLPDatasetCreation"]


class DLPDatasetCreation(BaseModel):
    dataset: DLPDataset

    max_cells: int

    version: int
    """The version to use when uploading the dataset."""

    secret: Optional[str] = None
    """The secret to use for Exact Data Match datasets.

    This is not present in Custom Wordlists.
    """
