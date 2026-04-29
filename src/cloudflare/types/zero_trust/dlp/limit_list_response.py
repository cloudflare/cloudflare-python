# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["LimitListResponse"]


class LimitListResponse(BaseModel):
    max_custom_regex_entries: int
    """Maximum number of custom regex entries allowed for the account."""

    max_dataset_cells: int
    """
    Maximum number of dataset cells allowed for the account, across all EDM and CWL
    datasets.
    """

    max_document_fingerprints: int
    """Maximum number of document fingerprints allowed for the account."""

    used_custom_regex_entries: int
    """Number of custom regex entries currently configured for the account."""

    used_dataset_cells: int
    """
    Number of dataset cells currently configured for the account, across all EDM and
    CWL datasets. Document fingerprints do not count towards this limit.
    """

    used_document_fingerprints: int
    """Number of document fingerprints currently configured for the account."""
