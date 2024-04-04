# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef122"]


class UnnamedSchemaRef122(BaseModel):
    prompt: str

    guidance: Optional[float] = None

    image: Optional[List[float]] = None

    mask: Optional[List[float]] = None

    num_steps: Optional[int] = None

    strength: Optional[float] = None
