# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef113"]


class UnnamedSchemaRef113(BaseModel):
    enabled: Optional[bool] = None
    """Indicates whether zone-level authenticated origin pulls is enabled."""
