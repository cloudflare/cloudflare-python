# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PipelineListParams"]


class PipelineListParams(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    page: str
    """Specifies which page to retrieve."""

    per_page: str
    """Specifies the number of pipelines per page."""

    search: str
    """Specifies the prefix of pipeline name to search."""
