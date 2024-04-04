# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..shared import UnnamedSchemaRef41
from ..._models import BaseModel

__all__ = ["ConsumerCreateResponse"]


class ConsumerCreateResponse(BaseModel):
    created_on: Optional[object] = None

    dead_letter_queue: Optional[str] = None

    environment: Optional[object] = None

    queue_name: Optional[object] = None

    script_name: Optional[object] = None

    settings: Optional[UnnamedSchemaRef41] = None
