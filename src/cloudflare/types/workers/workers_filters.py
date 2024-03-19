# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WorkersFilters"]


class WorkersFilters(BaseModel):
    id: str
    """Identifier"""

    enabled: bool

    pattern: str
