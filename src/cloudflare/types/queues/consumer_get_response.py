# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..shared import UnnamedSchemaRef41
from ..._models import BaseModel

__all__ = ["ConsumerGetResponse", "ConsumerGetResponseItem"]


class ConsumerGetResponseItem(BaseModel):
    created_on: Optional[object] = None

    environment: Optional[object] = None

    queue_name: Optional[object] = None

    service: Optional[object] = None

    settings: Optional[UnnamedSchemaRef41] = None


ConsumerGetResponse = List[ConsumerGetResponseItem]
