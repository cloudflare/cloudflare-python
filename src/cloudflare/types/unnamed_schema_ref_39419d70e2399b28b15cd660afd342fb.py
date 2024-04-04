# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef39419d70e2399b28b15cd660afd342fb"]


class UnnamedSchemaRef39419d70e2399b28b15cd660afd342fb(BaseModel):
    url: Optional[str] = None
    """URL that was submitted."""

    url_id: Optional[int] = None
    """ID assigned to this URL submission. Used to retrieve scanning results."""
