# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef61"]


class UnnamedSchemaRef61(BaseModel):
    recs_added: Optional[float] = None
    """Number of DNS records added."""

    total_records_parsed: Optional[float] = None
    """Total number of DNS records parsed."""
