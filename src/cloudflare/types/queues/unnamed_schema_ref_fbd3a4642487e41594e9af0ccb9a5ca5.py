# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRefFbd3a4642487e41594e9af0ccb9a5ca5"]


class UnnamedSchemaRefFbd3a4642487e41594e9af0ccb9a5ca5(BaseModel):
    batch_size: Optional[float] = None
    """The maximum number of messages to include in a batch"""

    max_retries: Optional[float] = None

    max_wait_time_ms: Optional[float] = None
