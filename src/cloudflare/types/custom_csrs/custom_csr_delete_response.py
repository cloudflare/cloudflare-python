# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CustomCsrDeleteResponse"]


class CustomCsrDeleteResponse(BaseModel):
    id: Optional[str] = None
    """Custom CSR identifier tag."""
