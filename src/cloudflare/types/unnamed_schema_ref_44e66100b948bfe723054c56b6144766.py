# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef44e66100b948bfe723054c56b6144766"]


class UnnamedSchemaRef44e66100b948bfe723054c56b6144766(BaseModel):
    url: Optional[str] = None
    """URL that was skipped."""

    url_id: Optional[int] = None
    """ID of the submission of that URL that is currently scanning."""
