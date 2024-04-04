# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef52"]


class UnnamedSchemaRef52(BaseModel):
    batch_size: Optional[float] = None

    max_retries: Optional[float] = None

    max_wait_time_ms: Optional[float] = None
