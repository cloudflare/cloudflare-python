# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef11"]


class UnnamedSchemaRef11(BaseModel):
    url: Optional[str] = None
    """URL that was skipped."""

    url_id: Optional[int] = None
    """ID of the submission of that URL that is currently scanning."""
