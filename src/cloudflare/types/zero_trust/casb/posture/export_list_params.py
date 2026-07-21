# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExportListParams"]


class ExportListParams(TypedDict, total=False):
    account_id: Required[str]

    page: int
    """A page number within the paginated result set."""

    per_page: int
    """Number of results to return per page."""

    status: Literal["Pending", "Success", "Failure", "Rescheduled", "In-Progress"]
    """Filter on export job's status"""
