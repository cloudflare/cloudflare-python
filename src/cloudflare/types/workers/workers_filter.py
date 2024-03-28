# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WorkersFilter"]


class WorkersFilter(BaseModel):
    id: str
    """Identifier"""

    enabled: bool

    pattern: str
