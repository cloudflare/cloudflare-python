# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .unnamed_schema_ref_fbd3a4642487e41594e9af0ccb9a5ca5 import UnnamedSchemaRefFbd3a4642487e41594e9af0ccb9a5ca5

__all__ = ["ConsumerCreateResponse"]


class ConsumerCreateResponse(BaseModel):
    created_on: Optional[object] = None

    dead_letter_queue: Optional[str] = None

    environment: Optional[object] = None

    queue_name: Optional[object] = None

    script_name: Optional[object] = None

    settings: Optional[UnnamedSchemaRefFbd3a4642487e41594e9af0ccb9a5ca5] = None
